from bs4 import BeautifulSoup
import requests
import pandas as pd
from prettytable import PrettyTable

def main():
    url = get_wikipedia_url()
    page_content = fetch_page_content(url)
    table = select_table(page_content)
    df = extract_table_data(table)
    display_table(df)
    save_to_csv(df)

def get_wikipedia_url():
    """Prompt the user for a Wikipedia URL and validate it."""
    url = input("Enter the Wikipedia article URL (e.g., https://en.wikipedia.org/wiki/Example): ").strip()
    if not url.startswith("https://en.wikipedia.org/wiki/"):
        print("Invalid Wikipedia URL. Please enter a valid Wikipedia article URL.")
        return None
    return url

def fetch_page_content(url):
    """Fetch and return the HTML content of the Wikipedia page."""
    try:
        print("Fetching data from Wikipedia...")
        page = requests.get(url)
        page.raise_for_status()
        return BeautifulSoup(page.text, "html.parser")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

def select_table(soup):
    """Prompt the user to select a table from the Wikipedia page."""
    tables = soup.find_all("table", {"class": "wikitable"})
    if not tables:
        print("No tables found in the given Wikipedia article.")
        return None
    print(f"Found {len(tables)} tables in the article.")
    for i, table in enumerate(tables):
        print(f"Table {i+1}")
    table_choice = input(f"Enter the table number to scrape (1-{len(tables)}), default is 1: ").strip()
    table_choice = int(table_choice) if table_choice.isdigit() and 1 <= int(table_choice) <= len(tables) else 1
    return tables[table_choice - 1]

def extract_table_data(table):
    """Extract data from the chosen table and return it as a DataFrame."""
    headers = [header.text.strip() for header in table.find_all("th")]
    df = pd.DataFrame(columns=headers)
    rows = table.find_all('tr')
    for row in rows[1:]:
        data = [cell.text.strip() for cell in row.find_all('td')]
        if len(data) == len(headers):
            df.loc[len(df)] = data
        else:
            print(f"Skipping row with mismatched columns: {data}")
    return df

def display_table(df):
    """Display the scraped data in a nicely formatted table."""
    print("\nHere is the scraped table data:")
    pretty_table = PrettyTable()
    pretty_table.field_names = df.columns
    for row in df.itertuples(index=False):
        pretty_table.add_row(row)
    print(pretty_table)

def save_to_csv(df):
    """Prompt the user for a file path and save the DataFrame to a CSV file."""
    file_path = input("Enter the file path to save the CSV (default: ScrapedTable.csv): ").strip() or "ScrapedTable.csv"
    df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")

if __name__ == "__main__":
    main()