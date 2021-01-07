import socket


cSocket = socket.socket()
host = '192.168.1.6'
port = 8888

print('Waiting for connection')
try:
        cSocket.connect((host, port))
except socket.error as e:
        print(str(e))


Response = cSocket.recv(1024)
print(Response)


print("Select menu")
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
        choice = input("Enter choice: ")
        cSocket.send(str.encode(choice))
        if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'):
                qty = input("Enter quantity: ")
                cSocket.send(str.encode(qty))


        else:
                print("Invalid Input")


        cSocket.send(str.encode(qty))
        Response = cSocket.recv(1024)
        print(Response.decode('utf-8'))
        print(type(Response))


cSocket.close()
