P = int(input("Realized products in first day\n"))
Q = int(input("Limit "))
print("P = {0}".format(P))
print("Q = {0}".format(Q))
counter = (P/100)*3
print("Percent from {0} is {1}".format(P, counter))

for day in 30:
    add = P+counter
    print(day, add)
    if add == Q:
        print(" Realized day are {0}".format(day))