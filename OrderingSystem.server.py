import socket
import os
import sys
import json
import random
import errno
import math
from multiprocessing import Process

def process_start(s_sock):

    s_sock.send(str.encode('\n\t\t\t\t*#*#*MUR MUR CAFE*#*#*\t\t\t'))
    while True:
        data = s_sock.recv(2048)
        data = data.decode("utf-8")

        #process/calculation
        try:
<<<<<<< HEAD
            menu, num , value = data.split(":")
            opt = str(menu)
            qty = int(num)
            prc = float(value)

            if opt[0]  == 'A':
                opt = 'Nasi lemak'
                prc = 5.3
                ans = qty * (prc)
            elif opt[0] == 'B':
                opt = 'Nasi lemak with curry chicken'
                prc = 6
                ans = qty * (prc)
            elif opt[0] == 'C':
                opt = 'Nasi lemak with chicken rendang'
                prc = 7
                ans = qty * (prc)
            elif opt[0] == 'D':
                opt = 'Special BBQ Chicken Rice'
                prc = 6
                ans = qty * (prc)
            elif opt[0] == 'E':
                opt = 'Ginger chicken steamed rice'
                prc = 7
                ans = qty * (prc)
            elif opt[0] == 'F':
                opt = 'Garlic Toast'
                prc = 6
                ans = qty * (prc)
            elif opt[0] == 'G':
                opt = 'Crunchy Sugar Hainan Toast'
                prc = 7
                ans = qty * (prc)
            elif opt[0] == 'H':
                opt = 'Condensed Milk Hainan Toast'
                prc = 6
                ans = qty * (prc)
            elif opt[0] == 'I':
                opt = 'Western Mixed Platter'
                prc = 7
                ans = qty * (prc)
            elif opt[:] == 'J':
                opt = 'BBQ Chicken Wrap'
                prc = 6
                ans = qty * (prc)
            elif opt[:] == 'K':
                opt = 'Chicken Bites Wrap'
                prc = 7
                ans = qty * (prc)
            elif opt[0] == 'L':
                opt = 'French Fries'
                prc = 6
                ans = qty * (prc)
            elif opt[0] == 'M':
                opt = 'White Coffee'
                prc = 7
                ans = qty * (prc)
            elif opt[0] == 'N':
                opt = 'Black Tea'
                prc = 6
                ans = qty * (prc)
            elif opt[0] == 'O':
                opt = 'Double Enriched Chocolate'
                prc = 7
                ans = qty * (prc)
            elif opt[0] == 'P':
                opt = 'White Coffee Hazelnut Freezy'
                prc = 6
                ans = qty * (prc)
            elif opt[0] == 'Q':
                opt = 'Fanta Grape Float'
                prc = 7
                ans = qty * (prc)
            elif opt[0] == 'R':
                opt = 'Mineral Water'
                prc = 7
                ans = qty * (prc)
            elif opt[0] == 'S':
                opt = 'Signature Ice Cream'
                prc = 6
                ans = qty * (prc)
            elif opt[0] == 'T':
                opt = 'Ice Kacang'
                prc = 7
                ans = qty * (prc)
            else:
                answer = ('ERROR')

            sendAns = (str(opt)+ '.... RM'+ str(prc)+ ' ['+ str(qty) + ']: RM' + str(ans))
            print(sendAns)
            print ('ORDER RECEIVED!!')
            #break
        except:
            print ('Connection Terminated')
            sendAns = ('Connection Terminated')
            break
        if not data:
            break

=======
            operation, num , value = data.split(":")
            opt = str(operation)
            qty = int(num)
            prc = float(value)

            if opt[0] == '1':
                opt = 'Nasi lemak'
                prc = 5.3
                ans = qty * (prc)
            elif opt[0] == '2':
                opt = 'Nasi lemak with curry chicken'
                prc = 6
                ans = qty * (prc)
            elif opt[0] == '3':
                opt = 'Nasi lemak with chicken rendang'
                prc = 7
                ans = qty * (prc)
            elif opt[0] == '4':
                opt = 'Special BBQ Chicken Rice'
                prc = 6
                ans = qty * (prc)
            elif opt[0] == '5':
                opt = 'Ginger chicken steamed rice'
                prc = 7
                ans = qty * (prc)
            elif opt[0] == '6':
                opt = 'Garlic Toast'
                prc = 6
                ans = qty * (prc)
            elif opt[0] == '7':
                opt = 'Crunchy Sugar Hainan Toast'
                prc = 7
                ans = qty * (prc)
            elif opt[0] == '8':
                opt = 'Condensed Milk Hainan Toast'
                prc = 6
                ans = qty * (prc)
            elif opt[0] == '9':
                opt = 'Western Mixed Platter'
                prc = 7
                ans = qty * (prc)
            elif opt[0] == '10':
                opt = 'BBQ Chicken Wrap'
                prc = 6
                ans = qty * (prc)
            elif opt[0] == '11':
                opt = 'Chicken Bites Wrap'
                prc = 7
                ans = qty * (prc)
            elif opt[0] == '12':
                opt = 'French Fries'
                prc = 6
                ans = qty * (prc)
            elif opt[0] == '13':
                opt = 'White Coffee'
                prc = 7
                ans = qty * (prc)
            elif opt[0] == '14':
                opt = 'Black Tea'
                prc = 6
                ans = qty * (prc)
            elif opt[0] == '15':
                opt = 'Double Enriched Chocolate'
                prc = 7
                ans = qty * (prc)
            elif opt[0] == '16':
                opt = 'White Coffee Hazelnut Freezy'
                prc = 6
                ans = qty * (prc)
            elif opt[0] == '17':
                opt = 'Fanta Grape Float'
                prc = 7
                ans = qty * (prc)
            elif opt[0] == '18':
                opt = 'Mineral Water'
                prc = 7
                ans = qty * (prc)
            elif opt[0] == '19':
                opt = 'Signature Ice Cream'
                prc = 6
                ans = qty * (prc)
            elif opt[0] == '20':
                opt = 'Ice Kacang'
                prc = 7
                ans = qty * (prc)
            else:
                answer = ('ERROR')

            sendAns = (str(opt)+ '.... RM'+ str(prc)+ ' ['+ str(qty) + ']: RM' + str(ans))
            print(sendAns)
            print ('ORDER RECEIVED!!')
            #break
        except:
            print ('Connection Terminated')
            sendAns = ('Connection Terminated')
            break
        if not data:
            break

>>>>>>> c8b71500ff0ba42a278244828ed4c136f327ac8f
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
