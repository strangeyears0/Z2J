#Simple Web Scraper
#Exctracting TExt From HTML With Strings Methods

#
# from urllib.request import urlopen
# url = "http://olympus.realpython.org/profiles/aphrodite"
# # url = "http://olympus.realpython.org/profiles/poseidon"
#
# page = urlopen(url)
# print(page)
# html_bytes = page.read()
# html = html_bytes.decode("utf-8")
# title_index = html.find("<title>")
# start_index = title_index + len("<title>")
# end_index = html.find("</title>")
# title = html[start_index:end_index]
# print(title)

#REGULAR EXPRESSIONS
#
# import re
# # match_results = re.search("ab*c","ABC",re.IGNORECASE)
# # print(match_results.group())
#
# string = "Everything is <replaced> if it's in <tags>."
# # string = re.sub("<.*>","ELEPHANTS",string)
# # print(string)
# string = re.sub("<.*?>","ELEPHANTS",string)
# print(string)


# EXtracting Text From HTML With Regular Expressions

# import re
# from urllib.request import urlopen
#
# url = "http://olympus.realpython.org/profiles/dionysus"
# page = urlopen(url)
# html = page.read().decode("utf-8")
#
# pattern = "<title.*?>.*?</title.*?>"
# match_results = re.search(pattern,html,re.IGNORECASE)
# title = match_results.group()
# title = re.sub("<.*?>","",title) # REMOVE HTML TAGS
# print(title)

# exercise1
from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/dionysus"
html_page = urlopen(url)
html_text = html_page.read().decode("utf-8")
# print(html_text)

#ex 2
for tag in["Name: ", "Favorite Color: "]:
    tag_start = html_text.find(tag) + len(tag)
    tag_end = html_text[tag_start:].find("<")
    print(html_text[tag_start : tag_start + tag_end].strip("\n"))

# ex3

import re

for tag in["Name: .*?[\n<]","Favorite Color: .*?[\n<]"]:
    match_results = re.search(tag, html_text)
    result = re.sub(".*:","",match_results.group())
    print(result.strip(" \n<"))