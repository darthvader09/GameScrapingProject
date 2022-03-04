import requests
from bs4 import BeautifulSoup as soup

print("CoolDude Search Machine =)")

ask = input("\nWhat game would you like to search about?")
game = ask

url = f"https://en.wikipedia.org/wiki/{game}"
page = requests.get(url)

#information
scraper = soup(page.content, 'html.parser')
# text = scraper.find_all('div', {'class': 'mw-parser-output'})
# table = scraper.find_all('table', {'class': "infobox hproduct"})
# labels = scraper.find_all("th", {"class": "infobox-label"})
#print(text[0].get_text())
#print(table[0].get_text())
#print(scraper.get_text())

labeltext = scraper.find_all("td", {"class": "infobox-data"})

# for t in labels:
#     x = t.get_text()
#     print("+=======+")
#     print(x)




def img():
  test = []
  for item in scraper.find_all('img'):
    x=item['src']
    test.append(x)
    
  return "https:" +str(test[1])
print(img())


def game_return():
  output = ask.lower()
  output = list(output)
  output[0] = output[0].upper()
  return "".join(output)

print(game_return())


def get_data(): 
  text = scraper.find_all("td", {"class": "infobox-data"})
  headings = scraper.find_all("th", {"class": "infobox-label"})
  output = []
  
  for t in text:
    output.append({
      "label": headings[text.index(t)].get_text(),
      "text": t.get_text()
    })

  return output






  
  
