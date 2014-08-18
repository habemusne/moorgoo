from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys,re,os
import urllib2
from bs4 import BeautifulSoup

def fetchBook (school, fetch_wait_time = 1):
  driver = webdriver.Chrome('/Users/a67/bin/chromedriver')
  driver.get("https://www.postyourbook.com/" + str(school))

  while (True):
    #Wait for the data to be fetched and displayed
    time.sleep(fetch_wait_time)

    # Get booknames
    booknames = driver.find_elements_by_xpath("//h3/a[@class='postingitem']")
    for bookname in booknames:
      source_code = bookname.get_attribute("innerHTML")
      # print source_code

    # Get authors
    authors = driver.find_elements_by_class_name("p-authors")
    for author in authors:
      source_code = author.get_attribute("innerHTML").strip().split(':&nbsp;')[1]
      # print source_code

    # Get ISBN10 and ISBN13
    isbns = driver.find_elements_by_xpath("//div[@class='post-desc']/span")
    ISBN10_arr = []
    ISBN13_arr = []
    for isbn in isbns:
      source_code = isbn.get_attribute("innerHTML").strip().split(":&nbsp;")
      if source_code[0] == str("ISBN10"):
        ISBN10_arr.append(source_code[1])
      elif source_code[0] == str("ISBN13"):
        ISBN13_arr.append(source_code[1])
      else:
        print "ISBN fetch error"
    # for i in ISBN10_arr:
    #   print i
    # for i in ISBN13_arr:
    #   print i

    # Get number of sellers
    seller_numbers = driver.find_elements_by_xpath("//span[@class='owner']/span")
    for seller_number in seller_numbers:
      source_code = seller_number.get_attribute("innerHTML").strip().split("&nbsp")[0]
      #print source_code

    # Get most recent date of posting
    most_recent_dates = driver.find_elemenqts_by_xpath("//span[@class='clock']/span")
    for most_recent_date in most_recent_dates:
      source_code = most_recent_date.get_attribute("innerHTML").strip()
      #print source_code

    # Get student's lowest posting price
    student_lowest_prices = driver.find_elements_by_class_name("post-price")
    for student_lowest_price in student_lowest_prices:
      source_code = student_lowest_price.get_attribute("innerHTML").split("from")[1].strip()
      print source_code

    # 

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