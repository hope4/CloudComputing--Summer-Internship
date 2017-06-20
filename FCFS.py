#FCFS algorithm  implementation using python

#Date : 16-6-2017

#Name : K Naveen Kumar

#*****************taking input from the file separate by comma and storing into a dictionary called inputdata

from __future__ import division 
import pylab as pl

inputdata={}

filename = raw_input("Give the name of the input file : ") 

with open(filename,'r') as input_file:

        for line in input_file:

                splitline=line.split(",")

                inputdata[str(splitline[0])]=",".join(splitline[1:])    
    
        for key in inputdata:

                inputdata[key]=inputdata[key].rstrip()

                inputdata[key]=list(inputdata[key].split(","))
  
#*****************Tasks sorting based on priority and storing into a list called Keyarray     

#used insertionsort for all kinds of sorting that take place in round1

#function for insertionsort

def insertionsort(list1,list2):

     for index in range(1,len(list1)):

             value1=list1[index]

             value2=list2[index]

             i = index-1

             while i >= 0:

                     if value1 < list1[i]:

                             list1[i+1] = list1[i]

                             list2[i+1] = list2[i]

                             list1[i] = value1

                             list2[i] = value2

                             i = i-1

                     elif (value1 == list1[i]): #the condition where deadlines are equal go for the priority it is used in dead line sorting

                             temp = int(inputdata[value2][7])

                             if int(inputdata[list2[i]][7]) > temp:

                                list1[i+1] = list1[i]

                                list2[i+1] = list2[i]

                                list1[i] = value1

                                list2[i] = value2

                                i = i-1

                             else:

                                break

                     else:

                             break

#******************************************

l1=[int(v[7]) for k,v in inputdata.items() if len(v)==8 ] #contains priority list of Tasks

keyArray=[k  for k,v in inputdata.items() if len(v)==8]         #contains corresponding Tasks



insertionsort(l1,keyArray) #calling insertionsort to sort based on priority

        
print "The keyArray containing sorted Tasks based on priorities:" ,keyArray

     

#******************calculating N1,N2,N3     



LAMBDA = 1     #LAMBDA which regulates the number of Tasks in HQ,MQ,LQ respectively

n=len(keyArray) #n : number of Tasks



