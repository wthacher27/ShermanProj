##WillThacher2024
import requests
import re
from datetime import datetime 
from bs4 import BeautifulSoup
##Object for storing the data
class Data:
  def __init__(refself, type, data,change):
    refself.data = data
    refself.type = type
    refself.change = change
  def print(obj):
    print(obj.type + ": " + obj.data + ", 24hrchange: " + obj.change)

method1 = requests.get("https://ucce-slo.westernweathergroup.com/dee79adc4bba41508a436140060280e2")
##soup stuff
soup = BeautifulSoup(method1.content, "html.parser")
tablecontent = soup.find(class_="table table-bordered table-condensed table-striped table-hover table-header-fixed tabular-report current-conditions-report")

##attempt 3, iterate through each <tr> tag them go to child to find specific "temp 30 ft" then use .next_sibling to get data
trsort = (tablecontent.find_all("tr"))
##making txt file
now = datetime.now()
datestr = now.strftime("%m-%d-%Y %H:%M:%S")
print(datestr)
with open("PastData/"+datestr,"w") as file:
  file.write("DATA FROM: " + datestr + "\n")
##print(trsort)
for x in trsort:
  temptype = x.find("th")
  datatype = temptype.prettify().strip().replace('<th>', '').replace('</th>', '')
  datatype = re.sub("\n","",datatype)
  datatype = re.sub(" ","",datatype)
  tempdata = x.find("td")
  strcurrent = re.sub(" ", "",str(tempdata))#removed spaces
  ##seperate html into lines in a list
  lines = []
  chars= ''
  aString = ""
  for chars in strcurrent:
    if chars == '\n':
      lines.append(aString)
      aString =""
    aString = aString + chars
  str24hr = lines.pop(5)
  sign24 = "+"
  ##check caret down or up (default up)
  if "down" in lines.pop(4):
    sign24 = "-"
  str24hr = re.sub("\n","",str24hr)
  str24hr = "24 hour change \n" + sign24 + str24hr + "\n"
  strcurrent = datatype + lines.pop(1)
  print(strcurrent)
  print(str24hr)
  with open("PastData/"+datestr, "a") as file:
    file.write(strcurrent)
    file.write(str24hr)

