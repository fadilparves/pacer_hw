from scheduler.recurring import recurring_scheduler
from pipeline import etl_manager
from datetime import datetime, timedelta

print("Scheduler started")

current_datetime = datetime.now()

time_diff = timedelta(minutes=5)

future_datetime = current_datetime + time_diff

# Run the etl_manager function every 5 minutes
recurring_scheduler.add_job(target=etl_manager,
                            period_in_seconds=300,
                            start=future_datetime.strftime("%b %d %H:%M:%S %Y"),
                            tz="Asia/Kuala_Lumpur")

recurring_scheduler.run()
