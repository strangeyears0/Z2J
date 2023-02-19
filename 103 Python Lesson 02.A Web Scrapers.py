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

import re
# match_results = re.search("ab*c","ABC",re.IGNORECASE)
# print(match_results.group())

string = "Everything is <replaced> if it's in <tags>."
# string = re.sub("<.*>","ELEPHANTS",string)
# print(string)
string = re.sub("<.*?>","ELEPHANTS",string)
print(string)
