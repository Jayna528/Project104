import csv

with open('height-weight.csv', newline='') as f: 
    reader = csv.reader(f)
    dataList = list(reader)

height = []


dataList.pop(0)

for i in range(len(dataList)):
    num = dataList[i][2]
    height.append(float(num))


sum = 0
for x in height:
    sum = sum + x


length = len(height)
mean = sum / length

print('The mean is', mean)




height.sort()

if(length % 2 == 0):
    val1 = float(height[length//2])
    val2 = float(height[length//2 + 1])    

    median = (val1 + val2)/2 

else: 
    median = float(height[length//2])

print('The median is', median)

