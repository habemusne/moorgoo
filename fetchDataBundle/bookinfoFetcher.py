from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
import logging
from pprint import pprint
import sys,re,os

MAX_WAITING_SEC = 10
MAX_WAITING_SEC_SECONDARY = 3
GENERAL_WAITING_SEC = 1
HARD_WAITING_SEC = 2
EMAIL_REGEX_OBJ = re.compile('\b[A-Z0-9._%+-]+@(?:[A-Z0-9-]+\.)+[A-Z]{2,4}\b', re.IGNORECASE)

def submitBooknameSearch(driver, bookname, waiting_increment = 0.1):
  waiting_sec = 0
  while (True):
    if (waiting_sec > MAX_WAITING_SEC):
      return False
    try:
      search_field = driver.find_element_by_id("searchField")
      break
    except selenium.common.exceptions.ElementNotVisibleException:
      waiting_sec = waiting_sec + waiting_increment
      time.sleep(waiting_increment)
      print "    ElementNotVisibleException. Waiting for " + str(waiting_sec) + " seconds..."      
      continue

  search_field.clear()
  search_field.send_keys(bookname.decode("utf8"))
  search_field.send_keys(Keys.RETURN)
  return True

def fetchPostBlock(driver, bookinfo, waiting_increment = 0.1):
  waiting_sec = 0
  while (True):
    if (waiting_sec > MAX_WAITING_SEC):
      return False
    try:      
      bookname = driver.find_element_by_xpath("//h3/a[@class='postingitem']").get_attribute("innerHTML")
      author = driver.find_element_by_class_name("p-authors").get_attribute("innerHTML").strip().split(':&nbsp;')[1]
      isbn10 = driver.find_elements_by_xpath("//div[@class='post-desc']/span")[0].get_attribute("innerHTML").strip().split(":&nbsp;")[1]
      isbn13 = driver.find_elements_by_xpath("//div[@class='post-desc']/span")[1].get_attribute("innerHTML").strip().split(":&nbsp;")[1]
      seller_number = driver.find_element_by_xpath("//span[@class='owner']/span").get_attribute("innerHTML").strip().split("&nbsp")[0]
      most_recent_date = driver.find_element_by_xpath("//span[@class='clock']/span").get_attribute("innerHTML").strip()
      student_lowest_price = driver.find_element_by_class_name("post-price").get_attribute("innerHTML").split("from")[1].strip()
      break
    except selenium.common.exceptions.ElementNotVisibleException:
      waiting_sec = waiting_sec + waiting_increment
      time.sleep(waiting_increment)
      print "    ElementNotVisibleException. Waiting for " + str(waiting_sec) + " seconds..."
      continue
  bookinfo["bookname"] = bookname
  bookinfo["author"] = author
  bookinfo["isbn10"] = isbn10
  bookinfo["isbn13"] = isbn13
  bookinfo["seller_number"] = seller_number
  bookinfo["most_recent_date"] = most_recent_date
  bookinfo["student_lowest_price"] = student_lowest_price
  pprint(bookinfo)
  return True

# def clickViewPostingButton(driver, view_posting_button):
#   try:
#     view_posting_button.click()
#     return True
#   except selenium.common.exceptions.StaleElementReferenceException:
#     return False

def fetchSellername(driver, waiting_increment = 0.1):
  waiting_sec = 0
  while(True):
    if (waiting_sec > GENERAL_WAITING_SEC):
      seller_name = None
      break
    try:
      seller_name = driver.find_element_by_id("cp_author").get_attribute("innerHTML").split("</span>")[1].strip()
      break
    except selenium.common.exceptions.NoSuchElementException:
      waiting_sec = waiting_sec + waiting_increment
      time.sleep(waiting_increment)
      print "      NoSuchElementException. Waiting for " + str(waiting_sec) + " seconds..."
      continue      
  return seller_name

def fetchPhonenumber(driver, waiting_increment = 0.1):
  waiting_sec = 0
  while(True):
    if (waiting_sec > GENERAL_WAITING_SEC/10):
      phone_number = None
      break
    try:
      phone_number = driver.find_element_by_xpath("//li[@id='cp_phone']").get_attribute("innerHTML").split("</span>")[1].strip()
      break
    except selenium.common.exceptions.NoSuchElementException:
      waiting_sec = waiting_sec + waiting_increment
      time.sleep(waiting_increment)
      print "      NoSuchElementException. Waiting for " + str(waiting_sec) + " seconds..."
      continue      
  return phone_number

