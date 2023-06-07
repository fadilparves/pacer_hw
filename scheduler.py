from scheduler.recurring import recurring_scheduler
from etl_pipeline import etl_manager

print("Scheduler started")

# Run the etl_manager function every 5 minutes
recurring_scheduler.add_job(target=etl_manager,
                            period_in_seconds=300,
                            start="Jun 07 09:40:00 2022",
                            tz="Asia/Kuala_Lumpur")

recurring_scheduler.run()
