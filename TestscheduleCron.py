from crontab import CronTab
 
my_cron = CronTab(user='ubuntu')
job = my_cron.new(command='python3 /home/ubuntu/workspace/slack_bot/writeDate.py >> test.txt')
job.minute.every(2)
 
my_cron.write()
