from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
import logging
import sys,re,os
import fetcherToolbox

MAX_WAITING_SEC = 10
GENERAL_WAITING_SEC = 1
HARD_WAITING_SEC = 2

def clickNextPostPage(driver, waiting_increment = 0.1):
  waiting_sec = 0
  while (True):
    if (waiting_sec > MAX_WAITING_SEC):
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

def fetchBookNamesOnCurrentPage(driver, waiting_increment = 0.1):
  waiting_sec = 0
  while(True):
    if (waiting_sec > MAX_WAITING_SEC):
      return None
    try:
      booknamesHandler = driver.find_elements_by_xpath("//h3/a[@class='postingitem']")
      break
    except selenium.common.exceptions.ElementNotVisibleException:
      waiting_sec = waiting_sec + waiting_increment
      print "    ElementNotVisibleException. Waiting for " + str(waiting_sec) + " seconds..."
      time.sleep(waiting_increment)
      continue

  booknames = []
  for i in range(0, len(booknamesHandler)):
    booknamesHandler = driver.find_elements_by_xpath("//h3/a[@class='postingitem']")
    booknames.append(booknamesHandler[i].get_attribute("innerHTML"))
  return booknames

def fetchAllBookNames(driver, outputfile, page_start, page_end):
  driver.get("https://www.postyourbook.com/ucsd")
  time.sleep(HARD_WAITING_SEC)
  currentPageNumber = 1

  # Go to the starting page
  print "Going to the starting page..."
  for i in range(1, page_start):
    clickNextPostPage(driver, 0.01)
  print "Already on the starting page. "
  currentPageNumber = page_start

  # Formally start working
  while (True):
    # Check if all pages are iterated
    if (currentPageNumber > page_end):
      print "Finished fetching all booknames from pages " + str(page_start) + " to " + str(page_end)
      break
    
    # Fetch booknames on current page
    print "  Fetching booknames on page " + str(currentPageNumber)
    time.sleep(HARD_WAITING_SEC)
    currentPageBooknames = fetchBookNamesOnCurrentPage(driver)
    if (currentPageBooknames == None):
      print "  Fail to fetch booknames on page " + str(currentPageNumber)
      raw_input("**Please inspect this problem. Press enter to continue to next page**")
    else:
      print "  Fetch success"
      # Put the fetch result into the big array
      for i in range(0, len(currentPageBooknames)):
        try:
          fetcherToolbox.writeLineToFile(currentPageBooknames[i], outputfile)
          continue
        except Exception, ex:
          logging.exception("****Exception in method fetcherToolbox.writeLineToFile()****")
          logging.debug("\n****Finishing Debug Info****\n")
          continue

    # Click on the next page button
    print "  Clicking on the next page..."
    if (clickNextPostPage(driver) == False):
      print "  Click failed on page " + str(currentPageNumber)
      raw_input("**Please inspect this problem. Press enter to exit program**")
      break
    else:
      print "  Click success"
      currentPageNumber = currentPageNumber + 1
      time.sleep(GENERAL_WAITING_SEC)
      continue

if __name__=='__main__':
  driver = webdriver.Firefox()
  start_from_page = int(sys.argv[1])
  end_at_page = int(sys.argv[2])
  outputfilename = "bookname" + str(start_from_page) + "_" + str(end_at_page)
  fetcherToolbox.createFile(outputfilename)
  outputfile = open(outputfilename, "a")
  fetchAllBookNames(driver, outputfile, start_from_page, end_at_page)
  outputfile.close()



