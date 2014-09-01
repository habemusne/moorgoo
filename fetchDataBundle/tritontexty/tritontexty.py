from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
import logging
import sys,re,os

def triton():
  driver = webdriver.Firefox()
  sign_in(driver)
  driver.get("http://tritontexty.com/books")
  books = driver.find_elements_by_class_name('book')
  line = []
  outFile = open('tritonOut_3','w')
  # skip = True
  for book in books:
    url = book.find_element_by_tag_name('a').get_attribute("href")
    # if url == "http://tritontexty.com/books/6809": skip = False
    # if not skip: 
    line.append(url)
  for i in line:
    driver.get(i)
    string = getBookInfo(driver)
    outFile.write(string)


def sign_in(driver):
  driver.get("http://tritontexty.com/users/sign_in")
  email_input = driver.find_element_by_id('user_email')
  email_input.send_keys("z2tao@ucsd.edu")
  pswd_input = driver.find_element_by_id('user_password')
  pswd_input.send_keys("12345678")
  driver.find_element_by_xpath("//div[@class='form-actions']/input").click()


def getBookInfo(driver):
  try:
    info = title = isbn = price = condition = contact = author = "None"
    class_number = ["No", "ne"]
    info = driver.find_element_by_class_name('book')
    title = info.find_element_by_class_name('title').get_attribute("innerHTML")
    price = info.find_element_by_class_name('price').get_attribute("innerHTML")
    condition = info.find_element_by_class_name('condition').get_attribute("innerHTML")
    class_number = info.find_element_by_class_name('class_number').get_attribute("innerHTML").encode('ascii','ignore').split()
    author = info.find_element_by_class_name('author').get_attribute("innerHTML")
    contact = driver.find_element_by_xpath("//div[@class='book ']/div/div[4]/a").get_attribute("innerHTML")
    isbn = info.find_element_by_class_name('isbn').get_attribute("innerHTML")
  except selenium.common.exceptions.NoSuchElementException:
    print("No such element")
  return "|".join([title, isbn, author, class_number, price, condition, contact, '\n'])


triton()