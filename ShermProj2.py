##WillThacher2024

import requests
import re

from datetime import datetime
from bs4 import BeautifulSoup

##URL used to grab
url = requests.get(
    "https://ucce-slo.westernweathergroup.com/reports/view?reportType=Tabular&stations=SLO-11&groups=&interval=15&fields=&dateType=12&deltas=#"
)

##soup stuff
soup = BeautifulSoup(url.content, "html.parser")
tablecontent = soup.find(
    class_="table table-bordered table-condensed table-striped table-hover table-freeze-panes tabular-report single-station-multi-field tabular-report-15"
)

##iterate through each <th> tag
thsort = tablecontent.find_all("th")

counter = 0
header = []
for x in thsort:
    datastr = str(x)
    datastr = datastr.replace('<th class="freeze-pane">', "").replace("</th>", "")
    datastr = datastr.replace('<th class="accum-none">', "").replace("</th>", "")
    datastr = datastr.replace('<th class="accum-daily">', "").replace("</th>", "")
    datastr = datastr.replace('<span class="units">', "").replace("</span>", "")
    datastr = "".join(datastr.splitlines())
    datastr = datastr.replace(" ", "").replace("(", ":(")
    datastr = datastr.replace("&amp;", " and ")
    header.append(datastr.strip())

    counter += 1

counter1 = 0
data = []
tdsort = tablecontent.find_all("td")
for x in tdsort:
    datastr = str(x)
    datastr = datastr.replace("<td>", "").replace("</td>", "")
    datastr = datastr.replace('<td class="accum-none">', "").replace("</td>", "")
    datastr = datastr.replace('<td class="accum-daily">', "").replace("</td>", "")
    datastr = datastr.replace('<td class="accum-daily cf-temp32">', "").replace(
        "</td>", ""
    )
    datastr = datastr.replace("<span>", "").replace("</span>", "")
    datastr = datastr.replace(" ", "").replace("-", " - ")
    datastr = "".join(datastr.splitlines())
    data.append(datastr.strip())

    counter1 += 1

# Check if the counters match
if counter != counter1:
    print("Counters don't match! First: %d Second %d", counter, counter1)
    quit()

# loop around and print out data

counter3 = 0

# Print out the Headers and Data

print("\tName\t\t:\tData")

while counter3 < counter:
    print(f"{header[counter3]:<19}\t:\t {data[counter3]}")
    counter3 += 1

# All Done

quit()

