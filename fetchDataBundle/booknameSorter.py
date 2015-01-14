import sys,re,os

def readBooknames(inputfilename):
  booknames = []
  with open(str(inputfilename)) as f:
    for line in f:
      booknames.append(line.strip())
  return booknames

if __name__=='__main__':
  filename = str(sys.argv[1])
  booknames = readBooknames(filename)

  filename2 = filename + "_sorted"
  outputfile = open(filename2, "w+")

  booknames.sort(key=len, reverse=True)
  for bookname in booknames:
    outputfile.write(bookname.decode("utf-8").encode("utf-8"))
    outputfile.write("\n")