# Codewars Leaderboard Rank Tracker 🚀

This PHP script automates the process of retrieving and storing your Codewars rankings, providing a convenient way to display your achievements and track your progress for portfolios, resumes, or personal websites.

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
*	Gain experience with essential PHP functionalities like DOM manipulation, cURL, and JSON handling.
*	Develop a reusable script for leaderboard data retrieval and storage.

## Getting Started

1.  **Clone the Repository:**

	```bash
	git clone https://github.com/BreadyBred/codewars_rank_fetcher
	```

2.  **Configure the Script:**

	*	Edit the `username` constant in the PHP file with your Codewars username.
	*	Optionally, modify the `$categories_to_check` array to specify the categories you want to track.
	*	Optionally, set `$hide_empty_ranks` to `false` to include empty ranks in the output.

3.  **Run the Script:**

	You have two main options for running the script:

	**a) Command Line (Recommended):**

	This is the most straightforward method, especially for automated tasks or server environments.

	1.  Open your terminal or command prompt.
	2.  Navigate to the directory where you saved the `rank_fetcher.php` file.
	3.  Execute the script using the PHP command-line interpreter:

		```bash
		php rank_fetcher.php
		```

	**b) Using XAMPP (For Local Development):**

	If you're using XAMPP for local development, you can either clone the repository or download a ZIP archive. This will create the project directory for you.

	1.  **Obtain the Project:**

		*	**Using Git (Recommended):** Open your terminal or Git Bash, navigate to your XAMPP `htdocs` directory (e.g., `C:\xampp\htdocs\`), and clone the repository:

			```bash
			cd C:\xampp\htdocs\
			git clone https://github.com/BreadyBred/codewars_rank_fetcher
			```

			This will create a folder with the repository name (`codewars_rank_fetcher`).

		*	**Downloading a ZIP:** Download the ZIP archive of the repository from GitHub. Extract the contents to your XAMPP `htdocs` directory. This will create a folder with the repository name.

	2.  **Start the Apache Server:** Start the Apache server in the XAMPP Control Panel.

	3.  **Access the Script:** Open your web browser and navigate to the appropriate URL. The URL will be `localhost/[PATH/TO/DIRECTORY]/codewars_rank_fetcher/rank_fetcher.php`.

	**Important Notes for XAMPP:**

	*	Ensure that PHP is correctly configured in your XAMPP setup.
	*	If you encounter any errors, check your PHP error logs (usually located in `C:\xampp\php\logs\` or a similar directory) for more information.
	*	Using the command line is generally preferred for running PHP scripts outside of a web browser context, especially for tasks that don't require user interaction.

This will fetch your latest ranks for the specified categories and store them in the `ranks.json` file.

## Further Enhancements

*	Consider adding command-line arguments for configuration options.
*	Adding modules that fetch user infos using the Codewars API.
*	Using cURL for implementation in hosted websites to make the ranks update dynamic.