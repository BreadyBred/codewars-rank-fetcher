# Codewars Rank Fetcher

This Python script automates the process of retrieving and storing your Codewars rankings, providing a convenient way to display your achievements and track your progress for portfolios, resumes, or personal websites.

## Key Features

*   **Dynamic Data Retrieval:** Fetches leaderboard data from Codewars using requests library, ensuring your ranks are up-to-date.
*   **Flexible Configuration:**
    *   Specify your Codewars username.
    *   Define categories to track (or track all categories).
    *   Choose to hide empty ranks and/or to sort the ranks in the output.
*   **JSON Storage:** Saves your ranks in a structured JSON file (`ranks.json`) for easy access and future use.

## Why Use This Script?

This script offers a practical solution for Codewars users who want to effortlessly track their Codewars ranking progress across various categories.

## Getting Started

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/BreadyBred/codewars_rank_fetcher
    ```

2.  **Run the Script:**

    **a) EXE File (Recommended):**
    1.  Just launch the executable file `codewars_rank_fetcher.exe`.
    2. Configure the way you want the data to be fetched.
    3. That's it!

    **b) Command-line:**
    1.  Open your terminal, command prompt or preferred IDE inside the directory where you saved the `codewars_rank_fetcher.py` file.
    2.  Run `pip install -r requirements.txt` in order to install all the necessary modules for the tool to work.
    3.  Execute the script using the Python command-line interpreter:

        ```bash
        python codewars_rank_fetcher.py
        py codewars_rank_fetcher.py
        ```
    4. Configure the way you want the data to be fetched.

This will fetch your latest ranks for the specified categories and store them in the `ranks.json` file.

## Further Enhancements

*   **Codewars API:** The addition of modules to gather information from the official Codewars API for potentially more reliable and efficient data retrieval. This might require additional code to interact with the API.
