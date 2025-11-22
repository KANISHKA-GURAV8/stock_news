📈 Stock Price & News Alert System (Python)

This project is a Python-based stock monitoring and alert system that automatically tracks the stock price of a selected company and sends the latest related news via email when the stock price changes significantly.

It uses:

1.Alpha Vantage API – for stock price data

2.NewsAPI – for latest company-related news

3.SMTP (Gmail) – to send email alerts

4.Python dotenv – to protect API keys

🚀 Features

✅ Tracks Tesla (TSLA) stock price daily
✅ Calculates % change in closing price
✅ Automatically triggers if the change is greater than 5%
✅ Fetches top 3 news articles related to the company
✅ Sends an email notification with:

*Stock change percentage

*Latest headlines

*News brief description

*Direct URLs to articles
✅ Secured using environment variables (.env)

🧩 How It Works

1.Fetches daily stock data from Alpha Vantage

2.Calculates change between:

3.Yesterday’s closing price

4.Day before yesterday’s closing price

5.If the difference is > 1%, it:

6.Fetches related news from NewsAPI

7.Sends the top 3 articles to your email

🛠️ Technologies Used

*Python 3

*requests

*smtplib

*dotenv

*Alpha Vantage API

*NewsAPI
