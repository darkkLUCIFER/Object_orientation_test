from random import choice
from user import User

FIRST_NAME = ['ali', 'sajad', 'mahdi']
LAST_NAME = ['shademan', 'amini', 'norouzi']
PHONE_NUMBER = ['09151234567', '09121234567', '09351234567', '09181234567', '09211234567', '09871234567']
if __name__ == '__main__':
    for number in PHONE_NUMBER:
        User(first_name=choice(FIRST_NAME), last_name=choice(LAST_NAME), phone_number=number)

    for user in User.objects_list:
        print(f'{user.id} \t{user.full_name}')
