#DAC algorithm Round1 implementation using python

#Date : 6-6-2017

#Name : K Naveen Kumar

#*****************taking input from the file separate by comma and storing into a dictionary called inputdata

inputdata={}

filename = raw_input("Give the name of the input file : ") 

with open(filename,'r') as input_file:

        for line in input_file:

                splitline=line.split(",")

                inputdata[str(splitline[0])]=",".join(splitline[1:])    
    
        for key in inputdata:

                inputdata[key]=inputdata[key].rstrip()

                inputdata[key]=list(inputdata[key].split(","))
  
#*****************tasks sorting based on priority and storing into a list called Keyarray     

#used insertionsort for all kinds of sorting that take place in round1

#function for insertionsort

print "\n********************ROUND 1 : DIVISION OF TASKS INTO HQ,MQ,LQ************************\n" 

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

l1=[int(v[7]) for k,v in inputdata.items() if len(v)==8 ] #contains priority list of tasks

keyArray=[k  for k,v in inputdata.items() if len(v)==8]         #contains corresponding tasks



insertionsort(l1,keyArray) #calling insertionsort to sort based on priority

        

print "The keyArray containing sorted tasks based on priorities:" ,keyArray

     

#******************calculating N1,N2,N3     



LAMBDA = 2     #LAMBDA which regulates the number of tasks in HQ,MQ,LQ respectively

n=len(keyArray) #n : number of tasks



N1= (n/3) + LAMBDA  #it automatically takes floor value unless we import division package

N2= (n-N1)/2

N3= (n-(N1+N2))



print "\nThe number of Tasks in \nHQ  : %d\nMQ  : %d\nLQ  : %d" %(N1,N2,N3)

#*****************division of elements into HQ,MQ,LQ 



HQ=[keyArray[i] for i in range(N1)]

MQ=[keyArray[i] for i in range(N1,N1+N2)]

LQ=[keyArray[i] for i in range(N1+N2,n)]



print "\nTasks in HQ:",HQ,"\n","Tasks in MQ:",MQ,"\n","Tasks in LQ:",LQ,"\n"





#******************internally sorting based on deadlines(working on this..)-->[done]



l1=[int(inputdata[HQ[i]][6]) for i in range(N1)]

l2=[HQ[i] for i in range(N1)]



insertionsort(l1,l2) #calling insertion sort for sorting HQ tasks based on deadlines



#putting in Finalised HQ

HQ=[str(i) for i in l2]





l1=[int(inputdata[MQ[i]][6]) for i in range(N2)]

l2=[MQ[i] for i in range(N2)]



insertionsort(l1,l2) #calling insertion sort for sorting MQ tasks based on deadlines



#putting in Finalized MQ

MQ=[str(i) for i in l2]





l1=[int(inputdata[LQ[i]][6]) for i in range(N3)]

l2=[LQ[i] for i in range(N3)]



insertionsort(l1,l2) #calling insertion sort for sorting LQ tasks based on deadlines



#putting in Finalized LQ

LQ=[str(i) for i in l2]



print "The Finalized internally sorted HQ based on deadlines:",HQ,'\n',"The Finalized internally sorted MQ based on deadlines:",MQ,'\n',"The Finalized internally sorted LQ based on deadlines:",LQ



#********************Calculation of time quantum to implement roundrobin for HQ  , MQ

#alpha1,alpha2 regulates the time quanta

ALPHA1=2

ALPHA2=1



l1=[int(inputdata[HQ[i]][6]) for i in range(len(HQ))]   

l2=[int(inputdata[MQ[i]][6]) for i in range(len(MQ))]



TQ1=max(l1)/pow(2,ALPHA1)   

TQ2=max(l2)/pow(2,ALPHA2) 



while(1):  

       if TQ1>TQ2 and TQ1>0:      

          ALPHA1=ALPHA1+1

          TQ1=max(l1)/pow(2,ALPHA1)   

       else:

          break

       

  

print "\nThe Calculated time quantum as follows:\nTQ1   :   %d\nTQ2   :   %d\n\n" %(TQ1,TQ2) 

