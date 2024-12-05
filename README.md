# Wiki Table Scraper
### Video Demo: [Watch it here](https://youtu.be/_sNeEctNUas?si=jAJnWBAwIBWbTFJP)

## Description
The Wiki Table Scraper is a Python project that allows users to extract structured data from tables found in Wikipedia articles. By specifying a Wikipedia URL, users can view available tables, select which one to scrape, and save the extracted data to a CSV file. This tool is ideal for anyone looking to quickly gather tabular data from Wikipedia for analysis or research.

## Features
- Fetches and parses HTML content from Wikipedia pages.
- Displays available tables for user selection.
- Extracts data from the selected table and formats it into a pandas DataFrame.
- Displays the extracted data in a neat, user-friendly table using PrettyTable.
- Saves the extracted data to a CSV file for further use.

## Technologies Used
- Python 3.x
- `requests` - To fetch HTML content from Wikipedia pages.
- `BeautifulSoup` - For parsing HTML and extracting table data.
- `pandas` - For storing and manipulating table data.
- `PrettyTable` - To display the extracted data in a formatted table.
- `csv` - For saving the data to a CSV file.

## Installation Instructions
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/wiki-table-scraper.git
2. Navigate into the project directory:
    cd wiki-table-scraper
3. Install the required dependencies:
    pip install -r requirements.txt

## What I learned
During this project, I learned how to scrape and manipulate data from the web using Python. I became familiar with libraries such as BeautifulSoup for parsing HTML, requests for making web requests, and pandas for handling tabular data. I also gained experience in formatting and presenting data neatly using PrettyTable and saving it to CSV files for future use!

## Future Improvements
- Allow users to specify the table's columns they want to scrape
- Include additional export options, such as saving the data to an Excel file