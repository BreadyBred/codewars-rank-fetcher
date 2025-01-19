# Codewars Leaderboard Rank Tracker 🚀

This Python script automates the process of retrieving and storing your Codewars rankings, providing a convenient way to display your achievements and track your progress for portfolios, resumes, or personal websites.

**⚠️ Important Performance Note:**

Fetching data for a large number of categories can take some time due to the nature of web scraping and the way Codewars structures its leaderboard pages. If you are tracking many categories, be prepared for the script to run for a longer duration. Consider tracking only the categories you are most interested in to improve performance.

## Key Features

*	**Dynamic Data Retrieval:** Fetches leaderboard data from Codewars using file_put_contents, ensuring your ranks are up-to-date.
*	**Flexible Configuration:**
	*	Specify your Codewars username.
	*	Define categories to track (or track all categories).
	*	Choose to hide empty ranks in the output.
*	**Robust Error Handling:** Handles potential issues like missing files, malformed JSON, and failed cURL requests.
*	**Sustainable Design:** Built for future-proofing, minimizing the need for rewrites when deployed in a hosted environment.
*	**Clean and Readable Code:** Prioritizes code clarity and maintainability with optimizations to avoid unnecessary loops.
*	**JSON Storage:** Saves your ranks in a structured JSON file (`ranks.json`) for easy access and future use.

## Why Use This Script?

This script offers a practical solution for Codewars users who want to:

*	Effortlessly track their Codewars ranking progress across various categories.
*	Gain experience with essential Python functionalities like DOM manipulation, cURL, and JSON handling.
*	Develop a reusable script for leaderboard data retrieval and storage.

## Getting Started

1.  **Clone the Repository:**

	```bash
	git clone https://github.com/BreadyBred/codewars_rank_fetcher
	```

2.  **Configure the Script:**

	*	Optionally, modify the `categories_to_check` array to specify the categories you want to track.

3.  **Run the Script:**

	You have two main options for running the script:

	**a) Command Line (Recommended):**

	This is the most straightforward method, especially for automated tasks or server environments.

	1.  Open your terminal or command prompt.
	2.  Navigate to the directory where you saved the `rank_fetcher.py` file.
	3.  Execute the script using the Python command-line interpreter:

		```bash
		py rank_fetcher.py
		```

This will fetch your latest ranks for the specified categories and store them in the `ranks.json` file.

## Further Enhancements

*	Consider adding command-line arguments for configuration options.
*	Adding modules that fetch user infos using the Codewars API.
*	Using cURL for implementation in hosted websites to make the ranks update dynamic.