def fetchISBN(driver, waiting_increment = 0.1):
  waiting_sec = 0
  while(True):
    if (waiting_sec > GENERAL_WAITING_SEC/10):
      isbn = None
      break
    try:
      isbn = driver.find_element_by_xpath("//li[@id='cp_isbn']").get_attribute("innerHTML").split("</span>")[1].strip()
      break
    except selenium.common.exceptions.NoSuchElementException:
      waiting_sec = waiting_sec + waiting_increment
      time.sleep(waiting_increment)
      print "      NoSuchElementException. Waiting for " + str(waiting_sec) + " seconds..."
      continue      
  return isbn

def fetchClassname(driver, waiting_increment = 0.1):
  waiting_sec = 0
  while(True):
    if (waiting_sec > GENERAL_WAITING_SEC/10):
      class_name = None
      break
    try:
      class_name = driver.find_element_by_xpath("//li[@id='cp_class_name']").get_attribute("innerHTML").split("</span>")[1].strip()
      break
    except selenium.common.exceptions.NoSuchElementException:
      waiting_sec = waiting_sec + waiting_increment
      time.sleep(waiting_increment)
      print "      NoSuchElementException. Waiting for " + str(waiting_sec) + " seconds..."
      continue      
  return class_name

def fetchTeachername(driver, waiting_increment = 0.1):
  waiting_sec = 0
  while(True):
    if (waiting_sec > GENERAL_WAITING_SEC/10):
      teacher_name = None
      break
    try:
      teacher_name = driver.find_element_by_xpath("//li[@id='cp_teacher_name']").get_attribute("innerHTML").split("</span>")[1].strip()
      break
    except selenium.common.exceptions.NoSuchElementException:
      waiting_sec = waiting_sec + waiting_increment
      time.sleep(waiting_increment)
      print "      NoSuchElementException. Waiting for " + str(waiting_sec) + " seconds..."
      continue      
  return teacher_name

def fetchCondition(driver, waiting_increment = 0.1):
  waiting_sec = 0
  while(True):
    if (waiting_sec > GENERAL_WAITING_SEC/10):
      condition = None
      break
    try:
      condition = driver.find_element_by_xpath("//li[@id='cp_condition_name']").get_attribute("innerHTML").split("</span>")[1].strip()
      break
    except selenium.common.exceptions.NoSuchElementException:
      waiting_sec = waiting_sec + waiting_increment
      time.sleep(waiting_increment)
      print "      NoSuchElementException. Waiting for " + str(waiting_sec) + " seconds..."
      continue      
  return condition

def fetchPosttime(driver, waiting_increment = 0.1):
  waiting_sec = 0
  while(True):
    if (waiting_sec > GENERAL_WAITING_SEC/10):
      post_time = None
      break
    try:
      post_time = driver.find_element_by_xpath("//li[@id='cp_listed']").get_attribute("innerHTML").split("</span>")[1].strip()
      break
    except selenium.common.exceptions.NoSuchElementException:
      waiting_sec = waiting_sec + waiting_increment
      time.sleep(waiting_increment)
      print "      NoSuchElementException. Waiting for " + str(waiting_sec) + " seconds..."
      continue      
  return post_time

def fetchDescription(driver, waiting_increment = 0.1):
  waiting_sec = 0
  while(True):
    if (waiting_sec > GENERAL_WAITING_SEC/10):
      description = None
      break
    try:
      description = driver.find_element_by_xpath("//div[@class='single-main']/p").get_attribute("innerHTML").strip()
      break
    except selenium.common.exceptions.NoSuchElementException:
      waiting_sec = waiting_sec + waiting_increment
      time.sleep(waiting_increment)
      print "      NoSuchElementException. Waiting for " + str(waiting_sec) + " seconds..."
      continue      
  return description

def fetchTotalViews(driver, waiting_increment = 0.1):
  waiting_sec = 0
  while(True):
    if (waiting_sec > GENERAL_WAITING_SEC/10):
      total_view = None
      break
    try:
      total_view = driver.find_element_by_xpath("//p[@class='stats']").get_attribute("innerHTML").split(" ")[0].strip()
      break
    except selenium.common.exceptions.NoSuchElementException:
      waiting_sec = waiting_sec + waiting_increment
      time.sleep(waiting_increment)
      print "      NoSuchElementException. Waiting for " + str(waiting_sec) + " seconds..."
      continue      
  return total_view

