from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
from pprint import pprint
import sys,re,os
import urllib2
from bs4 import BeautifulSoup

def fetchBook (school, start_from_page, end_at_page, fetch_wait_time = 1):
  driver = webdriver.Firefox()
  driver.get("https://www.postyourbook.com/" + str(school))
  bookinfo = {}
  time.sleep(fetch_wait_time)

  # This while loop goes to the 'start_from_page'
  current_page_number = 1
  
  while(True):
    if (current_page_number >= start_from_page):
      break

    # This while loop continuely tries to click on the "next page" button
    waiting_sec = 0
    while (True):
      try:
        driver.find_element_by_xpath("//div[@class='tabcontrol postingouter']/div/div/a[@class='rightalign nbtn']").click()
        current_page_number = current_page_number + 1
        break
      except selenium.common.exceptions.ElementNotVisibleException:
        waiting_sec = waiting_sec + 1
        print "Can't see 'next page' button at current page: " + current_page_number + ", waiting for " + waiting_sec + " seconds..."
        time.sleep(1)
        continue

  # This while loop fetches information from every post blocks and store it in bookinfo{}
  while (True):
    if (current_page_number >= end_at_page):
      break

    # This while loop fetches information for all post blocks
    waiting_sec = 0
    while (True):
      try:
        booknames = driver.find_elements_by_xpath("//h3/a[@class='postingitem']")
        authors = driver.find_elements_by_class_name("p-authors")
        isbns = driver.find_elements_by_xpath("//div[@class='post-desc']/span")
        seller_numbers = driver.find_elements_by_xpath("//span[@class='owner']/span")
        most_recent_dates = driver.find_elements_by_xpath("//span[@class='clock']/span")
        student_lowest_prices = driver.find_elements_by_class_name("post-price")
        view_posting_buttons = driver.find_elements_by_xpath("//button[@class='postingitem vpostingsbtn askseller_btn rc-btn']")
        break
      except selenium.common.exceptions.ElementNotVisibleException:
        waiting_sec = waiting_sec + 1
        print "Can't see post block at current page: " + current_page_number + ", waiting for " + waiting_sec + " seconds..."
        time.sleep(1)
        continue
    
    # This while loop fetches information on the first screen and then store it into bookinfo{}
    waiting_sec = 0
    total_post_block_number = len(booknames)
    current_post_block_number = 0
    while (True):
      if (current_post_block_number >= total_post_block_number):
        break
      bookname = booknames[current_post_block_number].get_attribute("innerHTML")
      bookinfo[bookname] = {}
      bookinfo[bookname]["author"] = authors[current_post_block_number].get_attribute("innerHTML").strip().split(':&nbsp;')[1]
      bookinfo[bookname]["isbn10"] = isbns[2*current_post_block_number].get_attribute("innerHTML").strip().split(":&nbsp;")[1]
      bookinfo[bookname]["isbn13"] = isbns[2*current_post_block_number+1].get_attribute("innerHTML").strip().split(":&nbsp;")[1]
      bookinfo[bookname]["seller_number"] = seller_numbers[current_post_block_number].get_attribute("innerHTML").strip().split("&nbsp")[0]
      bookinfo[bookname]["most_recent_date"] = most_recent_dates[current_post_block_number].get_attribute("innerHTML").strip()
      bookinfo[bookname]["student_lowest_price"] = student_lowest_prices[current_post_block_number].get_attribute("innerHTML").split("from")[1].strip()
      
      # This while loop clicks on the 'view postings' button
      waiting_sec = 0
      while (True):
        try:
          view_posting_buttons[current_post_block_number].click()
          break
        except selenium.common.exceptions.ElementNotVisibleException:
          waiting_sec = waiting_sec + 1
          print "Can't see 'view postings' button at current page: " + current_page_number + ", waiting for " + waiting_sec + " seconds..."
          time.sleep(1)
          continue

      # This while loop fetches information of all sellers for the current book and store it into bookinfo{}
      # loop breaks when there is no more clickable 'next page of sellers' button
      while(True):

        # This while loop fetches information of all sellers for the current book
        waiting_sec = 0
        while (True):
          try:
            item_sellers = driver.find_elements_by_class_name("rc-d")
            item_post_dates = driver.find_elements_by_class_name("rc-u")
            item_schools = driver.find_elements_by_class_name("rc-s")
            item_conditions = driver.find_elements_by_class_name("rc-ic")
            item_markings = driver.find_elements_by_class_name("rc-m")
            item_sellers = driver.find_elements_by_class_name("rc-d")
            item_prices = driver.find_elements_by_class_name("rc-p")
            view_details_buttons = driver.find_elements_by_class_name("detailsbtn")
            break
          except selenium.common.exceptions.ElementNotVisibleException:
            waiting_sec = waiting_sec + 1
            print "Can't see seller block at current page: " + current_page_number + ", waiting for " + waiting_sec + " seconds..."
            time.sleep(1)
            continue

        # This while loop gets information for each seller and store it into bookinfo{}
        total_seller_number = len(item_sellers)
        current_seller_number = 0
        while (True):
          if (current_seller_number >= total_seller_number):
            break
          item_seller = item_sellers[current_seller_number].get_attribute("innerHTML")
          bookinfo[bookname][item_seller] = {}
          bookinfo[bookname][item_seller]["item_post_date"] = item_post_dates[current_seller_number].get_attribute("innerHTML")
          bookinfo[bookname][item_seller]["item_school"] = item_schools[current_seller_number].get_attribute("innerHTML")
          bookinfo[bookname][item_seller]["item_condition"] = item_conditions[current_seller_number].get_attribute("innerHTML")
          bookinfo[bookname][item_seller]["item_marking"] = item_markings[current_seller_number].get_attribute("innerHTML")
          bookinfo[bookname][item_seller]["item_price"] = item_prices[current_seller_number].get_attribute("innerHTML")
          
          # This while loop continuously tries to click on the 'view details' button
          waiting_sec = 0
          while (True):
            try:
              view_details_buttons[current_seller_number].click()
              break
            except selenium.common.exceptions.ElementNotVisibleException:
              waiting_sec = waiting_sec + 1
              print "Can't see 'view details' button at current page: " + current_page_number + ", waiting for " + waiting_sec + " seconds..."
              time.sleep(1)
              continue
        
          # (If clicked into the third screen,) get the book description and store it into bookinfo{}
          try:
            bookinfo[bookname][item_seller]["item_description"] = driver.find_element_by_xpath("//div[@class='single-main']/p").get_attribute("innerHTML")
          except selenium.common.exceptions.NoSuchElementException:
            bookinfo[bookname][item_seller]["item_description"] = None
          driver.back()
          current_seller_number = current_seller_number + 1

        # This while loop continuouesly tries to find the 'next seller page' button and click it
        max_waiting_sec = 2
        waiting_sec = 0
        while (True):
          if (waiting_sec >= max_waiting_sec):
            break
          try:
            driver.find_element_by_xpath("//div[@class='item content_container active']/div[@class='tabcontrol instanceouter']/div[@class='paginationcontrol']/div[@class='pages']/a[@class='rightalign nbtn']").click()
            break
          except selenium.common.exceptions.NoSuchElementException:
            waiting_sec = waiting_sec + 1
            print "Can't find 'next seller page' button at current page: " + current_page_number + ", waiting for " + waiting_sec + " seconds..."
            time.sleep(1)
            continue
          except selenium.common.exceptions.ElementNotVisibleException:
            waiting_sec = waiting_sec + 1
            print "Can't see 'next seller page' button at current page: " + current_page_number + ", waiting for " + waiting_sec + " seconds..."
            time.sleep(1)
            continue
        driver.back()
        pprint(bookinfo)
      current_post_block_number = current_post_block_number + 1
      print "CONTINUE"

      # This while loop fetches the partner's lowest price on current book (this loads the slowest)
      waiting_sec = 0
      while (True):
        try:
          bookinfo[bookname]["partner_lowest_price"] = driver.find_element_by_class_name("aff-p").get_attribute("innerHTML")
          break
        except selenium.common.exceptions.NoSuchElementException:
          bookinfo[bookname]["partner_lowest_price"] = None
          break
        except selenium.common.exceptions.ElementNotVisibleException:
          waiting_sec = waiting_sec + 1
          print "Can't see 'See our partners price' panel at current page: " + current_page_number + ", waiting for " + waiting_sec + " seconds..."
          time.sleep(1)
          continue

    # This while loop continuously tries to click on the "next page" button
    max_waiting_sec = 2
    waiting_sec = 0
    while (True):
      if (waiting_sec >= max_waiting_sec):
        exit()
      try:
        driver.find_element_by_xpath("//div[@class='tabcontrol postingouter']/div/div/a[@class='rightalign nbtn']").click()
        break
      except selenium.common.exceptions.ElementNotVisibleException:
        waiting_sec = waiting_sec + 1
        print "Can't see 'next page' panel at current page: " + current_page_number + ", waiting for " + waiting_sec + " seconds..."
        time.sleep(1)
        continue
    current_page_number = current_page_number + 1

if __name__=='__main__':
  fetchBook("ucsd", 1, 4, 1)

