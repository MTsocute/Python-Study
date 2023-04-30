user_and_reason = {}

def reason_for_code():
    flag = True
    while flag:
        user_name = input("Can you tell me what is your name:")
        user_reason = input("Can you tell the reason you like Programming:")
        
        judge = input("Would you like to quit(yes/no)?")
        print(f'User says {judge}')

        if judge.strip().lower() == "yes":
            user_and_reason[user_name] = user_reason
            flag = False
        else:
            user_and_reason[user_name] = user_reason

def write_to_txt():
    with open("/Users/momo/Desktop/Python/Chapter10/data/guest_reason.txt", 'w') as file_obj:
        for user_name, user_reason in user_and_reason.items():
            file_obj.write(f'{user_name} loves programming because \"{user_reason}\"\n')
        print("End~")

if __name__ == '__main__':
    reason_for_code()
    print(user_and_reason)
    write_to_txt()