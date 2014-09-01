from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
from pprint import pprint
import codecs
import sys,re,os
import urllib2
from bs4 import BeautifulSoup

def fetchBook (driver, bookinfo, start_from_page, end_at_page, fetch_wait_time = 1):

  driver.get("https://www.postyourbook.com/ucsd")
  time.sleep(1)
  # This while loop goes to the 'start_from_page'
  current_page_number = 1
  
  while(True):
    print "while1"
    if (current_page_number == start_from_page):
      break

    # This while loop continuely tries to click on the "next page" button
    waiting_sec = 0
    has_next_page_button = True
    while (True):
      print "while2"
      if (waiting_sec > 10):
        has_next_page_button = False
        break
      time.sleep(0.01)
      try:
        driver.find_element_by_xpath("//div[@class='tabcontrol postingouter']/div/div/a[@class='rightalign nbtn']").click()
        current_page_number = current_page_number + 1
        print "On page " + str(current_page_number)
        break
      except selenium.common.exceptions.ElementNotVisibleException:
        waiting_sec = waiting_sec + 0.01
        print "Can't see 'next page' button at current page: " + str(current_page_number)
        print "Waiting for " + str(waiting_sec) + " seconds..."
        continue

    if (has_next_page_button == False):
      print "Can't find next page button on page " + str(current_page_number) + ". Stop program"
      return bookinfo

  # This while loop fetches information from every post blocks and store it in bookinfo{}
  while (True):
    print "while3"
    print current_page_number
    print end_at_page
    if (current_page_number > end_at_page):
      break

    # This while loop fetches information for all post blocks
    waiting_sec = 0
    has_next_post_block = True
    while (True):
      print "while4"
      if (waiting_sec > 10):
        has_next_post_block = False
        break
      time.sleep(0.1)
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
        waiting_sec = waiting_sec + 0.1
        print "Can't see post block at current page: " + str(current_page_number)
        print "Waiting for " + str(waiting_sec) + " seconds..."
        continue
    
    if (has_next_post_block == False):
      print "Can't find next post block on page " + str(current_page_number) + ". Stop program"
      return bookinfo

    # This while loop fetches information on the first screen and then store it into bookinfo{}
    waiting_sec = 0
    total_post_block_number = len(booknames)
    current_post_block_number = 0
    element_attached = True
    while (True):
      print "while5"
      if (current_post_block_number >= total_post_block_number):
        break
      try:
        bookname = booknames[current_post_block_number].get_attribute("innerHTML")
      except selenium.common.exceptions.StaleElementReferenceException:
        booknames = driver.find_elements_by_xpath("//h3/a[@class='postingitem']")
        total_post_block_number = len(booknames)
        authors = driver.find_elements_by_class_name("p-authors")
        isbns = driver.find_elements_by_xpath("//div[@class='post-desc']/span")
        seller_numbers = driver.find_elements_by_xpath("//span[@class='owner']/span")
        most_recent_dates = driver.find_elements_by_xpath("//span[@class='clock']/span")
        student_lowest_prices = driver.find_elements_by_class_name("post-price")
        view_posting_buttons = driver.find_elements_by_xpath("//button[@class='postingitem vpostingsbtn askseller_btn rc-btn']")
        continue
      except IndexError:
        print "IndexError!"
        print "current_post_block_number = " + str(current_post_block_number)
        break
      bookinfo[bookname] = {}
      try:
        bookinfo[bookname]["author"] = authors[current_post_block_number].get_attribute("innerHTML").strip().split(':&nbsp;')[1]
      except selenium.common.exceptions.StaleElementReferenceException:
        booknames = driver.find_elements_by_xpath("//h3/a[@class='postingitem']")
        authors = driver.find_elements_by_class_name("p-authors")
        isbns = driver.find_elements_by_xpath("//div[@class='post-desc']/span")
        seller_numbers = driver.find_elements_by_xpath("//span[@class='owner']/span")
        most_recent_dates = driver.find_elements_by_xpath("//span[@class='clock']/span")
        student_lowest_prices = driver.find_elements_by_class_name("post-price")
        view_posting_buttons = driver.find_elements_by_xpath("//button[@class='postingitem vpostingsbtn askseller_btn rc-btn']")
        continue
      try:
        bookinfo[bookname]["isbn10"] = isbns[2*current_post_block_number].get_attribute("innerHTML").strip().split(":&nbsp;")[1]
      except selenium.common.exceptions.StaleElementReferenceException:
        booknames = driver.find_elements_by_xpath("//h3/a[@class='postingitem']")
        authors = driver.find_elements_by_class_name("p-authors")
        isbns = driver.find_elements_by_xpath("//div[@class='post-desc']/span")
        seller_numbers = driver.find_elements_by_xpath("//span[@class='owner']/span")
        most_recent_dates = driver.find_elements_by_xpath("//span[@class='clock']/span")
        student_lowest_prices = driver.find_elements_by_class_name("post-price")
        view_posting_buttons = driver.find_elements_by_xpath("//button[@class='postingitem vpostingsbtn askseller_btn rc-btn']")
        continue
      try:
        bookinfo[bookname]["isbn13"] = isbns[2*current_post_block_number+1].get_attribute("innerHTML").strip().split(":&nbsp;")[1]
      except selenium.common.exceptions.StaleElementReferenceException:
        booknames = driver.find_elements_by_xpath("//h3/a[@class='postingitem']")
        authors = driver.find_elements_by_class_name("p-authors")
        isbns = driver.find_elements_by_xpath("//div[@class='post-desc']/span")
        seller_numbers = driver.find_elements_by_xpath("//span[@class='owner']/span")
        most_recent_dates = driver.find_elements_by_xpath("//span[@class='clock']/span")
        student_lowest_prices = driver.find_elements_by_class_name("post-price")
        view_posting_buttons = driver.find_elements_by_xpath("//button[@class='postingitem vpostingsbtn askseller_btn rc-btn']")
        continue
      try:
        bookinfo[bookname]["seller_number"] = seller_numbers[current_post_block_number].get_attribute("innerHTML").strip().split("&nbsp")[0]
      except selenium.common.exceptions.StaleElementReferenceException:
        booknames = driver.find_elements_by_xpath("//h3/a[@class='postingitem']")
        authors = driver.find_elements_by_class_name("p-authors")
        isbns = driver.find_elements_by_xpath("//div[@class='post-desc']/span")
        seller_numbers = driver.find_elements_by_xpath("//span[@class='owner']/span")
        most_recent_dates = driver.find_elements_by_xpath("//span[@class='clock']/span")
        student_lowest_prices = driver.find_elements_by_class_name("post-price")
        view_posting_buttons = driver.find_elements_by_xpath("//button[@class='postingitem vpostingsbtn askseller_btn rc-btn']")
        continue
      try:
        bookinfo[bookname]["most_recent_date"] = most_recent_dates[current_post_block_number].get_attribute("innerHTML").strip()
      except selenium.common.exceptions.StaleElementReferenceException:
        booknames = driver.find_elements_by_xpath("//h3/a[@class='postingitem']")
        authors = driver.find_elements_by_class_name("p-authors")
        isbns = driver.find_elements_by_xpath("//div[@class='post-desc']/span")
        seller_numbers = driver.find_elements_by_xpath("//span[@class='owner']/span")
        most_recent_dates = driver.find_elements_by_xpath("//span[@class='clock']/span")
        student_lowest_prices = driver.find_elements_by_class_name("post-price")
        view_posting_buttons = driver.find_elements_by_xpath("//button[@class='postingitem vpostingsbtn askseller_btn rc-btn']")
        continue
      try:
        bookinfo[bookname]["student_lowest_price"] = student_lowest_prices[current_post_block_number].get_attribute("innerHTML").split("from")[1].strip()
      except selenium.common.exceptions.StaleElementReferenceException:
        booknames = driver.find_elements_by_xpath("//h3/a[@class='postingitem']")
        authors = driver.find_elements_by_class_name("p-authors")
        isbns = driver.find_elements_by_xpath("//div[@class='post-desc']/span")
        seller_numbers = driver.find_elements_by_xpath("//span[@class='owner']/span")
        most_recent_dates = driver.find_elements_by_xpath("//span[@class='clock']/span")
        student_lowest_prices = driver.find_elements_by_class_name("post-price")
        view_posting_buttons = driver.find_elements_by_xpath("//button[@class='postingitem vpostingsbtn askseller_btn rc-btn']")
        continue
      # This while loop clicks on the 'view postings' button
      waiting_sec = 0
      has_view_posting_button = True
      while (True):
        print "while6"
        if (waiting_sec > 10):
          has_view_posting_button = False
          break
        time.sleep(0.1)
        try:
          view_posting_buttons[current_post_block_number].click()
          break
        except selenium.common.exceptions.ElementNotVisibleException:
          waiting_sec = waiting_sec + 0.1
          print "Can't see 'view postings' button at current page: " + str(current_page_number) + ", at book '" + str(bookname)
          print "Waiting for " + str(waiting_sec) + " seconds..."
          continue
        except selenium.common.exceptions.StaleElementReferenceException:
          booknames = driver.find_elements_by_xpath("//h3/a[@class='postingitem']")
          authors = driver.find_elements_by_class_name("p-authors")
          isbns = driver.find_elements_by_xpath("//div[@class='post-desc']/span")
          seller_numbers = driver.find_elements_by_xpath("//span[@class='owner']/span")
          most_recent_dates = driver.find_elements_by_xpath("//span[@class='clock']/span")
          student_lowest_prices = driver.find_elements_by_class_name("post-price")
          view_posting_buttons = driver.find_elements_by_xpath("//button[@class='postingitem vpostingsbtn askseller_btn rc-btn']")
          print "Can't find 'view postings' button at current page: " + str(current_page_number) + ", at book '" + str(bookname)
          waiting_sec = waiting_sec + 0.1
          continue

      if (has_view_posting_button == False):
        current_post_block_number = current_post_block_number + 1
        continue
  

      # This while loop fetches information of all sellers for the current book and store it into bookinfo{}
      # loop breaks when there is no more clickable 'next page of sellers' button
      previous_item_seller_names = []
      while(True):
        print "while7"
        # This while loop fetches information of all sellers for the current book
        waiting_sec = 0
        has_seller_blocks = True
        on_new_seller_page = True
        while (True):
          print "while8"
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

            if (item_match_count > len(item_seller_names) - 1):
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
            waiting_sec = waiting_sec + 0.1
            print "Can't see seller block at current page: " + str(current_page_number)  + ", at book '" + str(bookname)
            print "Waiting for " + str(waiting_sec) + " seconds..."
            continue
        
        if (has_seller_blocks == False):
          # print "Can't find any seller block on page " + str(current_page_number) + ", book '" + str(bookname) + "'. Skip this book."
          time.sleep(0.1)
          driver.back()
          break

        if (on_new_seller_page == False):
          # print "Can't find 'next seller page' button on page " + str(current_page_number) + ", book '" + str(bookname) + "'. Skip this book."
          time.sleep(0.1)
          driver.back()
          break

        # This while loop gets information for each seller and store it into bookinfo{}
        total_seller_number = len(item_sellers)
        current_seller_number = 0
        while (True):
          print "while9"
          if (current_seller_number >= total_seller_number):
            break
          try:
            item_seller = item_sellers[current_seller_number].get_attribute("innerHTML")
          except selenium.common.exceptions.StaleElementReferenceException:
            item_post_dates = driver.find_elements_by_class_name("rc-u")
            item_schools = driver.find_elements_by_class_name("rc-s")
            item_conditions = driver.find_elements_by_class_name("rc-ic")
            item_markings = driver.find_elements_by_class_name("rc-m")
            item_sellers = driver.find_elements_by_class_name("rc-d")
            item_prices = driver.find_elements_by_class_name("rc-p")
            view_details_buttons = driver.find_elements_by_class_name("detailsbtn")
            item_schools = driver.find_elements_by_class_name("rc-s")
            total_seller_number = len(item_sellers)
            continue
          finally:
            driver.back()
            break
            # driver.back()
            # break

          bookinfo[bookname]['sellers'] = {}
          bookinfo[bookname]['sellers'][item_seller] = {}
          bookinfo[bookname]['sellers'][item_seller]["item_post_date"] = item_post_dates[current_seller_number].get_attribute("innerHTML")
          bookinfo[bookname]['sellers'][item_seller]["item_school"] = item_schools[current_seller_number].get_attribute("innerHTML")
          bookinfo[bookname]['sellers'][item_seller]["item_condition"] = item_conditions[current_seller_number].get_attribute("innerHTML")
          bookinfo[bookname]['sellers'][item_seller]["item_marking"] = item_markings[current_seller_number].get_attribute("innerHTML")
          bookinfo[bookname]['sellers'][item_seller]["item_price"] = item_prices[current_seller_number].get_attribute("innerHTML")
          
          # This while loop continuously tries to click on the 'view details' button
          waiting_sec = 0
          view_details_button_clickable = True
          indexError = False
          while (True):
            print "while10"
            if (waiting_sec > 10):
              view_details_button_clickable = False
              break
            try:
              view_details_buttons[current_seller_number].click()
              time.sleep(0.1)
              break
            except selenium.common.exceptions.ElementNotVisibleException:
              waiting_sec = waiting_sec + 0.1
              print "Can't see 'view details' button at current page: " + str(current_page_number) + ", at book '" + str(bookname) + "', at seller '" + str(item_seller)
              print "Waiting for " + str(waiting_sec) + " seconds..."
              time.sleep(0.1)
              continue
            except selenium.common.exceptions.StaleElementReferenceException:
              print "Can't find 'view details' button at current page: " + str(current_page_number) + ", at book '" + str(bookname) + "', at seller '" + str(item_seller)
              view_details_buttons = driver.find_elements_by_class_name("detailsbtn")
              continue
            except IndexError:
              print "IndexError"
              indexError = True
              break

          if (indexError == True):
            driver.back()
            break

          if (view_details_button_clickable == False):
            print "Can't click on view details button on page " + str(current_page_number) + ", book '" + str(bookname) + "', seller '" + str(item_seller) + "'. Skip to next seller."
            current_seller_number = current_seller_number + 1
            continue

          # (If clicked into the third screen,) get the book description and store it into bookinfo{}
          try:
            bookinfo[bookname]['sellers'][item_seller]["item_description"] = driver.find_element_by_xpath("//div[@class='single-main']/p").get_attribute("innerHTML")
          except selenium.common.exceptions.NoSuchElementException:
            bookinfo[bookname]['sellers'][item_seller]["item_description"] = None

          try:
            bookinfo[bookname]['sellers'][item_seller]["phone_number"] = driver.find_element_by_class_name("cp_phone").get_attribute("innerHTML").strip()
          except selenium.common.exceptions.NoSuchElementException:
            bookinfo[bookname]['sellers'][item_seller]["phone_number"] = None

          try:
            bookinfo[bookname]['sellers'][item_seller]["class_name"] = driver.find_element_by_class_name("cp_class_name").get_attribute("innerHTML").strip()
          except selenium.common.exceptions.NoSuchElementException:
            bookinfo[bookname]['sellers'][item_seller]["class_name"] = None

          try:
            bookinfo[bookname]['sellers'][item_seller]["teacher_name"] = driver.find_element_by_class_name("cp_teacher_name").get_attribute("innerHTML").strip()
          except selenium.common.exceptions.NoSuchElementException:
            bookinfo[bookname]['sellers'][item_seller]["teacher_name"] = None

          time.sleep(0.1)
          driver.back()
          current_seller_number = current_seller_number + 1

        # This while loop continuouesly tries to find the 'next seller page' button and click it
        max_waiting_sec = 2
        waiting_sec = 0
        FLAG_has_next_seller_button = True
        while (True):
          print "while11"
          if (waiting_sec >= max_waiting_sec):
            FLAG_has_next_seller_button = False
            break
          try:
            driver.find_element_by_xpath("//div[@class='item content_container active']/div[@class='tabcontrol instanceouter']/div[@class='paginationcontrol']/div[@class='pages']/a[@class='rightalign nbtn']").click()
            break
          except selenium.common.exceptions.NoSuchElementException:
            waiting_sec = waiting_sec + 0.1
            print "Can't find 'next seller page' button at current page: " + str(current_page_number) + ", at book '" + str(bookname)
            print "Waiting for " + str(waiting_sec) + " seconds..."
            time.sleep(0.1)
            continue
          except selenium.common.exceptions.ElementNotVisibleException:
            waiting_sec = waiting_sec + 0.1
            print "Can't see 'next seller page' button at current page: " + str(current_page_number) + ", at book " + str(bookname)
            print "Waiting for " + str(waiting_sec) + " seconds..."
            time.sleep(0.1)
            continue
          finally:
            break
        if (FLAG_has_next_seller_button == True):
          continue
        else:
          time.sleep(0.1)
          driver.back()
          break

      current_post_block_number = current_post_block_number + 1

      # This while loop fetches the partner's lowest price on current book (this loads the slowest)
      waiting_sec = 0
      while (True):
        print "while12"
        try:
          bookinfo[bookname]["partner_lowest_price"] = driver.find_element_by_class_name("aff-p").get_attribute("innerHTML")
          break
        except selenium.common.exceptions.NoSuchElementException:
          bookinfo[bookname]["partner_lowest_price"] = None
          break
        except selenium.common.exceptions.ElementNotVisibleException:
          waiting_sec = waiting_sec + 0.1
          print "Can't see 'See our partners price' panel at current page: " + str(current_page_number) + ", at book '" + str(bookname)
          print "Waiting for " + str(waiting_sec) + " seconds..."
          time.sleep(0.1)
          continue

    # This while loop continuously tries to click on the "next page" button
    max_waiting_sec = 2
    waiting_sec = 0
    while (True):
      print "while13"
      if (waiting_sec > max_waiting_sec):
        return bookinfo
      try:
        driver.find_element_by_xpath("//div[@class='tabcontrol postingouter']/div/div/a[@class='rightalign nbtn']").click()
        break
      except selenium.common.exceptions.ElementNotVisibleException:
        waiting_sec = waiting_sec + 0.1
        print "Can't see 'next page' panel at current page: " + str(current_page_number)
        print "Waiting for " + str(waiting_sec) + " seconds..."
        time.sleep(0.1)
        continue
    current_page_number = current_page_number + 1
    print "On page " + str(current_page_number)

