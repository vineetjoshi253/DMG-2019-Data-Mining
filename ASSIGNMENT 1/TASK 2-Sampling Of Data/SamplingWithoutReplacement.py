import csv
import random
import math
import matplotlib.pyplot as plt

with open('RandomDataset.csv', 'r') as myData:
    reader = csv.reader(myData)
    Data = list(reader)
    
Data.pop(0)

SampleSpace = []
UniqueTrials =[]
Probability = []
k=int(input("Enter The Value Of K "))

def SampleOnce():
    Map = {'1':0, '2':0, '3':0, '4':0 , '5':0, '6':0, '7':0, '8':0, '9':0,'10':0}
    Output = 0
    
    while (1):
        DataObject = random.sample(Data,1)
        Output+=1
        Map[DataObject[0][2]]+=1
        count=0
        for value in Map.values():
            if(value >= k):
                count+=1
        if(count==10):
            return Output
            
def Graph1():    
    for item in UniqueTrials:
        fav = 0
        for values in SampleSpace:
            if( values <= item):
                fav+=1
        Probability.append(float(fav/1000.0))

    plt.plot(UniqueTrials, Probability) 
    plt.xlabel('Sample Size') 
    plt.ylabel('Probability') 
    
    plt.title('Sample Size Vs Probability Graph (Without Replacement) For Given K') 
    plt.show() 

def Graph2():
    Max= max(SampleSpace)
    Blocks = math.floor(Max/10)
    BlockValues = [0] * Blocks
    for item  in SampleSpace:
        BlockValues[math.floor(item/10)-1]+=1
    
    low = 10
    high = 20
    labels=[]
    for i in range(Blocks):
        labels.append(str(low)+'-'+str(high))
        low+=10
        high+=10
    Marks = [i for i in range(10,Blocks*10+10,10)]
    plt.bar(Marks, BlockValues, tick_label = labels,width = 5) 
    plt.xticks(rotation=90)
    plt.xlabel('Sample Size Ranges') 
    plt.ylabel('Frequency') 
    plt.title('Sample Size Vs Frequncy Graph (Without Replacement) For Given K') 
    plt.show() 
       
    
for i in range(1000):
    SampleSpace.append(SampleOnce())

UniqueTrials = list(set(SampleSpace))

Graph1()
Graph2()

