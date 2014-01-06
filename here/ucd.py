import urllib
import re
from bs4 import BeautifulSoup

class person:
	def __init__(self, name, email, major):
		self.name = name
		self.email = email
		self.major = major

# will return:
# - 1 element in list if successful
# - 0 elements in list if query doesn't match anything
# - > 1 elements in list if more than one name matches
def searchdir(query):
	#query the directory page
	peoplesearch = urllib.urlopen("http://www.ucdavis.edu/search/directory_results.shtml?filter={querystring}".format(querystring = query))
	#create tree
	bigsoup = BeautifulSoup(peoplesearch)
	#look for the div that contains the result
	results = bigsoup.find(id="directory_results_wrapper") 
	#the results are in a table, we find all the td tags to get to the data
	getName = results.find_all('td') #this will always be a list
	#will hold list of names. will only be 1 thing if success
	nameList = []
	if getName: #if we found td tags in the page
		#determine if there is a single name or multiple names
		if results.find_all(text=re.compile("Search")) == []: #success! single name
			#the name is in the first td, inside a bold tag
			#to avoid any potential special characters, wrap in unicode
			nameList.append(unicode(getName[0].b.text).encode("utf-8"))
	 
		else: #more names than expected. return list and let user choose
			for i in range(len(getName)):
				if i % 4 == 0: #we only grab the first column in this 4 column table
					#to avoid any potential special characters, wrap in unicode
					nameList.append(unicode(getName[i].text).encode("utf-8") ) 
			
	return nameList #will be empty if fails

print searchdir("sumamoto")

