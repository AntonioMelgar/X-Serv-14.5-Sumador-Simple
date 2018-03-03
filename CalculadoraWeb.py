#!/usr/bin/python3
"""
SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket
import random
import calculadora

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))

mySocket.listen(5)

while True:
	print('Waiting for connections')
	(recvSocket, address) = mySocket.accept()
	print('HTTP request received:')
	request = str(recvSocket.recv(1234), 'utf-8');
	request = request.split()[1].split('/')[1:]	
	operando1 = request[0];
	operacion = request[1];
	operando2 = request[2];
 
	resultado = calculadora.funciones[operacion](float(operando1), float(operando2));

	recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                    '<html><body><h1>El resultado es: ' + str(resultado) + '</h1></body></html>' +
                    "\r\n", 'utf-8'))
	recvSocket.close()


