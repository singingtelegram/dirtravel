#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

url_len = 0
i = 0
#dirs = []
def get_dir(url):
    global dirs
    entries = []
    global i
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, features="html.parser")
            try:
                if soup.find_all("h1")[0].text.find("Index of ") != -1:
                    entries = soup.find_all("a")[1:]
                    for entry in entries:
                        if entry.text[-1] == "/":
                            dirs.append(url[url_len:] + entry.text)
                            print(dirs[i], sep = "")
                            i += 1
                            get_dir(url + entry.text)
            except:
                pass
            
    except Exception as e:
        print("Request failed with exception: ", e, sep="")

            


if __name__ == "__main__":
    url = input("Please input the URL (with trailing slash): ")
    if url[-1] != "/":
        print("Please end your URL with a \"/\".")
        quit(-1)
    url_len = len(url)
    #entries = []
    dirs = []
    """try:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, features="html.parser")
            entries += soup.find_all("a")[1:]
            #entries.pop(0)
            for entry in entries:
                if entry.text[-1] == "/":
                    print(entry.text, sep="")

    except Exception as e:
        print("Request failed with exception: ", e, sep="")"""
    get_dir(url)