from slacker import Slacker
import github_parser as gp
import os
import pandas as pd
from datetime import datetime, timedelta


korean_time = datetime.now() + timedelta(hours=9)
specific_time = datetime.now()

## dd/mm/yyyy format

textfile = open("github_repositories.txt", "r", encoding="utf8")
members_github = textfile.read()
members_github_list = members_github.split(",")
members_commit_check = ["★★★"+specific_time.strftime("%Y-%m-%d %H:%M")+"의 커밋 결과★★★\n"]
commits_list = []
for url in members_github_list:
    commit_count = gp.commit_checker(url, specific_time.strftime("%Y-%m-%d"))
    if commit_count != "0":
        result = "완료"
    else:
        result = "미완료"
    username = url.split("/")[3]
    members_commit_check.append(username + "님의 커밋 결과: " + result +"(" + commit_count + "회)\n")
    commits_list.append(commit_count)

message = " ".join(members_commit_check)
token = os.environ['SLACK_TOKEN']
slack = Slacker(token)
slack.chat.post_message('#test', message, as_user=True)
print(specific_time.strftime("%Y-%m-%d")+" 확인 완료\n")


data = pd.read_csv('github_commits.csv')
commitDate = specific_time.strftime("%Y-%m-%d")
commits_list.insert(0, commitDate)
print(commits_list)
if (data['date'] == commitDate).any():
    update_df = pd.DataFrame(data=[commits_list], columns= data.columns)
    data.loc[data['date'] == commitDate] = update_df
    # pass
else:
    addingData = pd.DataFrame([commits_list], columns=data.columns)
    print(addingData)
    data = data.append(addingData,ignore_index=True)
    data.to_csv("github_commits.csv", sep=',', encoding='utf-8', index=False)