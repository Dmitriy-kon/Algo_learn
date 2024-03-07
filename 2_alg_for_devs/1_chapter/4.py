from faker import Faker


def get_random_phone():
    fake = Faker()
    return fake.phone_number()


phone_numbers = [
    "+78000000000",
    "+79000000000",
    "+79000000001",
    "+79000000002",
    "+79000000002",
    "+79000000003",
    "+79000000003",
    "+79000000003",
    "+79000000003",
    "+79000000004",
    "+79000000005",
    "+79000000005",
    "+79000000006",
    "+79000000006",
    "+79000000007",
]


def get_unique_phones(phone_number: list[int]):
    unuqie_phones = []
    prev_number = phone_number[0]

    for i in range(1, len(phone_number)):
        if phone_number[i] != prev_number:
            unuqie_phones.append(phone_number[i])
            prev_number = phone_number[i]
        
        
    return unuqie_phones


def main():
    print(get_unique_phones(phone_numbers))
    print(phone_numbers)


if __name__ == "__main__":
    main()
