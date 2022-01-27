from selenium import webdriver

'''READ-ME!

Temporary solution to Selenium driver processes lingering on 
MacOS following any scripting error involving Selenium:
Go to 'Activity Monitor', 
then 'CPU' or 'Memory' tab, 
then search 'chromedriver' 
and manually Quit each Process.'''

'''Stock Name + Ticker'''
ticker = 'dogef'
# ticker = input('Enter Stock Ticker: \n')

# Ratios tab
url = 'https://financials.morningstar.com/ratios/r.html?t=' + ticker + '&region=usa&culture=en-US'

driver = webdriver.Chrome('/Users/admin/PycharmProjects/webscraping/chromedriver')
driver.get(url)

# Stock name + ticker
element_stock = driver.find_element_by_class_name('r_title').text
print(element_stock + '\n')

'''Interest Coverage Ratio
= Operating Income / Interest Expense

(Tells you how much operating income a company
generates relative to its interest expense.
Want a ratio of ≥ 6, and the higher the better.)'''
element_ICname = driver.find_element_by_id('i95').text
element_ICnum = driver.find_element_by_xpath('//*[@id="tab-profitability"]/table[2]/tbody/tr[16]/td[11]').text
if element_ICnum == '—':
    print(element_ICname + ':', element_ICnum, '\n')
elif float(element_ICnum) > 6:
    print(element_ICname + ':', element_ICnum, '(> 6. Great!)\n')
elif float(element_ICnum) == 6:
    print(element_ICname + ':', element_ICnum, '(= 6. Not bad, but could be better.)\n')
else:
    print(element_ICname + ':', element_ICnum, '(< 6. Bad.)\n')

# Free Cash Flow (found in 'Ratios' tab)
element_FCF = driver.find_element_by_xpath('//*[@id="financials"]/table/tbody/tr[26]/td[11]').text

# Earnings Per Share (found in 'Ratios' tab)
element_EPS = driver.find_element_by_xpath('//*[@id="financials"]/table/tbody/tr[12]/td[11]').text

# ROIC (found in 'Ratios' tab)
elements = driver.find_elements_by_id('i27')
for e in elements:
    element_ROIC = e.find_element_by_xpath('//*[@id="tab-profitability"]/table[2]/tbody/tr[14]/td[11]').text

'''Debt-to-Assets Ratio 
= Total Liabilities / Total Assets

(Want to see a Debt-to Assets ratio < 0.75, ideally. The lower the better.
Tells you how much the company OWES (debt) relative to
how much it OWNS (assets))'''
# Financials tab > Balance Sheet tab
url = 'http://financials.morningstar.com/balance-sheet/bs.html?t=' + ticker + '&region=usa&culture=en-US'
driver.get(url)

# Total Assets
elements = driver.find_elements_by_id('data_tts1')
for e in elements:
    TotalAssets = e.find_element_by_css_selector('#Y_5').text
    print('Total Assets:', TotalAssets)

# Total Liabilities
elements = driver.find_elements_by_id('data_ttg5')
for e in elements:
    TotalLiabilities = e.find_element_by_css_selector('#Y_5').text
    print('Total Liabilities:', TotalLiabilities)

DAratio = round(float(TotalLiabilities.replace(',', ''))/float(TotalAssets.replace(',', '')), 2)
if DAratio < 0.75:
    print('Debt-to-Assets Ratio:', DAratio, '(< 0.75. Great!)\n')
else:
    print('Debt-to-Assets Ratio:', DAratio, '(> 0.75. Not so great.)\n')

'''Debt Payback Time 
= Long-Term Debt / Free Cash Flow

(Tells you how long it would take for the company to pay
off all its debt.
A good rule of thumb is 3 years or less. You don't want to
invest in a company that has much debt that it'll take too 
long to get out of debt.)'''

# Long-Term Debt (found in 'Balance Sheet' tab)
elements = driver.find_elements_by_id('data_i50')
for e in elements:
    element_LTD = e.find_element_by_css_selector('#Y_5').text
    print('Long-Term Debt:', element_LTD)

# print FCF
print('Free Cash Flow:', element_FCF)

DPT = round(float(element_LTD.replace(',', ''))/float(element_FCF.replace(',', '')), 2)
if DPT <= 3:
    print('Debt Payback Time:', DPT, 'years (≤ 3 years. Great!)\n')
else:
    print('Debt Payback Time:', DPT, 'years (> 3 years. Not so great.)\n')

'''Earnings Per Share (EPS)
= total net income of the company / the # of shares outstanding

(Want to look for strong, consistently positive & upward trending EPS numbers.
Looking at earnings on a per share basis makes it much easier to 
read and compare with other companies.)'''

print('Earnings Per Share:', element_EPS + '\n' + '(want to see positive & upward trending)\n')

'''Return on Invested Capital (ROIC)

(Most important measure of profitability. 
Shows how well the company is utilizing its resources to generate returns.
Look for companies w/ ROIC of ≥10%. The higher the better!)'''

if float(element_ROIC) >= 10:
    print('Return on Invested Capital (ROIC):', element_ROIC + '%', '(≥ 10%. Great!)\n')
else:
    print('Return on Invested Capital (ROIC):', element_ROIC + '%', '(< 10%. Not so great.)\n')

'''Price-to-Earnings (P/E) Ratio
= Stock Price / Earnings Per Share

(Quick & easy way to determine whether the stock is a bargain right now.
Compares the stock's current trading price to its most recently reported 
earnings per share.
The lower the PE Ratio, the cheaper the stock relative 
to the earnings its generates.
A good rule of thumb is to find stocks w/ PE ratios of 15 or less. 
It helps to compare a stock's PE ratio w/ its historical average, 
as well as w/ industry averages.
The lower the PE Ratio, the better the bargain!)'''
# Valuation tab
url = 'http://financials.morningstar.com/valuation/price-ratio.html?t=' + ticker + '&region=usa&culture=en-US'
driver.get(url)

# PE Ratio
element_PER = driver.find_element_by_xpath('//*[@id="currentValuationTable"]/tbody/tr[2]/td[1]').text
if element_PER == '—':
    print('Price-to-Earnings (P/E) Ratio:', element_PER + '\n')
elif float(element_PER) <= 15:
    print('Price-to-Earnings (P/E) Ratio:', element_PER, '(≤ 15. Great!)\n')
else:
    print('Price-to-Earnings (P/E) Ratio:', element_PER, '(> 15. Not so great.)\n')

driver.quit()
