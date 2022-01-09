# The year is 2163. Misha, who works in the customs department at the New Peter cosmodrome, was summoned to his office by the chief.
# As it turned out, recently the Ministry of Taxes and Duties allocated a certain amount of money to the department for the installation 
# of new devices for automatic inspection of goods. Naturally, the funds were allocated in such a way that the goods were now at customs for exactly as long as 
# it takes directly for their inspection.
# The chief somehow got into the hands of the information about the impending audit - a list of N cargoes that will be controlled by the Ministry. 
# For each cargo, the time of its arrival is known, counted from a certain moment, kept in great secret, and the time required for the apparatus to process this cargo. 
# The chief instructed Misha to use these data to determine what the minimum number of devices must be ordered at the factory 
# so that all the Ministry's cargo would begin to be inspected immediately after arrival. 
# It should be taken into account that the design of those devices that it was decided to install does not allow handling two loads at the same time on one device. 
# Write a program that will help Misha cope with his task.
# The first line of the input file contains the number N (0 ≤ N ≤ 50 000). 
# The next N lines contain 2 positive integers Ti and Li - the time of arrival of the corresponding cargo and the time required for its processing 
# (1 ≤ Ti ≤ 10^6, 1 ≤ Li ≤ 10^6)
# Print one number into the output file - the smallest number of devices that need to be installed so as not to arouse suspicion in the Ministry.

n = int(input())  # total goods
customs = []  # list of arrival time and departure time
for _ in range(n):
    t, l = map(int, input().split())  # input arrival time and time for goods' processing
    customs.append((t, 0))  # create tuple. The first element - arrival time, the second - 0
    customs.append((t + l, 1))  # create tuple. The first element - departure time (arrival time + time for goods' processing), the second - 1
customs = sorted(customs, key=lambda x: (x[0], -x[1]))  # sort the list by time in direct order. If times are the same departure time will be earlier
count = 0  # current count of necessary equipment
min_count = 0  # minimal count of necessary equipment
for eqip in range(len(customs)):
    if customs[eqip][1] == 0:
        count += 1  # increase quantity of equipment if it arrives
    else:
        count -= 1  # decrease quantity of equipment if it departs
    min_count = max(min_count, count)  # compare current quantity with minimum. Maximum of these numbers will be necessary result
print(min_count)
