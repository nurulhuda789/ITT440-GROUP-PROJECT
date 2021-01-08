import socket
import os
from _thread import *
import sys
import json
import random
import time
import math
import errno
from multiprocessing import Process

def process_start(s_sock):
<<<<<<< HEAD
    #s_sock.send(str.encode('\n===MUR MUR CAFE===\n'))
    #optn[0] = s_sock.recv(1024).decode()
	while True:
		s_sock.send(str.encode('\n===MUR MUR CAFE===\n'))
		data = s_sock.recv(1024).decode()
        #data = data.decode("utf-8")

        #process/calculation
		try:
			if optn[0]  == '1':
				optn = 'Nasi lemak'
				price = 2.5
				ans = (price * float(qty))
				print(optn,'......',price,'[',qty,']','=RM',ans)
			elif optn[0] == '2':
				optn = 'Nasi lemak with curry chicken'
				price = 5.4
				ans = (price * float(qty))
				print(optn,'......',price,'[',qty,']','=RM',ans)
			elif optn[0] == '3':
				optn = 'Nasi lemak with chicken rendang'
				price = 6.4
				ans = (price * float(qty))
				print(optn,'......',price,'[',qty,']','=RM',ans)
			elif optn[0] == '4':
				optn = 'Special BBQ Chicken Rice'
				price = 5.4
				ans = (price * float(qty))
				print(optn,'......',price,'[',qty,']','=RM',ans)
			elif optn[0] == '5':
				optn = 'Ginger chicken steamed rice'
				price = 5.4
				ans = (price * float(qty))
				print(optn,'......',price,'[',qty,']','=RM',ans)
			elif optn[0] == '6':
				optn = 'Garlic Toast'
				price = 5.4
				ans = (price * float(qty))
				print(optn,'......',price,'[',qty,']','=RM',ans)
			elif optn[0] == '7':
				optn = 'Crunchy Sugar Hainan Toast'
				price = 5.4
				ans = (price * float(qty))
				print(optn,'......',price,'[',qty,']','=RM',ans)
			elif optn[0] == '8':
				optn = 'Condensed Milk Hainan Toast'
				price = 5.4
				ans = (price * float(qty))
				print(optn,'......',price,'[',qty,']','=RM',ans)
			elif optn[0] == '9':
				optn = 'Western Mixed Platter'
				price = 5.4
				ans = (price * float(qty))
				print(optn,'......',price,'[',qty,']','=RM',ans)
			elif optn[0] == '10':
				optn = 'BBQ Chicken Wrap'
				price = 5.4
				ans = (price * float(qty))
				print(optn,'......',price,'[',qty,']','=RM',ans)
			elif optn[0] == '11':
				optn = 'Chicken Bites Wrap'
				price = 5.4
				ans = (price * float(qty))
				print(optn,'......',price,'[',qty,']','=RM',ans)
			elif optn[0] == '12':
				optn = 'French Fries'
				price = 5.4
				ans = (price * float(qty))
				print(optn,'......',price,'[',qty,']','=RM',ans)
			elif optn[0] == '13':
				optn = 'White Coffee'
				price = 5.4
				ans = (price * float(qty))
				print(optn,'......',price,'[',qty,']','=RM',ans)
			elif optn[0] == '14':
				optn = 'Black Tea'
				price = 5.4
				ans = (price * float(qty))
				print(optn,'......',price,'[',qty,']','=RM',ans)
			elif optn[0] == '15':
				optn = 'Double Enriched Chocolate'
				price = 5.4
				ans = (price * float(qty))
				print(optn,'......',price,'[',qty,']','=RM',ans)
			elif optn[0] == '16':
				optn = 'White Coffee Hazelnut Free'
				price = 5.4
				ans = (price * float(qty))
				print(optn,'......',price,'[',qty,']','=RM',ans)
			elif optn[0] == '17':
				optn = 'Fanta Grape Float'
				price = 5.4
				ans = (price * float(qty))
				print(optn,'......',price,'[',qty,']','=RM',ans)
			elif optn[0] == '18':
				optn = 'Mineral Water'
				price = 5.4
				ans = (price * float(qty))
				print(optn,'......',price,'[',qty,']','=RM',ans)
			elif optn[0] == '19':
				optn = 'Signature Ice Cream'
				price = 5.4
				ans = (price * float(qty))
				print(optn,'......',price,'[',qty,']','=RM',ans)
			elif optn[0] == '20':
				optn = 'Ice Kacang'
				price = 5.4
				ans = (price * float(qty))
				print(optn,'......',price,'[',qty,']','=RM',ans)
			elif opt == "x":
				print('YOUR ORDER HAS BEEN SUCCESFULLY RECORDED..\nTHANK YOU FOR YOUR ORDER :)')
				break
			else:
				print ('Invalid input')

			sndans = print(optn,'......',price,'[',qty,']','=RM',ans)
			print('Calculation successfully Done!')
		except:
			print('Connection Terminated')
			sndans = ('Connection Terminated')
			break
		if not opt:
			break

		s_sock.send(str.encode(str(sendAns)))
    	#s_sock.close()

