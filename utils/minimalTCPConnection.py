#!/usr/bin/env python3

import socket, argparse

parser = argparse.ArgumentParser()

# Allows inputs from bash

parser.add_argument ('-ip', required =True) # IP Address
parser.add_argument ('-port', type=int, required =True) # Port number
args = parser.parse_args() 

print ('Connecting to', args.ip, args.port)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates the client socket
client_socket.connect((args.ip, args.port)) #Connects the client to the server

print('Connected to', args.ip, args.port)
print('Trying to read ...')

while True:


	data = client_socket.recv(1)

	if not data:
		print ('Connection Lost!')
		break

	else:
		print(data)
		# print data.encode('utf-8').hex()


client_socket.close()