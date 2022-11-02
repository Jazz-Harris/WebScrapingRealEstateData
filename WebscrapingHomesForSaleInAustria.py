from bs4 import BeautifulSoup 
import requests 
from random import randint
from time import sleep
from csv import writer
url= 'https://search.savills.com/list/property-for-sale/austria/page/'


for page in range(1,2): 
    req = requests.get(url + str(page)+'/')
    soup = BeautifulSoup(req.content, 'html.parser')


    lists = soup.find_all('div', class_="sv-details sv--show-price")

    with open ('HomeForSalesInAustria.csv', 'a', encoding='utf8', newline='') as f:
        thewriter = writer(f)
        header = ['Title','Address','Price','Size','bedrooms','bathrooms','ContactName','ContactPhone']
        thewriter.writerow(header)

        for list in lists:
            title = list.find('span', class_="sv-details__address1--truncate").text.replace('\n', '')
            address = list.find('p', class_="sv-details__address2").text.replace('\n', '')
            price = list.find('span', class_="sv-property-price__value").text.replace('\n', '')
            bedrooms = list.find('div', class_="sv-property-attribute sv--bedrooms")
            if bedrooms is not None:
                bedrooms = list.find('div', class_="sv-property-attribute sv--bedrooms").text.replace('\n', '')
            bathrooms = list.find('div', class_="sv-property-attribute sv--bathrooms")
            if bathrooms is not None:
                bathrooms = list.find('div', class_="sv-property-attribute sv--bathrooms").text.replace('\n', '')
            contactname = list.find('h6', class_="sv-details__contacts-name").text.replace('\n', '')
            contactphone = list.find('p', class_="sv-details__contacts-phone").text.replace('\n', '')
            
            info = [title,address,price,bedrooms,bathrooms,contactname,contactphone]
            thewriter.writerow(info)


     
        sleep(randint(2,10))


