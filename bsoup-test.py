# a quick sandbox for playing around with the BeautifulSoup library


from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime
from pathlib import Path

# declaring a bunch of variables and doing some string and type manipulation
sourcepage = "https://myip.ms/browse/sites/1/ipID/23.227.38.32/ipIDii/23.227.38.32/sort/6/asc/1#sites_tbl_top"
shortname = str.upper(sourcepage[8:15]) #should replace this with regex 
mydoc = urlopen(sourcepage)
soup = BeautifulSoup(mydoc, "lxml")
website_title = "Website Title: " + str(soup.title.string)
timestamp = str(datetime.datetime.utcnow())
entrycount = 1
entry = str(entrycount)
my_file = Path("rawpulldown.txt")

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

Filechecker()
NewWrite()

# finally a print statement to confirm the program ended without errors
print("Confirmed! You saved the scrape from " + shortname
	)

# need to grab class="JCLRgrips"