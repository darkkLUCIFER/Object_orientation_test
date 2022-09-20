from random import choice

from advertisment import ApartmentSell, HouseSell, ApartmentRent, HouseRent
from user import User
from estate import Apartment, House, Store
from region import Region

FIRST_NAME = ['ali', 'sajad', 'mahdi']
LAST_NAME = ['shademan', 'amini', 'norouzi']
PHONE_NUMBER = ['09151234567', '09121234567', '09351234567', '09181234567', '09211234567', '09871234567']
if __name__ == '__main__':
    for number in PHONE_NUMBER:
        User(first_name=choice(FIRST_NAME), last_name=choice(LAST_NAME), phone_number=number)

    for user in User.objects_list:
        print(f'{user.id} \t{user.full_name}')

    reg1 = Region(name='R1')
    apt1 = Apartment(
        user=User.objects_list[0], area=80, rooms_count=2, built_year=1393,
        has_elevator=True, has_parking=True, floor=2, region=reg1, address='iran-mashhad'
    )
    # apt1.show_description()

    house1 = House(
        has_yard=True, floors_count=1, user=User.objects_list[1], area=400,
        rooms_count=6, built_year=1370, region=reg1, address='iran-mashhad'
    )
    # house1.show_description()

    store1 = Store(
        user=User.objects_list[2], area=30, rooms_count=0, built_year=1390,
        region=reg1, address='iran-mashhad'
    )
    # store1.show_description()

    apartment_sell = ApartmentSell(
        user=User.objects_list[0], area=80, rooms_count=2, built_year=1393,
        has_elevator=True, has_parking=True, floor=2, region=reg1, address='iran-mashhad',
        price_per_meter=10, discountable=True, convertable=False
    )
    apartment_sell.show_detail()

    house_sell = HouseSell(
        has_yard=True, floors_count=1, user=User.objects_list[1], area=400,
        rooms_count=6, built_year=1370, region=reg1, address='iran-mashhad',
        price_per_meter=20, discountable=False, convertable=False

    )
    house_sell.show_detail()

    apartment_rent = ApartmentRent(
        user=User.objects_list[0], area=80, rooms_count=2, built_year=1393,
        has_elevator=True, has_parking=True, floor=2, region=reg1, address='iran-mashhad',
        discountable=True, convertable=False, initial_price=100, monthly_price=3.5
    )

    house_rent = HouseRent(
        has_yard=True, floors_count=1, user=User.objects_list[1], area=400,
        rooms_count=6, built_year=1370, region=reg1, address='iran-mashhad',
        convertable=True, initial_price=130, monthly_price=5.5
    )

    print(ApartmentSell.manager.search(region=reg1))
    print(ApartmentRent.manager)
    print(HouseSell.manager)
    print(HouseRent.manager)
    print(HouseRent.manager.get(region=reg1))
