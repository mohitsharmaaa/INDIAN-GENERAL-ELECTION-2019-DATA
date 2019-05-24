### INDIAN GENERAL ELECTION 2019 DATA
##### Scrapped using Python

India is worlds largest democracy.

It has total 29 States and 7 Union Territories.
The 2019 Indian general election is held on 542/543 Seats.

The web_scrapper.py scraps the constituency wise data for all the 542 seats.
Data is scrapped from http://results.eci.gov.in maintained by election commision of India.

URL INFO :

http://results.eci.gov.in/pc/en/constituencywise/Constituencywise{area}{constituency}.htm?ac={constituency}

- area = State(S)[01 to 29] + constituency_number
	     Union Territory(U) [01 to 07] + consituency_number

- constituency = Consitituency Number



### candidates_info.csv file contains the scrapped data.
- Delimiter = ","
- Columns    
	- stateID
	- stateName
	- constID
	- constituencyName
	- sNo
	- candidateName
	- party
	- evmVotes
	- postalVotes
	- totalVotes
	- percentVotes
				