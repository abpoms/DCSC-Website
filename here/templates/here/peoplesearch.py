import urllib
from bs4 import BeautifulSoup

class person:
	def __init__(self, name, email, major):
		self.name = name
		self.email = email
		self.major = major

#for now, only returns name
def searchdir(query):
	#query the page
	peoplesearch = urllib.urlopen("http://www.ucdavis.edu/search/directory_results.shtml?filter={querystring}".format(querystring = query)) #open main page
	#create tree
	bigsoup = BeautifulSoup(peoplesearch)
	#look for the div that contains the result
	results = bigsoup.find(id="directory_results_wrapper") 
	#the results are in a table, we find all the td tags to get to the data
	getName = results.find_all('td') 
	#the name is in the first td, inside a bold tag
	return getName[0].b.text

print searchdir("sosoi@ucdavis.edu")
