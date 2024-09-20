import threading
import time
import datetime
from .data_getter import jobs
# from jobfinder.utils import load_jobs  # Assuming load_jobs is your function to refresh jobs

def job_loader():
    while True:
        current_hour = datetime.datetime.now().hour
        print(f"Current Hour: {current_hour}")
        
        if current_hour % 3 == 0:
            print("Loading jobs")  # Debugging print
            try:
                jobs("Software Developer")
                jobs("UI UX")
                jobs("Graphic Designer")
                jobs("App Developer")
                jobs("AI ML")
                print("Jobs loaded successfully")
            except Exception as e:
                print(f"Failed to load jobs {e}")
            print(f"Current Hour: {current_hour}")
            print("Sleeping for 2 hours...")
            time.sleep(7200)  # Sleep for 2 hours
        else:
            print("Sleeping for 10 minutes ... ")  # Debugging print
            time.sleep(600)  # Sleep for 10 minutes


def start_background_job_loader():
    print("Starting job loader thread")  # Debugging print
    thread = threading.Thread(target=job_loader, daemon=True)
    thread.start()