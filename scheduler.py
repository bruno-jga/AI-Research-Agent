from apscheduler.schedulers.blocking import BlockingScheduler
from main import run_pipeline

def schedule_job():
    scheduler = BlockingScheduler()
    # Run every day at 9 AM
    scheduler.add_job(run_pipeline, "cron", hour=19, minute=50)
    print("Scheduler started... (Ctrl+C to stop)")
    scheduler.start()