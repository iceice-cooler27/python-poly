#Chia Wei En Wayne (S10257584) - CSF02

datafile = open("trip_prices.txt", "r")
trip_prices_list = []

#a
#Ignore 1st Line, Store Separately
line = datafile.readline()
line = line.strip("\n")
trip_list = line.split(",")

for line in datafile:
    line = line.strip("\n")
    line = line.split(",")
    trip_prices_list.append(line)
datafile.close() #Remember to close the file

#b
num_a = 5
num_c = 2
num_extend = 3
num_total = num_a + num_c
if num_a%2 != 0:
    num_a_sgl = 1
    num_a_twn = int((num_a-1)/2)
else:
    num_a_sgl = 0
    num_a_twn = int(num_a/2)
if num_total&2 != 0:
    num_total += 1
num_extend_room = int(num_total/2)

#c
total_amt_list = []
for i in trip_list:
    print("{}".format(i), end = "  ")
print("{}  {}".format("Total Amount", "Amount w Land Tour"))

for n in trip_prices_list:
    space = 0
    for i in n:
        print("{}".format(i), end = "")
        space = len(trip_list[n.index(i)]) - len(i) + 2
        print(" " * space, end = "")
        if n == trip_prices_list[1] and i == n[3]:
            break
        
    pos_a_twn = trip_list.index("A_TWN")
    pos_land_a_twn = trip_list.index("LAND_A_TWN")
    
    pos_a_sgl = trip_list.index("A_SGL")
    pos_land_a_sgl = trip_list.index("LAND_A_SGL")

    pos_chd = trip_list.index("CHD")
    pos_land_chd = trip_list.index("LAND_CHD")

    pos_ext = trip_list.index("EXT")
    
    total_amount = num_a_sgl*int(n[pos_a_sgl]) + \
                   num_a_twn*int(n[pos_a_twn]) + \
                   num_c*int(n[pos_chd]) + \
                   num_extend*int(n[pos_ext])*num_extend_room
    
    w_land = total_amount + \
             num_a_sgl*int(n[pos_land_a_sgl]) + \
             num_a_twn*int(n[pos_land_a_twn]) + \
             num_c*int(n[pos_land_chd])

    total_amt_list.append([total_amount, w_land])
    print("{:<12}  {:<18}".format(total_amount, w_land))







