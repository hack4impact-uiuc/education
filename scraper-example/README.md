# Web Scraping Example

## Motivation

Not all data is nicely organized and easily accessible through a RESTful API, so we have to find creative ways to get the data we need. Enter web scraping. Using this tool, we can programmatically target the data we need from a website and retrieve it.

## Tools and Setup

* [homebrew](https://brew.sh) or the appropriate package manager
* python 3.x (`brew install python3` on mac will give you python 3.7.2)
* pip (brew installs this for you with python)
* pipenv/virtualenv (`pip install pipenv` should be enough)
* [geckodriver](https://github.com/mozilla/geckodriver/releases/). This is a headless version of Firefox we can use to render webpages; to install it, just download it and put it somewhere you’ll remember (I put mine in `~/webdrivers/`). Place a copy in the same directory as your scraper.
* [Selenium WebDriver](https://www.seleniumhq.org/projects/webdriver/) (this will get installed by pipenv)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) (this will also get installed by pipenv)
* To use pipenv, go to the project directory, make sure `requirements.txt` is there, and `pipenv install -r requirements.txt`
* Use [Black](https://black.readthedocs.io/en/stable/) (`pip install black`) — An automatic code formatter for python. Most projects using python will run black on all of your PRs, so if you don’t format correctly, the tests will fail.

## GlobalGiving SP19 Intro Assignment

* Look at an NGO's website. What do you think they do? Out of [Animals, Children, Climate Change, Democracy and Governance, Disaster Recovery, Economic Development, Education, Environment, Microfinance, Women and Girls, Health, Humanitarian Assistance, Human Rights, Sport, Technology, Hunger, Arts and Culture, LGBTQAI+], which category do you think fits best? Why?
* Write down the thought process used in the previous point.
* What information might we need to choose a classification?
* From the information presented on the page, how might you programmatically find an appropriate categorization?
* What other information can you find about the organization that's not on their website? (News articles, social media references, etc.)

## Sites to Scrape
* http://www.aghauganda.org/
* http://www.scan-goa.in/
* http://www.poptani.asia/
* https://catbeachpenang.com/
* http://www.destinystartingpoint.com/
* https://www.facebook.com/righttolearnkl/
* http://www.rumahkasih.org/RKHKL/Home.html
