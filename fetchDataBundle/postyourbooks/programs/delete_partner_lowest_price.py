import re, sys
import fetcherToolbox

def delete_partner_price(line):
  p = re.compile('partner_lowest_price:.\w+.\w+,')
  match = p.findall(line)
  line = line.replace(str(match[0]), "")
  return line

if __name__=='__main__':
  filename = str(sys.argv[1])
  outputfilename = filename + "_plpdeleted"
  fetcherToolbox.createFile(outputfilename)
  outputfile = open(outputfilename, "a")
  lines = fetcherToolbox.readFileLines(filename)
  for line in lines:
    new_line = delete_partner_price(line)
    outputfile.write(new_line + '\n')
  outputfile.close()
