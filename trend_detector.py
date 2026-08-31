from config import yt_api
import requests
import json
import datetime
import time

while True:
    raw_data = requests.get(f"https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&regionCode=US&maxResults=50&key={yt_api}")
    converted_data = raw_data.json()
    items = converted_data["items"]
    title_index = dict()
    for item in items:
        titles = item["snippet"]["title"].split(" ")
        for title in titles:
            title = title.strip("!@#$%^&*()_=+[]|;:\'\",<>./?  ").lower()
            if title == '' or title == '-' or title.isnumeric():
                continue
            if title not in title_index:
                title_index[title] = 1
            else:
                title_index[title] += 1
    try: 
        with open("youtube_titles.json", "r") as outfile:
            loaded_data = json.load(outfile)
    except FileNotFoundError:
        loaded_data = list()
    timestamp = str(datetime.datetime.now())
    snapshot = {"time": timestamp, "counts": title_index}
    loaded_data.append(snapshot)
    with open("youtube_titles.json", "w") as outfile:
        json.dump(loaded_data, outfile, indent=2)

    title_data = dict()
    for parts in loaded_data:
        count_of_titles = parts["counts"].items()
        for titles in count_of_titles:
            list_of_titles=list(titles)
            headline = list_of_titles[0]
            count = list_of_titles[1]
            if headline not in title_data:
                title_data[headline] = [count]
            else:
                title_data[headline].append(count)

    for keywords in title_data:
        try:
            average = sum(title_data[keywords][:-1]) / len(title_data[keywords][:-1])
        except ZeroDivisionError:
            average = float(title_data[keywords][0])
        latest_reading = title_data[keywords][-1]
        if len(title_data[keywords]) > 5 and latest_reading > average * 2:
            print(f"{keywords.upper()} is hot right now at {timestamp}")

    time.sleep(3600)

      