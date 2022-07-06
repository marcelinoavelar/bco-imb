from dataclasses import dataclass
from typing import Optional

from attr import field


@dataclass
class Property:
    price: float
    rental: float
    owner: str = None
    status: str = "available"

    def __post_init__(self):
        if self.price < 0.1:
            raise ValueError('Invalid price')
        if self.rental < 0.1:
            raise ValueError('Invalid rental')
