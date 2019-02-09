import json  # just for outputting Album objects
import multiprocessing as mp  # ignore this one for now
from bs4 import BeautifulSoup  # for traversing web data
from selenium import webdriver  # for rendering JS
from selenium.webdriver.firefox.options import Options


class Album:
    """Class to model an Album"""

    def __init__(self, title, artist, year, rating, sample_size):
        self.title = title
        self.artist = artist
        self.year = year
        self.rating = rating
        self.sample_size = sample_size

    def __str__(self):
        """
        Overloaded str method to make printing albums pretty(ish).
        Out: json
        """
        return json.dumps(
            {
                "Title": self.title,
                "Artist": self.artist,
                "Year": self.year,
                "Rating": self.rating,
                "Sample Size": self.sample_size,
            }
        )

    def to_dict(self):
        return {
            "Title": self.title,
            "Artist": self.artist,
            "Year": self.year,
            "Rating": self.rating,
            "Sample Size": self.sample_size,
        }


def get_albums_from(year):
    """
    Gets the top albums on spunikmusic and basic information about them.
    """
    if year < 1990 or year > 2018 or type(year) != int:
        raise ValueError("Year must be an integer in [1990, 2018].")

    print("DEBUG: getting top albums from {}".format(year))

    # specify url to scrape from, send GET request, then render the JS
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.sputnikmusic.com/best/albums/" + str(year) + "/")
    # pass the page off to bs4
    page_data = BeautifulSoup(driver.page_source, "html.parser")
    # once we have the data, we can destroy the web driver
    driver.quit()

    """
    Luckily the data we want is very well organized in an HTML table, so all we
    need to do is break it down into rows, then pinpoint where each field is.

    This looks super messy, but let's look at the source and break it down.
    """

    # extract rows
    rows = page_data.find_all("tr", {"class": "alt1"})

    albums = []
    for row in rows:
        # find the first album info in the row
        title = row.find("font", {"size": "2"}).text
        artist = row.find("b").text
        rating = float(row.find("font", {"color": "#333333"}).b.font.text)

        # find the sample size and strip off the " votes", then interpret it as an integer
        sample_size = int(
            row.find("font", {"size": "2", "class": "contrasttext"}).text[:-6]
        )
        albums.append(Album(title, artist, year, rating, sample_size))

        # find the information for the second album in the row
        second = row.find_all("td")[-2]
        title = second.find("font", {"class": "darktext"}).text
        artist = second.font.b.text
        rating = float(row.find_all("td")[-1].font.b.font.text)

        # find the sample size and strip off the " votes", then interpret it as an integer
        sample_size = int(row.find_all("td")[-1].find_all("font")[-1].text[:-6])
        albums.append(Album(title, artist, year, rating, sample_size))
    return albums


if __name__ == "__main__":
    # span all available data
    FIRST_YEAR = 1990
    LAST_YEAR = 2018

    # you don't need to know this part rn, but it's just so we don't sit here
    # forever waiting for 28 consecutive GET requests
    with mp.Pool(LAST_YEAR - FIRST_YEAR) as pool:
        data = pool.map(get_albums_from, range(FIRST_YEAR, LAST_YEAR + 1))

    # output the data to JSON
    with open("output.json", "w") as file:
        file.write("[\n")
        for year in data:
            for album in year:
                json.dump(album.to_dict(), file, indent=4, separators=(",", ": "))
                file.write(",\n")
        file.write("]")

    # Now what?