def login (driver, username, password):
  driver.get("https://www.postyourbook.com/login")
  time.sleep(1)
  username_input = driver.find_element_by_xpath("//form[@class='signinform loginform']/div[@class='input-prepend']/input[@class='text your_login']")
  password_input = driver.find_element_by_xpath("//form[@class='signinform loginform']/div[@class='input-prepend']/input[@class='text your_password']")
  username_input.send_keys(username)
  password_input.send_keys(password)
  password_input.send_keys(Keys.RETURN)

if __name__=='__main__':
  start_from_page = int(sys.argv[1])
  end_at_page = int(sys.argv[2])
  username = str(sys.argv[3])
  password = str(sys.argv[4])

  driver = webdriver.Firefox()
  login (driver, username, password)
  time.sleep(2)

  allbookinfo = []
  i = start_from_page
  while (i < end_at_page):
    bookinfo = {}

    fetchBook(driver, bookinfo, i, i, 1)
    allbookinfo.append(bookinfo)
    i = i + 1

    # try:
    #   fetchBook(driver, bookinfo, i, i, 1)
    #   allbookinfo.append(bookinfo)
    #   i = i + 1
    # except:
    #   print "Error at page " + str(i)
    #   allbookinfo.append(bookinfo)
    #   i = i + 1
    #   continue
  output_file_name = "page" + str(start_from_page) + "-" + str(end_at_page - 1)
  output_file = codecs.open(output_file_name, "w+", 'utf8')

  output_string = ""
  for singlebookinfo in allbookinfo:
    for bookname in singlebookinfo:
      output_string += str(bookname)
      output_string += ":"
      try:
        output_string += str(singlebookinfo[bookname]['author'])
      except KeyError:
        output_string += "None"
      output_string += '|'
      try:
        output_string += str(singlebookinfo[bookname]['isbn10'])
      except KeyError:
        output_string += "None"
      output_string += '|'
      try:
        output_string += str(singlebookinfo[bookname]['isbn13'])
      except KeyError:
        output_string += "None"
      output_string += '|'
      try:
        output_string += str(singlebookinfo[bookname]['partner_lowest_price'])
      except KeyError:
        output_string += "None"
      output_string += '|'
      try:
        output_string += str(singlebookinfo[bookname]['seller_number'])
      except KeyError:
        output_string += "None"
      output_string += '|'
      try:
        output_string += str(singlebookinfo[bookname]['student_lowest_price'])
      except KeyError:
        output_string += "None"
      output_string += '/'
      output_string += 'Sellers:['
      try:
        sellers = singlebookinfo[bookname]['sellers']
      except KeyError:
        output_string += ']'
        continue
      for seller in singlebookinfo[bookname]['sellers']:
        output_string += str(seller)
        output_string += ':'
        try:
          output_string += str(singlebookinfo[bookname]['sellers'][seller]['item_price'])
        except KeyError:
          output_string += "None"
        output_string += '|'
        try:
          output_string += str(singlebookinfo[bookname]['sellers'][seller]['item_condition'])
        except KeyError:
          output_string += "None"
        output_string += '|'
        try:
          output_string += str(singlebookinfo[bookname]['sellers'][seller]['phone_number'])
        except KeyError:
          output_string += "None"
        output_string += ','
      output_string += '];\n'

  output_file.write(output_string)

  # hahathereisme, itisnanful1@gmail.com
  # erlanger, regrantmyassisstance@gmail.com
  # quertily, regrantmyassisstance2@gmail.com
  # bovanna, regrantmyassisstance1@gmail.com
  # retiligious, regrantmyassisstance3@gmail.com
  # tifoler, regrantmyassisstance4@gmail.com
  # hollisos, regrantmyassisstance5@gmail.com
  # ciaolis, regrantmyassisstance6@gmail.com
  # yellitis, stopmaking1@gmail.com
  # jakiolo, stopmaking2@gmail.com
  # , stopmaking1@yahoo.com

  # python steal.py 66 76 hahathereisme 3141592653
  # python steal.py 76 86 erlanger 3141592653
  # python steal.py 86 96 quertily 3141592653
  # python steal.py 96 106 bovanna 3141592653
  # python steal.py 106 116 retiligious 3141592653
  # python steal.py 116 126 tifoler 3141592653
  # python steal.py 126 136 hollisos 3141592653
  # python steal.py 36 41 ciaolis 3141592653
  # python steal.py 46 51 yellitis 3141592653
  # python steal.py 51 56 jakiolo 3141592653

