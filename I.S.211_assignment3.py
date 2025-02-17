import requests

def download_file(url='http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'):
    response = requests.get(url)
    with open('weblog.csv', 'wb') as file:
        file.write(response.content)

# Call download_file with the URL directly
download_file()  # You can also specify a different URL here if needed

import csv

def process_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Assuming the file has 5 columns: path, datetime_accessed, browser, status, size
            try:
                path, datetime_accessed, browser, status, size = row
                print(f'Path: {path}, DateTime: {datetime_accessed}, Browser: {browser}, Status: {status}, Size: {size}')
            except ValueError:
                # Handle rows with different number of columns (e.g., skip them or print an error message)
                print(f"Skipping row: {row} - Invalid format")

if __name__ == "__main__":
    process_file('weblog.csv')

import re

def find_image_hits(filename):
    image_extensions = re.compile(r'\.(jpg|gif|png)$', re.IGNORECASE)
    total_requests = 0
    image_requests = 0

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            total_requests += 1
            path = row[0]
            if image_extensions.search(path):
                image_requests += 1

    percentage = (image_requests / total_requests) * 100
    print(f'Image requests account for {percentage:.1f}% of all requests')

if __name__ == "__main__":
    find_image_hits('weblog.csv')

from collections import Counter

def find_most_popular_browser(filename):
    browsers = ['Firefox', 'Chrome', 'Internet Explorer', 'Safari']
    browser_counts = Counter()

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            user_agent = row[2]
            for browser in browsers:
                if browser in user_agent:
                    browser_counts[browser] += 1
                    break

    most_popular_browser = browser_counts.most_common(1)[0]
    print(f'The most popular browser is {most_popular_browser[0]} with {most_popular_browser[1]} hits')

if __name__ == "__main__":
    find_most_popular_browser('weblog.csv')