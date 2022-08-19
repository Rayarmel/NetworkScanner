#!/usr/bin/env python3

import sys
# Import argparse to call program from command line
import argparse
# Import Scapy
import scapy.layers.l2 as scapy2
import scapy.sendrecv as scapy3
# use to format input correctly by creating regular expressions
# import re
parser = argparse.ArgumentParser()
# need root/admin privileges to call from command line
parser.add_argument("-ip", "--ipadd", help="IP Address/Subnet Mask")
args = parser.parse_args()
# regular expression pattern for IPv4 address
# ipPattern = re.compile("^(?:[0-9]{1,3}\\.){3}[0-9]{1,3}/[0-9]*$")
if not args.ipadd:
    print("Invalid Syntax \n Use --help or -h for options")
    sys.exit(1)
else:
    # pdst = destination ip addr
    request = scapy2.ARP(pdst=args.ipadd)
    frame = scapy2.Ether(dst="ff:ff:ff:ff:ff:ff")
    finalRequest = frame/request
    answered = scapy3.srp(finalRequest, timeout=2, verbose=False)[0]
    result = []

    for i in range(0, len(answered)):
        devices = {"ip": answered[i][1].psrc, " mac": answered[i][1].hwsrc}
        result.append(devices)
# psrc = source ip addr
# hwsrc = destination mac addr
    for i in range(len(result)):
        print(result[i])
# # address range to ARP
# while True:
#     ipEntered = input("\n Enter ip address and range you want to send ARP request to (ex: 255.255.255.0/24)")
#     if ipPattern.search(ipEntered):
#         print(f"{ipEntered} is a valid ip address range")
#         break
#
# # ARP ip address range given
# # If valid, a list of all results will be returned
#
# arpResult = arping(ipEntered)
