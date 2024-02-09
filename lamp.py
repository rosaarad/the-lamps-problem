n = int(input())
data = {}
sum = 0
counter = 0

for i in range(n):
    name , lifeSpan , count = input().split()
    
    lifeSpan = float(lifeSpan)
    count = float(count)
    
    data[name] = lifeSpan
    
    sum += lifeSpan * count
    counter += count
    
avg = sum / counter

myList = []

for company in data:
    if data[company] >= avg:
        myList.append(company)
        
myList.sort()

for i in myList:
    print(i)

    