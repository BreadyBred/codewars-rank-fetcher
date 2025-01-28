# Codewars Rank Fetcher

The **Codewars Rank Fetcher** is a user-friendly desktop application that automates the process of retrieving and storing your Codewars rankings. It provides a convenient way to display your achievements and track your progress for portfolios, resumes, or personal websites.

## Key Features

- **Dynamic Data Retrieval:** Fetches leaderboard data directly from Codewars using the `requests` library, ensuring your ranks are always up-to-date.
- **Flexible Configuration:**
  - Specify your Codewars username.
  - Select specific categories to track or track all categories.
  - Option to hide empty ranks.
  - Option to sort ranks from highest to lowest.
- **JSON Storage:** Saves your ranks and user data in a structured JSON file (`output/output.json`) for easy access and future use.
- **User-Friendly GUI:** Built with `tkinter`, the application provides an intuitive interface for configuring and running the rank-fetching process.

## Why Use This Application?

This application is perfect for Codewars users who want to effortlessly track their ranking progress across various programming languages and categories. Whether you're preparing for a job interview, updating your portfolio, or just curious about your progress, this tool makes it easy to gather and organize your Codewars achievements.

---

## Getting Started

1. **Download the Executable:**
   - Download the `codewars_rank_fetcher.exe` file from the [Releases](https://github.com/BreadyBred/codewars-rank-fetcher/releases) section of this repository.

2. **Run the Application:**
   - Double-click the `codewars_rank_fetcher.exe` file to launch the application.

3. **Configure and Fetch Ranks:**
   - Enter your Codewars username.
   - Select the categories you want to track (or leave all selected to track everything).
   - Choose whether to hide empty ranks and/or sort ranks.
   - Click the **Fetch Ranks** button to start the process.

4. **View the Results:**
   - Once the process is complete, your ranks and user data will be saved in the `output/output.json` file.

---

### Example Output

After running the application, the `output/output.json` file will contain your Codewars data in the following format:

```json
{
	"YourUsername": {
		"user_data": {
			"honor": 1796,
			"leaderboard_position": 11049,
			"total_completed": 124,
			"languages_scores": {
				"javascript": 811,
				"php": 2830,
				"python": 418,
				"riscv": 21
			}
		},
		"ranks": {
			"RISC-V": 35,
			"PHP": 60
		}
	}
}
```

## How It Works

1. Username Validation:
    * The application first validates your Codewars username by fetching your profile data from the Codewars API.
2. Rank Fetching:
    * For each selected category, the application fetches your rank from the Codewars leaderboard using web scraping techniques.
3. Data Storage:
    * Your ranks and user data are saved in a JSON file (output/output.json) for easy access and integration into other projects.

## Requirements
	
No additional requirements. Just download and run the .EXE file.

## Support

If you encounter any issues or have questions, please open an issue [here](https://github.com/BreadyBred/codewars-rank-fetcher/issues).