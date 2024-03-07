mobiles = {
    "87773456201": 392,
    "87776543820": 184,
    "87779876543": 217,
    "87771234567": 289,
    "87775678901": 356,
    "87772345678": 402,
    "87774567890": 168,
    "87778765432": 231,
    "87770123456": 305,
    "87778901234": 274,
}


def get_index_by_key(data: int | str) -> int:
    if isinstance(data, str):
        data = int(data)
    res = data % len(mobiles)
    return res


def get_value_by_index(data: int) -> int:
    index = get_index_by_key(data)
    return list(mobiles)[index], index, data


for i in mobiles:
    print(get_value_by_index(i))
