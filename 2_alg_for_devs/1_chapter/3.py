from faker import Faker


def get_random_phone():
    fake = Faker()
    return fake.phone_number()


phones = [
    "+77491111111",
    "+98991122222",
    "+89891133333",
    "+87491144444",
    "+77491155555",
    "+77491111111",
    "+77491155555",
]

def get_unique_phones():
    unuqie_phones = []
    
    for i in phones:
        alrady_exist = False
        
        for exist_number in unuqie_phones:
            if exist_number == i:
                alrady_exist = True
                break
        
        if not alrady_exist:
            unuqie_phones.append(i)
        # if i not in unuqie_phones:
            # unuqie_phones.append(i)
            
    return unuqie_phones


def main():
    print(get_unique_phones())
    print(phones)

if __name__ == "__main__":
    main()