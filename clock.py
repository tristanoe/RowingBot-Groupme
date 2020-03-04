from apscheduler.schedulers.blocking import Blocking Scheduler

sched = BlockingScheduler()
@sched.scheduled_job('interval', minutes = 1)
def timed_job():
    print('This job is running every minute')
@sched.scheduled_job('cron', day_of_week='mon-fri', hour=1, minute=30):
def scheduled_job():
    print('this job is running every day at 1:30')

sched.start()
