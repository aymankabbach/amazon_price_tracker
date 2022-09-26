from bs4 import BeautifulSoup
import requests
import smtplib
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language":"fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,ar;q=0.6"
}
## here you should enter a product amazon URL (URL from amazon.de seems like not giving the right information)
URL=input("enter an amazon URL\n")

def get_data():
    response=requests.get(url=URL, headers=headers)
    return response.text
def make_soup():
    data=get_data()
    try:
        soup=BeautifulSoup(data, 'html.parser')
    except:
        print("error in make_soup function")
    else:
        return soup
def get_price():
    Price=make_soup().find(name="span", class_="a-offscreen")
    print(f"the price is {Price.text}")
get_price()
