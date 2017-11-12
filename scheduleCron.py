from crontab import CronTab
from datetime import datetime

my_cron = CronTab(user='ubuntu')
job = my_cron.new(command='python3 /home/ubuntu/workspace/slack_bot/slack_bot.py')
job.minute.every(10)
job.enable()
#print(datetime.now())
my_cron.write()
