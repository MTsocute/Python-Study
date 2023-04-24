cities = {
    'California': {
        'country': 'America',
        'population': 1000,
        'fact': 'haha'
    },
    'WenZhou': {
        'country': 'China',
        'population': 200,
        'fact': 'WenZhounese never live here'
    },
    'Good View': {
        'country': 'Africa',
        'population': 280,
        'fact': 'Zebra!!!'
    }
}

for str_City_Name, dc_City_attr in cities.items():
    print("City:", str_City_Name)
    print('\tLocation: ', dc_City_attr['country'])
    print('\tPopulation: ', dc_City_attr['population'])
    print('\tFact: ', dc_City_attr['fact'])