print "********************END OF ROUND1************************\n\n" 

print "\n********************ROUND 2 - CREATION OF VIRTUAL MACHINES************************\n"    



#*************************************************************************************

#DAC algorithm Round2 implementation using python

#Date : 7-6-2017

#Name : K Naveen Kumar



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

AN= sum(Instructions)/len(Instructions) #Average strategy

AR= sum(RAM)/len(RAM)

AS= sum(SIZE)/len(SIZE) 



#taking minimum of specifications of HQ

MN= min(Instructions)  #minimum strategy

MR= min(RAM)

MS= min(SIZE)

  

Vms=[]   #list of vms

m=len(Hosts) #m : number of hosts, calculated since intially the number vms created are equal to number of hosts



vmdict={}

#constraint check

for i in range(m):

        if i > 0:

                AN=int(vmdict[1][0])+(Hmips[i]/2)

                AR=int(vmdict[1][1])+(Hram[i]/2)

                AS=int(vmdict[1][2])+(Hsize[i]/2)  

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

                        MN1=MN+(Hmips[i]/2)

                        MR1=MR+(Hram[i]/2)

                        MS1=MS+(Hsize[i]/2)  



                        if MN1 <= Hmips[i] and MR1 <= Hram[i] and MS1 <= Hsize[i]:

                                V=[MN1,MR1,MS1]

                                Vms.append(i+1)

                                vmdict[(Vms[len(Vms)-1])]=V

                                print "\nVM%d is successfully created for Host%d using Minimum strategy with specifications\nMIPS      :     %d\nRAM       :     %d\nSIZE      :     %d\n\n" %(i+1,i+1,V[0],V[1],V[2]) 

                        else:

                                print "\nMinimum stratergy failed for VM%d creation for Host%d\nTrying another stratery for creation of VM%d...." %(i+1,i+1,i+1)    

#*************************************Default strategy*****************************************************

                                if i>0 and (i+1)<=m-1:

                                        DN=(Hmips[0]/2)+(Hmips[i]/2)

                                        DR=(Hram[0]/2)+(Hram[i]/2)

                                        DS=(Hsize[0]/2)+(Hsize[i]/2)  

                

                                        if DN <= Hmips[i] and DR <= Hram[i] and DS <= Hsize[i]:

                                                V=[DN,DR,DS]

                                                Vms.append(i+1)

                                                vmdict[(Vms[len(Vms)-1])]=V

                                                print "\nVM%d is successfully created for Host%d using Defualt strategy with specifications\nMIPS      :     %d\nRAM       :     %d\nSIZE      :     %d\n" %(i+1,i+1,V[0],V[1],V[2]) 

                                        else:

                                                DN=(Hmips[i]/2)

                                                DR=(Hram[i]/2)

                                                DS=(Hsize[i]/2) 

                                                V=[DN,DR,DS]

                                                Vms.append(i+1)

                                                vmdict[(Vms[len(Vms)-1])]=V

                                                print "\nVM%d is successfully created for Host%d using Defualt strategy with specifications\nMIPS      :     %d\nRAM       :     %d\nSIZE      :     %d\n" %(i+1,i+1,V[0],V[1],V[2]) 

                                else:

                                        DN=(Hmips[i]/2)

                                        DR=(Hram[i]/2)

                                        DS=(Hsize[i]/2) 

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

                                        DN=(Hmips[0]/2)+(Hmips[i]/2)

                                        DR=(Hram[0]/2)+(Hram[i]/2)

                                        DS=(Hsize[0]/2)+(Hsize[i]/2)  
                

                                        if DN <= Hmips[i] and DR <= Hram[i] and DS <= Hsize[i]:

                                                V=[DN,DR,DS]

                                                Vms.append(i+1)

                                                vmdict[(Vms[len(Vms)-1])]=V

                                                print "\nVM%d is successfully created for Host%d using Defualt strategy with specifications\nMIPS      :     %d\nRAM       :     %d\nSIZE      :     %d\n" %(i+1,i+1,V[0],V[1],V[2]) 

                                        else:

                                                print "*************************"

                                                DN=(Hmips[i]/2)

                                                DR=(Hram[i]/2)

                                                DS=(Hsize[i]/2) 

                                                V=[DN,DR,DS]

                                                Vms.append(i+1)

                                                vmdict[(Vms[len(Vms)-1])]=V

                                                print "\nVM%d is successfully created for Host%d using Defualt strategy with specifications\nMIPS      :     %d\nRAM       :     %d\nSIZE      :     %d\n" %(i+1,i+1,V[0],V[1],V[2]) 

                                else:

                                        DN=(Hmips[i]/2)

                                        DR=(Hram[i]/2)

                                        DS=(Hsize[i]/2) 

                                        if DN <= Hmips[i] and DR <= Hram[i] and DS <= Hsize[i]:

                                                V=[DN,DR,DS]

                                                Vms.append(i+1)

                                                vmdict[(Vms[len(Vms)-1])]=V 

                                                print "\nVM%d is successfully created for Host%d using Default strategy with specification\nMIPS      :     %d\nRAM       :     %d\nSIZE      :     %d\n" %(i+1,i+1,V[0],V[1],V[2]) 

                                                                     

