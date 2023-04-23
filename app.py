# Description: This is the main file for the Stock Price Alert app. It contains the main logic for the app.
# Author: @anushiltimsina

# Import the necessary libraries
from twilio.rest import Client
import smtplib
import yfinance as yf
import schedule
import threading
import os


price = 0 
# set up the Flask app
from flask import Flask, render_template, request
app = Flask(__name__)


# Set up the home page
@app.route('/')
def index():
    return render_template('index.html')


#get the data from the form 
@app.route('/submit', methods=['POST'])
def submit():
    ticker = request.form['ticker']
    threshold = request.form['threshold']
    frequency = request.form['frequency']
    type = request.form['type']

    # check type of notification
    if type == 'email':
        to = request.form['email']
        print(to)
    else:
        to = request.form['phone']
        print(to)

    # check frequency of notification and set up the schedule
    threading.Timer(frequency, get_stock_price(ticker,threshold,to)).start()

    return render_template('success.html',symbol=ticker, threshold=threshold, frequency=frequency)


# Get the current price of the stock
def get_stock_price(ticker,threshold,to):
    ticker = yf.Ticker(ticker)

    price = ticker.info['currentPrice']

    print(price)
    if threshold <= price and type == 'email':
        return send_email('Stock Price Alert', f'{ticker} has reached {threshold},to {to}', to)
        
    elif threshold <= price and type == 'sms':
        return send_sms(f'{ticker} has reached {threshold},to {to}', to)

    

# Send email notification
def send_email(subject, body, to):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465
    smtp_username = 'ga819544@gmail.com'
    smtp_password = os.environ.get('PASSWORD') 

    msg = f'Subject: {subject}\n\n{body}'

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to, msg)


# Send SMS notification
def send_sms( body, to):
    # Replace the placeholders below with  Twilio account SID, auth token, and Twilio phone number
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    twilio_phone_number = os.environ['TWILIO_PHONE_NUMBER']
    # Create a Twilio client object
    client = Client(account_sid, auth_token)

    # Send the SMS message
    message = client.messages.create(
        body=body,
        from_=twilio_phone_number,
        to=to
    )

    # Print the message ID
    print(f"SMS sent to {to}. Message ID: {message.sid}")    


# Run the app
if __name__ == '__main__':
    app.run(debug=True)



