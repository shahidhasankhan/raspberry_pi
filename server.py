import socket

HOST = '192.168.8.124' 
PORT = 12345 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'socket created'

try:
	s.bind((HOST, PORT))
except socket.error:
	print 'Bind Failed'

s.listen(1)
print 'Socket awaiting messages'
(conn,addr) = s.accept()
print 'Connected'
print addr

while True:
	data = conn.recv(1024)
	print 'I sent a message back in response to: ' +data

	if data == 'Hello':
		reply = 'Hi, back!'
	elif data == 'This is important':
		reply = 'OK, I have done the important thing you asked'
	elif data == 'quit':
		conn.send('Terminating')
		break
	else:
		reply = 'Unknown command'

	conn.send(reply)
conn.close()
