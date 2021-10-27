from pprint import pprint
import requests
import json

token = 2619421814940190


def request_heroes(hero_list):
    temp = []
    for name in hero_list:
        url_1 = "https://superheroapi.com/api/2619421814940190/search/"
        url = url_1 + name
        response = requests.get(url, timeout=5)
        data = response.json()
        info = data['results']
        for stats in info:
            temp.append({
                'Name': stats['name'],
                'Intelligence': int(stats['powerstats']['intelligence'])
            })
    return temp


def comparison():
    most_intelligent = 0
    hero_name = ""
    for hero in heroes_data:
        if most_intelligent < hero['Intelligence']:
            most_intelligent = hero['Intelligence']
            hero_name = hero['Name']
    print(f'Самый умный из всех - {hero_name}. Интеллекта у него {most_intelligent}')


list_of_heroes = ["Hulk", "Captain_America", "Thanos"]
heroes_data = request_heroes(list_of_heroes)
pprint(heroes_data)
comparison()
