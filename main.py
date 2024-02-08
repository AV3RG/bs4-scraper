import pandas
import requests
import re
from bs4 import BeautifulSoup
import os.path
import shutil


if __name__ == '__main__':
    data = pandas.read_excel("sites.xlsx");
    regex = re.compile('(https://)?(www\\.)?(?P<url>.+)')
    shutil.rmtree("sites")
    os.mkdir("sites")
    for e in data["site link"]:
        url = "https://" + regex.match(e).group('url');
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        with open("sites/" + e + ".html", "wb") as file:
            file.write(soup.prettify('utf-8'))
