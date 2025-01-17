from pyjoystick.sdl2 import Key, Joystick, run_event_loop
import socket
import protocol

HOST = socket.gethostname()#"127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

state = protocol.State()

connection = None

def print_add(joy):
  print('Added', joy)
def print_remove(joy):
  print('Removed', joy)

def key_received(key: Key):
  print(key)
  if key.keytype == Key.KeyTypes.BUTTON:
    if key.number == 0:
      state.button_A = key.value
    elif key.number == 1:
      state.button_B = key.value
    elif key.number == 2:
      state.button_X = key.value
    elif key.number == 3:
      state.button_Y = key.value
    elif key.number == 4:
      state.button_L_SHOULDER = key.value
    elif key.number == 5:
      state.button_R_SHOULDER = key.value
    elif key.number == 6:
      state.button_BACK = key.value
    elif key.number == 7:
      state.button_START = key.value
    # elif key.number == 8: # no this button on steam deck
    #   pass
    elif key.number == 9:
      state.button_L_THUMB = key.value
    elif key.number == 10:
      state.button_R_THUMB = key.value
  elif key.keytype == Key.KeyTypes.AXIS:
    if key.number == 0:
      state.left_joystick_x = int(
          (key.value + 1) / 2 * 65535)  # [-1, 1] => [0, 65535]
    elif key.number == 1:
      state.left_joystick_y = int(
          (-key.value + 1) / 2 * 65535)  # reverse axis-Y value
    elif key.number == 2:
      state.left_trigger = int(key.value * 255)  # [0, 1] => [0, 255]
    elif key.number == 3:
      state.right_joystick_x = int(
          (key.value + 1) / 2 * 65535)  # [-1, 1] => [0, 65535]
    elif key.number == 4:
      state.right_joystick_y = int(
          (-key.value + 1) / 2 * 65535)  # reverse axis-Y value
    elif key.number == 5:
      state.right_trigger = int(key.value * 255)  # [0, 1] => [0, 255]
  elif key.keytype == Key.KeyTypes.HAT:
    state.button_DPAD = key.value

  print(state.encode())
  connection.sendall(state.encode())

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print(f"Listening at: {s.getsockname()}: {PORT}")
connection, addr = s.accept()

    # with connection:
    #     print(f"Connected by {addr}")
        # while True:
        #     connection.sendall(state.encode())

run_event_loop(print_add, print_remove, key_received)
