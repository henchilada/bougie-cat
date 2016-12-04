# a quick sandbox for playing around with the BeautifulSoup library


from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime
from pathlib import Path

# declaring a bunch of variables and doing some string and type manipulation
sourcepage = "https://www.happyballs.com/collections/standard-antenna-balls"
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
	file.write("Entry #"+entry+" : " +"\n")
	file.write("Timestamp: " + timestamp + " (UTC) " +"\n") 
	file.write("Site URL: "+sourcepage + "\n" + "\n")
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
print("Confirmed! You saved the scrape from " + sourcepage)
