import urllib3
from bs4 import BeautifulSoup
import pandas as pd

A = []
B = []
C = []
D = []
E = []
F = []
G = []

wiki = "https://af.wikipedia.org/wiki/Tale_van_Rusland"
http = urllib3.PoolManager(cert_reqs="CERT_REQUIRED")
page = http.request("GET", wiki)
soup = BeautifulSoup(page, 'features="xml"')
print(soup.prettify())
print(soup.title)
all_links = soup.find_all("a")
for link in all_links:
    print(link.get("href"))
all_tables = soup.find_all("table")
right_tables = soup.find("table", class_="wikitable sortable plainrowheaders")
print(right_tables)
for row in right_tables.find_all("tr"):
    cells = row.find_all("td")
    language = row.find_all("th")
    if len(cells) == 6:
        A.append(cells[0].find(text=True))
        B.append(language[1].find(text=True))
        C.append(cells[0].find(text=True))
        D.append(cells[0].find(text=True))
        E.append(cells[0].find(text=True))
        F.append(cells[0].find(text=True))
        G.append(cells[0].find(text=True))

df = pd.DataFrame(A, columns=["Numbers"])
df[" "] = B
df[" "] = C
df[" "] = D
df[" "] = E
df[" "] = F
df[" "] = G
print(df)
