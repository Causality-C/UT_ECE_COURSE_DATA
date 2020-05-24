from bs4 import BeautifulSoup
import requests
import csv
url  = "https://www.ece.utexas.edu/undergraduate/courses?field_ug_technical_core_value="

# Get the results from all
taskList = ["All", "1", "2", "3", "4", "5", "6", "7"]
nameList = ["General","Communications, Signal Processing, Networks and Systems","Electronics and Integrated Circuits", "Energy Systems and Renewable Energy", "Fields, Waves and Electromagnetic Systems", "Nanoelectronics and Nanotechnology", "Computer Architecture and Embedded Systems", "Software Engineering and Design"]
curr = 0
for task in taskList:
    r = requests.get(url+str(task))
    soup = BeautifulSoup(r.text, 'html.parser')
    classNames = soup.find_all('div', attrs={"class": 'views-row'})
    i = 0
    output_rows = []
    output_rows.append(["Symbol","Name","Division"])
    for entry in classNames:
        output_row = []
        for value in entry.contents:
            #Symbol and Name
            if i == 1: 
                s = (str(value.text)).split(":")
                output_row.append(s[0])
                output_row.append(s[1])
            if i == 3:
                output_row.append(str(value.text))
            i = i+1
        output_rows.append(output_row)
        i = 0
    with open(str(nameList[curr])+'.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(output_rows)
    curr = curr+1




