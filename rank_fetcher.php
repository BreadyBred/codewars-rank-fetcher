<?php
ini_set('max_execution_time', 0);

# Add your Codewars username
define("username", "BreadyBred");

# Add the path to the JSON file (it will be created if it doesn't exist)
define("file_path", "ranks.json");

# Add the categories you want the script to check
# Keep empty to check all categories
$categories_to_check = ["RISC-V", "VB"];

# Hide empty ranks (true/false)
$hide_empty_ranks = true;

function create_json_file(): void {
	if(!file_exists(file_path)) {
		$data = [ username => [] ];
		file_put_contents(file_path, json_encode($data, JSON_PRETTY_PRINT));
	}
}

function get_categories(): array {
	$file_path = "categories.json";

	if(!file_exists($file_path)) {
		throw new Exception("File not found: $file_path");
	}

	$json_data = file_get_contents($file_path);

	return json_decode($json_data, true);
}

function initialize_categories(): void {
	$GLOBALS["categories"] = get_categories();
}

function fill_all_categories(): array {
	$categories = get_categories();
	$categories_to_check = [];

	foreach($categories as $category_name => $formatted_name) {
		$categories_to_check[] = $category_name;
	}

	return $categories_to_check;
}

function get_formatted_category_name(string $category): string {
	return $GLOBALS["categories"][$category];
}

function write_rank_in_json(string $category, int|null $rank): bool {
	$json_data = file_get_contents(file_path);
	$data = json_decode($json_data, true);

	$data[username][$category] = $rank;

	return !file_put_contents(file_path, json_encode($data, JSON_PRETTY_PRINT));
}

function add_codewars_rank(string $category): int|null {
	$formatted_category = get_formatted_category_name($category);
	$url = "https://www.codewars.com/users/leaderboard/ranks?language=$formatted_category";

	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
	curl_setopt($ch, CURLOPT_USERAGENT, "Mozilla/5.0");

	$html = curl_exec($ch);
	curl_close($ch);

	if(!$html) {
		die("Impossible de récupérer les données du site.");
	}

	$dom = new DOMDocument();
	libxml_use_internal_errors(true); 
	$dom->loadHTML($html);
	libxml_clear_errors();

	$xpath = new DOMXPath($dom);	
	$rows = $xpath->query("//div[contains(@class, 'leaderboard')]//table//tr");
	
	foreach($rows as $row) {
		if($row instanceof DOMElement) {
			$data_username = $row->getAttribute("data-username");

			if($data_username === username) {
				$rank_cell = $xpath->query(".//td[contains(@class, 'rank')]", $row);
				if($rank_cell->length > 0) {
					$user_rank = trim($rank_cell->item(0)->textContent);
					$user_rank = (int) str_replace("#", "", $user_rank);
					return $user_rank;
				}
			}
		}
	}

	return null;
}

function get_codewars_ranks(array $categories, bool $hide_empty_ranks): void {
	if(empty($categories_to_check)) {
		$categories_to_check = fill_all_categories();
	}

	foreach($categories as $category) {
		$user_rank = add_codewars_rank($category);

		if($hide_empty_ranks && $user_rank === null) {
			continue;
		}
		
		write_rank_in_json($category, $user_rank);
	}
}

initialize_categories();
create_json_file();
get_codewars_ranks($categories_to_check, $hide_empty_ranks);