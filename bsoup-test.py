# a quick sandbox for playing around with the BeautifulSoup library


from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime
from pathlib import Path

# declaring a bunch of variables and doing some string and type manipulation
timestamp = str(datetime.datetime.utcnow())
entrycount = 1
entry = str(entrycount)
my_file = Path("rawpulldown.txt")
# website-related data extraction and formatting
sourcepage = "https://myip.ms/browse/sites/1/ipID/23.227.38.32/ipIDii/23.227.38.32/sort/6/asc/1#sites_tbl_top"
shortname = str.upper(sourcepage[8:15]) #should replace this with regex 
mydoc = urlopen(sourcepage)
soup = BeautifulSoup(mydoc, "lxml")
website_title = "Website Title: " + str(soup.title.string)
link_set = []

# traversing the soup to get the website links
def GrabLinks():
	myLinks = []
	for div in soup.find_all('td', attrs={'class':'row_name'}):
		myLinks.append(div.find('a').contents[0])
	link_set = myLinks #need to return the list to a variable outside the function

# take my link_set list object and make it printable
# print ('\n'.join(link_set))

# here's our main writing function
def NewWrite(): 
	file = open("rawpulldown.txt", "a+")
	file.write("Entry No.: "+entry +"\n")
	file.write("Timestamp: " + timestamp + " (UTC) " +"\n") 
	file.write("Site Name: " + shortname + "\n")
	file.write("Full URL: "+sourcepage + "\n" + "\n")
	file.write(website_title)
	file.write("\n")
	file.close

# checking to see if the file is already there
def Filechecker():
	if my_file.is_file():
		print("File already exists. We'll just write entries below")
	else:
		file = open("rawpulldown.txt", "w")
		file.write("Henry's Little Web Scraper" + "\n" +"\n")
		file.close

link_content = GrabLinks()
Filechecker()
NewWrite()

# finally a print statement to confirm the program ended without errors
print("Confirmed! You saved the scrape from " + shortname
	)
