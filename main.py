import requests
import os
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage

# Load environment variables
load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

Stock_api_key = os.environ.get("stock_api_key")
News_api_key = os.environ.get("news_api_key")
Email_password = os.environ.get("email_password")

# STEP 1: Get stock data
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": Stock_api_key
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
data_json = response.json()

# Check if stock data exists
if "Time Series (Daily)" not in data_json:
    print("Error in API response:", data_json)
else:
    stock_data = data_json["Time Series (Daily)"]

    # Convert dict to list of (date, values) pairs
    data = list(stock_data.items())

    # Yesterday and day before
    yesterday_date, yesterday_data = data[0]
    day_before_date, day_before_data = data[1]

    yesterday_close = float(yesterday_data["4. close"])
    day_before_close = float(day_before_data["4. close"])

    print(f"Yesterday ({yesterday_date}): {yesterday_close}")
    print(f"Day before ({day_before_date}): {day_before_close}")

    # Difference
    difference = abs(yesterday_close - day_before_close)
    percentage_diff = (difference / day_before_close) * 100
    print(f"Percentage difference: {percentage_diff:.2f}%")

    # STEP 2: Get news if > 1%
    if percentage_diff > 1:
        parameters1 = {
            "apiKey": News_api_key,
            "qInTitle": COMPANY_NAME
        }

        response1 = requests.get(NEWS_ENDPOINT, params=parameters1)
        news_data = response1.json()

        if "articles" not in news_data:
            print("Error in News API response:", news_data)
        else:
            articles = news_data["articles"][:3]

            formatted_articles = [
                f"{STOCK_NAME}: {percentage_diff:.2f}%\n"
                f"Headline: {article['title']}\n"
                f"Brief: {article['description']}\n"
                f"URL: {article['url']}"
                for article in articles
            ]

            # Prepare email
            msg = EmailMessage()
            msg["Subject"] = f"{STOCK_NAME} Stock Alert"
            msg["From"] = "kanigurav@gmail.com"
            msg["To"] = "kanishkagurav@yahoo.com"
            msg.set_content("\n\n".join(formatted_articles))

            # Send email
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user="kanigurav@gmail.com", password=Email_password)
                connection.send_message(msg)

            print("Email sent successfully")
    else:
        print("Price change < 5%... no news sent")


