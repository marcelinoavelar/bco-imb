from dataclasses import dataclass
from select import select

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

    def purchase(self, owner_name: str) -> bool:
        if len(owner_name) > 0:
            self.owner = owner_name
            self.status = "purchased"
    
    def free(self):
        self.owner = None
        self.status = "available"