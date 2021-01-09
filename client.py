import socket
import signal
import sys


cSocket = socket.socket()
host = '192.168.1.6'
port = 8888

print('Waiting for connection')
try:
        cSocket.connect((host, port))
except socket.error as e:
        print(str(e))


Response = cSocket.recv(2048)
print(Response.decode("utf-8"))

print (	"\n=========================================================================================\n"
			"\t\t\t* *** *** *** MENU LIST *** **** *** *\t\t\t\n"
			"=========================================================================================\n");

print("   ------------------------------------------------------------------------------------")
print("   | [A]  Nasi lemak" , end =" ")
print("                               [B]  Nasi lemak with curry chicken|")
print("   | [C]  Nasi lemak with chicken rendang", end =" ")
print("          [D]  Special BBQ Chicken Rice     |")
print("   | [E]  Ginger chicken steamed rice", end =" ")
print("              [F]  Garlic Toast                 |")
print("   | [G]  Crunchy Sugar Hainan Toast", end =" ")
print("               [H]  Condensed Milk Hainan Toast  |")
print("   | [I]  Western Mixed Platter", end =" ")
print("                    [J] BBQ Chicken Wrap              |")
print("   | [K]  Chicken Bites Wrap", end =" ")
print("                       [L] French Fries                  |")
print("   | [M]  White Coffee", end =" ")
print("                             [N] Black Tea                     |")
print("   | [O]  Double Enriched Chocolate", end =" ")
print("                [P] White Coffee Hazelnut Freezy  |")
print("   | [Q]  Fanta Grape Float", end =" ")
print("                        [R] Mineral Water                 |")
print("   | [S]  Signature Ice Cream", end =" ")
print("                      [T] Ice Kacang                    |")
print("   ------------------------------------------------------------------------------------")
print("=========================================================================================")

while True:
    opt = input('\nSelect Your Menu [Code Number] Press exit if you are done..\n> ')

    if opt == "A" or opt == "B" or opt == "C" or opt == "D" or opt == "E" or opt == "F" or opt == "G" or opt == "H" or opt == "I" or opt == "J" or opt == "K" or opt == "L" or opt == "M" or opt == "N" or opt == "O" or opt == "P" or opt == "Q" or opt == "R" or opt == "S" or opt == "T":
        qty = input("Quantity per Order: ")
        prc = '0'
        Input = opt + ":" + qty + ":" + prc
        cSocket.send(str.encode(Input))
        Response = cSocket.recv(1024)
        print(Response.decode("utf-8"))

    elif opt == 'exit':
        print('YOUR ORDER HAS BEEN SUCCESFULLY RECORDED..\nTHANK YOU FOR YOUR ORDER :)')
        break

    else:
        print("WRONG INPUT, TRY AGAIN!!")
        cSocket.send(str.encode(Input))
        Response = cSocket.recv(1024)
        print(Response.decode("utf-8"))

cSocket.close()
