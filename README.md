# Web Scraping Adventure

This Python script scrapes the latest deals from the RedFlagDeals forum and provides several functionalities to analyze and log deal information.

## Features

1. **Display Latest Deals**: Fetches and displays the latest deals including store, item, votes, username, timestamp, category, replies, views, and URL.

2. **Analyze Deals by Category**: Analyzes and displays the number of deals in each category.

3. **Find Top Stores**: Allows the user to input the number of top stores to display based on the number of deals.

4. **Log Deal Information**: Logs URLs of deals from a selected category into a text file (`log.txt`).

5. **Exit**: Exits the program.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## How to Use

1. Clone the repository:
   ```
   git clone https://github.com/your_username/your_repository.git
   cd your_repository
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the script:
   ```
   python main.py
   ```

4. Choose an option from the menu:
   - Enter `1` to display latest deals.
   - Enter `2` to analyze deals by category.
   - Enter `3` to find top stores.
   - Enter `4` to log deal information.
   - Enter `5` to exit the program.

## Notes

- Ensure you have a stable internet connection to fetch data from RedFlagDeals.
- Deal information is fetched from the "Hot Deals" section of RedFlagDeals.
- This script may require adjustments if RedFlagDeals changes its HTML structure.

Feel free to explore and modify the script according to your needs!

---

This README provides an overview of the script's functionality, instructions for setup, usage guidelines, and important notes for users. Adjust the URLs and repository details as per your actual GitHub repository.
