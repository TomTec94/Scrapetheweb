import csv

url_1 = 'https://bitinfocharts.com/de/comparison/bitcoin-hashrate.html#3y'
url_2 = 'https://www.coindesk.com/price/bitcoin/'
url_3 = 'https://www.coincarp.com/de/currencies/bitcoin/'

# create the csv file

"""
csv_file_path = 'webpages.csv'
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Webpage to scrape', 'URL'])

    writer.writerow(['Bitcoin Hashrate', url_1])
    writer.writerow(['Bitcoin Price', url_2])
    writer.writerow(['Bitcoin Market Cap', url_3])
    """

def read_urls_from_csv(csv_file_path):
    urls = []

    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            urls.append(row[1])

    url_1 = urls[0] if len(urls) > 0 else None
    url_2 = urls[1] if len(urls) > 1 else None
    url_3 = urls[2] if len(urls) > 2 else None

    return url_1, url_2, url_3

csv_file_path = 'webpages.csv'

url_1, url_2, url_3 = read_urls_from_csv(csv_file_path)

print(url_1, url_2, url_3)