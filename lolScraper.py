import requests
from bs4 import BeautifulSoup
import re

name = input("Enter name: ")
url = f"https://www.op.gg/summoners/euw/{name}-EUW"
headers = {"User-Agent": "Mozilla/5.0"}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")
text = soup.get_text()

matchSoloDuo = re.search(r"(\d+)W\s+(\d+)L", text)
if matchSoloDuo:
    w = int(matchSoloDuo.group(1))
    l = int(matchSoloDuo.group(2))
    g = w + l
    print("Solo/Duo ", round((w/g)*100, 2), "%")
else: print ("Not enough games played!")
