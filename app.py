from playwright.sync_api import sync_playwright
import psycopg2
from psycopg2.extras import execute_values

def main():
    with sync_playwright() as p:
        ## divided into 2 sections 
        # 1) scraping
        browser = p.chromium.launch(headless=False) #opens the website
        # headless = False we see browser popup
        page = browser.new_page()
        page.goto('https://coinmarketcap.com/')
        
        # playwright need to scroll down page before scraping
        for i in range(5):
            page.mouse.wheel(0, 2000)
            page.wait_for_timeout(1000)
        
        # sc-7b3ac367-3 etbcea cmc-table
        trs_xpath = "//table[@class='sc-7b3ac367-3 etbcea cmc-table']/tbody/tr"
        trs_list = page.query_selector_all(trs_xpath)
        # print(len(trs_list)) should print 100 items in the crypto list
        
        master_list = []
        for tr in trs_list:
            coin_dict = {}
            
            tds = tr.query_selector_all('//td')
            
            coin_dict['id'] = tds[1].inner_text()
            coin_dict['Name'] = tds[2].query_selector("//p[@class='sc-65e7f566-0 iPbTJf coin-item-name']").inner_text()
            coin_dict['Symbol'] = tds[2].query_selector("//p[@class='sc-65e7f566-0 byYAWx coin-item-symbol']").inner_text()
            coin_dict['Price'] = float(tds[3].inner_text().replace('$','').replace(',',''))
            coin_dict['Market_cap_usd'] = int(tds[7].inner_text().replace('$','').replace(',',''))
            coin_dict['Volume_24hr_usd'] = int(tds[8].query_selector("//p[@color='text']").inner_text().replace('$','').replace(',',''))
            
            master_list.append(coin_dict)
        
        
        # tuples (id, name, symbol, ...)
        list_of_tuples = [tuple(dic.values()) for dic in master_list]
    
        # 2) saving data to PostgresSQL
        
        # connect to db
        pgconn = psycopg2.connect(
            host = 'localhost',
            database = 'personalprojects',
            user = 'postgres',
            password = 'tylerpostgres'
        )
        
        # create cursor to write code
        pgcursor = pgconn.cursor()
        
        execute_values(pgcursor, 
           "INSERT INTO crypto (id, name, symbol, price_usd, market_cap_usd, volume_24h_usd) VALUES %s",
           list_of_tuples)

        # commit
        pgconn.commit()
        
        # close the connection
        pgconn.close()
        
        browser.close()
if __name__ == '__main__':
    main()