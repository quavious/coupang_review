# -*- encoding: utf-8 -*-

import sys
import requests
from bs4 import BeautifulSoup
import csv
import os
import re

def save_to_file(one_list):
    filename = "./coupang_data.csv"
    file = open(filename, mode="w")
    writer = csv.writer(file)
    print(file)
    writer.writerow(["user", "title","main_content"])
    for i in one_list:
        writer.writerow(i)
    return


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.146 Whale/2.6.90.16 Safari/537.36"}

#item_id = input(input item id : )

names=[]
titles=[]
contents=[]

all_list=[]
total_list=[]

url = "https://www.coupang.com/vp/products/193688164?itemId=532740640&isAddedCart="
review_url="https://www.coupang.com/vp/product/reviews?productId=193688164&page=1&size=5&sortBy=ORDER_SCORE_ASC&ratings=&q=&viRoleCode=3&ratingSummary=true"

html = requests.get(review_url, headers = headers)
print(html.status_code)
#soup = BeautifulSoup(html.text, "html.parser")
#review = soup.find_all("div",{"class":"sdp-review__article__list__review__content js_reviewArticleContent"})
#print(review)
soup=BeautifulSoup(html.text, "html.parser")
review_name = soup.find_all("span",{"class":"sdp-review__article__list__info__user__name js_reviewUserProfileImage"})
for i in review_name:
    text = re.sub('<.+?>', '', str(i), 0).strip()
    text = text.replace("\n"," ")
    names.append(text)
review_title = soup.find_all("div",{"class":"sdp-review__article__list__headline"})
for i in review_title:
    text = re.sub('<.+?>', '', str(i), 0).strip()
    text = text.replace("\n"," ")
    if text != " ":
        titles.append(text)
    else:
        titles.append("No titles found")    

review_content = soup.find_all("div",{"class":"sdp-review__article__list__review__content js_reviewArticleContent"})
for i in review_content:
    text = re.sub('<.+?>', '', str(i), 0).strip()
    text = re.sub('[^가-힝0-9a-zA-Z\\s]', '', text)
    text = text.replace("\n"," ")
    if len(text) > 150:
        text = text[:150] + " ...."
    contents.append(text)

width = len(titles)
max_width = len(names)

for i in range(width): 
    all_list=[names[i], titles[i], contents[i]]
    total_list.append(all_list)

for j in range(max_width - width):
    all_list=[names[j+width], "No titles found", contents[j+width]]
    total_list.append(all_list)    

save_to_file(total_list)    