def fetchPrice(driver, waiting_increment = 0.1):
  waiting_sec = 0
  while(True):
    if (waiting_sec > GENERAL_WAITING_SEC/10):
      price = None
      break
    try:
      price = driver.find_element_by_xpath("//div[@class='item content_container active']/div[@id='details_container']/div[@class='shadowblock_out']/div[@class='shadowblock']/div/div[@class='price-wrap']/p[@class='post-price']").get_attribute("innerHTML").strip()
      break
    except selenium.common.exceptions.NoSuchElementException:
      waiting_sec = waiting_sec + waiting_increment
      time.sleep(waiting_increment)
      print "      NoSuchElementException. Waiting for " + str(waiting_sec) + " seconds..."
      continue
  return price

def checkEmailProvided(description):
  try:
    emails = EMAIL_REGEX_OBJ.findall(str(description.encode("utf-8")))
  except AttributeError: # description is None
    return None
  if (emails == []):
    return None
  else:
    return emails[0]

def clickNextSellerPage(driver, waiting_increment = 01):
  waiting_sec = 0
  while (True):
    if (waiting_sec > MAX_WAITING_SEC_SECONDARY):
      return False
    try:
      driver.find_element_by_xpath("//div[@class='item content_container active']/div[@class='tabcontrol instanceouter']/div[@class='paginationcontrol']/div[@class='pages']/a[@class='rightalign nbtn']").click()
      break
    except selenium.common.exceptions.ElementNotVisibleException:
      waiting_sec = waiting_sec + waiting_increment
      print "    ElementNotVisibleException. Waiting for " + str(waiting_sec) + " seconds..."
      time.sleep(waiting_increment)
      continue
    except selenium.common.exceptions.NoSuchElementException:
      print "    NoSuchElementException. Continue to next post block"
      return False
  return True

def fetchSellerNames(driver, waiting_increment = 0.1):
  waiting_sec = 0
  while(True):
    seller_names = []
    if (waiting_sec > GENERAL_WAITING_SEC):
      seller_names = []
      break
    try:
      seller_namesHandler = driver.find_elements_by_class_name("rc-d")
      for handler in seller_namesHandler:
        seller_names.append(handler.get_attribute("innerHTML"))
      break
    except selenium.common.exceptions.ElementNotVisibleException:
      waiting_sec = waiting_sec + waiting_increment
      time.sleep(waiting_increment)
      print "      ElementNotVisibleException. Waiting for " + str(waiting_sec) + " seconds..."
      continue
    except selenium.common.exceptions.NoSuchElementException:
      waiting_sec = waiting_sec + waiting_increment
      time.sleep(waiting_increment)
      print "      NoSuchElementException. Continue to next post block"
      break
  return seller_names

def checkSameSellerPage(driver, prev_seller_names):
  curr_page_sellers = fetchBooknames(driver)
  matchHit = 0
  for curr_page_seller in curr_page_sellers:
    if curr_page_seller in prev_seller_names:
      matchHit = matchHit + 1
  if (matchHit > len(prev_seller_names) - 1):
    return True
  else:
    return False

def fetchAllSellerInfo(driver, bookinfo, waiting_increment = 0.5):

  # Get view detail buttons
  time.sleep(HARD_WAITING_SEC)
  print "      Fetching view details button"
  view_details_buttonsHandler = driver.find_elements_by_class_name("detailsbtn")

  # Get the current seller names
  curr_seller_names = fetchSellerNames(driver)

  time.sleep(GENERAL_WAITING_SEC)
  bookinfo["sellers"] = {}
  for i in range(0, len(view_details_buttonsHandler)):
    view_details_buttonsHandler = driver.find_elements_by_class_name("detailsbtn")
    clickViewDetails(driver, view_details_buttonsHandler[i])
    time.sleep(HARD_WAITING_SEC)
