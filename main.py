from pprint import pprint
import requests
import json

token = 2619421814940190


def hulk_request():
    url = "https://superheroapi.com/api/2619421814940190/search/Hulk"
    response = requests.get(url, timeout=5)
    data = response.json()
    with open('Hulk.json', 'w') as f:
        json.dump(data, f, indent=2)


def ca_request():
    url = "https://superheroapi.com/api/2619421814940190/search/Captain_America"
    response = requests.get(url, timeout=5)
    data = response.json()
    with open('Captain_America.json', 'w') as f:
        json.dump(data, f, indent=2)


def thanos_request():
    url = "https://superheroapi.com/api/2619421814940190/search/Thanos"
    response = requests.get(url, timeout=5)
    data = response.json()
    with open('Thanos.json', 'w') as f:
        json.dump(data, f, indent=2)


def hulk_ps():
    with open('Hulk.json') as f:
        data = json.load(f)
        info = data['results']
        temp = {}
        for stats in info:
            # print(f"Name: {stats['name']}")
            temp['Name'] = stats['name']
            # print(f"ID: {stats['id']}")
            temp['ID'] = stats['id']
            for a, b in stats['powerstats'].items():
                temp[f"{a}"] = b
            return temp



def ca_ps():
    with open('Captain_America.json') as f:
        data = json.load(f)
        info = data['results']
        temp = {}
        for stats in info:
            # print(f"Name: {stats['name']}")
            temp['Name'] = stats['name']
            # print(f"ID: {stats['id']}")
            temp['ID'] = stats['id']
            for a, b in stats['powerstats'].items():
                temp[f"{a}"] = b
            return temp


def thanos_ps():
    with open('Thanos.json') as f:
        data = json.load(f)
        info = data['results']
        temp = {}
        for stats in info:
            # print(f"Name: {stats['name']}")
            temp['Name'] = stats['name']
            # print(f"ID: {stats['id']}")
            temp['ID'] = stats['id']
            for a, b in stats['powerstats'].items():
                temp[f"{a}"] = b
            return temp


def comparison():
    name_list = [(hulk_stats['Name']), (captain_stats['Name']), (thanos_stats['Name'])]
    int_list = [int(hulk_stats['intelligence']), int(captain_stats['intelligence']), int(thanos_stats['intelligence'])]
    x = dict(zip(name_list, int_list))
    y = list(zip(x.values(), x.keys()))
    print(f"Самый умный: {max(y)[1]}")

hulk_stats = hulk_ps()
print(hulk_stats)
captain_stats = ca_ps()
print(captain_stats)
thanos_stats = thanos_ps()
print(thanos_stats)
comparison()
