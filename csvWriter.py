import csv 
from os.path import exists

sampleOutput = {'NumTrainingEpisode': [1,2], 'AvgRewardsForAll': [127.8, 129.4], 'LastEpisodeReward': [128.9, 130.4], 'Alpha': 0.9, 'Epsilon': 0.1, 'Gamma': 0.5, 'Lambda': 0.3 }
fileName='output.csv'
# Header Row
#fields = ['NumTrainingEpisode', 'AvgRewardsForAll', 'LastEpisodeReward', 'Alpha','Epsilon','Gamma','Lambda']

listfields = [k for k,v in sampleOutput.items() if isinstance(v, list)]
constfields = [k for k,v in sampleOutput.items() if not isinstance(v, list)]
numrows = len(sampleOutput['NumTrainingEpisode'])

# Writing first row
if not exists(fileName):    
    with open(fileName, 'w') as outputfile:
        csvwriter = csv.writer(outputfile) 
        fields = listfields + constfields
        csvwriter.writerow(fields)
        outputfile.close()

# Writing runHistiry to output file 
with open(fileName, 'a') as outputfile: 
    csvwriter = csv.writer(outputfile)
    for i in range(numrows): 
        row=[[]]
        
        for each in listfields:
            row[0].append(sampleOutput[each][i])
        for each in constfields:
            row[0].append(sampleOutput[each])

        #print("Row.....",row)
        #print("Type....",type(row))
        
        csvwriter.writerows(row)
    
    outputfile.close()