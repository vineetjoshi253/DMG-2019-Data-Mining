import csv
import random

with open('RandomDataset.csv', mode='w',newline='') as myData:
    writer = csv.writer(myData)
    label=1
    for x in range(1000):
        writer.writerow([random.randint(0,50),random.randint(0,50),label])
        label=label+1;
        if(label>10):
            label=1
    
    
with open('RandomDataset.csv', mode='r',newline='') as myData:
    DataSet = myData.readlines()
    random.shuffle(DataSet)

with open('RandomDataset.csv', mode='w',newline='') as myData:
    myData.writelines(DataSet)