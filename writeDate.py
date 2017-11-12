import datetime
 
with open('/home/ubuntu/workspace/slack_bot/dateInfo.txt','a') as outFile:
    outFile.write('\n' + str(datetime.datetime.now()))

print("datetime 완료\n")
