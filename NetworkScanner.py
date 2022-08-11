import scapy.all as scapy
import re

#--------------------------------------------------
#Regular Expression to detect IPv4 Addresses
#--------------------------------------------------
ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")


#--------------------------------------------------
#Require input of IPv4 Address + Subnet mask
#Check if user input is valid
#print acknowledgement to console if input is valid
#--------------------------------------------------
while True:
    ip_add_range_entered = input("\n Enter IP Address and Range")
    if ip_add_range_pattern.search(ip_add_range_entered):
        print("${ip_add_range_entered} is a valid range")
        break

#----------------------------------------------------------------------------
#Scapy creates ARP packets and sends them into the network to capture trafic
#----------------------------------------------------------------------------
arp_result = scapy.arping(ip_add_range_entered)

#This program does NOT save the information anywhere (not yet, anyway)


