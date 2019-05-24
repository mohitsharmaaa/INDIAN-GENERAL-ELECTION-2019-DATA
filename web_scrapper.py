import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

# Web_Scrapper for Election Results 2019
#Total States (S01-S29) + Union Territories (U01-U07) 
STATES = 29
UNION_TERRITORIES = 7

result_list=[]
url_list=[]


def check_page_exists(area,constituency):
	
	url = f"http://results.eci.gov.in/pc/en/constituencywise/Constituencywise{area}{constituency}.htm?ac={constituency}"
	try:
		html_page = urlopen(url)
		html_data = html_page.read()
		html_page.close()

		print("Success : " +url)
		url_list.append(url)

		return (True,html_data)

	except:
		print("Error 404 : " +url)
		return (False,"")
			
def parse_page(html_page,state_code,constituency_id):

	soup_page = soup(html_page,"html.parser")
	table_tag = soup_page.findAll(id="div1")[0].table
	tr_tags   = table_tag.findAll("tr")
	
	state_name = tr_tags[0].text.split("-")[0].strip()
	constituency_name =" ".join([x.strip() for x in tr_tags[0].text.split("-")[1:]])
	#result_status = tr_tags[1].text.strip()
	candidates_list = tr_tags[3:]

	

	for candidates in candidates_list:
		a=[member.text.replace(",","") for member in candidates.findAll("td")]
		
		try:
			sr_no,name,party,evm_votes,postal_votes,total_votes,vote_percentage=a
		except:
			sr_no,name,party,evm_votes,migrant_votes,postal_votes,total_votes,vote_percentage=a
			postal_votes=int(postal_votes)+int(migrant_votes)
		
		if len(sr_no)>0:
			result_list.append([state_code,state_name,constituency_id,constituency_name,sr_no,name,party,evm_votes,postal_votes,total_votes,vote_percentage])
			print(state_name+"  "+constituency_name+"  "+name +"  " +party)



# For Scraping All the States and their Constituencies
for state in range(1,STATES+1):
	for constituency_id in range(1,300):
	
		state_code = ( "S"+str(state), "S0"+str(state) )[state<10]
		page_exists,html_page = check_page_exists(state_code,constituency_id)
		
		if page_exists:
			parse_page(html_page,state_code,constituency_id)
		else:
			break			


# For Scraping All the Union Teritories and their Constituencies
for ut in range(1,UNION_TERRITORIES+1):
	for constituency_id in range(1,50):
		ut_code = "U0"+str(ut)
		page_exists,html_page = check_page_exists(ut_code,constituency_id)

		if page_exists:
			parse_page(html_page,ut_code,constituency_id)
		else:
			break	


# Writing Candidates into CSV File
file=open(r"C:\Users\Mohit\Desktop\Desk\Py\Elections_Scraping\2019\candidates_info.csv","w")
file.write("stateID,stateName,constID,constituencyName,sNo,candidateName,party,evmVotes,postalVotes,totalVotes,percentVotes")
file.write("\n")
for lst in result_list:
	file.write(",".join([str(item) for item in lst]))
	file.write("\n")
file.close()	


# Writing All the Scraped URLs in urls.csv file
file=open(r"C:\Users\Mohit\Desktop\Desk\Py\Elections_Scraping\2019\urls.csv","w")
for lst in url_list:
	file.write(lst)
	file.write("\n")
file.close()	




	