if __name__ == '__main__':
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("",8888))
	print("listening...")
	s.listen(3)
	try:
		while True:
			try:
				s_sock, s_addr = s.accept()
				print('Client from : ' + str(s_addr))
				p = Process(target=process_start, args=(s_sock,))
				p.start()

			except socket.error:
				print('got a socket error')

	except Exception as e:
		print("an exception occurred!")
		print(e)
		sys.exit(1)
	finally:
		s.close()
=======
    s_sock.send(str.encode('\n===MUR MUR CAFE===\n'))
    while True:
        data = s_sock.recv(2048)
        data = data.decode("utf-8")

        #process/calculation
        try:
            if optn[0] == '1':
                optn = 'Nasi lemak'
                price = 2.5
                ans = (price * float(qty))
                print(optn,'......',price,'[',qty,']','=RM',ans)
            elif optn[0] == '2':
                optn = 'Nasi lemak with curry chicken'
                price = 5.4
                ans = (price * float(qty))
                print(optn,'......',price,'[',qty,']','=RM',ans)
            elif optn[0] == '3':
                optn = 'Nasi lemak with chicken rendang'
                price = 6.4
                ans = (price * float(qty))
                print(optn,'......',price,'[',qty,']','=RM',ans)
            elif optn[0] == '4':
                optn = 'Special BBQ Chicken Rice'
                price = 5.4
                ans = (price * float(qty))
                print(optn,'......',price,'[',qty,']','=RM',ans)
            elif optn[0] == '5':
                optn = 'Ginger chicken steamed rice'
                price = 5.4
                ans = (price * float(qty))
                print(optn,'......',price,'[',qty,']','=RM',ans)
            elif optn[0] == '6':
                optn = 'Garlic Toast'
                price = 5.4
                ans = (price * float(qty))
                print(optn,'......',price,'[',qty,']','=RM',ans)
            elif optn[0] == '7':
                optn = 'Crunchy Sugar Hainan Toast'
                price = 5.4
                ans = (price * float(qty))
                print(optn,'......',price,'[',qty,']','=RM',ans)
            elif optn[0] == '8':
                optn = 'Condensed Milk Hainan Toast'
                price = 5.4
                ans = (price * float(qty))
                print(optn,'......',price,'[',qty,']','=RM',ans)
            elif optn[0] == '9':
                optn = 'Western Mixed Platter'
                price = 5.4
                ans = (price * float(qty))
                print(optn,'......',price,'[',qty,']','=RM',ans)
            elif optn[0] == '10':
                optn = 'BBQ Chicken Wrap'
                price = 5.4
                ans = (price * float(qty))
                print(optn,'......',price,'[',qty,']','=RM',ans)
            elif optn[0] == '11':
                optn = 'Chicken Bites Wrap'
                price = 5.4
                ans = (price * float(qty))
                print(optn,'......',price,'[',qty,']','=RM',ans)
            elif optn[0] == '12':
                optn = 'French Fries'
                price = 5.4
                ans = (price * float(qty))
                print(optn,'......',price,'[',qty,']','=RM',ans)
            elif optn[0] == '13':
                optn = 'White Coffee'
                price = 5.4
                ans = (price * float(qty))
                print(optn,'......',price,'[',qty,']','=RM',ans)
            elif optn[0] == '14':
                optn = 'Black Tea'
                price = 5.4
                ans = (price * float(qty))
                print(optn,'......',price,'[',qty,']','=RM',ans)
            elif optn[0] == '15':
                optn = 'Double Enriched Chocolate'
                price = 5.4
                ans = (price * float(qty))
                print(optn,'......',price,'[',qty,']','=RM',ans)
            elif optn[0] == '16':
                optn = 'White Coffee Hazelnut Freezy'
                price = 5.4
                ans = (price * float(qty))
                print(optn,'......',price,'[',qty,']','=RM',ans)
            elif optn[0] == '17':
                optn = 'Fanta Grape Float'
                price = 5.4
                ans = (price * float(qty))
                print(optn,'......',price,'[',qty,']','=RM',ans)
            elif optn[0] == '18':
                optn = 'Mineral Water'
                price = 5.4
                ans = (price * float(qty))
                print(optn,'......',price,'[',qty,']','=RM',ans)
            elif optn[0] == '19':
                optn = 'Signature Ice Cream'
                price = 5.4
                ans = (price * float(qty))
                print(optn,'......',price,'[',qty,']','=RM',ans)
            elif optn[0] == '20':
                optn = 'Ice Kacang'
                price = 5.4
                ans = (price * float(qty))
                print(optn,'......',price,'[',qty,']','=RM',ans)
            elif opt == "x":
                print('YOUR ORDER HAS BEEN SUCCESFULLY RECORDED..\nTHANK YOU FOR YOUR ORDER :)')
                break
            else:
                print ('Invalid input')
                
            sndans = print(optn,'......',price,'[',qty,']','=RM',ans)   
            print('Calculation successfully Done!')
        except:
            print('Connection Terminated')
            sndans = ('Connection Terminated')
            break
        if not opt:
            break

        s_sock.send(str.encode(str(sendAns)))
    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('got a socket error')

    except Exception as e:
                print("an exception occurred!")
                print(e)
                sys.exit(1)
    finally:
           s.close()
>>>>>>> f7dcf49e4c5893b3765879283223279dd33d21fc
