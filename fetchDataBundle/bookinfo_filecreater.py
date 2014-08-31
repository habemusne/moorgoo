import sys

def createFile(filename):
  outputfile = open(filename, "w+")
  outputfile.write("")
  outputfile.close()

if __name__=='__main__':
  booknames_filename = str(sys.argv[1])
  filename = booknames_filename + "_info"
  createFile(filename)