from ipaddress import *

ip = "117.191.37.84"
add = "117.191.37.80"
for i in range(0, 33, 1):
    net = ip_network(ip+"/"+str(i), 0)
    if str(net.network_address) == add:
        print(i)
        print(net.netmask)