#      print "      Fetching book name..."
#      book_name = fetchBookname(driver)
    print "      Fetching phone number..."
    phone_number = fetchPhonenumber(driver)
    print "      Fetching description..."
    description = fetchDescription(driver)
    print "      Checking email..."
    email = checkEmailProvided(description)
    if (phone_number == None and email == None):
      print "    No phone number or email provided. Skip this seller"
      driver.back()
      continue

    print "      Fetching price..."
    price = fetchPrice(driver)

    if (price == None):
      print "    No price found. Skip this seller"
      driver.back()
      continue

    print "      Fetching seller name..."
    seller_name = fetchSellername(driver)
    print "      Fetching isbn..."
    isbn = fetchISBN(driver)
    print "      Fetching class name..."
    class_name = fetchClassname(driver)
    print "      Fetching teacher name..."
    teacher_name = fetchTeachername(driver)
    print "      Fetching condition..."
    condition = fetchCondition(driver)
    print "      Fetching post time..."
    post_time = fetchPosttime(driver)
    print "      Fetching total view..."
    total_view = fetchTotalViews(driver)

    bookinfo["sellers"][seller_name] = {}
    bookinfo["sellers"][seller_name]["phone_number"] = phone_number
    bookinfo["sellers"][seller_name]["email"] = email
    bookinfo["sellers"][seller_name]["isbn"] = isbn
    bookinfo["sellers"][seller_name]["class_name"] = class_name
    bookinfo["sellers"][seller_name]["teacher_name"] = teacher_name
    bookinfo["sellers"][seller_name]["condition"] = condition
    bookinfo["sellers"][seller_name]["post_time"] = post_time
    bookinfo["sellers"][seller_name]["price"] = price
    bookinfo["sellers"][seller_name]["total_view"] = total_view
    driver.back()
    time.sleep(HARD_WAITING_SEC)

    if (i == len(view_details_buttonsHandler) - 1):
      print "      All sellers on current page iterated. Checking if next seller page exists"
      if (clickNextSellerPage(driver) == False):
        print "      Next seller page button does not exist. Continue to next book"
        break
      else:
        time.sleep(GENERAL_WAITING_SEC)
        print "      Next seller page button exists. Checking if effective"
        if (checkSameSellerPage(driver, curr_seller_names) == False):
          print "      On a new seller page. continue fetching sellers"
          continue
        else:
          print "      Not on a new seller page. continue to next post block"
          break

# def fetchAllSellerInfo_old(driver, bookinfo, waiting_increment = 0.5):
#   waiting_sec = 0
#   while (True):
#     if (waiting_sec > MAX_WAITING_SEC):
#       return False
#     try:
#       item_sellersHandler = driver.find_elements_by_class_name("rc-d")
#       item_post_datesHandler = driver.find_elements_by_class_name("rc-u")
#       item_schoolsHandler = driver.find_elements_by_class_name("rc-s")
#       item_conditionsHandler = driver.find_elements_by_class_name("rc-ic")
#       item_markingsHandler = driver.find_elements_by_class_name("rc-m")
#       item_pricesHandler = driver.find_elements_by_class_name("rc-p")
#       view_details_buttonsHandler = driver.find_elements_by_class_name("detailsbtn")
      
#       if (len(item_sellersHandler) != len(item_post_datesHandler) != len(item_schoolsHandler) != len(item_conditionsHandler) != len(item_pricesHandler) != len(view_details_buttonsHandler)):
#         waiting_sec = waiting_sec + waiting_increment
#         time.sleep(waiting_increment)
#         print "    info array length not consistent. Waiting for " + str(waiting_sec) + " seconds..."
#         continue

#       if (0 == len(item_sellersHandler) == len(item_post_datesHandler) == len(item_schoolsHandler) == len(item_conditionsHandler) == len(item_pricesHandler) == len(view_details_buttonsHandler)):
#         print("    No seller block found")

