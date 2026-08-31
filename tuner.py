import json

with open("youtube_titles.json", "r") as file:
    data = json.load(file)

empty_dict = dict()
word_history = dict()
for parts in data:
    count_of_titles = parts["counts"].items()
    for titles in count_of_titles:
        list_of_titles=list(titles)
        headline = list_of_titles[0]
        count = list_of_titles[1]
        if headline not in empty_dict:
            empty_dict[headline] = [count]
        else:
            empty_dict[headline].append(count)

for keywords in empty_dict:
    try:
        average = sum(empty_dict[keywords][:-1]) / len(empty_dict[keywords][:-1])
    except ZeroDivisionError:
        average = float(empty_dict[keywords][0])
    latest_reading = empty_dict[keywords][-1]
    print(f"average of '{keywords.upper()}' is:", average)
    outlier_multiplier = latest_reading / average
    print(f"outlier multiplier of '{keywords.upper()}' is {outlier_multiplier}")
    if latest_reading > average * 5:
        print(f"{keywords.upper()} is trending")