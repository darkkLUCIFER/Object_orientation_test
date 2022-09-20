from sample import create_samples
from advertisment import ApartmentSell, HouseSell, ApartmentRent, HouseRent, StoreSell, StoreRent


class Handler:
    ADVERTISMENT_TYPES = {
        1: ApartmentSell, 2: ApartmentRent, 3: HouseRent, 4: HouseSell, 5: StoreSell, 6: StoreRent
    }

    SWITCHES = {
        'r': "get_report",
        's': 'show_all_reports',
    }

    def get_report(self):
        for adv in self.ADVERTISMENT_TYPES.values():
            print(adv, adv.manager.count())

    def show_all(self):
        for adv in self.ADVERTISMENT_TYPES:
            print(adv, adv.manager.count())
            for obj in adv.objects_list:
                print(obj.show_detail())

    def run(self):
        print('hello world')
        for key in self.SWITCHES:
            print(f'{key} for {self.SWITCHES[key]}')
        user_input = input('enter your choice: ')
        switch = self.SWITCHES.get(user_input, None)
        if switch is None:
            print('invalid input')
            self.run()
        choice = getattr(self, switch, None)
        choice()
        self.run()


if __name__ == '__main__':
    create_samples()
    handler = Handler()

    handler.run()
