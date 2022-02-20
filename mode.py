# Python program to print
# mode of elements
from collections import Counter
import csv


with open('height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(n_num)


#Calculating Mode
data = Counter(new_data)
mode_data_for_range = {
                        "50-60": 0,
                        "60-70": 0,
                        "70-80": 0
                    }


for height, occurence in data.items():
    if 50 < float(height) < 60:
        mode_data_for_range["50-60"] += occurence
    elif 60 < float(height) < 70:
        mode_data_for_range["60-70"] += occurence
    elif 70 < float(height) < 80:
        mode_data_for_range["70-80"] += occurence

mode_range, mode_occurence = 0, 0
#print(mode_data_for_range.items())

for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        rangesplit=range.split("-")
        mode_range = [rangesplit[0],rangesplit[1]]
        mode_occurence= occurence
mode = float((mode_range[0] + mode_range[1]) / 2)


print("Mode is "+ str(mode))