#       item_sellers = []
#       item_post_dates = []
#       item_schools = []
#       item_conditions = []
#       item_markings = []
#       item_prices = []
#       view_details_buttons = []
#       for i in range(0, len(item_sellersHandler)):
#         item_sellers.append(item_sellersHandler[i].get_attribute("innerHTML"))
#         item_post_dates.append(item_post_datesHandler[i].get_attribute("innerHTML"))
#         item_schools.append(item_schoolsHandler[i].get_attribute("innerHTML"))
#         item_conditions.append(item_conditionsHandler[i].get_attribute("innerHTML"))
#         item_markings.append(item_markingsHandler[i].get_attribute("innerHTML"))
#         item_prices.append(item_pricesHandler[i].get_attribute("innerHTML"))
#         view_details_buttons.append(view_details_buttonsHandler[i])
#       bookinfo["sellers"] = {}
#       for i in range(0, len(item_sellers)):
#         view_details_buttons[i].click()
#         time.sleep(HARD_WAITING_SEC)
#         print "    Fetching info of seller '" + str(item_sellers[i]) + "'"
#         print "      Fetching phone number..."
#         phone_number = fetchPhonenumber(driver)
#         print "      Fetching description..."
#         description = fetchDescription(driver)
#         print "      Checking email..."
#         email = checkEmailProvided(description)
#         if (phone_number == None and email == None):
#           print "    No phone number or email provided. Skip this seller '" + str(item_sellers[i]) + "'"
#           driver.back()
#           time.sleep(GENERAL_WAITING_SEC)
#           continue
#         print "      Fetching class name..."
#         class_name = fetchClassname(driver)
#         print "      Fetching teacher name..."
#         teacher_name = fetchTeachername(driver)
#         bookinfo["sellers"][item_sellers[i]] = {}
#         bookinfo["sellers"][item_sellers[i]]["post_date"] = item_post_dates[i]
#         bookinfo["sellers"][item_sellers[i]]["school"] = item_schools[i]
#         bookinfo["sellers"][item_sellers[i]]["condition"] = item_conditions[i]
#         bookinfo["sellers"][item_sellers[i]]["marking"] = item_markings[i]
#         bookinfo["sellers"][item_sellers[i]]["price"] = item_prices[i]
#         bookinfo["sellers"][item_sellers[i]]["phone_number"] = phone_number
#         bookinfo["sellers"][item_sellers[i]]["description"] = description
#         bookinfo["sellers"][item_sellers[i]]["email"] = email
#         bookinfo["sellers"][item_sellers[i]]["class_name"] = class_name
#         bookinfo["sellers"][item_sellers[i]]["teacher_name"] = teacher_name        
#         driver.back()
#         time.sleep(GENERAL_WAITING_SEC)
#       break
#     except selenium.common.exceptions.ElementNotVisibleException:
#       waiting_sec = waiting_sec + waiting_increment
#       time.sleep(waiting_increment)
#       print "    ElementNotVisibleException. Waiting for " + str(waiting_sec) + " seconds..."
#       continue
#     return True

def fetchPartnerPrice(driver, waiting_increment = 0.1):
  waiting_sec = 0
  while (True):
    if (waiting_sec > GENERAL_WAITING_SEC):
      partner_lowest_price = None
      break
    try:
      partner_lowest_price = driver.find_element_by_class_name("aff-p").get_attribute("innerHTML")
      break
    except selenium.common.exceptions.NoSuchElementException:
      partner_lowest_price = None
      break
    except selenium.common.exceptions.ElementNotVisibleException:
      waiting_sec = waiting_sec + waiting_increment
      print "    ElementNotVisibleException. Waiting for " + str(waiting_sec) + " seconds..."
      time.sleep(0.1)
      continue
  return partner_lowest_price

def writeBookinfoToFile(bookinfo, outputfile):
  output_string = ""
  output_string += str(bookinfo['bookname'])
  output_string += ":"

  output_string += "partner_lowest_price:"

  try:
    output_string += str(bookinfo["partner_lowest_price"])
  except KeyError:
    output_string += "None"
  output_string += ","

  output_string += 'Sellers:['
  try:
    sellers = bookinfo['sellers']
  except KeyError:
    output_string += ']'
    return False

  if (len(sellers) == 0):
    return False

  for seller_name in sellers:
    output_string += str(seller_name)
    output_string += ':'
    try:
      output_string += str(bookinfo["sellers"][seller_name]["phone_number"])
    except KeyError:
      output_string += "None"
    output_string += '|'
    try:
      output_string += str(bookinfo["sellers"][seller_name]["email"])
    except KeyError:
      output_string += "None"
    output_string += '|'
    try:
      output_string += str(bookinfo["sellers"][seller_name]["isbn"])
    except KeyError:
      output_string += "None"
    output_string += '|'
    try:
      output_string += str(bookinfo["sellers"][seller_name]["class_name"])
    except KeyError:
      output_string += "None"
    output_string += '|'
    try:
      output_string += str(bookinfo['sellers'][seller_name]['teacher_name'])
    except KeyError:
      output_string += "None"
    output_string += '|'
    try:
      output_string += str(bookinfo["sellers"][seller_name]["condition"])
    except KeyError:
      output_string += "None"
    output_string += '|'
    try:
      output_string += str(bookinfo["sellers"][seller_name]["post_time"])
    except KeyError:
      output_string += "None"
    output_string += '|'
    try:
      output_string += str(bookinfo["sellers"][seller_name]["price"])
    except KeyError:
      output_string += "None"
    output_string += '|'
    try:
      output_string += str(bookinfo["sellers"][seller_name]["total_view"])
    except KeyError:
      output_string += "None"
    output_string += ","
  output_string += '];\n'
  outputfile.write(output_string.decode("utf-8").encode("utf-8"))
  return True

