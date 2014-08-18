from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys,re,os
import urllib2
from bs4 import BeautifulSoup

def fetchBook (school, fetch_wait_time = 1):
  driver = webdriver.Chrome('/Users/a67/bin/chromedriver')
  driver.get("https://www.postyourbook.com/" + str(school))
  bookinfo = {}
  bookname_arr = []
  author_arr = []
  ISBN10_arr = []
  ISBN13_arr = []
  seller_number_arr = []
  most_recent_date_arr = []
  student_lowest_price_arr = []

  while (True):
    #Wait for the data to be fetched and displayed
    time.sleep(fetch_wait_time)
    book_counter = 0;

    # Get booknames
    booknames = driver.find_elements_by_xpath("//h3/a[@class='postingitem']")
    for bookname in booknames:
      book_counter = book_counter + 1
      # print source_code

    authors = driver.find_elements_by_class_name("p-authors")
    isbns = driver.find_elements_by_xpath("//div[@class='post-desc']/span")
    seller_numbers = driver.find_elements_by_xpath("//span[@class='owner']/span")
    most_recent_dates = driver.find_elements_by_xpath("//span[@class='clock']/span")
    student_lowest_prices = driver.find_elements_by_class_name("post-price")
    for i in range(0, book_counter):
      bookname_arr.append(booknames[i].get_attribute("innerHTML"))
      author_arr.append(authors[i].get_attribute("innerHTML").strip().split(':&nbsp;')[1])
      source_code = isbns[i].get_attribute("innerHTML").strip().split(":&nbsp;")
      if source_code[0] == str("ISBN10"):
        ISBN10_arr.append(source_code[1])
      elif source_code[0] == str("ISBN13"):
        ISBN13_arr.append(source_code[1])
      else:
        print "ISBN fetch error"
      seller_number_arr.append(seller_numbers[i].get_attribute("innerHTML").strip().split("&nbsp")[0])
      most_recent_date_arr.append(most_recent_dates[i].get_attribute("innerHTML").strip())
      student_lowest_price_arr.append(student_lowest_prices[i].get_attribute("innerHTML").split("from")[1].strip())

    # Wait for the "next page" button to show up. Solves ElementNotVisibleException
    time.sleep(fetch_wait_time)

    # Click on the "next page" button
    driver.find_element_by_xpath("//div[@class='tabcontrol postingouter']/div/div/a[@class='rightalign nbtn']").click()
    

if __name__=='__main__':
  fetchBook("ucsd", 1)
# 1. User specify object_url
# 2. Program goes to url
# 3. Program fetches the first book results shown on page
#   - Results contain: 
#   - Fetched results are stored as ()
# 4. Program click on "->" button
# 5. Program continues from step 3, until "->" is not clickable
# 6. 