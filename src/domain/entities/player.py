from dataclasses import dataclass
import random

from src.domain.entities.property import Property


@dataclass
class Player:
    balance: float

    def __post_init__(self):
        if self.balance < 0.1:
            raise ValueError('Invalid balance')


class PlayerInpulsive(Player):
    profile: str = "impulsive"

    def __post_init__(self):
        if len(self.profile) < 1:
            raise ValueError('Invalid profile')

    def evaluate_purchase(self, property: Property) -> bool:
        return True


class PlayerPicky(Player):
    profile: str = "picky"

    def __post_init__(self):
        if len(self.profile) < 1:
            raise ValueError('Invalid profile')

    def evaluate_purchase(self, property: Property) -> bool:
        if property.rental > 50:
            return True
        return False


class PlayerCautious(Player):
    profile: str = "cautious"

    def __post_init__(self):
        if len(self.profile) < 1:
            raise ValueError('Invalid profile')

    def evaluate_purchase(self, property: Property) -> bool:
        balance =  self.balance - property.price
        print(f'\n {balance}  \n')
        if balance >= 80:
            return True
        return False


class PlayerRandom(Player):
    profile: str = "random"

    def __post_init__(self):
        if len(self.profile) < 1:
            raise ValueError('Invalid profile')

    
    def evaluate_purchase(self, property: Property) -> bool:
        if (round(random.uniform(1, 2))%2) == 0:
            return True
        else:
            False