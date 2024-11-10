import socket
import protocol
# import vgamepad as vg



HOST = input("Enter IP Address(default: 192.168.0.12 ): ").strip() or "192.168.0.12"  # Standard loopback interface address (localhost)
PORT = int(input("Enter Port(default: 2300): ").strip() or 2300)  # Port to listen on (non-privileged ports are > 1023)

# gamepad = vg.VDS4Gamepad()


data = protocol.State()
protocol_len = len(data.encode())

def main():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		while(1):
			data = s.recv(protocol_len)
			# controller(data)
			if len(data) > 0:
			    print(f"Received: {data.decode()}")




#controller([2,2,185,125])
main()


