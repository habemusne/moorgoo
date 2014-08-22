from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
from pprint import pprint
import sys,re,os
import urllib2
from bs4 import BeautifulSoup

def fetchBook (driver, bookinfo, start_from_page, end_at_page, fetch_wait_time = 1):

  driver.get("https://www.postyourbook.com/ucsd")
  time.sleep(1)
  # This while loop goes to the 'start_from_page'
  current_page_number = 1
  
  while(True):
    if (current_page_number >= start_from_page):
      break

    # This while loop continuely tries to click on the "next page" button
    waiting_sec = 0
    has_next_page_button = True
    while (True):
      if (waiting_sec > 10):
        has_next_page_button = False
        break
      time.sleep(1)
      try:
        driver.find_element_by_xpath("//div[@class='tabcontrol postingouter']/div/div/a[@class='rightalign nbtn']").click()
        current_page_number = current_page_number + 1
        break
      except selenium.common.exceptions.ElementNotVisibleException:
        waiting_sec = waiting_sec + 1
        print "Can't see 'next page' button at current page: " + str(current_page_number) + ", waiting for " + str(waiting_sec) + " seconds..."
        continue

    if (has_next_page_button == False):
      print "Can't find next page button on page " + str(current_page_number) + ". Stop program"
      return

  # This while loop fetches information from every post blocks and store it in bookinfo{}
  while (True):
    if (current_page_number > end_at_page):
      break

    # This while loop fetches information for all post blocks
    waiting_sec = 0
    has_next_post_block = True
    while (True):
      if (waiting_sec > 10):
        has_next_post_block = False
        break
      time.sleep(1)
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
        print "Can't see post block at current page: " + str(current_page_number) + ", waiting for " + str(waiting_sec) + " seconds..."
        continue
    
    if (has_next_post_block == False):
      print "Can't find next post block on page " + str(current_page_number) + ". Stop program"
      return

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
      has_view_posting_button = True
      while (True):
        if (waiting_sec > 10):
          has_view_posting_button = False
          break
        time.sleep(1)
        try:
          view_posting_buttons[current_post_block_number].click()
          break
        except selenium.common.exceptions.ElementNotVisibleException:
          waiting_sec = waiting_sec + 1
          print "Can't see 'view postings' button at current page: " + str(current_page_number) + ", at book '" + str(bookname) +  "', waiting for " + str(waiting_sec) + " seconds..."
          continue

      if (has_view_posting_button == False):
        current_post_block_number = current_post_block_number + 1
        print "CONTINUE"
        continue
  

      # This while loop fetches information of all sellers for the current book and store it into bookinfo{}
      # loop breaks when there is no more clickable 'next page of sellers' button
      previous_item_seller_names = []
      while(True):

        # This while loop fetches information of all sellers for the current book
        waiting_sec = 0
        has_seller_blocks = True
        on_new_seller_page = True
        while (True):
          if (waiting_sec > 10):
            has_seller_blocks = False
            break
          time.sleep(1)
          try:
            item_sellers = driver.find_elements_by_class_name("rc-d")
            
            # This checks if the seller page is a new page (to see if clicking 'next seller page' button is effective)
            
            item_seller_names = []
            for i in range(0, len(item_sellers)):
              item_seller_names.append(item_sellers[i].get_attribute("innerHTML"))

            item_match_count = 0
            for i in range(0, len(item_seller_names)):
              if item_seller_names[i] in previous_item_seller_names:
                item_match_count = item_match_count + 1

            if (item_match_count == len(item_seller_names)):
              on_new_seller_page = False
              break
            for i in range(0, len(item_seller_names)):
              previous_item_seller_names.append(item_seller_names[i])

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
            print "Can't see seller block at current page: " + str(current_page_number)  + ", at book '" + str(bookname) + "', waiting for " + str(waiting_sec) + " seconds..."
            continue
        
        if (has_seller_blocks == False):
          print "Can't find any seller block on page " + str(current_page_number) + ", book '" + str(bookname) + "'. Skip this book."
          time.sleep(1)
          driver.back()
          break

        if (on_new_seller_page == False):
          print "Can't find 'next seller page' button on page " + str(current_page_number) + ", book '" + str(bookname) + "'. Skip this book."
          time.sleep(1)
          driver.back()
          break

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
          view_details_button_clickable = True
          while (True):
            if (waiting_sec > 10):
              view_details_button_clickable = False
              break
            try:
              view_details_buttons[current_seller_number].click()
              time.sleep(1)
              break
            except selenium.common.exceptions.ElementNotVisibleException:
              waiting_sec = waiting_sec + 1
              print "Can't see 'view details' button at current page: " + str(current_page_number) + ", at book '" + str(bookname) + "', at seller '" + str(item_seller) + "', waiting for " + str(waiting_sec) + " seconds..."
              time.sleep(1)
              continue
            except selenium.common.exceptions.StaleElementReferenceException:
              waiting_sec = waiting_sec + 1
              print "Can't see 'view details' button at current page: " + str(current_page_number) + ", at book '" + str(bookname) + "', at seller '" + str(item_seller) + "', waiting for " + str(waiting_sec) + " seconds..."
              time.sleep(1)
              continue

          if (view_details_button_clickable == False):
            print "Can't click on view details button on page " + str(current_page_number) + ", book '" + str(bookname) + "', seller '" + str(item_seller) + "'. Skip to next seller."
            current_seller_number = current_seller_number + 1
            continue

          # (If clicked into the third screen,) get the book description and store it into bookinfo{}
          try:
            bookinfo[bookname][item_seller]["item_description"] = driver.find_element_by_xpath("//div[@class='single-main']/p").get_attribute("innerHTML")
          except selenium.common.exceptions.NoSuchElementException:
            bookinfo[bookname][item_seller]["item_description"] = None

          try:
            bookinfo[bookname][item_seller]["phone_number"] = driver.find_element_by_class_name("cp_phone").get_attribute("innerHTML").strip()
          except selenium.common.exceptions.NoSuchElementException:
            bookinfo[bookname][item_seller]["phone_number"] = None

          try:
            bookinfo[bookname][item_seller]["class_name"] = driver.find_element_by_class_name("cp_class_name").get_attribute("innerHTML").strip()
          except selenium.common.exceptions.NoSuchElementException:
            bookinfo[bookname][item_seller]["class_name"] = None

          try:
            bookinfo[bookname][item_seller]["teacher_name"] = driver.find_element_by_class_name("cp_teacher_name").get_attribute("innerHTML").strip()
          except selenium.common.exceptions.NoSuchElementException:
            bookinfo[bookname][item_seller]["teacher_name"] = None

          time.sleep(1)
          driver.back()
          current_seller_number = current_seller_number + 1

        # This while loop continuouesly tries to find the 'next seller page' button and click it
        max_waiting_sec = 2
        waiting_sec = 0
        FLAG_has_next_seller_button = True
        while (True):
          if (waiting_sec >= max_waiting_sec):
            FLAG_has_next_seller_button = False
            break
          try:
            driver.find_element_by_xpath("//div[@class='item content_container active']/div[@class='tabcontrol instanceouter']/div[@class='paginationcontrol']/div[@class='pages']/a[@class='rightalign nbtn']").click()
            break
          except selenium.common.exceptions.NoSuchElementException:
            waiting_sec = waiting_sec + 1
            print "Can't find 'next seller page' button at current page: " + str(current_page_number) + ", at book '" + str(bookname) + "', waiting for " + str(waiting_sec) + " seconds..."
            time.sleep(1)
            continue
          except selenium.common.exceptions.ElementNotVisibleException:
            waiting_sec = waiting_sec + 1
            print "Can't see 'next seller page' button at current page: " + str(current_page_number) + ", at book " + str(bookname) + ", waiting for " + str(waiting_sec) + " seconds..."
            time.sleep(1)
            continue
        if (FLAG_has_next_seller_button == True):
          continue
        else:
          time.sleep(1)
          driver.back()
          break

      current_post_block_number = current_post_block_number + 1

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
          print "Can't see 'See our partners price' panel at current page: " + str(current_page_number) + ", at book '" + str(bookname) + "', waiting for " + str(waiting_sec) + " seconds..."
          time.sleep(1)
          continue

    # This while loop continuously tries to click on the "next page" button
    max_waiting_sec = 2
    waiting_sec = 0
    while (True):
      if (waiting_sec >= max_waiting_sec):
        return
      try:
        driver.find_element_by_xpath("//div[@class='tabcontrol postingouter']/div/div/a[@class='rightalign nbtn']").click()
        break
      except selenium.common.exceptions.ElementNotVisibleException:
        waiting_sec = waiting_sec + 1
        print "Can't see 'next page' panel at current page: " + str(current_page_number) + ", waiting for " + str(waiting_sec) + " seconds..."
        time.sleep(1)
        continue
    current_page_number = current_page_number + 1

if __name__=='__main__':
  driver = webdriver.Firefox()
  driver.get("https://www.postyourbook.com/login")
  time.sleep(1)
  username_input = driver.find_element_by_xpath("//form[@class='signinform loginform']/div[@class='input-prepend']/input[@class='text your_login']")
  password_input = driver.find_element_by_xpath("//form[@class='signinform loginform']/div[@class='input-prepend']/input[@class='text your_password']")
  username_input.send_keys("hahathereisme")
  password_input.send_keys("3141592653")
  password_input.send_keys(Keys.RETURN)
  time.sleep(3)

  allbookinfo = []
  i = 1
  while (i < 260):
    bookinfo = {}
    try:
      fetchBook(driver, bookinfo, i, i, 1)
      allbookinfo.append(bookinfo)
      i = i + 1
    except:
      print "Error at page " + str(i) + " and " + str(i+1)
      pprint(bookinfo)
      allbookinfo.append(bookinfo)
      i = i + 1
      continue
  pprint(bookinfo)

