#Output plot file comparing the standard FCFS and DAC Algorithm


filename = raw_input("Give the name of the input file : ") 

filename1 = 'outputDAC'+filename

count=0
inputdata={}

with open(filename1,'r') as input_file:

        for line in input_file:

                splitline=line.split(",")

                inputdata[count]=",".join(splitline[0:])
                
                count=count+1    
    


filename2 = 'outputFCFS'+filename


with open(filename2,'r') as input_file:

        for line in input_file:

                splitline=line.split(",")

                inputdata[count]=",".join(splitline[0:]) 
                
                count=count+1   
    
        for key in inputdata:

                inputdata[key]=inputdata[key].rstrip()

                inputdata[key]=list(inputdata[key].split(","))
        

Tasks=[i for i in range(len(inputdata[0]))]

TWT1=inputdata[1]
TExecTime1=inputdata[2]

TWT2=inputdata[4]
TExecTime2=inputdata[5]

import numpy as np
import matplotlib.pyplot as plt

N=2
ind = np.arange(N)
width=0.27

fig=plt.figure()
ax=fig.add_subplot(111)

TTAT1=inputdata[0]
rects1=ax.bar(ind,TTAT1,width=0.2,color="r")
TTAT2=inputdata[3]
rects2=ax.bar(ind+width,TTAT2,width=0.2,color="g")

ax.set_ylabel('TurnAroundTimes')
ax.set_xlabel('Tasks')
ax.set_xticks(ind+width)
ax.set_xticklabels(('1','2','3','4','5','6','7','8','9','10'))
ax.legend((rects1[0],rects1[2]),('DAC','FCFS'))


plt.show()                
