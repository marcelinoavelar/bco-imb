from dataclasses import dataclass
from src.domain.entities.property import Property


@dataclass
class Game:
    properties: list[Property]

    def __post_init__(self):
        if len(self.properties) != 20:
            raise ValueError('Invalid number of properties')
