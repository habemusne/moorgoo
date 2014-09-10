import sys

def createFile(filename):
  outputfile = open(filename, "w+")
  outputfile.write("")
  outputfile.close()

def readFileLines(inputfilename):
  lines = []
  with open(str(inputfilename)) as f:
    for line in f:
      lines.append(line.strip())
  return lines

def writeLineToFile(line, outputfile):
  outputfile.write(line.encode("utf-8") + "\n")

