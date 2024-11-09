import socket
import vgamepad as vg



HOST = input("Enter IP Address(default: 192.168.0.12 ): ").strip() or "192.168.0.12"  # Standard loopback interface address (localhost)
PORT = int(input("Enter Port(default: 2300): ").strip() or 2300)  # Port to listen on (non-privileged ports are > 1023)

gamepad = vg.VDS4Gamepad()


# def controller(buttons = []):
# #buttons
# 	gamepad.reset()
# 	if (buttons[0] >> 0) & 1:
# 		#print("pressed SQUARE")
# 		gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)
# 	if (buttons[0] >> 1) & 1:
# 		#print("pressed TRIANGLE")
# 		gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
# 	if (buttons[0] >> 2) & 1:
# 		#print("pressed CIRCLE")
# 		gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
# 	if (buttons[0] >> 3) & 1:
# 		#print("pressed CROSS")
# 		gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
# #directions
# 	if ((buttons[0] >> 4) & 1) and ((buttons[0] >> 6) & 1):
# 		gamepad.directional_pad(direction=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NORTHWEST)
# 	elif ((buttons[0] >> 5) & 1) and ((buttons[0] >> 6) & 1):
# 		gamepad.directional_pad(direction=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_SOUTHWEST)
# 	elif ((buttons[0] >> 5) & 1) and ((buttons[0] >> 7) & 1):
# 		gamepad.directional_pad(direction=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_SOUTHEAST)
# 	elif ((buttons[0] >> 4) & 1) and ((buttons[0] >> 7) & 1):
# 		gamepad.directional_pad(direction=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NORTHEAST)
# 	elif ((buttons[0] >> 4) & 1) or ((buttons[0] >> 5) & 1) or ((buttons[0] >> 6) & 1) or ((buttons[0] >> 7) & 1):
# 		if (buttons[0] >> 4) & 1:
# 			#print("pressed UP")
# 			gamepad.directional_pad(direction=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NORTH)
# 		elif (buttons[0] >> 5) & 1:
# 			#print("pressed DOWN")
# 			gamepad.directional_pad(direction=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_SOUTH)
# 		elif (buttons[0] >> 6) & 1:
# 			#print("pressed LEFT")
# 			gamepad.directional_pad(direction=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_WEST)
# 		elif (buttons[0] >> 7) & 1:
# 			#print("pressed RIGHT")
# 			gamepad.directional_pad(direction=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_EAST)
# 	else:
# 		gamepad.directional_pad(direction=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NONE)
# #triggers start and select
# 	if (buttons[1] >> 0) & 1:
# 		#print("pressed LTRIGGER")
# 		gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
# 	if (buttons[1] >> 1) & 1:
# 		#print("pressed RTRIGGER")
# 		gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_RIGHT)
# 	if (buttons[1] >> 2) & 1:
# 		#print("pressed SELECT")
# 		gamepad.press_button(button=vg.DS4_SPECIAL_BUTTONS.DS4_SPECIAL_BUTTON_PS)
# 	if (buttons[1] >> 3) & 1:
# 		#print("pressed START")
# 		gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_OPTIONS)
# #stick
# 	#print(buttons[2])
# 	#print(buttons[3])
# 	gamepad.left_joystick(x_value=buttons[2], y_value=buttons[3])  # value between 0 and 255
# 	gamepad.update()

def main():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		while(1):
			data = s.recv(1024)
			# controller(data)
			print(f"Received: {data}")




#controller([2,2,185,125])
main()


