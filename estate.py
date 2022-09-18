from abc import abstractmethod
from base import BaseClass


class EstateAbstract(BaseClass):
    """
    Abstract class for tracking information about the current state of the  simulation.
    """

    def __init__(self, user, area, rooms_count, built_year, region, address, *args, **kwargs):
        self.user = user
        self.area = area
        self.rooms_count = rooms_count
        self.built_year = built_year
        self.region = region
        self.address = address
        super().__init__(*args, **kwargs)

    @abstractmethod
    def show_description(self):
        pass


class Apartment(EstateAbstract):
    """
    Apartment class for tracking information about the current state of the simulation.
    """

    def __init__(self, has_elevator, has_parking, floor, *args, **kwargs):
        self.has_elevator = has_elevator
        self.has_parking = has_parking
        self.floor = floor
        super().__init__(*args, **kwargs)

    def show_description(self):
        print(f'Apartment {self.id}')


class House(EstateAbstract):
    """
    House class for tracking information about the current state of the  simulation.
    """

    def __init__(self, has_yard, floors_count, *args, **kwargs):
        self.has_yard = has_yard
        self.floors_count = floors_count
        super().__init__(*args, **kwargs)

    def show_description(self):
        print(f'House {self.id}')


class Store(EstateAbstract):
    """
    Store class for tracking information about the current state of the  simulation.
    """

    def show_description(self):
        print(f'Store {self.id}')