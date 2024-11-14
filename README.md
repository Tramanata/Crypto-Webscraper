## Crypto Webscraper

![image](https://github.com/user-attachments/assets/cf396365-5743-4835-b395-da07bedefab4)

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

![image](https://github.com/user-attachments/assets/ab6d4d5c-a956-4ae6-97d8-864076ee990c)
- Wrote this query to generate the table


### Challenge
- I ran into a challenge with the size of the data types for my table values
![image](https://github.com/user-attachments/assets/a90ea95a-5da3-4236-bf20-d9c362ea9f54)

- To solve this problem, I adjusted the size of the integer data types
![image](https://github.com/user-attachments/assets/943f139e-95b3-4187-9d2c-3025511d7992)



### Output
![image](https://github.com/user-attachments/assets/7ba0b1a9-3f05-49de-90ab-286488bb5ad5)


  



### Notes
- The code uses a headless browser for scraping, but the `headless=False` option allows the browser window to be visible.
- PostgreSQL credentials (`host`, `database`, `user`, `password`) need to be adjusted as per your setup.
