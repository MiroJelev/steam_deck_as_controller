import socket
import protocol
import vgamepad as vg



HOST = input("Enter IP Address(default: 192.168.0.17 ): ").strip() or "192.168.0.17"  # Standard loopback interface address (localhost)
PORT = int(input("Enter Port(default: 65432): ").strip() or 65432)  # Port to listen on (non-privileged ports are > 1023)

gamepad = vg.VDS4Gamepad()
# gamepad = vg.VX360Gamepad()
state = protocol.State()
new_state = protocol.State()
protocol_len = len(state.encode())
recv_len = 2**((protocol_len - 1).bit_length())
buffer = bytes()

def apply_btn(btn: int, value: int):
  if value == 0:
    gamepad.release_button(btn)
  else:
    gamepad.press_button(btn)



def controller():
    global state
    global new_state
	 # joysticks
    if new_state.left_joystick_x != state.left_joystick_x or new_state.left_joystick_y != state.left_joystick_y:
      gamepad.left_joystick(
          new_state.left_joystick_x - 32768,  # [0, 65535] => [-32768, 32767]
          new_state.left_joystick_y - 32768)
      print("update left joystick")
    if new_state.right_joystick_x != state.right_joystick_x or new_state.right_joystick_y != state.right_joystick_y:
      gamepad.right_joystick(
          new_state.right_joystick_x - 32768,  # [0, 65535] => [-32768, 32767]
          new_state.right_joystick_y - 32768)
      print("update right joystick")

    # triggers
    if new_state.left_trigger != state.left_trigger:
      gamepad.left_trigger(new_state.left_trigger)
      print("update left trigger")
    if new_state.right_trigger != state.right_trigger:
      gamepad.right_trigger(new_state.right_trigger)
      print("update richt trigger")

    # buttons
    if new_state.button_A != state.button_A:
      apply_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_A, new_state.button_A)
      print("update A")
    if new_state.button_B != state.button_B:
      apply_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_B, new_state.button_B)
      print("update B")
    if new_state.button_X != state.button_X:
      apply_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_X, new_state.button_X)
      print("update X")
    if new_state.button_Y != state.button_Y:
      apply_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y, new_state.button_Y)
      print("update Y")
    if new_state.button_L_SHOULDER != state.button_L_SHOULDER:
      apply_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
                new_state.button_L_SHOULDER)
    if new_state.button_R_SHOULDER != state.button_R_SHOULDER:
      apply_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,
                new_state.button_R_SHOULDER)
    if new_state.button_BACK != state.button_BACK:
      apply_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK, new_state.button_BACK)
    if new_state.button_START != state.button_START:
      apply_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_START,
                new_state.button_START)
    if new_state.button_L_THUMB != state.button_L_THUMB:
      apply_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB,
                new_state.button_L_THUMB)
    if new_state.button_R_THUMB != state.button_R_THUMB:
      apply_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB,
                new_state.button_R_THUMB)

    # dpad
    if new_state.button_DPAD != state.button_DPAD:
      if new_state.button_DPAD & 0x01 == 0 and state.button_DPAD & 0x01 != 0:
        gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
      if new_state.button_DPAD & 0x01 != 0 and state.button_DPAD & 0x01 == 0:
        gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
      if new_state.button_DPAD & 0x02 == 0 and state.button_DPAD & 0x02 != 0:
        gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
      if new_state.button_DPAD & 0x02 != 0 and state.button_DPAD & 0x02 == 0:
        gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
      if new_state.button_DPAD & 0x04 == 0 and state.button_DPAD & 0x04 != 0:
        gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
      if new_state.button_DPAD & 0x04 != 0 and state.button_DPAD & 0x04 == 0:
        gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
      if new_state.button_DPAD & 0x08 == 0 and state.button_DPAD & 0x08 != 0:
        gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
      if new_state.button_DPAD & 0x08 != 0 and state.button_DPAD & 0x08 == 0:
        gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)

    gamepad.update()
    state = new_state

def main():
  global state
  global new_state
  global protocol_len
  global buffer

  print(protocol_len)

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
      data = s.recv(recv_len)
      print(data)
      controller()

  # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  #   s.connect((HOST, PORT))
  #   while True:
  #     # recv more if buffer is not enough
  #     while len(buffer) < protocol_len:
  #       data = s.recv(recv_len)
  #     buffer += data
  #
  #     new_state = state.decode(buffer[:protocol_len])
  #     buffer = buffer[protocol_len:]
  #     controller()

    # while(1):
    #   # buffer = s.recv(protocol_len)
    #   data = s.recv(recv_len)
    #   buffer += data
    #   new_state = state.decode(buffer[:protocol_len])
    #   buffer = buffer[protocol_len:]
    #   controller()


 




#controller([2,2,185,125])
main()


