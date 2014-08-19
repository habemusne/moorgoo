from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
from pprint import pprint
import sys,re,os
import urllib2
from bs4 import BeautifulSoup

def fetchBook (school, fetch_wait_time = 1):
  driver = webdriver.Firefox()
  driver.get("https://www.postyourbook.com/" + str(school))
  bookinfo = {}
  bookname_arr = []
  author_arr = []
  ISBN10_arr = []
  ISBN13_arr = []
  seller_number_arr = []
  most_recent_date_arr = []
  student_lowest_price_arr = []
  partner_lowest_price_arr = []

  while (True):
    #Wait for the data to be fetched and displayed
    time.sleep(fetch_wait_time)

    # Get booknames
    booknames = driver.find_elements_by_xpath("//h3/a[@class='postingitem']")
    authors = driver.find_elements_by_class_name("p-authors")
    isbns = driver.find_elements_by_xpath("//div[@class='post-desc']/span")
    seller_numbers = driver.find_elements_by_xpath("//span[@class='owner']/span")
    most_recent_dates = driver.find_elements_by_xpath("//span[@class='clock']/span")
    student_lowest_prices = driver.find_elements_by_class_name("post-price")
    view_posting_buttons = driver.find_elements_by_xpath("//button[@class='postingitem vpostingsbtn askseller_btn rc-btn']")
    for i in range(0, len(booknames)):
      time.sleep(fetch_wait_time)
      bookname = booknames[i].get_attribute("innerHTML")
      bookinfo[bookname] = {}
      bookinfo[bookname]["author"] = authors[i].get_attribute("innerHTML").strip().split(':&nbsp;')[1]
      bookinfo[bookname]["isbn10"] = isbns[2*i].get_attribute("innerHTML").strip().split(":&nbsp;")[1]
      bookinfo[bookname]["isbn13"] = isbns[2*i+1].get_attribute("innerHTML").strip().split(":&nbsp;")[1]
      bookinfo[bookname]["seller_number"] = seller_numbers[i].get_attribute("innerHTML").strip().split("&nbsp")[0]
      bookinfo[bookname]["most_recent_date"] = most_recent_dates[i].get_attribute("innerHTML").strip()
      bookinfo[bookname]["student_lowest_price"] = student_lowest_prices[i].get_attribute("innerHTML").split("from")[1].strip()
      time.sleep(fetch_wait_time)
      view_posting_buttons[i].click()
      time.sleep(fetch_wait_time + 1)

      try:
        bookinfo[bookname]["partner_lowest_price"] = driver.find_element_by_class_name("aff-p").get_attribute("innerHTML")
      except selenium.common.exceptions.NoSuchElementException:
        bookinfo[bookname]["partner_lowest_price"] = None
    
      while(True):

        item_sellers = driver.find_elements_by_class_name("rc-d")
        item_post_dates = driver.find_elements_by_class_name("rc-u")
        item_schools = driver.find_elements_by_class_name("rc-s")
        item_conditions = driver.find_elements_by_class_name("rc-ic")
        item_markings = driver.find_elements_by_class_name("rc-m")
        item_sellers = driver.find_elements_by_class_name("rc-d")
        item_prices = driver.find_elements_by_class_name("rc-p")
        view_details_buttons = driver.find_elements_by_class_name("detailsbtn")
        for i in range(0, len(item_sellers)):
          item_seller = item_sellers[i].get_attribute("innerHTML")
          bookinfo[bookname][item_seller] = {}
          bookinfo[bookname][item_seller]["item_post_date"] = item_post_dates[i].get_attribute("innerHTML")
          bookinfo[bookname][item_seller]["item_school"] = item_schools[i].get_attribute("innerHTML")
          bookinfo[bookname][item_seller]["item_condition"] = item_conditions[i].get_attribute("innerHTML")
          bookinfo[bookname][item_seller]["item_marking"] = item_markings[i].get_attribute("innerHTML")
          bookinfo[bookname][item_seller]["item_price"] = item_prices[i].get_attribute("innerHTML")
          view_details_buttons[i].click()
          time.sleep(fetch_wait_time)
          try:
            bookinfo[bookname][item_seller]["item_description"] = driver.find_element_by_xpath("//div[@class='single-main']/p").get_attribute("innerHTML")
          except selenium.common.exceptions.NoSuchElementException:
            bookinfo[bookname][item_seller]["item_description"] = None
          driver.back()
        try:
          driver.find_element_by_xpath("//div[@class='item content_container active']/div[@class='tabcontrol instanceouter']/div[@class='paginationcontrol']/div[@class='pages']/a[@class='rightalign nbtn']").click()
          time.sleep(fetch_wait_time + 1)
        except selenium.common.exceptions.NoSuchElementException:
          print "NoSuchElementException when clicking next seller page button"
          driver.back()
          pprint(bookinfo)
          break
        except selenium.common.exceptions.ElementNotVisibleException:
          print "ElementNotVisibleException when clicking next seller page button"
          driver.back()
          pprint(bookinfo)
          break
      print "CONTINUE"

    time.sleep(fetch_wait_time)

    # Click on the "next page" button
    try:
      driver.find_element_by_xpath("//div[@class='tabcontrol postingouter']/div/div/a[@class='rightalign nbtn']").click()
    except selenium.common.exceptions.ElementNotVisibleException:
      exit()

if __name__=='__main__':
  fetchBook("ucsd", 1)

