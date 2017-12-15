#!/usr/bin/python3

import json
import random # Mersenne Twister
from collections import OrderedDict

ticket_file = '../data/tickets.json'
registration_file = '../data/registration_fake.json'    # TODO: use real data!
results_file = '../data/lottery_results.json'

# read in ticket count for everyone
print("Reading ticket data...")
with open(ticket_file) as data_file:    
    tickets_data = json.load(data_file)
# read in participants
print("Reading registration data...")
with open(registration_file) as data_file: 
    registration_data = json.load(data_file)



print("Distributing tickets to participants...")
#empty dict for lottery participants
participants = {}

# assign each participant their tickets and count total tickets
nTickets = 0
nParticipants = 0
for iopAddr, ethAddr in registration_data.items():
    # We will later draw a random rumber in the range (0,totalTickets)
    # We accumulate the ticket number so each participant gets a unique range
    # of ticket numbers. Participant 1 has e.g. 50 tickets, so we assign him 
    # the tickets 1 to 50 and we write down 50, participant 2 has e.g. 20 tickets, 
    # so he gets tickets 51 to 70 and we write down 70, and so on. We can then find 
    # the winner  of the lottery by searching through the list of participants for 
    # the one with a value that is larger than or equal to the number drawn in the 
    # lottery, because he must have the ticket in question.
    nTickets += tickets_data[ iopAddr ]
    participants[ nTickets ] = ethAddr # We use the number as key to the addr.
    nParticipants += 1
totalTickets = nTickets

print("{} participants with a total of {} tickets.".format(nParticipants,totalTickets))

# Lottery parameters
totalHydra = 500_000
lotteryHydra = totalHydra - nParticipants # every address gets one Hydra for registering
print("Every address is awarded 1 HYD for registering...")
winnings = {}
for num, part in participants.items():
    winnings[ part ] = 1
print("{} HYD remaining for random distribution".format(lotteryHydra))

# Seed the lottery
print("Seeding the lottery...")
random.seed(17052016) # IOP genesis block

print("Drawing {} random integers in the range (1,{})".format(lotteryHydra,totalTickets))
for i in range(lotteryHydra):
    if i>0 and i % 100_000 == 0:
        print("{} Hydra awarded".format(i)) 

    winner = random.randint(1,totalTickets) # this is the ticket that won

    # search for the address with the smallest value still larger than or equal to winner 
    while winner <= totalTickets: 
        if winner in participants: # we found the winner
            winnings [ participants[ winner ] ] += 1 # award one HYD
            break 
        else: # try next number
            winner += 1
            
print("Awarded all Hydras")
print("Reordering participants by winnings...")
results = OrderedDict(sorted(winnings.items(), key=lambda x: x[1]))

print("Dumping results to JSON...")
with open(results_file, 'w') as outfile:
    json.dump(results, outfile, indent=2)

print("Minimum won: {}".format(results.popitem(last=False)))
print("Maximum won: {}".format(results.popitem(last=True)))

print("Done. Goodbye!")
