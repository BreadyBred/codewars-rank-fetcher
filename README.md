# Codewars Leaderboard Rank Fetcher

This Python script automates the process of retrieving and storing your Codewars rankings, providing a convenient way to display your achievements and track your progress for portfolios, resumes, or personal websites.

## Key Features

*   **Dynamic Data Retrieval:** Fetches leaderboard data from Codewars using requests library, ensuring your ranks are up-to-date.
*   **Flexible Configuration:**
    *   Specify your Codewars username.
    *   Define categories to track (or track all categories).
    *   Choose to hide empty ranks and/or to sort the ranks in the output.
*   **JSON Storage:** Saves your ranks in a structured JSON file (`ranks.json`) for easy access and future use.

## Why Use This Script?

This script offers a practical solution for Codewars users who want to:

*   Effortlessly track their Codewars ranking progress across various categories.
*   Gain experience with essential Python libraries like `requests`, `json`, and web scraping techniques.
*   Develop a reusable script for leaderboard data retrieval and storage.

## Getting Started

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/BreadyBred/codewars_rank_fetcher
    ```

2.  **Configure the Script:**

    *   Run `pip install -r requirements.txt` in order to install all the necessary modules for the tool to work.
    *   Set categories_to_check to the names of the categories you want the script to process. Leave it empty to check all the available categories.

3.  **Run the Script:**

    1.  Open your terminal, command prompt or preferred IDE.
    2.  Navigate to the directory where you saved the `rank_fetcher.py` file.
    3.  Execute the script using the Python command-line interpreter:

        ```bash
        python rank_fetcher.py
        py rank_fetcher.py
        ```
    4. Configure the way you want the data to be fetched.

This will fetch your latest ranks for the specified categories and store them in the `ranks.json` file.

## Further Enhancements

*   **Codewars API:** The addition of modules to gather information from the official Codewars API for potentially more reliable and efficient data retrieval. This might require additional code to interact with the API.