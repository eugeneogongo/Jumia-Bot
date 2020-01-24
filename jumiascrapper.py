import random

from bs4 import BeautifulSoup
import requests


class JumiaScrapper:
    categories = []
    excludedlinks = []
    selectedproduct = ""

    def findCategories(self):
        # Get the Homepage
        r = requests.get("https://www.jumia.co.ke/")
        soup = BeautifulSoup(r.content, 'html.parser')
        # find all links in footer add them to excludelinks
        for a in soup.footer.find_all('a'):
            link = str(a.get('href'))
            self.excludedlinks.append(link)
        for a in soup.header.find_all('a'):
            link = str(a.get('href'))
            self.excludedlinks.append(link)
        # find all the anchor page
        for a_tag in soup.find_all('a'):
            # append catogery if its starts with jumia and doesnt end with .html or htm tag
            link = str(a_tag.get('href'))
            if link.startswith('https://www.jumia.co.ke/') and not (
                    link.endswith(".html") or link.endswith('.htm')) and link not in self.excludedlinks:
                self.categories.append(link)

    def getcategories(self):
        return self.categories

    def createpost(self):
        self.findCategories()
        cat = self.randomindex(self.categories)
        r = requests.get(cat)
        soup = BeautifulSoup(r.content, 'html.parser')
        products = []
        # find all the anchor page
        for a_tag in soup.find_all('a'):
            # append catogery if its starts with jumia and doesnt end with .html or htm tag
            link = str(a_tag.get('href'))
            if link.startswith('https://www.jumia.co.ke/') and (
                    link.endswith(".html") or link.endswith('.htm')) and link not in self.excludedlinks:
                products.append(link)
        singleproduct = self.randomindex(products)
        return self.getdescription(singleproduct)

    def getdescription(self, link):
        self.selectedproduct = link
        r = requests.get(link)
        print("Product link {0}", link)
        soup = BeautifulSoup(r.content)
        desc = soup.find("meta", property="og:description")
        return str(desc['content'])

    # Returns a random index from a list
    def randomindex(self, collection):
        return random.choice(collection)

    def productlink(self):
        return self.selectedproduct