print "********************END OF ROUND2************************\n\n" 



#*********************************ROUND 3 : Execution of Tasks using  virtual machines***********************                                
#*************************************************************************************

#DAC algorithm Round3 implementation using python

#Date : 9-6-2017

#Name : K Naveen Kumar


print "\n************ROUND 3 : EXECUTION OF TASKS USING VIRTUAL MACHINES*****************\n"    


#VMs specifications

VMs=[k  for k,v in vmdict.items()]         #contains corresponding Vms

Vram=[int(vmdict[VMs[i]][1]) for i in range(len(VMs))]   #contains ram list of Vms

Vsize=[int(vmdict[VMs[i]][2]) for i in range(len(VMs))]  #contains size list of Vms

Vmips=[int(vmdict[VMs[i]][0]) for i in range(len(VMs))]  #contains Mips list of Vms

#VMflags : 1 indicate the VMs are busy and 0 indicate they are free to use

#initially taken them as 0 : means not assigned

Vflags=[0 for i in range(len(VMs))]

print "We have following resources:\nHosts     : ",Hosts,"\nRAMs      : ",Hram,"\nSizes     : ",Hsize,"\nMIPS      : ",Hmips,"\n"

print "We have following Vms:\nVMs       : ",VMs,"\nRAMs      : ",Vram,"\nSizes     : ",Vsize,"\nMIPS      : ",Vmips,"\n"

#***********decrement of resources
for i in range(len(Hosts)):
  
        Hram[i]=Hram[i]-Vram[i]
  
        Hsize[i]=Hsize[i]-Vsize[i]
  
        Hmips[i]=Hmips[i]-Vmips[i]
        
print "We have following remaining resources after creation of initial virtual:\nHosts     : ",Hosts,"\nRAMs      : ",Hram,"\nSizes     : ",Hsize,"\nMIPS      : ",Hmips,"\n"

#*/*/*/**/*/*/*/*/*/
print "Execution of Tasks in HQ......\n"
                
#Tasks specifications

Tasks = HQ

n=len(Tasks)

Tram=[int(inputdata[Tasks[i]][2]) for i in range(len(Tasks))]   #contains ram list of Tasks

Tsize=[int(inputdata[Tasks[i]][3]) for i in range(len(Tasks))]  #contains size list of Tasks

Tno_of_Instr=[int(inputdata[Tasks[i]][1]) for i in range(len(Tasks))]  #contains Number Of Instructions list of Tasks

TArrival=[int(inputdata[Tasks[i]][4]) for i in range(len(Tasks))]  #contains Mips list of Tasks

TBurst=[int(inputdata[Tasks[i]][5]) for i in range(len(Tasks))]   #contains ram list of Tasks

TDL=[int(inputdata[Tasks[i]][6]) for i in range(len(Tasks))]  #contains size list of Tasks

Talloc={} #contains allocation details of tasks to vms during execution

TCL={} #contains completion time of tasks

