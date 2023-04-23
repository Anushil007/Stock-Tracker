import requests
from bs4 import BeautifulSoup
import smtplib

# def get_stock_price(ticker):
#     url = f'https://finance.yahoo.com/quote/{ticker}/quote'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     price = soup.find('span', {'data-reactid': '50'}).text
#     return float(price.replace(',', ''))


# def check_stock_price(ticker, threshold):
#     current_price = get_stock_price(ticker)
#     if current_price >= threshold:
#         # send notification to user
#         pass



# def send_email(subject, body, to):
#     smtp_server = 'smtp.gmail.com'
#     smtp_port = 587
#     smtp_username = 'your_email@gmail.com'
#     smtp_password = 'your_email_password'

#     msg = f'Subject: {subject}\n\n{body}'

#     with smtplib.SMTP(smtp_server, smtp_port) as server:
#         server.starttls()
#         server.login(smtp_username, smtp_password)
#         server.sendmail(smtp_username, to, msg)

ticker = 'AAPL'
import yfinance as yf

# Replace "TICKER" with the actual ticker symbol of the stock you want
ticker = yf.Ticker(ticker)

# Get the current price of the stock
price = ticker.info['currentPrice']

print(price)




