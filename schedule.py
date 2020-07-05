import schedule
import time

def job():
    print("Hi")
    
schedule.every(6).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)