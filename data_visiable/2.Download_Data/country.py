from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """ 根据指定的国家，返回对应的国别嘛 """
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        # 没找到就返回 None
    return None


print(get_country_code("Andorra"))
print(get_country_code("United Arab Emirates"))
print(get_country_code("Afghanistan"))