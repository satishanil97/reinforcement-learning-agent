import matplotlib.pyplot as plt
import numpy as np
import numpy_indexed as npi
import os


output_files = list(filter(lambda f: f.endswith('.csv'), os.listdir(".")))
agents = list({file.split("_")[1] for file in output_files})
layouts = list({file.split("_")[2].split(".")[0] for file in output_files})


fig, axes2d = plt.subplots(nrows=len(layouts), ncols=len(agents), sharex=True, sharey=True, figsize=(20,20))

for i, row in enumerate(axes2d):
    for j, cell in enumerate(row): 
        filename = [file for file in output_files if agents[j] in file and layouts[i] in file]
        if len(filename)>0:

            raw_data = np.genfromtxt(filename[0], delimiter=",", names=True)
            data = raw_data.view((float, len(raw_data.dtype.names)))

            lambda_exists = True in np.isnan(data[:,6])
            
            if not lambda_exists:
                param_combos = np.vstack(tuple({tuple(e) for e in data[:,[3,4,5,6]]}))
            else:
                param_combos = np.vstack(tuple({tuple(e) for e in data[:,[3,4,5]]}))                

            for each in param_combos:
                label = "Alpha=" + str(each[0]) + " ; Epsilon=" + str(each[1]) + " ; Gamma=" + str(each[2]) 
                
                if not lambda_exists:
                    label += " ; Lambda=" + str(each[3])
                else:
                    label += " ; Lambda= -NA- "
                    
                if not lambda_exists:                
                    plot_data = data[(data[:,3] == each[0]) & (data[:,4] == each[1]) & (data[:,5] == each[2]) & (data[:,6] == each[3])][:,[0,1]]
                else:
                    plot_data = data[(data[:,3] == each[0]) & (data[:,4] == each[1]) & (data[:,5] == each[2])][:,[0,1]]

                avg_plot_data = npi.group_by(plot_data[:, 0]).mean(plot_data)[1]

                x_data = avg_plot_data[:,0]
                y_data = avg_plot_data[:,1]

                cell.plot(x_data, y_data, label=label)
                cell.legend(loc='lower right')

                if i == len(axes2d) - 1:
                    cell.set_xlabel(agents[j],fontsize=20)
                if j == 0:
                    cell.set_ylabel(layouts[i],fontsize=20)
                                    
fig.tight_layout()