from bs4 import BeautifulSoup as soup
html = '0<span class="a">1</span>'
doc = soup(html, "lxml")
print(doc.find("span", class_ = "a").string)