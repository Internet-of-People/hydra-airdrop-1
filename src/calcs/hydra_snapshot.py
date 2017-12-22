#!/usr/bin/python3

import numpy as np
import json
import random # Mersenne Twister

raw_file = '../data/airdrop.data'
snapshot_file = '../data/snapshot.json'
tickets_file = '../data/tickets.json'

# read raw snapshot data
rawData = np.asarray( np.genfromtxt(raw_file, skip_header=6, dtype= None) )

# Ticket distribution parameters
stepSize = 2.0 # one ticket every full stepSize
maximumTickets = 250 # the maximum number of tickets an address can get

# open empty dicts
snapshot_data = {}
tickets_data = {}

# fill dicts from raw data
for x in rawData:
    address = x[2].decode("utf-8")
    tickets = int(x[0]/stepSize)

    # only addresses with a balance of 2 IOP or more are eligible
    # timelocked tokens are excluded
    if tickets > 0 and address .startswith('p') :
        snapshot_data[ address ] = x[0] 
        tickets_data[   address ] = min( tickets, maximumTickets )


# output data to json
with open(snapshot_file, 'w') as outfile:
    json.dump(snapshot_data, outfile, indent=2)
with open(tickets_file, 'w') as outfile:
    json.dump(tickets_data, outfile, indent=2)


