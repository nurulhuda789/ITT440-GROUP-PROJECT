import socket
import signal
import sys


cSocket = socket.socket()
host = '192.168.1.109'
port = 8888

print('Waiting for connection')
try:
        cSocket.connect((host, port))
except socket.error as e:
        print(str(e))


Response = cSocket.recv(1024)
print(Response.decode("utf-8"))

print("\t\t\t\t\tMENU LIST\n")
print("[1]  Nasi lemak" , end =" ")
print("                              [2]  Nasi lemak with curry chicken")
print("[3]  Nasi lemak with chicken rendang", end =" ")
print("         [4]  Special BBQ Chicken Rice")
print("[5]  Ginger chicken steamed rice", end =" ")
print("             [6]  Garlic Toast")
print("[7]  Crunchy Sugar Hainan Toast", end =" ")
print("              [8]  Condensed Milk Hainan Toast")
print("[9]  Western Mixed Platter", end =" ")
print("                   [10] BBQ Chicken Wrap")
print("[11] Chicken Bites Wrap", end =" ")
print("                      [12] French Fries")
print("[13] White Coffee", end =" ")
print("                            [14] Black Tea")
print("[15] Double Enriched Chocolate", end =" ")
print("               [16] White Coffee Hazelnut Freezy")
print("[17] Fanta Grape Float", end =" ")
print("                       [18] Mineral Water")
print("[19] Signature Ice Cream", end =" ")
print("                     [20] Ice Kacang")


while True:
    opt = input('\nSelect Your Menu [Code Number] Press exit if you are done..\n> ')

    if opt == '1' or opt == '2' or opt == '3' or opt == '4' or opt == '5' or opt == '6' or opt == '7' or opt == '8' or opt == '9' or opt == '10' or opt == '11' or opt == "12" or opt == "13" or opt == "14" or opt == "15" or opt == "16" or opt == "17" or opt == "18" or opt == "19" or opt == "20":
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
