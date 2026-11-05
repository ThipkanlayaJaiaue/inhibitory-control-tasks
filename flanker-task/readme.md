# **Flanker Task**


This task consisted of a familiarisation block followed by an experimental task.

### ⚙️ **Familiarisation**

* Complete 20 trials identifying the direction of the central arrow while ignoring flanking distractors.
* Trial sequence: Fixation cross (500–700 ms) followed by a horizontal array of five arrows (1000 ms).
* Trial composition: 80% congruent and 20% incongruent, presented in random order.
* Repeat until ≥70% accuracy.

### ⚙️ **Experimental Task**
- One uninterrupted block of 300 trials.
- Trial sequence: Fixation cross (450–700 ms) followed by a horizontal array of five arrows (1000 ms).
- Trial composition: 80% congruent and 20% incongruent, presented in random order.

---

## 🔧 Task setup and modification (user-friendly guide)


### 1. Both Practice and Experimental Blocks


**1.1 Stimulus Sequences Control**

Practice block

- Controlled in the *End Routine* of practSequenceGeneration component
- Location: `practStimuliSequenceGeneration`

Experimental block

- Controlled in the *End Routine* of expSequenceGeneration component
- Location:  `expStimuliSequenceGeneration`


> 🧩 Within these components, you can manipulate task parameters and predictability under the following sections:


**a. Trial Numbers and Distributions**

- Total trial number (trialAll_num) ⚠️ Please note that a higher number of trials may result in longer sequence generation times due to strict constraints.

- Proportion of trial types (trialCongruent_proportion)


**b. Assign Stimuli Pool**: define stimulus pools (congruent_trials, incongruent_trials)


**c. Assign Response Keys**

- Set response keys for the task 
⚠️ Must also match the allowedKeys field of the xTrial_key component in `practiceTrial` and `experimentalTrial`


**1.2 Data Identification and Recording**
- Controlled in the x_addData component
- Location:  `practiceTrial` or `experimentalTrial`


### 2. Practice Block Settings

**2.1 Feedback for Each Trial**
- Text and colour controlled in the *Begin Routine* of practFB_code component
- Location:  `practiceTrial_feedback`

**2.2 Target Accuracy Threshold**
- Controlled in the *End Routine* of practFB_code2 component
- Location:  `practiceBlock_feedback`

**2.3 Practice Repetition**
- Controlled in the `Num. repeats` field of the `practiceRepetition` loop


---


### 🗃️ **Process the data**

Data collected from each task can be processed using *processFlanker.py*
⚠️ Make sure the list of folder paths (line 6) is updated to match the location of your data folder(s).

