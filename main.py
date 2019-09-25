# @Author: Shiva
# @Date: 25th Sep 2019

import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://zerodha.com/margin-calculator/Equity/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
                    AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/39.0.2171.95 Safari/537.36'
}


# request to zerodha
data = requests.get(url, headers=headers)


# converting the response to beautifulsoup element for scraping
soup = BeautifulSoup(data.text)


# storing the html data into list format
final_data = []


# iterating over html to get the stock name and margin values
for k in range(0, len(soup.findAll('td'))):
    if soup.findAll('td')[k].text.endswith(":EQ"):
        final_data.append([soup.findAll('td')[k].text.strip(),
            soup.findAll('td')[k+2].text.strip()]
        )


# converting the list to dataframe
df = pd.DataFrame(final_data, columns=["Stock Name", "Margin Value"])


# saving the dataframe(data) into cvs format
df.to_csv("zerodha_margin_values.csv", index=False)
