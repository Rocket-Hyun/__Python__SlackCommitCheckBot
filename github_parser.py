# parser.py
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# korean_time = datetime.now() + timedelta(hours=9)
# korean_date = korean_time.strftime("%Y-%m-%d")

def commit_checker(repository_url, specific_date):
    # HTTP GET Request
    req = requests.get(repository_url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    block = soup.find('rect',{"data-date":specific_date})
    commit_count =  block.get("data-count")
    print(repository_url.split("/")[3] + "님 크롤링 중...")

    # blocks = soup.find_all('rect')
    # last_block = blocks[len(blocks)-1]
    # commit_count = last_block.get("data-count")
    return commit_count


if __name__ == "__main__":
    textfile = open("github_repositories.txt", "r", encoding="utf8")
    members_github = textfile.read()
    members_github_list = members_github.split(",")
    for user in members_github_list:
        print(commit_checker(user))