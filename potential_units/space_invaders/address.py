
#
# type StreetAddress = {
#   HouseNumber: HouseNumber of int
#   StreetName: StreetName of string
# }
#
# type City = City of string
# type PostLeitzahl = PostLeitzahl of int
# type Country =
#   Germany | Kazakhstan | USA
#
# type Address = {
#   Street: StreetAddress
#   City: String
#   PostLeitzahl: PostLeitzahl
#   Country: Country
# }



from dataclasses import dataclass
from typing import NewType
from enum import Enum, auto


@dataclass
class StreetAddress:
    house_number: int
    street_name: str


City = NewType("City", str)
PostLeitzahl = NewType("PostLeitzahl", int)


class Country(Enum):
    Germany = auto()
    Kazakhstan = auto()
    USA = auto()


@dataclass
class Address:
    street: StreetAddress
    city: City
    plz: PostLeitzahl
    country: Country



address = Address(StreetAddress(3, "Karl-Witthalm-Str"), city="Munich", plz=81375, country=Country.Germany)

print(address.street.house_number)
