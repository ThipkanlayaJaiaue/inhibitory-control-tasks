# **Go/No-Go Task**


## 🔧 Task setup and modification (user-friendly guide)


Each task includes:

1\. Instructions

2\. A practice block

3\. An experimental block


### 1. Both Practice and Experimental Blocks


**1.1 Stimulus Sequences Control**

Practice block

- Stimuli controlled in the *End Routine* of practStimuli_sequenceGeneration component; Location: `practStimuliSequenceGeneration`
- No-Go letter controlled in the *End Routine* of practLetter_sequenceGeneration component; Location: `practLetterSequenceGeneration`

Experimental block

- Stimuli controlled in the *End Routine* of expStimuli_sequenceGeneration component; Location:  `expStimuli_sequenceGeneration`
- No-Go letter controlled in the *End Routine* of expLetter_sequenceGeneration component; Location: `expLetterSequenceGeneration`

> 🧩 Within these components, you can manipulate task parameters under the following sections:


**a. Trial Numbers**

- Total trial number (trialAll_num) ⚠️ Please note that a higher number of trials may result in longer sequence generation times due to strict constraints.

**b. Assign Stimuli Pool** ⚠️ Match the stimulus pool with the No-Go letter pool


**c. Assign Response Keys**: set the allowedKeys field of the xTrial_key component in `practiceTrial` and `experimentalTrial`


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

Data collected from each task can be processed using *processGoNogo.py*
⚠️ Make sure the list of folder paths (line 7) is updated to match the location of your data folder.

