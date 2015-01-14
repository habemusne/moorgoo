import sys,re,os
import fetcherToolbox

if __name__=='__main__':
  filename = str(sys.argv[1])
  booknames = fetcherToolbox.readFileLines(filename)

  filename2 = filename + "_sorted"
  outputfile = open(filename2, "w+")

  booknames.sort(key=len, reverse=True)
  for bookname in booknames:
    outputfile.write(bookname.decode("utf-8").encode("utf-8"))
    outputfile.write("\n")