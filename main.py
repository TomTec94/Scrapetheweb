import logging
from scheduler import BlockingScheduler
from scheduler import run_scrape_data
from hdfs import read_from_hdf5
def main():
    # Logging for Scarping Monitoring
    logging.basicConfig()
    logging.getLogger('apscheduler').setLevel(logging.DEBUG)

    scheduler = BlockingScheduler()

# Set scraping intverals to 30 Minutes
    scheduler.add_job(run_scrape_data, 'interval', hours=0.5)

    try:
        print("Scheduler gestartet. Drücken Sie Ctrl+C, um zu beenden.")
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

if __name__ == "__main__":
    main()
