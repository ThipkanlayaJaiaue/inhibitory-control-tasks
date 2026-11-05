import pandas as pd
import glob
import numpy as np
from scipy.stats import norm

# set folder path and find all go-nogo .csv files
task_folder = glob.glob(r"D:\github\study3\inhibitory-control-tasks\go-nogo-task\data\*.csv")
gng_files = [file for file in task_folder if "gonogo" in file]

# create an empty list to store data
gng_dataList = []

# create the for loop to process each participant's data
for file in range(0, len(gng_files)):

    # read data files
    task = pd.read_csv(gng_files[file])

    total_trials = task["myExp.trial"].max() * 5
    go_num = len(task[task['myExp.nogo'] == 0])
    nogo_num = len(task[task['myExp.nogo'] == 1])
    correctTrials_all = task["myExp.RT_correctTrials"]
    correctTrials_go = task.loc[(task['myExp.nogo'] == 0), "myExp.RT_correctTrials"]
    incorrectTrials_nogo = task.loc[(task['myExp.nogo'] == 1) & (task['myExp.Accuracy'] == 0), "myExp.RT_allTrials"]

    # create median RT variables
    medianRT_all = correctTrials_all.median() * 1000
    medianRT_go = correctTrials_go.median() * 1000
    medianRT_nogo = incorrectTrials_nogo.median() * 1000

    # create accuracy variables
    accuracy_all = task["myExp.Accuracy"].sum()
    accuracy_go = task.loc[(task['myExp.nogo'] == 0), "myExp.Accuracy"].sum()
    accuracy_nogo = task.loc[(task['myExp.nogo'] == 1), "myExp.Accuracy"].sum()
    commission_error = nogo_num - accuracy_nogo

    ## computation of d-prime
    # The d-prime index is the difference between Z transforms of hit rate and false alarms.
    # Hit rate is defined as the proportion of hits when a signal is present to all target stimuli and
    # false alarms represent the proportion of responses when a signal is absent to all non-target stimuli.
    # Perfect scores were adjusted according to following formulas: 1 – 1/(2n) for perfect hits, and 1/(2n) for zero false alarms,
    # where n was the number of total hits or false alarms (Rogala et al., 2024)

    hit_rate = accuracy_go / go_num
    false_rate = commission_error / nogo_num

    if hit_rate == 1:
        hit_rate = 1 - 1 / (2 * go_num)
    if false_rate == 0:
        false_rate = 1 / (2 * nogo_num)

    z_hit_rate= norm.ppf(hit_rate)
    z_false_rate = norm.ppf(false_rate)

    d_prime = z_hit_rate - z_false_rate

    # append data
    gng_dataList.append({'participant': task.iloc[1]["participant"],
                      'RT_go(ms)': medianRT_go,
                      'RT_nogo(ms)': medianRT_nogo,
                      'accuracy_all(num)': accuracy_all,
                      'accuracy_go(num)': accuracy_go,
                      'accuracy_nogo(num)': accuracy_nogo,
                      'accuracy_all(%)': accuracy_all / total_trials * 100,
                      'accuracy_go(%)': accuracy_go / go_num * 100,
                      'accuracy_nogo(%)': accuracy_nogo / nogo_num * 100,
                      'commission_error(%)': commission_error / nogo_num * 100,
                      'd_prime': d_prime})

gngData_long = pd.DataFrame(gng_dataList)

# save dataframe as .csv
gngData_long.to_csv('gonogo_longFormat.csv', index=False)