# Scheduler to run the scraping tasks every hour
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from hdfs import read_from_hdf5, save_to_hdf5
from scrapper import *
from urls import *

def run_scrape_data():
    try:
        # convert string to numeric
        hashrate = float(get_hashrate(url_1))
        btc_preis = float(get_preis(url_2).replace(',', ''))
        market_cap  = float(get_market_cap(url_3).replace('$', '').replace(',', ''))

        #save in HDF5
        save_to_hdf5(hashrate, btc_preis, market_cap)

        print(f"[{datetime.now()}] Daten erfolgreich gescraped und gespeichert.")
    except Exception as e:
        print(f"Fehler beim Scrapen oder Speichern: {e}")


# create the shedeuler
scheduler = BlockingScheduler()


