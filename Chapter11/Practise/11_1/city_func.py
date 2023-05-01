def city_and_country(city_name, counrty_name, population=''):
    if population:
        format_string = f'{city_name},{counrty_name} - {population}'
        return format_string
    else:
        format_string = f'{city_name},{counrty_name}'
        return format_string
