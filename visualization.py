# Contains functions to visualize the data
from datetime import datetime
import h5py
import matplotlib.pyplot as plt
import numpy as np
# path
file_path ='scraped_data.h5'
import matplotlib.dates as mdates



# Take a look at the scraped data
def print_all_data(file_path):
    with h5py.File(file_path, 'r') as file:
        # print all data
        def print_dataset(name, obj):
            if isinstance(obj, h5py.Dataset):
                print(f"Dataset: {name}")
                print("Daten:", obj[()])
                print()

        # Interare through all datasets
        file.visititems(print_dataset)




# Closer look at the data
def hdf5_overview(file_path):
    with h5py.File(file_path, 'r') as file:
        # Show groups
        num_groups = len(file.keys())
        print(f"Count of Groups: {num_groups}")


        # Count of datasets of the groups
        datasets_per_group = {}
        for group_name in file.keys():
            group = file[group_name]
            datasets_per_group[group_name] = sum(isinstance(obj, h5py.Dataset) for _, obj in group.items())

        print("Count of Datasets for each group:")
        for group_name, count in datasets_per_group.items():
            print(f"  {group_name}: {count}")


# Take a look at a specific group
def print_group_data(file_path, group_name):
    with h5py.File(file_path, 'r') as file:
        if group_name in file:
            print(f"Data in Group '{group_name}':")
            group = file[group_name]
            for dataset_name, dataset in group.items():
                print(f"  Dataset: {dataset_name}")
                print("  Data:", dataset[()])
                print()
        else:
            print(f"Group '{group_name}' does not exist.")

# Testset randomly chosen
group_name = '2023-12-14_21-45-25'

print_group_data(file_path, group_name)

# Call of the Funktion if needed
hdf5_overview(file_path)
# print_all_data(file_path)


import matplotlib
matplotlib.use('TkAgg')   # Chose plot in seperate window



import matplotlib.pyplot as plt
import h5py
from datetime import datetime
import numpy as np


def plot_data(file_path):
    with h5py.File(file_path, 'r') as hdf:
        # Create lists to save the data
        timestamps = []
        hashrates = []
        btc_prices = []
        market_caps = []

        # Iterate through the groups to retrieve the data
        for group_name in hdf.keys():
            group = hdf[group_name]
            # Convert group name into date format
            timestamp = datetime.strptime(group_name, "%Y-%m-%d_%H-%M-%S")
            timestamps.append(timestamp)
            hashrates.append(group['hashrate'][()])
            btc_prices.append(group['btc_preis'][()])
            market_caps.append(group['market_cap'][()])

        # Create the plot for each dataset
        plt.figure(figsize=(12, 8))

        # Function to plot each dataset and highlight gaps
        def plot_with_gaps_and_highlight(ax, timestamps, data, label, color):
            # Plot the data
            ax.plot(timestamps, data, linestyle='-', color=color)

            # Highlight gaps
            for i in range(1, len(timestamps)):
                if (timestamps[i] - timestamps[i - 1]).total_seconds() > 3000:
                    ax.axvspan(timestamps[i - 1], timestamps[i], color='red', alpha=0.3)

            ax.set_ylabel(label)
            ax.legend()
            ax.grid(True)  # Enable grid

        # Hashrate Plot
        ax1 = plt.subplot(3, 1, 1)
        plot_with_gaps_and_highlight(ax1, timestamps, hashrates, 'Hashrate [TH/s]', 'blue')

        # BTC Price Plot
        ax2 = plt.subplot(3, 1, 2)
        plot_with_gaps_and_highlight(ax2, timestamps, btc_prices, 'BTC Price [$]', 'orange')

        # Market Cap Plot
        ax3 = plt.subplot(3, 1, 3)
        plot_with_gaps_and_highlight(ax3, timestamps, market_caps, 'Market Cap [B $]', 'green')

        plt.xlabel('Zeit')
        plt.tight_layout()
        plt.show()


# Replace 'file_path' with the actual path to your HDF5 file
plot_data(file_path)




import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# plot data gaps and relevant scraping times
def plot_data_gaps_and_periods(file_path):
    with h5py.File(file_path, 'r') as hdf:
        # list to save time stamps (groupnames)
        timestamps = []

        # Iterate through group name
        for group_name in hdf.keys():
            # convert group name into date format
            timestamp = datetime.strptime(group_name, "%Y-%m-%d_%H-%M-%S")
            timestamps.append(timestamp)

       # sort timestamps
        timestamps.sort()

        # create plot
        plt.figure(figsize=(12, 6))

        # define starting point for plot axis
        start_period = timestamps[0]

        # mark the gaps
        for i in range(1, len(timestamps)):
            # calculate timedistance between timestamps
            gap = timestamps[i] - timestamps[i - 1]

            # if gap larger than 2 intervals
            if gap > timedelta(minutes=40):
                plt.axvspan(start_period, timestamps[i - 1], color='green', alpha=0.5)
                plt.axvspan(timestamps[i - 1], timestamps[i], color='red', alpha=0.5)
                start_period = timestamps[i]

        # define end point of timestamps
        plt.axvspan(start_period, timestamps[-1], color='green', alpha=0.5)

        plt.title('Zeitspannen mit und ohne Daten')
        plt.xlabel('Zeit')
        plt.yticks([])

        # farmatting axises
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())
        plt.gcf().autofmt_xdate()  # Bessere Darstellung der Datumsangaben

        plt.tight_layout()
        plt.show()

# call function if needed
#plot_data_gaps_and_periods(file_path)

