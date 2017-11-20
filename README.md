# The Game Of RISC

The Game of Reviewing Security Clearances is the new and fun way to see the mistakes of others. Completely free to play, come on over and take a stab...just not at a human. You wont get a clearance that way.

## Steps done to create this website

### 1

First, I downloaded and parsed the data from http://ogc.osd.mil/doha/industrial/

### 2 

Using the Python html parser, Beautiful Soup, I organized the security clearance data into a progrmattically-accessbile format.
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

### 3

Each adjudication has a digest which briefly describes the decision-making process for each adjudication. I looked for keywords in each digest which would clarify if an application for clearance was accepted or denied. Using the python Natural Language Toolkit, I parsed each adjudication for specific keywords, and stored the outputs in an sqlite3 database
http://www.nltk.org/

#4

Inputted the results from previous web scraping into the django backend sqlite database. Required previously created django models in order to correctly organize the data for usage in django.