TTAT={} #contains turnaround time of tasks

TWT={} #contains waiting times of tasks
                
print "We have following Tasks to be executed in HQ with specifications:\nTasks                   :     ",Tasks,"\nRAMs                    :     ",Tram,"\nSizes                   :     ",Tsize,"\nNo of Instructions      :     ",Tno_of_Instr,"\nArrivalTime             :     ",TArrival,"\nBurstTime               :     ",TBurst,"\nDeadLine                :     ",TDL,"\n"
         
completionflag=[0 for i in range(len(Tasks))]  #indication execution of all tasks in HQ                
timer=[0 for i in range(len(VMs))]
#**********************************/*/*/*/*/*/*/NEED TO WORK ON THIS@#$^&*()))(*&^%$###@@!!!/*/*//*/
while(sum(completionflag)!=n): 
 #choosing best fit vm for execution of tasks
      TempTQ=TQ1 
      for i in range(len(VMs)):
             #if tasks find a virtual machine then allocate it to the virtual machine
          for j in range(len(VMs)):
               if Tram[i]<=Vram[j] and Tno_of_Instr[i]<=Vmips[j] and Tsize[i]<=Vsize[j] and Vflags[j]==0:
                   Talloc[str(VMs[j])]=Tasks[i]
                   Vflags[j]=1   
                     #else create a new virtual machine provided we have the resources other wise throw an exception to the user 
               else:
                   temp=0
                   for k in range(len(Hosts)):
                        #checking for host, whether we have resources to incorporte the virtual machine
                        if Tram[i]<=Hram[k] and Tno_of_Instr[i]<=Hmips[k] and Tsize[i]<=Hsize[k] and temp==0:
                            V=[Tram[i],Tno_of_Instr[i],Tsize[i]]
                            VMs.append(len(VMs)+1)
                            vmdict[(VMs[len(VMs)-1])]=V
                            print "\n\n\n",i,len(VMs)-1,vmdict,VMs,VMs[len(VMs)-1],"\n\n\n\n"
                            Talloc[str(VMs[len(VMs)-1])]=Tasks[i]
                            Vflags.append(1)
                            Hram[k]=Hram[k]-Tram[i]
                            Hsize[k]=Hsize[k]-Tsize[i]
                            Hmips[k]=Hmips[k]-Tno_of_Instr[i]
                            temp=1 
                  
      print "\nThe Tasks are allocated to VMs in the order....\nVMs",Talloc.keys(),"<-------","Tasks",Talloc.values(),"\n\n"                        
      allocvm=Talloc.keys()
      alloctasks=Talloc.values()
     
      print allocvm,alloctasks
      for i in range(len(alloctasks)):
                if(inputdata[alloctasks[i]][6]<TempTQ and timer[int(allocvm[i])-1] < inputdata[alloctasks[i]][6]):
                        #execute till deadline
                        timer[int(allocvm[i])-1]=timer[int(allocvm[i])-1]+inputdata[alloctasks[i]][6] 
                        TCT[alloctasks[i]]=timer[int(allocvm[i])-1]       
                        completionflag[i]=1 #completion done so remove the task from the list
                        index=Tasks.index(alloctasks[i])
                        Tasks.pop(index)
                        Tram.pop(index)
                        Tsize.pop(index)
                        Tno_of_Instr.pop(index)
                        Vflags[int(allocvm[i])-1]=0
                        
                elif (inputdata[alloctasks[i]][6] >= TempTQ and timer[int(allocvm[i])-1] < inputdata[alloctasks[i]][6]):
                        #execute till Timequanta and put the task again on the queue
                        timer[int(allocvm[i])-1]=timer[int(allocvm[i])-1]+TempTQ        
                        index=Tasks.index(alloctasks[i])
                        b=Tasks.pop(index)
                        Tasks.append(b)
                        b=Tram.pop(index)
                        Tram.append(b)
                        b=Tsize.pop(index)
                        Tsize.append(b)
                        b=Tno_of_Instr.pop(index)
                        Tno_of_Instr.append(b)
                        Vflags[int(allocvm[i])-1]=0
                
                      
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
