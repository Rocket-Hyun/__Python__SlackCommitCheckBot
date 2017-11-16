from slacker import Slacker
import github_parser as gp
import os
import pandas as pd
from datetime import datetime, timedelta


korean_time = datetime.now() + timedelta(hours=9)
specific_time = datetime.now() - timedelta(days=1)

## dd/mm/yyyy format

textfile = open("github_repositories.txt", "r", encoding="utf8")
members_github = textfile.read()
members_github_list = members_github.split(",")
members_commit_check = ["★★★"+specific_time.strftime("%Y-%m-%d %H:%M")+"의 커밋 결과★★★\n"]
commits_list = []
for url in members_github_list:
    if gp.commit_checker(url) != "0":
        result = "완료"
    else:
        result = "미완료"
    username = url.split("/")[3]
    members_commit_check.append(username + "님의 커밋 결과: " + result +"(" + gp.commit_checker(url) + "회)\n")
    commits_list.append(gp.commit_checker(url))

message = " ".join(members_commit_check)
token = os.environ['SLACK_TOKEN']
slack = Slacker(token)
slack.chat.post_message('#general', message, as_user=True)
print(korean_time.strftime("%Y-%m-%d")+" 확인 완료\n")


# data = pd.read_csv('github_commits.csv')
# commitDate = specific_time.strftime("%Y-%m-%d")
# if (data['date'] == commitDate).any():
#     pass
# else:
#     # commits_str = ",".join(commits_list)
#     commits_list.insert(0, commitDate)
#     print(commits_list)
#     addingData = pd.DataFrame([commits_list], columns=data.columns[1:])
#     print(addingData)
#     data = data.append(addingData,ignore_index=True)
#     data.to_csv("github_commits.csv", sep=',', encoding='utf-8')