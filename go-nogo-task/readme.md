# **Go/No-Go Task**

This task includes: instructions, a practice block, and an experimental block


### ⚙️ **Familiarisation**

* Complete 20 trials assessing response inhibition by responding to Go letters and withholding responses to the designated No-Go letter.
* One block of 20 trials, preceded by a 2000-ms instruction screen indicating the designated No-Go letter, selected from a pool of five letters (A–E)
* Trial sequence: Fixation cross (500–700 ms), followed by a letter (1000 ms).
* Trial composition: 80% Go and 20% No-Go trials, presented in random order, with each letter appearing in 20% of trials.
* Repeat until participants achieve ≥70% accuracy overall and ≥70% correct response inhibition.

### ⚙️ **Experimental Task**

* Five blocks of 60 trials, separated by 2000-ms interruptions to indicate the designated No-Go letter, selected from a pool of five letters (A–E).
* Trial sequence: Fixation cross (450–700 ms), followed by a letter (1000 ms).
* Trial composition: 80% Go and 20% No-Go trials, presented in random order, with each letter appearing in 20% of trials.

---

## 🔧 Task setup and modification (user-friendly guide)

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

