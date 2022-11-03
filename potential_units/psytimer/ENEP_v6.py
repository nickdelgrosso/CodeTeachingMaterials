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
stim_order = [{'time': 10, 'trigger': 50},  # Pedal Phase (phase number: 0)
              {'time': 7, 'trigger': 60}   # Rest Phase  (phase number: 1)
              ]

trials = data.TrialHandler(stim_order, nReps=2, method='sequential')


# Create some custom functions, for easily performing a set of actions.
def update_window_and_keyboard():
    """Updates the window, draws the text, and checks the keyboard."""
    timer_text.draw()
    word_text.draw()
    win.flip()

    # Check the keyboard to see if anything was pressed recently.
    if 'escape' in event.getKeys():  # Check if 'escape' key pressed, for window close ("hard exit")
        core.quit()


# Run the Trials (this is the main experiment loop)
for trial in trials:

    # Send triggers to the parallel port for the EEG system
    port.send_trigger(trials.thisN + 1)  # Current trial number
    port.send_trigger(trial['trigger'])  # Current phase number

    timer_text.reset(trial['time'])
    while timer_text.getTime() > 0:

        # Decide which message to show, based on the phase number and the time remaining on the timer.
        if trials.thisTrialN == 0:  #
            if timer_text.getTime() > 3:
                word_text.setText('Gleich geht es los!')
            else:
                word_text.setText('Fast fertig!')  # For all other times not included in above cases

        elif trials.thisTrialN == 1:
            if timer_text.getTime() > 4:
                word_text.setText('Gleich beginnt die Ruheaufzeichnung')
            elif timer_text.getTime() > 0:  # Another way for specifying times. elif means "else if" and works the same as "if" statements
                word_text.setText('Gleich beginnt das naechste Zeitfahren')

        # Update the onscreen text and check the keyboard events
        update_window_and_keyboard()


# Once everything has completed, close the window!
win.close()






