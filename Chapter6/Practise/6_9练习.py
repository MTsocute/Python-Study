pet_1 = {
    'type': 'Happy doge1',
    'Owner_Name': 'Momo1',
}

pet_2 = {
    'type': 'Happy doge2',
    'Owner_Name': 'Momo2',
}

pet_3 = {
    'type': 'Happy doge3',
    'Owner_Name': 'Momo3',
}

pets = [pet_1, pet_2, pet_3]

count = 0
for pet in pets:
    count = count + 1
    print("Type of Pet" + str(count) + " is " + pet['type'])
    print("Owner of Pet" + str(count) + " is " + pet['Owner_Name'])
    print("-"*32, '\n')