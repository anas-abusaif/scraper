import requests
from bs4 import BeautifulSoup
def get_citations_needed_count(url):

  response = requests.get(url)

  html_text=response.text

  with open("file.html", "w") as file:
      file.write(html_text)

  soup = BeautifulSoup(html_text, "html.parser")
  result = soup.find_all("sup", class_="noprint Inline-Template Template-Fact")
  return len(result)




def get_citations_needed_report(url):
  response = requests.get(url)

  html_text=response.text

  with open("file.html", "w") as file:
      file.write(html_text)

  soup = BeautifulSoup(html_text, "html.parser")
  result = soup.find_all("sup", class_="noprint Inline-Template Template-Fact")
  report=""
  for j in result:
    add=j.parent.text+"\n"
    report+=add
  return report



print(get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico"))