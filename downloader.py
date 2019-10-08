import requests
import json
import time

# Some fake headers as a boilerplate
HEADERS = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-GB,en;q=0.5",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Cookie": "",
"Host": "books.google.co.uk",
"TE": "Trailers",
"Upgrade-Insecure-Requests": "1",
"User-Agent": ""
}

OUTPUT_FOLDER = 'output/'
OUTPUT_FILE_PREFIX = 'book-page'
OUTPUT_FILE_EXTENSION = '.png'
URL_IDENTIFIER = 'content?id='
HAR_FILE = 'books.har'

if __name__ == '__main__':
    # Start by extracting the useable URLs from the HAR file
    # Load the data into JSON
    with open(HAR_FILE, 'r') as f:
        har_data = json.load(f)

    # Iterate over entries, get the URLs, validate them
    # and add to a list if it's useable
    urls = []
    for entry in har_data['log']['entries']:
        if 'url' in entry['request']:
            if URL_IDENTIFIER in entry['request']['url']:
                urls.append(entry['request']['url'])

    # Open a request for each URL and save the response to a file
    file_counter = 0
    for url in urls:
        # Increment counter for file output
        file_counter += 1
        output = f'{OUTPUT_FOLDER}{OUTPUT_FILE_PREFIX}{str(file_counter)}{OUTPUT_FILE_EXTENSION}'
        qs = {}

        # Output the response to a file
        with open(output, 'wb') as f:
            res = requests.get(url, headers=HEADERS)
            f.write(res.content)
            time.sleep(2)
