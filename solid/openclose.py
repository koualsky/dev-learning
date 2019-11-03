""" KOD ZŁY:
class Profession(Enum):
    ARTIST = auto()
    LAWYER = auto()

@dataclass
class TaxPayer:
    profession: str
    salary: float


def calculate_tax(tax_payer):
    if tax_payer.profession == Profession.ARTIST:
        return tax_payer.salary * 0.25
    elif tax_payer.profession == Profession.LAWYER:
        return tax_payer.salary * 0.34

Poniżej kod dobry, umożliwiający dalsze proste rozszerzanie.
"""

from abc import ABC, abstractmethod
from enum import Enum, auto
from dataclasses import dataclass


class Profession(Enum):
    ARTIST = auto()
    LAWYER = auto()

# dataclass zamienia mi salary: float tak jakby to bylo uzyte w metodzie init
# pozniej moge tego uzywac jak w zwyklym init: self.salary
@dataclass
class TaxPayer(ABC):

    salary: float

    @abstractmethod
    def calculate_tax(self):
        pass


class Artist(TaxPayer):

    profession = Profession.ARTIST

    def calculate_tax(self):
        return self.salary * 0.25


class Lawyer(TaxPayer):

    profession = Profession.LAWYER

    def calculate_tax(self):
        return self.salary * 0.34


artist = Artist(1000)
print(artist.calculate_tax())