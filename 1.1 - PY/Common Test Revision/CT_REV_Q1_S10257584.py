#Chia Wei En Wayne (S10257584) - P07 (CSF02)

#Name: Chia Wei En Wayne
#Student ID: S10257584G
#Status: Completed

times = input('Enter time taken of 2 laps separated by semi-colon (seconds): ')

times_list = times.split(';')

firstlap_time = float(times_list[0])
secondlap_time = float(times_list[1])

if firstlap_time < secondlap_time: 
    best = firstlap_time 
else:
    best = secondlap_time 

total = firstlap_time + secondlap_time 

print('Tom\'s best time is {:.1f} s and average time is {:.1f} s'.format(best,total/2))
