from pynput.keyboard import Key, Controller
import time
import datetime
import threading

print()
print('-----------------------------------------------------------------------------------------------------')
print()

keyboard = Controller()
adv = int(input('Which adventure did you want to idle? '))
boosters = input('Do you have boosters enabled? Y/N ').upper()
leng = adv * 3600

if boosters == 'Y':
    leng = leng/2

convert = datetime.timedelta(seconds=leng)
counter = 0

def adventure():
    while True:
        time.sleep(5)
        keyboard.type('@Idl')
        time.sleep(0.5)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.5)
        keyboard.type(f'adventure {adv}')
        time.sleep(0.2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print(f'Adventure Started | Level {adv} | Length {convert}')
        time.sleep(leng)
        keyboard.type('@Idl')
        time.sleep(0.5)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.5)
        keyboard.type('status')
        time.sleep(0.2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        counter = counter+1
        print(f'Adventure {adv} Complete!')
        print(f'You have completed {counter} adventure(s) this session!')

def pray():
    while True:
        time.sleep(10)
        keyboard.type('@Idl')
        time.sleep(0.5)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.5)
        keyboard.type('pray')
        time.sleep(0.2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print(f'Pray attempted, will try again in 1 hour')
        time.sleep(3600)

def steal():
    while True:
        time.sleep(15)
        keyboard.type('@Idl')
        time.sleep(0.5)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.5)
        keyboard.type('steal')
        time.sleep(0.2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print(f'Steal attempted, will try again in 1 hour')
        time.sleep(3600)

if __name__ == "__main__":
    p1 = threading.Thread(target=adventure)
    p2 = threading.Thread(target=pray)
    p3 = threading.Thread(target=steal)

    p1.start()
    p2.start()
    p3.start()