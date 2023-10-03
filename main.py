import lxml
import requests
from bs4 import BeautifulSoup
import smtplib






#write here your password and your email
app_password = 'YOUR PASSWORD'
MY_EMAIL = "YOUR EMAIL"



#the url of product
URL = "https://www.amazon.com/All-new-Essentials-including-Graphite-Amazon/dp/B07RQNBBL8/ref=sr_1_1?keywords=Kindle+E-readers&pd_rd_r=d5b594e6-c479-4b0a-9b27-2e00123581bd&pd_rd_w=LF2nb&pd_rd_wg=1reYm&pf_rd_p=b9deb6fa-f7f0-4f9b-bfa0-824f28f79589&pf_rd_r=1YENTC6HG2ME1BXHB5JY&qid=1688307122&sr=8-1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,fr;q=0.8"
}


response = requests.get(url=URL, headers=headers)

soup = BeautifulSoup(response.text, "lxml")

span = soup.find(name="span", class_="a-offscreen")
price = span.getText()
price_in_float = float(price.split("$")[1])


title = soup.find(name="span", id="productTitle").getText()


link_of_product = "https://www.amazon.com/All-new-Essentials-including-Graphite-Amazon/dp/B07RQNBBL8/ref=sr_1_1?keywords=Kindle+E-readers&pd_rd_r=d5b594e6-c479-4b0a-9b27-2e00123581bd&pd_rd_w=LF2nb&pd_rd_wg=1reYm&pf_rd_p=b9deb6fa-f7f0-4f9b-bfa0-824f28f79589&pf_rd_r=1YENTC6HG2ME1BXHB5JY&qid=1688307122&sr=8-1"

text = "check the link now --> {link_of_product} your product {title} is reduced from 319.97$ to {price_in_float}"


#you can change the 400 to target price
if price_in_float < 400:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        message = f"{title} is now {price_in_float}"
        connection.starttls()
        connection.login(MY_EMAIL, app_password)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="TO EMAIL",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{link_of_product}".encode("utf-8")
        )
