from slacker import Slacker
import github_parser as gp
import time
import os
from datetime import datetime, timedelta

korean_time = datetime.now() + timedelta(hours=9)

## dd/mm/yyyy format

textfile = open("github_repositories.txt", "r", encoding="utf8")
members_github = textfile.read()
members_github_list = members_github.split(",")
members_commit_check = ["★★★"+korean_time.strftime("%Y-%m-%d")+"의 커밋 결과★★★\n"]
for url in members_github_list:
    if gp.commit_checker(url):
        result = "완료"
    else:
        result = "미완료"
    username = url.split("/")[3]
    members_commit_check.append(username + "님의 커밋 결과: " + result +"\n")

message = " ".join(members_commit_check)

token = os.environ['SLACK_TOKEN']
slack = Slacker(token)
slack.chat.post_message('#test', message, as_user=True)