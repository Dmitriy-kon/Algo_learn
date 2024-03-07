from functools import wraps
import random
import time

random.seed(1)
arr = random.sample(range(1, 10000), 1000)
arr.sort()

search = 8807


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter() - start

        name = func.__name__
        arg_str = ", ".join(f"{arg!r}" for arg in args)
        kwarg_str = ", ".join(
            f"{kwarg1!r} = {kwarg2!r}" for kwarg1, kwarg2 in kwargs.items()
        )
        print(f"[{end:.4f}s] {name}({arg_str}, {kwarg_str}) -> {res!r}")
        return res

    return wrapper


class Player:
    def __init__(self, rating: int, nick_name: str) -> None:
        self.rating = rating
        self.nick_name = nick_name
    
    def __repr__(self) -> str:
        return f"Player ({self.nick_name}, {self.rating})"


rating = [
    Player(1100, "Crowbar Freeman"),  # 0
    Player(1200, "London Mollarik"),  # 1
    # Player(1600, "Shmike"),
    Player(1600, "Raziel of Kain"),  # 2
    Player(1600, "Gwinter of Rivia"),  # 3
    Player(1600, "Slayer of Fate"),  # 4
    Player(3000, "Jon Know"),  # 5
    Player(4000, "Caius Cosades"),  # 6
]


class Doka3:
    def __init__(self, ratings: list) -> None:
        # Наша рейтинговая таблица выглядит примерно так
        self.ratings = ratings

    def find_spot(self, new_player: Player):
        left = 0
        right = len(self.ratings) - 1

        while left < right:
            middle = (left + right) // 2
            
            if self.ratings[middle].rating < new_player.rating:
                left = middle + 1
            else:
                right = middle
        return left
    
    def add_player(self, new_player):
        self.ratings.append("")
        spot = self.find_spot(new_player)
        length = len(self.ratings)
        
        for i in range(length-1, spot, -1):
            self.ratings[i] = self.ratings[i-1]
            
        self.ratings[spot] = new_player
            


if __name__ == "__main__":
    rating = Doka3(rating)
    player = Player(1600, "Shmike")
    print(rating.ratings)
    rating.add_player(player)
    for i in rating.ratings:
        print(i)
