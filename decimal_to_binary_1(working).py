binary=[]
ip_val=int(input('enter yout number'))
def decimalToBinary(ip_val):
    
    global binary
    if ip_val >= 1:
        decimalToBinary(ip_val // 2)
        binary.append(ip_val % 2)

decimalToBinary(ip_val)
print(binary)
