# Functions to interact with HDFS
import h5py
import numpy as np
from datetime import datetime


def save_to_hdf5(hashrate, btc_preis, market_cap, hdf5_file='scraped_data.h5'):
   # add timestamps
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    with h5py.File(hdf5_file, 'a') as hdf:  # 'a' für Append-Modus
        # new datafile for each scraping routine
        group = hdf.create_group(timestamp)

        # save the datapoints
        group.create_dataset('hashrate', data=np.array(hashrate))
        group.create_dataset('btc_preis', data=np.array(btc_preis))
        group.create_dataset('market_cap', data=np.array(market_cap))


def read_from_hdf5(hdf5_file='scraped_data.h5'):
    with h5py.File(hdf5_file, 'r') as hdf:
        # Iterate throuh the hdf5
        for timestamp in hdf.keys():
            # get keys
            group = hdf[timestamp]

            # read data of each dataset
            hashrate = group['hashrate'][()]
            btc_preis = group['btc_preis'][()]
            market_cap = group['market_cap'][()]

            # print data
            print(f"Zeitstempel: {timestamp}, Hashrate: {hashrate}, BTC Preis: {btc_preis}, Market Cap: {market_cap}")