N1= (n//3) + LAMBDA  #it automatically takes floor value unless we import division package

N2= (n-N1)//2

N3= (n-(N1+N2))




#*****************division of elements into HQ,MQ,LQ 



HQ=[keyArray[i] for i in range(N1)]

MQ=[keyArray[i] for i in range(N1,N1+N2)]

LQ=[keyArray[i] for i in range(N1+N2,n)]

Tasks=HQ+MQ+LQ





#******************internally sorting based on deadlines(working on this..)-->[done]



l1=[int(inputdata[HQ[i]][6]) for i in range(N1)]

l2=[HQ[i] for i in range(N1)]



insertionsort(l1,l2) #calling insertion sort for sorting HQ Tasks based on deadlines



#putting in Finalised HQ

HQ=[str(i) for i in l2]





l1=[int(inputdata[MQ[i]][6]) for i in range(N2)]

l2=[MQ[i] for i in range(N2)]



insertionsort(l1,l2) #calling insertion sort for sorting MQ Tasks based on deadlines



#putting in Finalized MQ

MQ=[str(i) for i in l2]





l1=[int(inputdata[LQ[i]][6]) for i in range(N3)]

l2=[LQ[i] for i in range(N3)]



insertionsort(l1,l2) #calling insertion sort for sorting LQ Tasks based on deadlines



#putting in Finalized LQ

LQ=[str(i) for i in l2]


print "\n********************ROUND 2 - CREATION OF VIRTUAL MACHINES************************\n"    

#*************************************************************************************

#hosts specifications

Hosts=[k  for k,v in inputdata.items() if len(v)==4]         #contains corresponding Hosts

HId=[int(v[0]) for k,v in inputdata.items() if len(v)==4 ]   #contains id's of hosts



insertionsort(HId,Hosts)



Hram=[int(inputdata[Hosts[i]][1]) for i in range(len(HId))]   #contains ram list of Hosts

Hsize=[int(inputdata[Hosts[i]][2]) for i in range(len(HId))]  #contains size list of Hosts

Hmips=[int(inputdata[Hosts[i]][3]) for i in range(len(HId))]  #contains Mips list of Hosts



print "We have following resources:\nHosts     : ",Hosts,"\nRAMs      : ",Hram,"\nSizes     : ",Hsize,"\nMIPS      : ",Hmips,"\n"



#Average stratergy

Instructions=[int(inputdata[HQ[i]][1]) for i in range(len(HQ))]

RAM=[int(inputdata[HQ[i]][2]) for i in range(len(HQ))]

SIZE=[int(inputdata[HQ[i]][3]) for i in range(len(HQ))]





#taking minimum of specifications of HQ

AN= sum(Instructions)//len(Instructions) #Average strategy

AR= sum(RAM)//len(RAM)

AS= sum(SIZE)//len(SIZE) 



#taking minimum of specifications of HQ

MN= min(Instructions)  #minimum strategy

MR= min(RAM)

MS= min(SIZE)

  

Vms=[]   #list of Vms

m=len(Hosts) #m : number of hosts, calculated since intially the number Vms created are equal to number of hosts



vmdict={}

#constraint check

for i in range(m):

        if i > 0:

                AN=int(vmdict[1][0])+(Hmips[i]//2)

                AR=int(vmdict[1][1])+(Hram[i]//2)

                AS=int(vmdict[1][2])+(Hsize[i]//2)  

        #******************Average Strategy**********************

        if AN <= Hmips[i] and AR <= Hram[i] and AS <= Hsize[i]:

                V=[AN,AR,AS]

                Vms.append(i+1)

                vmdict[(Vms[len(Vms)-1])]=V 

                print "\nVM%d is successfully created for Host%d with specifications\nMIPS      :     %d\nRAM       :     %d\nSIZE      :     %d\n" %(i+1,i+1,V[0],V[1],V[2])

        else:

                print "Average stratergy failed for VM%d creation for Host%d\nTrying another stratery for creation of VM%d...." %(i+1,i+1,i
                +1)             

#************************************Minimum strategy**************************                   

                if i>0 and (i+1)<=m:

                        MN1=MN+(Hmips[i]//2)

                        MR1=MR+(Hram[i]//2)

                        MS1=MS+(Hsize[i]//2)  



                        if MN1 <= Hmips[i] and MR1 <= Hram[i] and MS1 <= Hsize[i]:

                                V=[MN1,MR1,MS1]

                                Vms.append(i+1)

                                vmdict[(Vms[len(Vms)-1])]=V

                                print "\nVM%d is successfully created for Host%d using Minimum strategy with specifications\nMIPS      :     %d\nRAM       :     %d\nSIZE      :     %d\n\n" %(i+1,i+1,V[0],V[1],V[2]) 

                        else:

                                print "\nMinimum stratergy failed for VM%d creation for Host%d\nTrying another stratery for creation of VM%d...." %(i+1,i+1,i+1)    

#*************************************Default strategy*****************************************************

                                if i>0 and (i+1)<=m-1:

                                        DN=(Hmips[0]//2)+(Hmips[i]//2)

                                        DR=(Hram[0]//2)+(Hram[i]//2)

                                        DS=(Hsize[0]//2)+(Hsize[i]//2)  

                

                                        if DN <= Hmips[i] and DR <= Hram[i] and DS <= Hsize[i]:

                                                V=[DN,DR,DS]

                                                Vms.append(i+1)

                                                vmdict[(Vms[len(Vms)-1])]=V

                                                print "\nVM%d is successfully created for Host%d using Defualt strategy with specifications\nMIPS      :     %d\nRAM       :     %d\nSIZE      :     %d\n" %(i+1,i+1,V[0],V[1],V[2]) 

                                        else:

                                                DN=(Hmips[i]//2)

                                                DR=(Hram[i]//2)

                                                DS=(Hsize[i]//2) 

                                                V=[DN,DR,DS]

                                                Vms.append(i+1)

                                                vmdict[(Vms[len(Vms)-1])]=V

                                                print "\nVM%d is successfully created for Host%d using Defualt strategy with specifications\nMIPS      :     %d\nRAM       :     %d\nSIZE      :     %d\n" %(i+1,i+1,V[0],V[1],V[2]) 

                                else:

                                        DN=(Hmips[i]//2)

                                        DR=(Hram[i]//2)

                                        DS=(Hsize[i]//2) 

                                        if DN <= Hmips[i] and DR <= Hram[i] and DS <= Hsize[i]:

                                                V=[DN,DR,DS]

                                                Vms.append(i+1)

                                                vmdict[(Vms[len(Vms)-1])]=V 

                                                print "\nVM%d is successfully created for Host%d using Default strategy with specifications\nMIPS      :     %d\nRAM       :     %d\nSIZE      :     %d\n" %(i+1,i+1,V[0],V[1],V[2]) 

                                                                     

#********************* ***Minimum strategy for VM1***************************                                                                

                else:

                        if MN <= Hmips[i] and MR <= Hram[i] and MS <= Hsize[i]:

                                V=[MN,MR,MS]

                                Vms.append(i+1)

                                vmdict[(Vms[len(Vms)-1])]=V 

                                print "\nVM%d is successfully created for Host%d using Minimum strategy with specifications\nMIPS      :     %d\nRAM       :     %d\nSIZE      :     %d\n" %(i+1,i+1,V[0],V[1],V[2]) 

                        else:

                                print "\nMinimum stratergy failed for VM%d creation for Host%d\nTrying another stratery for creation of VM%d...." %(i+1,i+1,i+1)   

#*************************************Default strategy*****************************************************

                                if i>0 and (i+1)<=m:

                                        print "******************************"

                                        DN=(Hmips[0]//2)+(Hmips[i]//2)

                                        DR=(Hram[0]//2)+(Hram[i]//2)

                                        DS=(Hsize[0]//2)+(Hsize[i]//2)  
                

                                        if DN <= Hmips[i] and DR <= Hram[i] and DS <= Hsize[i]:

                                                V=[DN,DR,DS]

                                                Vms.append(i+1)

                                                vmdict[(Vms[len(Vms)-1])]=V

                                                print "\nVM%d is successfully created for Host%d using Defualt strategy with specifications\nMIPS      :     %d\nRAM       :     %d\nSIZE      :     %d\n" %(i+1,i+1,V[0],V[1],V[2]) 

                                        else:

                                                print "*************************"

                                                DN=(Hmips[i]//2)

                                                DR=(Hram[i]//2)

                                                DS=(Hsize[i]//2) 

                                                V=[DN,DR,DS]

                                                Vms.append(i+1)

                                                vmdict[(Vms[len(Vms)-1])]=V

                                                print "\nVM%d is successfully created for Host%d using Defualt strategy with specifications\nMIPS      :     %d\nRAM       :     %d\nSIZE      :     %d\n" %(i+1,i+1,V[0],V[1],V[2]) 

                                else:

                                        DN=(Hmips[i]//2)

                                        DR=(Hram[i]//2)

                                        DS=(Hsize[i]//2) 

                                        if DN <= Hmips[i] and DR <= Hram[i] and DS <= Hsize[i]:

                                                V=[DN,DR,DS]

                                                Vms.append(i+1)

                                                vmdict[(Vms[len(Vms)-1])]=V 

                                                print "\nVM%d is successfully created for Host%d using Default strategy with specification\nMIPS      :     %d\nRAM       :     %d\nSIZE      :     %d\n" %(i+1,i+1,V[0],V[1],V[2]) 

                                                                     

#************************************

#Vms specifications

Vms=[k  for k,v in vmdict.items()]         #contains corresponding Vms

Vram=[int(vmdict[Vms[i]][1]) for i in range(len(Vms))]   #contains ram list of Vms

Vsize=[int(vmdict[Vms[i]][2]) for i in range(len(Vms))]  #contains size list of Vms

Vmips=[int(vmdict[Vms[i]][0]) for i in range(len(Vms))]  #contains Mips list of Vms

#VMflags : 1 indicate the Vms are busy and 0 indicate they are free to use

#initially taken them as 0 : means not assigned

Vflags=[0 for i in range(len(Vms))]

print "We have following resources:\nHosts     : ",Hosts,"\nRAMs      : ",Hram,"\nSizes     : ",Hsize,"\nMIPS      : ",Hmips,"\n"

print "We have following Vms:\nVms       : ",Vms,"\nRAMs      : ",Vram,"\nSizes     : ",Vsize,"\nMIPS      : ",Vmips,"\n"

#***********decrement of resources
for i in range(len(Hosts)):
  
        Hram[i]=Hram[i]-Vram[i]
  
        Hsize[i]=Hsize[i]-Vsize[i]
  
        Hmips[i]=Hmips[i]-Vmips[i]
        
print "We have following remaining resources after creation of initial virtual:\nHosts     : ",Hosts,"\nRAMs      : ",Hram,"\nSizes     : ",Hsize,"\nMIPS      : ",Hmips,"\n"

#************  
#Tasks specifications

l1=[int(v[0]) for k,v in inputdata.items() if len(v)==8 ] #contains priority list of Tasks

keyArray=[k  for k,v in inputdata.items() if len(v)==8]         #contains corresponding Tasks


insertionsort(l1,keyArray) #calling insertionsort to sort based on priority

Tasks=keyArray

Tram=[int(inputdata[Tasks[i]][2]) for i in range(len(Tasks))]   #contains ram list of Tasks

Tsize=[int(inputdata[Tasks[i]][3]) for i in range(len(Tasks))]  #contains size list of Tasks

Tno_of_Instr=[int(inputdata[Tasks[i]][1]) for i in range(len(Tasks))]  #contains Number Of Instructions list of Tasks

TArrival=[int(inputdata[Tasks[i]][4]) for i in range(len(Tasks))]  #contains Mips list of Tasks

TBurst=[int(inputdata[Tasks[i]][5]) for i in range(len(Tasks))]   #contains ram list of Tasks

TDL=[int(inputdata[Tasks[i]][6]) for i in range(len(Tasks))]  #contains size list of Tasks
              
Talloc={} #contains allocation details of Tasks to Vms during execution 

print "We have following Tasks to be executed with specifications:\nTasks                   :     ",Tasks,"\nRAMs                    :     ",Tram,"\nSizes                   :     ",Tsize,"\nNo of Instructions      :     ",Tno_of_Instr,"\nArrivalTime             :     ",TArrival,"\nBurstTime               :     ",TBurst,"\nDeadLine                :     ",TDL,"\n"    

#print TBurst
                 
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


n=len(Tasks)

m=len(Vms)

l=len(Hosts)

Talloc={} #contains allocated tasks

TCT={} #contains completion time of Tasks

TTAT={} #contains turnaround time of Tasks

TWT={} #contains waiting times of Tasks

TExec={} #contains execution times of Tasks
                
Vflags=[0 for i in range(m)]

Vtimer=[0 for i in range(m)]


#Vtimer=[0 for i in range(m)]

#****************now round3 starts

count=0

while(count<5 and len(Tasks)>0):     

         i=0 

         n=len(Tasks)

         m=len(Vms)

         #print "\n\n\nEnter for  count = %d\n\n\n" %count

         #print Vflags,Tasks,TBurst,TDL,Tram,Tsize,Tno_of_Instr,Vms,Vram,Vsize,Vmips,"\n\n",Vtimer,"\n\n"

         while(i<n):

                #print "\n\n",i,n,"\n\n"        
                for j in range(m):

                     if(Tram[i]<=Vram[j] and Tsize[i]<=Vsize[j] and Tno_of_Instr[i]<=Vmips[j] and Vflags[j]==0):

                        Talloc[Vms[j]]=Tasks[i]

                        #print "\n\n",Talloc,"\n\n"

                        Vflags[j]=1

                        break

                    

                if Tasks[i] not in Talloc.values():

                        print "Trying to create a new virtual machine for Tasks %s\n" %Tasks[i]

                        mips=(Tno_of_Instr[i])

                        ram=(Tram[i])

                        size=(Tsize[i])
                        
                        done=0

                        for k in range(l): 
                        
                                if done==0:

                                    if mips <= Hmips[k] and ram <= Hram[k] and size <= Hsize[k]:

                                          V=[mips,ram,size]

                                          Vms.append(len(Vms)+1)

                                          vmdict[(Vms[len(Vms)-1])]=V        

                                          Vram.append(ram)

                                          Vsize.append(size)

                                          Vmips.append(mips)

                                          Hram[k]=Hram[k]-Vram[k]

                                          Hsize[k]=Hsize[k]-Vsize[k]

                                          Hmips[k]=Hmips[k]-Vmips[k]

                                          Talloc[Vms[len(Vms)-1]]=Tasks[i]

                                          Vflags.append(1)

                                          Vtimer.append(0)
                                          
                                          done=1

                                else:
                                    
                                    break      
                                          

                        if Tasks[i] not in Talloc.values():

                                    print "Unable to create a new virtual machine for Tasks %s,due to lack of resources,hence waiting for existing Vms to get free\n" %Tasks[i]

                                    
                                    index=Tasks.index(Tasks[i])

                                        
                                    b=Tasks.pop(index)

                                    Tasks.append(b)

                                   
                                    #index=Tram.index(Tram[i])

                                    b=Tram.pop(index)

                                    Tram.append(b)

                                   
                                    #index=Tsize.index(Tsize[i])

                                    b=Tsize.pop(index)

                                    Tsize.append(b)

                                    
                                    #index=Tno_of_Instr.index(Tno_of_Instr[i])

                                    b=Tno_of_Instr.pop(index)

                                    Tno_of_Instr.append(b)

                                   
                                    
                                    #index=TBurst.index(TBurst[i])
                                    
                                    b=TBurst.pop(index)

                                    TBurst.append(b)

                                    
                                    #index=TDL.index(TDL[i])

                                    b=TDL.pop(index)

                                    TDL.append(b)

                                    
                                    i=i-1

                                    n=n-1
                i=i+1

               
         print "Allocated virtual machines for Tasks for execution are as follows\n",Talloc.keys(),Talloc.values(),"\n\n"                                  

         #print "\n\n\n",Vtimer,"\n\n\n"

         

         h=0 

         m=len(Talloc.keys())

         valloc=[]

         i=0

         if m > n:

                m=n

         for i in range(m):              

              for k,v in Talloc.items():

                  if Tasks[i]==v:

                        valloc.append(k)          

         #print "\n\n",valloc,Tasks,"\n\n"

         

         counter=0

         
         while(h<m):
         
                 alreadydone=0
                 
                 #print "\n\ni am here",Tasks[h],valloc[counter]-1,Vtimer[valloc[counter]-1],TDL[h],"\n\n" 

                 if (TDL[h] > Vtimer[valloc[counter]-1] and TBurst[h]>0):

                          #print "The Tasks entered here is :  %s" %Tasks[h]

                          #print "The Vtimer here is :  %d" %Vtimer[valloc[counter]-1]
                          
                          Executiontime=Vtimer[valloc[counter]-1]+TBurst[h]

                          if Executiontime>TDL[h] and TDL[h]>Vtimer[valloc[counter]-1]:
                                
                                Executiontime = TDL[h] - Vtimer[valloc[counter]-1]
                                
                          if Executiontime>TBurst[h]:
                                
                                Executiontime=TBurst[h]  
                           
                          Vtimer[valloc[counter]-1]=Vtimer[valloc[counter]-1]+Executiontime

                          #print "The Vtimer here is :  %d" %Vtimer[valloc[counter]-1]

                          TBurst[h]=TBurst[h]-Executiontime                       

                          #print "here here bursttime,executiontime",TBurst[h],Executiontime,"\n\n"
                          
                          if (TBurst[h]==0 or TDL[h]<=Vtimer[valloc[counter]-1]):

                                TCT[Tasks[h]]=Vtimer[valloc[counter]-1]
                                
                                #print TCT[Tasks[h]]
                                
                                if Tasks[h] in TExec.keys():

                                        TExec[Tasks[h]]=TExec[Tasks[h]]+Executiontime

                                else:

                                        TExec[Tasks[h]]=Executiontime

                                index=Tasks.index(Tasks[h])

                                
                                b=Tasks.pop(index)

                                #index=Tram.index(Tram[h])

                                b=Tram.pop(index)

                                #index=Tsize.index(Tsize[h])

                                b=Tsize.pop(index)

                                #index=Tno_of_Instr.index(Tno_of_Instr[h])

                                b=Tno_of_Instr.pop(index)

                                #index=TBurst.index(TBurst[h])

                                b=TBurst.pop(index)

                                #index=TDL.index(TDL[h])

                                b=TDL.pop(index)

                                Executiontime=0
                                
                                Vflags[valloc[counter]-1]=0

                                counter=counter+1

                                h=h-1

                                m=m-1
                                
                                alreadydone=1

                          if (len(Tasks)>0):
                                                         
                                if Tasks[h] in TExec.keys():

                                        TExec[Tasks[h]]=TExec[Tasks[h]]+Executiontime

                                else:

                                        TExec[Tasks[h]]=Executiontime

                                #print "Execution times",TExec,"\n\n"

                                if alreadydone==0:
                                     
                                        index=Tasks.index(Tasks[h])

                                        #print "i m looking in here",index,Tasks[h],Tasks,"\n\n"
                                
                                        b=Tasks.pop(index)

                                        Tasks.append(b)

                                
                                
                                        #index=Tram.index(Tram[h])

                                        b=Tram.pop(index)

                                        Tram.append(b)

                                        #index=Tsize.index(Tsize[h])

                                        b=Tsize.pop(index)

                                        Tsize.append(b)

                                        #index=Tno_of_Instr.index(Tno_of_Instr[h])

                                        b=Tno_of_Instr.pop(index)

                                        Tno_of_Instr.append(b)

                                        #index=TBurst.index(TBurst[h])

                                        b=TBurst.pop(index)

                                        TBurst.append(b)

                                        #index=TDL.index(TDL[h])

                                        b=TDL.pop(index)

                                        TDL.append(b)

                                        Vflags[valloc[counter]-1]=0

                                        counter=counter+1

                                        h=h-1

                                        m=m-1


                 else:
                        print "Task %s cannot be executed...because of low deadline,please extend deadline or increase the priority for the task to execute..\n\n" %Tasks[h]

                        TCT[Tasks[h]]=0

                        TExec[Tasks[h]]=0

                        Vflags[valloc[counter]-1]=0

                        index=Tasks.index(Tasks[h])

                        b=Tasks.pop(index)

   #                     index=Tram.index(Tram[h])

                        b=Tram.pop(index)

  #                      index=Tsize.index(Tsize[h])

                        b=Tsize.pop(index)

 #                       index=Tno_of_Instr.index(Tno_of_Instr[h])

                        b=Tno_of_Instr.pop(index)

 #                       index=TBurst.index(TBurst[h])

                        b=TBurst.pop(index)

#                        index=TDL.index(TDL[h])

                        b=TDL.pop(index)
                        
                        counter=counter+1

                        h=h-1

                        m=m-1

                 h=h+1
         
         del(Talloc)

         count=count+1        
        
         Talloc={}

for k,v in TCT.items():

        TTAT[k]=TCT[k]-int(inputdata[k][4])

        TWT[k]=TTAT[k]-TExec[k]

for k in TExec.keys():

        T=int(TExec[k])/int(inputdata[k][5])

        T=T*int(inputdata[k][1])

        TExec[k]=T

Tasks=[k for k,v in TCT.items()]

l2=[int(inputdata[Tasks[i]][0]) for i in range(len(Tasks))]

insertionsort(l2,Tasks)

#**************************************************

Tram=[int(inputdata[Tasks[i]][2]) for i in range(len(Tasks))]   #contains ram list of Tasks

Tsize=[int(inputdata[Tasks[i]][3]) for i in range(len(Tasks))]  #contains size list of Tasks

Tno_of_Instr=[int(inputdata[Tasks[i]][1]) for i in range(len(Tasks))]  #contains Number Of Instructions list of Tasks

TArrival=[int(inputdata[Tasks[i]][4]) for i in range(len(Tasks))]  #contains Mips list of Tasks

TBurst=[int(inputdata[Tasks[i]][5]) for i in range(len(Tasks))]   #contains ram list of Tasks

TDL=[int(inputdata[Tasks[i]][6]) for i in range(len(Tasks))]  #contains size list of Tasks
              
TCTime=[int(TCT[Tasks[i]]) for i in range(len(Tasks))] #contains completion time of Tasks

TTATime=[int(TTAT[Tasks[i]]) for i in range(len(Tasks))] #contains turnaround time of Tasks

TWTime=[int(TWT[Tasks[i]]) for i in range(len(Tasks))] #contains waiting times of Tasks

TExecTime=[int(TExec[Tasks[i]]) for i in range(len(Tasks))] #contains execution times of Tasks
                
print "We have following output after executing Tasks :\nTasks                       :     ",Tasks,"\nRAMs                        :     ",Tram,"\nSizes                       :     ",Tsize,"\nNo of Instructions          :     ",Tno_of_Instr,"\nArrivalTime                 :     ",TArrival,"\nBurstTime                   :     ",TBurst,"\nDeadLine                    :     ",TDL,"\nTasks completionTime        :     ",TCTime,"\nTasks TurnAroundtime        :     ",TTATime,"\nTasks WaitingTime           :     ",TWTime,"\nNo.of Instructions Executed :     ",TExecTime,"\n\n"                      
                     
#************COMPLETION OF ALGORITHM**********                     

print "END OF THE ALGORITHM.....\n\n"

print "Average Turnaround Time                 :          %f" %(sum(TTATime)/len(TTATime))
print "Average Waiting Time                    :          %f" %(sum(TWTime)/len(TWTime))
print "Total Number Of Instructions Executed   :          %d" % (sum(TExecTime))
print "Given Total Number Of Instructions      :          %d\n\n" % (sum(Tno_of_Instr))

print "To plot results type python outputplot.py....\n\n"

filename='outputFCFS'+filename

with open(filename,'w') as output_file:

        for i in range(len(TTATime)):
                
                if i==len(TTATime)-1:
                
                        output_file.write("%d\n" %TTATime[i])
                        
                else :
                
                        output_file.write("%d," %TTATime[i])
        
        for i in range(len(TWTime)):
                
                if i==len(TTATime)-1:
                
                        output_file.write("%d\n" %TWTime[i])
                        
                else :
                
                        output_file.write("%d," %TWTime[i])
        
        for i in range(len(TExecTime)):
                
                if i==len(TTATime)-1:
                
                        output_file.write("%d\n" %TExecTime[i])
                        
                else :
                
                        output_file.write("%d," %TExecTime[i])
