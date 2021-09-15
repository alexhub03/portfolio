#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import csv

pages=[0,10,20,30,40,50,60,70,80,90,100]
file_name = "yelp_reviews_new.csv"
# set newline to be '' so that that new rows are appended without skipping any
f = csv.writer(open(file_name, 'w', newline=''))
 # write a new row as a header
f.writerow(['Name', 'Location', 'Reviews'])
for page in pages:
    source= requests.get('https://www.yelp.com/biz/bar-karaoke-lounge-toronto?start={}'.format(page))  #format page will iterate over the list
    print(source)
    soup = BeautifulSoup(source.text, 'html.parser')
    # print(soup)
    reviews=soup.find(class_="css-79elbk border-color--default__373c0__2oFDT")
    # print(reviews)
    # my_review=reviews.find_all('li',class_="margin-b5__373c0__2ErL8 border-color--default__373c0__2oFDT")
    my_review=reviews.find_all('li' ,class_="margin-b5__373c0__2ErL8 border-color--default__373c0__2oFDT") 
    # print((my_review))
    for reviews in my_review:
        people_name=reviews.find('span', class_="fs-block css-m6anxm").get_text()
        people_location=reviews.find('span', class_="css-n6i4z7").get_text()
        people_reviews=reviews.find('span',class_="raw__373c0__3rcx7").get_text()
        # print(people_name)
        # print(people_location)
        # print((people_reviews))
        # print('people_name', people_name)
        # print('people_location', people_location)
        # print('people_reviews', people_reviews)
        # print('Writing rows')
        # add the information as a row into the csv table
        f.writerow([people_name,people_location, people_reviews])
