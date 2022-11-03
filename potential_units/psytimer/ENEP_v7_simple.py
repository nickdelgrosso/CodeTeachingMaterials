__author__ = 'ella'

import time
from psychopy import visual, core, event, data
from psytimer import CountdownTimerStim
from easy_parallel import ParallelPort

# Connect to parallel port
port = ParallelPort(address=0x0378, testing=True)  # Set testing to False to actually send triggers.

# Create Window
win = visual.Window(color=(-1, -1, -1), colorSpace='rgb', fullscr=False)

# Create Text Stimuli (visual.TextStim, from psychopy)
word_text = visual.TextStim(win, text='', pos=(0.0, 0.25), alignHoriz='center', color=(1.0, 1.0, 1.0))  # text set later
timer_text = CountdownTimerStim(1111, win, pos=(0.0, -0.4), color=(0.0, 1.0, 0.0))  # Random time, set later.


# Create Trial Variables (
stim_order = [{'time': 10, 'trigger': 50, 'message': 'Gleich geht es los!'},  # Pedal Phase (phase number: 0)
              {'time': 7, 'trigger': 60, 'message': 'Gleich beginnt die Ruheaufzeichnung'}   # Rest Phase  (phase number: 1)
              ]

trials = data.TrialHandler(stim_order, nReps=2, method='sequential')


# Display a "Press Space to Start" Message before beginning
word_text.setText("Press Space key to Continue")
while not 'space' in event.getKeys():
    word_text.draw()
    win.flip()


# Run the Trials (this is the main experiment loop)
for trial in trials:

    # Send triggers to the parallel port for the EEG system
    port.send_trigger(trials.thisRepN + 1)  # Current trial number
    port.send_trigger(trial['trigger'])  # Current phase number

    # Reset the text for the new phase.
    timer_text.reset(trial['time'])
    word_text.setText(trial['message'])

    # Update the window an until timer_text.getTime() reaches 0.
    while timer_text.getTime() > 0:

        # Update the window
        timer_text.draw()
        word_text.draw()
        win.flip()

        # Check the keyboard to see if anything was pressed recently.
        if 'escape' in event.getKeys():  # Check if 'escape' key pressed, for window close ("hard exit")
            core.quit()


# Once everything has completed, close the window!
win.close()






