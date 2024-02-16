#Name: Chia Wei En Wayne
#Student ID: S10257584G
#Date: 29 May 2023
#Status: Complete, Checked

#List
numbers = [2, 7, 11, 6, 7, 3, 17, 7, 12, 41, 8, 11, 13, 10, 15]
store = []
count = 0

#Choose Loop Program
for chosen in numbers:
    if chosen in store:
        continue
    if chosen % 2 != 0:
        store.append(chosen)
        count += 1
    else:
        continue
    if count >= 5:
        break

#List Display
print(store)
