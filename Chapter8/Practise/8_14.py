def make_car(manufacture, type, **info):
    info['Manufacture'] = manufacture
    info['Type'] = type
    print(info)


car = make_car('subaru', 'outback', color='blue', tow_package=True)