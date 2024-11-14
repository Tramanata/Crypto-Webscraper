## Crypto Webscraper

This Python script uses **Playwright** for web scraping and **psycopg2** to insert data into a PostgreSQL database.

### 1. Scraping Data with Playwright
- **Playwright** is used to open a Chromium browser and navigate to the CoinMarketCap website.
- The script scrolls down the page multiple times to ensure all data is loaded.
- The `query_selector_all` method is used to extract data from a table containing cryptocurrency information.
- For each row in the table, the script gathers data such as:
  - `id`
  - `Name`
  - `Symbol`
  - `Price`
  - `Market Cap`
  - `24hr Volume`
- The data is collected into a list of dictionaries (`master_list`).

### 2. Storing Data in PostgreSQL
- The data from `master_list` is converted into a list of tuples (`list_of_tuples`).
- A connection is made to a PostgreSQL database using **psycopg2**.
- The script inserts the data into the `crypto` table using the `execute_values` function, which is efficient for bulk inserts.
- The connection is committed and closed.

### Notes
- The code uses a headless browser for scraping, but the `headless=False` option allows the browser window to be visible.
- PostgreSQL credentials (`host`, `database`, `user`, `password`) need to be adjusted as per your setup.