def clickViewDetails(driver, view_detail_button, waiting_increment = 0.1):
  waiting_sec = 0
  while (True):
    if (waiting_sec > MAX_WAITING_SEC):
      return False
    try:
      view_detail_button.click()
      break
    except selenium.common.exceptions.ElementNotVisibleException:
      waiting_sec = waiting_sec + waiting_increment
      time.sleep(waiting_increment)
      print "    ElementNotVisibleException. Waiting for " + str(waiting_sec) + " seconds..."
      continue
  return True

def clickViewPosting(driver, view_posting_button, waiting_increment = 0.1, Max_waiting_sec = MAX_WAITING_SEC):
  try:
    view_posting_button.click()
    return True
  except selenium.common.exceptions.ElementNotVisibleException:
    return False

def checkSameBook(driver, workingon_bookname, waiting_increment = 0.1):
  waiting_sec = 0
  while (True):
    if (waiting_sec > MAX_WAITING_SEC):
      return False
    try:
      displayed_bookname = driver.find_element_by_xpath("//div[@class='item content_container active']/div/div/div/div/div/h3/a").get_attribute("innerHTML").strip()
      break
    except selenium.common.exceptions.ElementNotVisibleException:
      waiting_sec = waiting_sec + waiting_increment
      time.sleep(waiting_increment)
      print "    ElementNotVisibleException. Waiting for " + str(waiting_sec) + " seconds..."
      continue
    except selenium.common.exceptions.NoSuchElementException:
      driver.refresh()
      waiting_sec = waiting_sec + HARD_WAITING_SEC
      print "    Oh No, NoSuchElementException. Waiting for " + str(waiting_sec) + " seconds..."
      continue

  if (displayed_bookname.encode("utf-8") == workingon_bookname):
    return True
  else:
    return False

def clickNextPostPage(driver, waiting_increment = 0.1):
  waiting_sec = 0
  while (True):
    if (waiting_sec > MAX_WAITING_SEC_SECONDARY):
      return False
    try:
      driver.find_element_by_xpath("//div[@class='tabcontrol postingouter']/div/div/a[@class='rightalign nbtn']").click()
      break
    except selenium.common.exceptions.ElementNotVisibleException:
      waiting_sec = waiting_sec + waiting_increment
      print "    ElementNotVisibleException. Waiting for " + str(waiting_sec) + " seconds..."
      time.sleep(waiting_increment)
      continue
  return True

def fetchBooknames(driver, waiting_increment = 0.5):
  waiting_sec = 0
  while(True):
    book_names = []
    if (waiting_sec > GENERAL_WAITING_SEC/2):
      book_names = []
      break
    try:
      book_namesHandler = driver.find_elements_by_xpath("//div[@class='item content_container active']/div/div/div/div/div/h3/a")
      for handler in book_namesHandler:
        book_names.append(handler.get_attribute("innerHTML"))
      break
    except selenium.common.exceptions.NoSuchElementException:
      waiting_sec = waiting_sec + waiting_increment
      time.sleep(waiting_increment)
      print "      NoSuchElementException. Waiting for " + str(waiting_sec) + " seconds..."
      continue
  return book_names

def checkSamePostPage(driver, prev_page_booknames):
  curr_page_booknames = fetchBooknames(driver)
  matchHit = 0
  for curr_page_bookname in curr_page_booknames:
    if curr_page_bookname in prev_page_booknames:
      matchHit = matchHit + 1
  if (matchHit > len(prev_page_booknames) - 1):
    return True
  else:
    return False

