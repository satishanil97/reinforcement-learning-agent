import matplotlib.pyplot as plt
import numpy as np


def getSplitIndices(data):
    indices=[0]
    maxidx=len(data)-1
    for idx, row in enumerate(data):
        if idx+1 <= maxidx:
            if data[idx]['NumTrainingEpisode'] > data[idx+1]['NumTrainingEpisode']:
                #[part1,part2]=np.split(data,[idx+1],axis=0)
                indices.append(idx+1)
    indices.append(len(data))
    return indices


data = np.genfromtxt("test_file.csv", delimiter=",", names=True)
indices=getSplitIndices(data)

maxi=len(indices)-1
for i, idx in enumerate(indices):
    #print(i,idx)
    if i+1 <= maxi:
        plt.plot(data['NumTrainingEpisode'][indices[i]:indices[i+1]], data['AvgRewardsForAll'][indices[i]:indices[i+1]])
