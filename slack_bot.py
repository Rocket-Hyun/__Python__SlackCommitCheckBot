from slacker import Slacker
import github_parser as gp
import os
import pandas as pd
from datetime import datetime, timedelta

# utf 적용되는 서버에선 한국 시간 적용하려면 +9시간 해야함
korean_time = datetime.now() + timedelta(hours=9)
# 특정 날짜로 가고 싶을 때 사용
specific_time = datetime.now() - timedelta(days=1)

# 깃헙 리포 주소들이 저장되어 있는 텍스트 파일 열어서 배열에 각각 저장
textfile = open("github_repositories.txt", "r", encoding="utf8")
members_github = textfile.read()
members_github_list = members_github.split(",")

# 슬랙 메세지로 보낼 리스트를 초기화
members_commit_check = ["★★★"+specific_time.strftime("%Y-%m-%d %H:%M")+"의 커밋 결과★★★\n"]
# 모든 멤버들의 커밋 횟수들이 저장될 리스트 초기화
commits_list = []
for url in members_github_list:
    # gp.commit_checker 메서드: 깃헙 url과 특정 날짜 보내면 해당 날짜 커밋 횟수 리턴
    commit_count = gp.commit_checker(url, specific_time.strftime("%Y-%m-%d"))
    # 커밋 횟수가 0이 아니면 완료
    if commit_count != "0":
        result = "완료"
    else:
        result = "미완료"

    # 깃헙 리포지토리 url에서 / 기준으로 split하면 3번째 부분이 username에 해당 됨
    username = url.split("/")[3]
    # 슬랙 메세지로 보낼 말을 append
    members_commit_check.append(username + "님의 커밋 결과: " + result +"(" + commit_count + "회)\n")
    # 모든 멤버들의 커밋횟수가 저장되는 list에 추가
    commits_list.append(commit_count)

# list로 되어 있는 걸 string으로 다 합쳐서 하나의 메세지로 만듦
message = " ".join(members_commit_check)
token = os.environ['SLACK_TOKEN']
slack = Slacker(token)
slack.chat.post_message('#general', message, as_user=True)
print(specific_time.strftime("%Y-%m-%d")+" 확인 완료\n")


data = pd.read_csv('github_commits.csv')
commitDate = specific_time.strftime("%Y-%m-%d")
# 리스트 맨 앞에 커밋 날짜를 넣기
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