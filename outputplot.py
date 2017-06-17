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
    
        
filename3 = 'outputSJF'+filename


with open(filename3,'r') as input_file:

        for line in input_file:

                splitline=line.split(",")

                inputdata[count]=",".join(splitline[0:]) 
                
                count=count+1   
    
        for key in inputdata:

                inputdata[key]=inputdata[key].rstrip()

                inputdata[key]=list(inputdata[key].split(","))
   


Tasks=[i for i in range(len(inputdata[0]))]
TTAT1=map(int,inputdata[0])
TWT1=map(int,inputdata[1])
TExecTime1=map(int,inputdata[2])

TTAT2=map(int,inputdata[3])
TWT2=map(int,inputdata[4])
TExecTime2=map(int,inputdata[5])

TTAT3=map(int,inputdata[6])
TWT3=map(int,inputdata[7])
TExecTime3=map(int,inputdata[8])

#matplotlib inline
#import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


raw_data = {'first_name': ['1', '2', '3', '4', '5','6', '7', '8', '9', '10'],
        'DACExec': TExecTime1,
        'FCFSExec': TExecTime2,
        'SJFExec': TExecTime3}
        #'post_score': [5, 43, 23, 23, 51]}
#raw_data = pd.DataFrame(raw_data, columns = ['first_name', 'DACExec', 'FCFSExec', 'post_score'])


# Setting the positions and width for the bars
pos = list(range(len(raw_data['DACExec'])))
width = 0.25

# Plotting the bars
fig, ax = plt.subplots(figsize=(10,10))

# Create a bar with DACExec data,
# in position pos,
plt.bar(pos,
        #using raw_data['DACExec'] data,
        raw_data['DACExec'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='r',
        # with label the first value in first_name
        label=raw_data['first_name'][0])

# Create a bar with FCFSExec data,
# in position pos + some width buffer,
plt.bar([p + width for p in pos],
        #using raw_data['FCFSExec'] data,
        raw_data['FCFSExec'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='b',
        # with label the second value in first_name
        label=raw_data['first_name'][1])

plt.bar([p + width*2 for p in pos],
        #using raw_data['FCFSExec'] data,
        raw_data['SJFExec'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='g',
        # with label the second value in first_name
        label=raw_data['first_name'][2])


# Set the y axis label
ax.set_ylabel('Executiontimes')
ax.set_xlabel('Tasks')

# Set the chart's title
ax.set_title('Exectution times of DAC,FCFS,SJF on '+filename)

# Set the position of the x ticks
ax.set_xticks([p + 1.5 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(raw_data['first_name'])

# Setting the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, max(raw_data['DACExec'] + raw_data['FCFSExec']+ raw_data['SJFExec'])])

# Adding the legend and showing the plot
plt.legend(['DACExec', 'FCFSExec','SJFExec'], loc='upper right')
plt.grid()
#plt.show()

#***********************************


raw_data = {'first_name': ['1', '2', '3', '4', '5','6', '7', '8', '9', '10'],
        'DACTAT': TTAT1,
        'FCFSTAT': TTAT2,
        'SJFTAT': TTAT3}
        #'post_score': [5, 43, 23, 23, 51]}
#raw_data = pd.DataFrame(raw_data, columns = ['first_name', 'DACExec', 'FCFSExec', 'post_score'])


# Setting the positions and width for the bars
pos = list(range(len(raw_data['DACTAT'])))
width = 0.25

# Plotting the bars
fig, ax = plt.subplots(figsize=(10,10))

# Create a bar with DACExec data,
# in position pos,
plt.bar(pos,
        #using raw_data['DACExec'] data,
        raw_data['DACTAT'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='r',
        # with label the first value in first_name
        label=raw_data['first_name'][0])

# Create a bar with FCFSExec data,
# in position pos + some width buffer,
plt.bar([p + width for p in pos],
        #using raw_data['FCFSExec'] data,
        raw_data['FCFSTAT'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='b',
        # with label the second value in first_name
        label=raw_data['first_name'][1])

plt.bar([p + width*2 for p in pos],
        #using raw_data['FCFSExec'] data,
        raw_data['SJFTAT'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='g',
        # with label the second value in first_name
        label=raw_data['first_name'][2])


# Set the y axis label
ax.set_ylabel('TurnAroundtimes')
ax.set_xlabel('Tasks')

# Set the chart's title
ax.set_title('TurnAround times of DAC,FCFS,SJF on '+filename)

# Set the position of the x ticks
ax.set_xticks([p + 1.5 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(raw_data['first_name'])

# Setting the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, max(raw_data['DACTAT'] + raw_data['FCFSTAT']+ raw_data['SJFTAT'])])

# Adding the legend and showing the plot
plt.legend(['DACTAT', 'FCFSTAT','SJFTAT'], loc='upper right')
plt.grid()
#plt.show()
#*********************************************************


raw_data = {'first_name': ['1', '2', '3', '4', '5','6', '7', '8', '9', '10'],
        'DACWT': TWT1,
        'FCFSWT': TWT2,
        'SJFWT': TWT3}
        #'post_score': [5, 43, 23, 23, 51]}
#raw_data = pd.DataFrame(raw_data, columns = ['first_name', 'DACExec', 'FCFSExec', 'post_score'])


# Setting the positions and width for the bars
pos = list(range(len(raw_data['DACWT'])))
width = 0.25

# Plotting the bars
fig, ax = plt.subplots(figsize=(10,10))

# Create a bar with DACExec data,
# in position pos,
plt.bar(pos,
        #using raw_data['DACExec'] data,
        raw_data['DACWT'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='r',
        # with label the first value in first_name
        label=raw_data['first_name'][0])

# Create a bar with FCFSExec data,
# in position pos + some width buffer,
plt.bar([p + width for p in pos],
        #using raw_data['FCFSExec'] data,
        raw_data['FCFSWT'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='b',
        # with label the second value in first_name
        label=raw_data['first_name'][1])

plt.bar([p + width*2 for p in pos],
        #using raw_data['FCFSExec'] data,
        raw_data['SJFWT'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='g',
        # with label the second value in first_name
        label=raw_data['first_name'][2])


# Set the y axis label
ax.set_ylabel('Waitingtimes')
ax.set_xlabel('Tasks')

# Set the chart's title
ax.set_title('Waiting times of DAC,FCFS,SJF on '+filename)

# Set the position of the x ticks
ax.set_xticks([p + 1.5 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(raw_data['first_name'])

# Setting the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, max(raw_data['DACWT'] + raw_data['FCFSWT']+ raw_data['SJFWT'])])

# Adding the legend and showing the plot
plt.legend(['DACWT', 'FCFSWT','SJFWT'], loc='upper right')
plt.grid()
plt.show()
