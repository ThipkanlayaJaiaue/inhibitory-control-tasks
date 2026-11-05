import pandas as pd
import glob
import numpy as np

# set folder path and find all flanker .csv files
task_folder = glob.glob(r"D:\github\study3\inhibitory-control-tasks\flanker-task\data\*.csv")
flanker_files = [file for file in task_folder if "flanker" in file]

# create an empty list to store data
flanker_dataList = []

# create the for loop to process each participant's data
for file in range(0, len(flanker_files)):

    # read data files
    task = pd.read_csv(flanker_files[file])

    # set variables for computation
    total_trials = task["myExp.trial"].max()
    congruent_num = len(task[task['myExp.congruent'] == 1])
    incongruent_num = len(task[task['myExp.congruent'] == 0])
    correctTrials_all = task["myExp.RT_correctTrials"]
    correctTrials_congruent = task.loc[(task['myExp.congruent'] == 1), "myExp.RT_correctTrials"]
    correctTrials_incongruent = task.loc[(task['myExp.congruent'] == 0), "myExp.RT_correctTrials"]

    # create median RT variables
    medianRT_all = correctTrials_all.median() * 1000
    medianRT_congruent = correctTrials_congruent.median() * 1000
    medianRT_incongruent = correctTrials_incongruent.median() * 1000
    medianRT_cost = medianRT_incongruent - medianRT_congruent

    # create accuracy variables
    accuracy_all = task["myExp.Accuracy"].sum()
    accuracy_all_pct = accuracy_all / total_trials * 100
    accuracy_congruent = task.loc[(task['myExp.congruent'] == 1), "myExp.Accuracy"].sum()
    accuracy_congruent_pct = accuracy_congruent / congruent_num * 100
    accuracy_incongruent = task.loc[(task['myExp.congruent'] == 0), "myExp.Accuracy"].sum()
    accuracy_incongruent_pct = accuracy_incongruent / incongruent_num * 100

    # append data
    flanker_dataList.append({'participant': task.iloc[1]["participant"],
                      'RT_all(ms)': medianRT_all,
                      'RT_congruent(ms)': medianRT_congruent,
                      'RT_incongruent(ms)': medianRT_incongruent,
                      'RT_cost(ms)': medianRT_cost,
                      'accuracy_all(num)': accuracy_all,
                      'accuracy_congruent(num)': accuracy_congruent,
                      'accuracy_incongruent(num)': accuracy_incongruent,
                      'accuracy_all(%)': accuracy_all_pct,
                      'accuracy_congruent(%)': accuracy_congruent_pct,
                      'accuracy_incongruent(%)': accuracy_incongruent_pct})

flankerData_long = pd.DataFrame(flanker_dataList)

# save dataframe as .csv
flankerData_long.to_csv('flanker_longFormat.csv',index=False)