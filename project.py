import ipaddress

lst_ip=[]
valid_ip=[]
bny_ip=[]
hex_ip=[]
oc_ip=[]
dec_ip=[]


def inpt():
    for i in range(0,10):
        adrs = input("Enter the "+str(i+1)+" ip address: ")
        lst_ip.append(adrs)
inpt()

def chk_ip():
    for i in range(0,10):
        try:
            ipaddress.IPv4Address(lst_ip[i])
            valid_ip.append(lst_ip[i])
        except:
            print("-----------------------------------")
            print("\n The ip address "+str(i+1)+" : "+str(lst_ip[i])+" is invalid\n\n")
            print("-----------------------------------")
chk_ip()

size= len(valid_ip)

def prt():
    for i in range(size):
        print("The valid Ipv4 address are: "+valid_ip[i])
    print("\n\n")
    print("-------------------------------------")
prt()

def bnum_ip():
    for i in range(size):
        part=valid_ip[i].split('.')
        biny_ip= format(int(part[0]),   '08b') + format(int(part[1]), '08b') + format(int(part[2]), '08b') + format(int(part[3]), '08b')
        bny_ip.append("0b"+str(biny_ip))

bnum_ip()

def hxnum_ip():
    for i in range(size):
        part=valid_ip[i].split('.')
        h_ip=   format(int(part[0]), '02X') + format(int(part[1]), '02X') + format(int(part[2]), '02X') + format(int(part[3]), '02X')
        hex_ip.append("0x"+str(h_ip))

hxnum_ip()

def ocnum_ip():
    for i in range(size):
        part=valid_ip[i].split('.')
        o_ip= format(int(part[0]), '03o')+ format(int(part[1]), '03o')+ format(int(part[2]), '03o')+ format(int(part[3]), '03o')
        oc_ip.append("0o"+str(o_ip))

ocnum_ip()

def decnum_ip():
    for i in range(size):
        part=valid_ip[i].split('.')
        d_ip=format(int(part[0]), '03d')+ format(int(part[1]), '03d')+ format(int(part[2]), '03d')+ format(int(part[3]), '03d')
        dec_ip.append(d_ip)

decnum_ip()
    
def trans():
    wfile= open('Conversion.txt', 'w')
    for i in range(size):
        wfile.write("The decimal conversion of ipv4 address"+str(valid_ip[i])+" is: "+str(dec_ip[i]))
        wfile.write("\n")
        wfile.write("The binary conversion of ipv4 address "+str(valid_ip[i])+" is: "+str(bny_ip[i]))
        wfile.write("\n")
        wfile.write("The octal conversion of ipv4 address "+str(valid_ip[i])+" is: "+str(hex_ip[i]))
        wfile.write("\n")
        wfile.write("The hexa decimal conversion of ipv4 address "+str(valid_ip[i])+" is: "+str(oc_ip[i]))
        wfile.write("\n \n")
    wfile.close()

trans()

def fnl_output():
    with open("Conversion.txt", 'r') as rfile:
        lines = rfile.readlines()
        for i in lines:
            print(i)
    rfile.close()

fnl_output()


    
    
    

    


















        
