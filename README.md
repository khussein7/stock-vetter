# stock-vetter
Basic Stock Vetting Program.
<br>
Using the Selenium library, I created a working prototype Python script within 2 days (ending 06/25/2021) to grab relevant stock information from multiple web pages, make calculations and output those calculations to aid in better decision-making when looking to buy stocks.
<br>
## Instructions
In order to run Selenium, you'll need to install a driver to your computer. Since I like Chrome, I chose 'chromedriver,' but there are other browser options. You can find more info about them [here](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/).
<br>
<br>
Make sure to have your installed driver in the same folder or directory as your python file. 
<br>
E.g., line 14: `driver = webdriver.Chrome('/Users/admin/PycharmProjects/webscraping/chromedriver')`
<br>
<br>
To start, either run the code one of two ways
- enter your desired stock ticker symbol into the variable 'ticker' (line 13) as such: `'AAPL'`
- comment line 13 and uncomment line 14, which reads as, `# ticker = input('Enter Stock Ticker: \n')`
<br>
Concepts include: webscraping, stock-related math concepts (e.g. ratios)