def fetchAllBookinfo(driver, booknames, outputfile):
  driver.get("https://www.postyourbook.com/ucsd")
  for i in range(0, len(booknames)):
    time.sleep(GENERAL_WAITING_SEC)

    # Search for book
    print "Submitting search for book " + str(booknames[i]).strip()
    if (submitBooknameSearch(driver, booknames[i]) == False):
      print "Can't find search field. **Please inspect this problem**"
      continue
    print "Finished search"
    
    bookinfo = {}
    bookinfo["bookname"] = str(booknames[i]).strip()

    # # Fetch the post block
    # time.sleep(HARD_WAITING_SEC)
    # print "  Fetching current post block"
    # if (fetchPostBlock(driver, bookinfo) == False):
    #   print "  Fail to find the view_posting button at book '" + str(booknames[i]) + "'. **Please inspect this problem**"
    #   continue

    # Find all of the view_posting button
    time.sleep(HARD_WAITING_SEC)
    view_posting_buttonsHandler = driver.find_elements_by_xpath("//button[@class='postingitem vpostingsbtn askseller_btn rc-btn']")

    # Get the booknames on current page
    curr_page_booknames = fetchBooknames(driver)

    for i in range(0, len(view_posting_buttonsHandler)):
      print "  Click on the View Posting button..."
      view_posting_buttonsHandler = driver.find_elements_by_xpath("//button[@class='postingitem vpostingsbtn askseller_btn rc-btn']")
      if (clickViewPosting(driver, view_posting_buttonsHandler[i]) == False):
        print "  ElementNotVisibleException. Continue to next view posting button."
        continue
      print "  Finished click"
      time.sleep(HARD_WAITING_SEC)

      # 
      if (checkSameBook(driver, bookinfo["bookname"]) == False):
        print "  Bookname not match. Skip to the next post block."
        driver.back()
        time.sleep(HARD_WAITING_SEC)
        continue

      # Fetch seller information
      print "  Fetching seller information"
      if (fetchAllSellerInfo(driver, bookinfo) == False):
        print "  Fail to fetch seller block. Continue to next book search"
        continue
      print "  Fetch finished"

      # Fetch partner price
      print "  Fetching partner_lowest_price"
      partner_lowest_price = fetchPartnerPrice(driver)
      bookinfo["partner_lowest_price"] = partner_lowest_price
      print "  Fetch finished"
      driver.back()
      time.sleep(HARD_WAITING_SEC)

      if (i == len(view_posting_buttonsHandler) - 1):
        print "  Trying to click on next page button"
        if (clickNextPostPage(driver) == False):
          print "  Can't find next page button Continue to write to file."
          break
        else:
          print "  Nextpage button clicked. Checking if effective"
          time.sleep(GENERAL_WAITING_SEC)
          if (checkSamePostPage(driver, curr_page_booknames) == False):
            print "  On a new page. Continue on post blocks"
            continue
          else:
            print "  Not on a new page. Continue to write to file"
            break

    # Write bookinfo to file
    print "  Writing bookinfo to file"
    if (writeBookinfoToFile(bookinfo, outputfile) == False):
      print "Book '" + str(bookinfo["bookname"]) + "' not written to file because no sellers are available"
    else:
      print "Book '" + str(bookinfo["bookname"]) + "' written to file '" + str(outputfile) + "'"

def login (driver, username, password):
  driver.get("https://www.postyourbook.com/login")
  time.sleep(GENERAL_WAITING_SEC)
  username_input = driver.find_element_by_xpath("//form[@class='signinform loginform']/div[@class='input-prepend']/input[@class='text your_login']")
  password_input = driver.find_element_by_xpath("//form[@class='signinform loginform']/div[@class='input-prepend']/input[@class='text your_password']")
  username_input.send_keys(username)
  password_input.send_keys(password)
  password_input.send_keys(Keys.RETURN)
  time.sleep(HARD_WAITING_SEC)

def readBooknames(inputfilename):
  booknames = []
  with open(str(inputfilename)) as f:
    for line in f:
      booknames.append(line.strip())
  return booknames

if __name__=='__main__':
  driver = webdriver.Firefox()
  username = str(sys.argv[1])
  password = str(sys.argv[2])
  booknames_filename = str(sys.argv[3])

  login(driver, username, password)
  booknames = readBooknames(booknames_filename)
  outputfilename = str(booknames_filename) + "_info"

  outputfile = open(outputfilename, "a")
  fetchAllBookinfo(driver, booknames, outputfile)
  outputfile.close()
