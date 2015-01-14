import urllib2
import mechanize
import re,os,sys
from bs4 import BeautifulSoup

if __name__=='__main__':
  isbn = str(sys.argv[1])
  br = mechanize.Browser()
  br.open('http://www.lookupbyisbn.com')
  br.select_form(nr=0)
  br.form.set_all_readonly(False)
  br.form['SearchKeywords'] = isbn
  response = br.submit()
  link = br.click_link(url_regex = re.compile('^\/Lookup\/Book.*'))
  response = br.open(link)
  soup = BeautifulSoup(response)
  image_url = soup.find_all(class_="specimage")[0].img
  #image = image.split('src="')[1].split('" title=')[0]
  image_url = str(image_url).split('src="')[1].split('" title=')[0]
  print image_url
