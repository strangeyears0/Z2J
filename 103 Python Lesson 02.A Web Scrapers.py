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

# # exercise1
# from urllib.request import urlopen
# url = "http://olympus.realpython.org/profiles/dionysus"
# html_page = urlopen(url)
# html_text = html_page.read().decode("utf-8")
# # print(html_text)
#
# #ex 2
# for tag in["Name: ", "Favorite Color: "]:
#     tag_start = html_text.find(tag) + len(tag)
#     tag_end = html_text[tag_start:].find("<")
#     print(html_text[tag_start : tag_start + tag_end].strip("\n"))
#
# # ex3
#
# import re
#
# for tag in["Name: .*?[\n<]","Favorite Color: .*?[\n<]"]:
#     match_results = re.search(tag, html_text)
#     result = re.sub(".*:","",match_results.group())
#     print(result.strip(" \n<"))

#CREATE OBJECT IN BEAUTFULSOUP

# from bs4 import BeautifulSoup
# from urllib.request import urlopen
#
# url = "http://olympus.realpython.org/profiles/dionysus"
# page = urlopen(url)
# html = page.read().decode("utf-8")
# soup = BeautifulSoup(html,"html.parser")
# # print(soup.get_text())
# image1, image2 = soup.find_all("img")
# print(image1.name)
# print(image1["src"])
# print(soup.title)
# print(soup.title.string)
# print(soup.find_all("img",src = "/static/dionysus.jpg"))

# # ex1
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# # Exercise 1
# # Get the full HTML from the "profiles" page
# base_URL = "http://olympus.realpython.org"
# address = base_URL + "/profiles"
# html_page = urlopen(address)
# html_text = html_page.read().decode("utf-8")
# soup = BeautifulSoup(html_text, "html.parser")
#
# # Exercise 2
# # Parse out all the values of the page links
# for anchor in soup.find_all("a"):
#     # Could also have used urlparse.urljoin() to get absolute URL
#     link_address = base_URL + anchor["href"]
#     print(f"--- Fetching {link_address}:")
#
#     # Exercise 3
#     # Display the text in the HTML page of each link
#     link_page = urlopen(link_address)
#     link_text = link_page.read().decode("utf-8")
#     link_soup = BeautifulSoup(link_text, "html.parser")
#     print(link_soup.get_text())

# 16.3 Interact With HTML Forms

#create a browser object

# import mechanicalsoup
# browser = mechanicalsoup.Browser()
# url = "http://olympus.realpython.org/login"
# page = browser.get(url)
# print(page)
# print(type(page.soup))
# print(page.soup)

#submitting a a form with mechanicalsoup

# import mechanicalsoup
#
# browser = mechanicalsoup.Browser()
# url = "http://olympus.realpython.org/login"
# login_page = browser.get(url)
# login_html = login_page.soup
#
# form = login_html.select("form")[0]
# form.select("input")[0]["value"] = "zeus"
# form.select("input")[1]["value"] = "ThunderDude"
#
# profiles_page = browser.submit(form,login_page.url)
#
# print(profiles_page.url)
#
# links = profiles_page.soup.select("a")
#
# for link in links:
#     address = link["href"]
#     text = link.text
#     print(f"{text}:{address}")

#exercise1

# import mechanicalsoup
#
# browser =  mechanicalsoup.Browser()
# login_url = "http://olympus.realpython.org/login"
# login_page = browser.get(login_url)
# login_html = login_page.soup
#
# form = login_html.form
# form.select("input")[0]["value"] = "zeus"
# form.select("input")[1]["value"] = "ThunderDude"
#
# profiles_page = browser.submit(form, login_page.url)
# # ex2
# title = profiles_page.soup.title
# print(f"Title: {title.text}")
#
# #ex3
# login_page = browser.get(login_url)
# login_title = login_page.soup.title
# print(f"Title:{login_title.text}")
#
# # ex4
#
# form = login_html.form
# form.select("input")[0]["value"] = "wrong"
# form.select("input")[1]["value"] = "password"
# error_page = browser.submit(form,login_page.url)
#
# if error_page.soup.text.find("Wrong username or password!") != -1:
#     print("Login Failed.")
# else:
#     print("Login Successful.")

# 16.4 Interact With Websites in Real Time
# import time
# import mechanicalsoup
#
# browser = mechanicalsoup.Browser()
# for i in range(4):
#     page = browser.get("http://olympus.realpython.org/dice")
#     tag = page.soup.select("#result")[0]
#     result = tag.text
#     print(f"The result of your dice roll is {result}")
#     if i < 3:
#
#         time.sleep(10)
#
# import time
# print("I'm about to wait for five seconds")
# time.sleep(5)
# print("Done Waiting!")
#
# ex1

from time import sleep
import mechanicalsoup
my_browser = mechanicalsoup.Browser()

for i in range (0, 6):
    page = my_browser.get("http://olympus.realpython.org/dice")
    html_text = page.soup

    dice_result_tag = html_text.select("#result")

    dice_result = dice_result_tag[0].text

    time_tag = page.soup.select("#time")
    time = time_tag[0].text
    time = time[: time.find(" - ")]

    print(f"Rolled a {dice_result} on {time}")

    if i < 5:
        sleep(10)