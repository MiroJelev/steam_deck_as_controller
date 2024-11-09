from pyjoystick.sdl2 import Key, Joystick, run_event_loop

def print_add(joy):
    print('Added', joy)

def print_remove(joy):
    print('Removed', joy)

def key_received(key):
    print('received', key)
    if key.value == Key.HAT_UP:
        print('UP')
        #do something
    elif key.value == Key.HAT_DOWN:
        print('DOWN')
        #do something
    if key.value == Key.HAT_LEFT:
        print('LEFT')
        #do something
    elif key.value == Key.HAT_UPLEFT:
        print('UPLEFT')
        #do something
    elif key.value == Key.HAT_DOWNLEFT:
        print('DOWNLEFT')
        #do something
    elif key.value == Key.HAT_RIGHT:
        print('RIGHT')
        #do something
    elif key.value == Key.HAT_UPRIGHT:
        print('UPRIGHT')
        #do something
    elif key.value == Key.HAT_DOWNRIGHT:
        print('DOWNRIGHT')
        #do something

run_event_loop(print_add, print_remove, key_received)