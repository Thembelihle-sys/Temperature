temps = [[0.0 for h in range (24)] for d in range(31)]

total = 0.0

for day in temps:
    total += day[11]

    average = total/31 

    print('average temperature at noon', average)

    i=0
    while i<=5 :
        i+= 1
        if i % 2 ==0:
            break
        print('*')