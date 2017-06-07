#DAC algorithm Round1 implementation using python
#Date : 6-6-2017

import operator

#*****************taking input from the file separate by comma and storing into a dictionary called inputdata
inputdata={}
with open('testcase1.txt','r') as input_file:
        for line in input_file:
                splitline=line.split(",")
                inputdata[str(splitline[0])]=",".join(splitline[1:])    
    
        for key in inputdata:
                inputdata[key]=inputdata[key].rstrip()
                inputdata[key]=list(inputdata[key].split(","))
  
#*****************taskssorting based on priority and storing into a list called Keyarray     
#temporary variables
temp={}
l1=[int(v[7]) for k,v in inputdata.items() if len(v)==8 ]
l2=[k  for k,v in inputdata.items() if len(v)==8]

for i in range(len(l2)):         #collecting tasks and priorities into a dictionary
        temp[l2[i]]=l1[i]

#sorting based on priority
sorted_x=sorted(temp.items(),key=operator.itemgetter(1))

#putting in keyarray
keyArray=[str(i[0]) for i in sorted_x]  
        
print "\nThe array containing sorted tasks based on priorities:" ,keyArray
     
#******************calculating N1,N2,N3     

LAMBDA = 2     #LAMBDA which regulates the number of tasks in HQ,MQ,LQ respectively
n=len(keyArray) #n : number of tasks

N1= (n/3) + LAMBDA  #it automatically takes floor value unless we import division package
N2= (n-N1)/2
N3= (n-(N1+N2))

print "The number of elements in \nHQ queue : %d\nMQ queue : %d\nLQ queue : %d" %(N1,N2,N3)

#*****************division of elements into HQ,MQ,LQ (optimization possible)-->[done]

HQ=[keyArray[i] for i in range(N1)]
MQ=[keyArray[i] for i in range(N1,N1+N2)]
LQ=[keyArray[i] for i in range(N1+N2,n)]

print "Tasks in HQ:",HQ,"\n","Tasks in MQ:",MQ,"\n","Tasks in LQ:",LQ,"\n"


#******************internally sorting based on deadlines(working on this..)

#temporary variables
temp={}

l1=[inputdata[HQ[i]][6] for i in range(N1)]
l2=[HQ[i] for i in range(N1)]


for i in range(len(l2)):
        temp[l2[i]]=int(l1[i])

#sorting HQ based on deadlines(*need to work on sorting that if deadlines are same then sorting is done based on priority)
sorted_x=sorted(temp.items(),key=operator.itemgetter(1))

#temporary variables
temp={}

l1=[inputdata[MQ[i]][6] for i in range(N2)]
l2=[MQ[i] for i in range(N2)]


for i in range(len(l2)):
        temp[l2[i]]=int(l1[i])

#sorting MQ based on deadlines(*need to work on sorting that if deadlines are same then sorting is done based on priority)
sorted_y=sorted(temp.items(),key=operator.itemgetter(1))

#temporary variables
temp={}

l1=[inputdata[LQ[i]][6] for i in range(N3)]
l2=[LQ[i] for i in range(N3)]

for i in range(len(l2)):
        temp[l2[i]]=int(l1[i])

#sorting LQ based on deadlines(*need to work on sorting that if deadlines are same then sorting is done based on priority)
sorted_z=sorted(temp.items(),key=operator.itemgetter(1))

#putting in keyarray
HQ=[str(i[0]) for i in sorted_x]
MQ=[str(i[0]) for i in sorted_y]
LQ=[str(i[0]) for i in sorted_z]
     
print "The Finalized internally sorted HQ based on deadlines:",HQ,'\n',"The Finalized internally sorted MQ based on deadlines:",MQ,'\n',"The Finalized internally sorted LQ based on deadlines:",LQ


#********************Calculation of time quantum for HQ  , MQ

#alpha1,alpha2 regulates the time quanta
ALPHA1=2
ALPHA2=1

l1=[int(inputdata[HQ[i]][6]) for i in range(len(HQ))]   
l2=[int(inputdata[MQ[i]][6]) for i in range(len(MQ))]

TQ1=max(l1)/pow(2,ALPHA1)   
TQ2=max(l2)/pow(2,ALPHA2)   
        
print "\nThe Calculated time quantum as follows:\nTQ1:%d\nTQ2:%d" %(TQ1,TQ2) 







      
 
