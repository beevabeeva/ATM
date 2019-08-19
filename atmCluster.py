from os import system
import sys


# Get input:
val = sys.argv[1]

# set path to xpanes if it isnt installed in bin
xpanes='/home-mscluster/abank/scripts/xpanes'

# Set login node
login='abank@mscluster0'

# Set our selected hosts
hosts3='mscluster23 mscluster24 mscluster25 mscluster26 mscluster27 mscluster28 mscluster30 mscluster31 mscluster33 mscluster34 mscluster35 mscluster36 mscluster37 mscluster38 mscluster39 mscluster40'


# Make all batch partition hosts (mscluster11...mscluster70) procedurely:
batch = ""
for i in range(10,70):
    batch+= 'mscluster'+str(i+1)+" "

# Make batch1 partition hosts (mscluster11...mscluster20) procedurely:
batch1 = ""
for i in range(10,20):
    batch1+= 'mscluster'+str(i+1)+" "

# Make batch2 partition hosts (mscluster20...mscluster30) procedurely:
batch2 = ""
for i in range(19,30):
    batch2+= 'mscluster'+str(i+1)+" "

# Make batch3 partition hosts (mscluster30...mscluster40) procedurely:
batch3 = ""
for i in range(29,40):
    batch3+= 'mscluster'+str(i+1)+" "

# Make batch4 partition hosts (mscluster40...mscluster50) procedurely:
batch4 = ""
for i in range(39,50):
    batch4+= 'mscluster'+str(i+1)+" "


# Make batch5 partition hosts (mscluster50...mscluster60) procedurely:
batch5 = ""
for i in range(49,60):
    batch5+= 'mscluster'+str(i+1)+" "

# Make batch6 partition hosts (mscluster60...mscluster70) procedurely:
batch6 = ""
for i in range(59,70):
    batch6+= 'mscluster'+str(i+1)+" "


# Make ha partition hosts (mscluster1...mscluster10) procedurely:
ha = ""
for i in range(0,10):
    ha+= 'mscluster'+str(i+1)+" "



# Check which cluster partition we want (passed from input):
if(val=='ha'):
	hosts=ha
	# run2=xpanes+" -C 2 -t -c \"ssh -t abank@{} ''\" "+hosts
	run2=xpanes+" -C 2 -t -c \"ssh abank@{} -t bash -ci 'atm-run'\" "+hosts
elif(val=='batch1'):
	hosts=batch1
	run2=xpanes+" -C 2 -t -c \"ssh -t abank@{} ''\" "+hosts
elif(val=='batch2'):
	hosts=batch2
	run2=xpanes+" -C 2 -t -c \"ssh -t abank@{} ''\" "+hosts
elif(val=='batch3'):
	hosts=batch3
	run2=xpanes+" -C 2 -t -c \"ssh -t abank@{} ''\" "+hosts
elif(val=='batch4'):
	hosts=batch4
	run2=xpanes+" -C 2 -t -c \"ssh -t abank@{} ''\" "+hosts
elif(val=='batch5'):
	hosts=batch5
	run2=xpanes+" -C 2 -t -c \"ssh -t abank@{} ''\" "+hosts
elif(val=='batch6'):
	hosts=batch6
	run2=xpanes+" -C 2 -t -c \"ssh -t abank@{} ''\" "+hosts
elif(val=='gpu'):
	hosts='mscluster71 mscluster72 mscluster73'
	run2=xpanes+" -t -c \"ssh -t abank@{} '/home-mscluster/abank/scripts/nvtop/bin/nvtop'\" "+hosts
elif(val=='gpucpu'):
	hosts='mscluster71 mscluster72 mscluster73'
	run2=xpanes+" -t -c \"ssh -t abank@{} 'top'\" "+hosts
elif(val=='ours'):
	hosts=hosts3
	run2=xpanes+" -t -c \"ssh -t abank@{} ''\" "+hosts



# run2=xpanes+" -t -c \"ssh -t abank@{} ''\" "+hosts

system(run2)