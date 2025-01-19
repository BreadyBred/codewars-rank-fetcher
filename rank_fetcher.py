import subprocess
import sys
import json
import os
import requests
import time
from lxml import html
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# File paths
file_path = "ranks.json"
categories_file_path = "data/categories.json"
requirements_file = 'requirements.txt'

username = input(f"{Fore.CYAN}Please enter your Codewars username: {Fore.WHITE}")

hide_empty_ranks_input = input(f"{Fore.CYAN}Would you like to hide the empty ranks? (Y/n): ").strip().lower()
hide_empty_ranks = False if hide_empty_ranks_input in ["no", "n", "N"] else True

categories_to_check = []

def install_requirements():
	"""Install required dependencies from requirements.txt."""
	print(f"\n{Fore.YELLOW}Checking and installing required dependencies...")

	if not os.path.exists(requirements_file):
		print(f"{Fore.RED}requirements.txt not found!")
		sys.exit(1)

	try:
		subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		print(f"{Fore.GREEN}All dependencies installed successfully.")
	except subprocess.CalledProcessError as e:
		print(f"{Fore.RED}Failed to install dependencies: {e}")
		sys.exit(1)

def create_json_file():
	"""Create or reset the ranks.json file."""
	if os.path.exists(file_path):
		os.remove(file_path)

	data = {username: {}}
	with open(file_path, 'w') as f:
		json.dump(data, f, indent=4)

def initialize_categories():
    global global_categories
    print(f"{Fore.CYAN}Initializing categories...\n")
    global_categories = get_categories()

def get_categories():
	"""Fetch categories from categories.json."""
	print(f"\n{Fore.CYAN}Fetching categories from {categories_file_path}...")

	if not os.path.exists(categories_file_path):
		raise Exception(f"{Fore.RED}File not found: {categories_file_path}")

	with open(categories_file_path, "r") as f:
		categories = json.load(f)

	print(f"{Fore.GREEN}Categories loaded.\n")
	return categories

def write_rank_in_json(category, rank):
	"""Write the user's rank to ranks.json."""
	if os.path.exists(file_path):
		with open(file_path, 'r') as f:
			data = json.load(f)
	else:
		data = {username: {}}

	data[username][category] = rank

	with open(file_path, 'w') as f:
		json.dump(data, f, indent=4)

def get_formatted_category_name(category):
	"""Return formatted category name."""
	return global_categories.get(category, category)

def add_codewars_rank(category):
	"""Fetch the user's rank for a specific category."""
	print(f"\n{Fore.CYAN}Fetching rank for category '{category}' from Codewars...")
	formatted_category = get_formatted_category_name(category)
	url = f"https://www.codewars.com/users/leaderboard/ranks?language={formatted_category}"

	try:
		response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
		response.raise_for_status()
		print(f"{Fore.GREEN}Data fetched successfully.")
	except requests.RequestException as e:
		print(f"{Fore.RED}Error fetching data for category '{category}': {e}")
		return None

	tree = html.fromstring(response.content)
	rows = tree.xpath("//div[contains(@class, 'leaderboard')]//table//tr")

	for row in rows:
		data_username = row.get("data-username")
		if data_username == username:
			rank_cell = row.xpath(".//td[contains(@class, 'rank')]")
			if rank_cell:
				user_rank = rank_cell[0].text_content().strip()
				user_rank = int(user_rank.replace("#", ""))
				print(f"{Fore.GREEN}Rank for {username} in category '{category}' is: {user_rank}")
				return user_rank

	print(f"{Fore.YELLOW}No rank found for {username}.")
	return None

def get_codewars_ranks(categories, hide_empty_ranks):
	"""Get ranks for the specified categories."""
	if not categories:
		print(f"{Fore.CYAN}No specific categories provided, filling all categories...")
		categories = list(global_categories.keys())

	print(f"{Fore.CYAN}Fetching ranks for categories: {categories}")
	for category in categories:
		user_rank = add_codewars_rank(category)

		if hide_empty_ranks and user_rank is None:
			print(f"{Fore.YELLOW}Rank is empty for category '{category}', skipping...")
			continue

		write_rank_in_json(category, user_rank)

def sort_json_ranks():
	"""Ask the user if they want the ranks sorted, and then sort the JSON if requested."""
	sort_input = input(f"\n{Fore.CYAN}Would you like to sort the ranks from highest to lowest? (Y/n): ").strip().lower()

	if sort_input in ["yes", "y", "Y"]:
		with open(file_path, 'r') as f:
			data = json.load(f)

		for user_data in data.get(username, {}):
			sorted_ranks = sorted(data[username].items(), key=lambda x: (x[1] if x[1] is not None else float('inf')))
			data[username] = dict(sorted_ranks)

		with open(file_path, 'w') as f:
			json.dump(data, f, indent=4)

		print(f"{Fore.GREEN}Ranks sorted from highest to lowest.")
	else:
		print(f"{Fore.YELLOW}Ranks not sorted.")

def main():
	install_requirements()

	try:
		initialize_categories()
	except Exception as e:
		print(f"{Fore.RED}Error initializing categories: {e}")
		sys.exit(1)

	start_time = time.time()

	create_json_file()

	get_codewars_ranks(categories_to_check, hide_empty_ranks)
	end_time = time.time()
	elapsed_time = end_time - start_time

	sort_json_ranks()
	print(f"\n{Fore.GREEN}Rank fetching process completed in {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
	main()