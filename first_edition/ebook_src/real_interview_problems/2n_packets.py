#!/bin/python

import math
import os
import random
import re
import sys

# Complete the 'largestRepackaged' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arrivingPackets as parameter.
#

def largestRepackaged(arrivingPackets):

    packet_size = arrivingPackets[0]
    packets = arrivingPackets[1:]
    largest_packet = 0
    remaining = 0

    for packet in packets:
        print packet
        if remaining:
            packet += remaining
            remaining = 0

        if packet % 2 != 0:
            remaining = packet % 2 
            packet -= remaining
        
        if packet > largest_packet:
            largest_packet = packet

    return largest_packet


if __name__ == '__main__':
    arrivingPackets= [5, 1, 2, 4, 7, 5]
   
    print(largestRepackaged(arrivingPackets))