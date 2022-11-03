__author__ = 'ella'

from psychopy import visual, core, event
from psychopy import data
from psytimer import CountdownTimerStim

# Create Window
win = visual.Window(color=(-1, -1, -1), colorSpace='rgb', fullscr=False)

# Create Text Stimuli (visual.TextStim, from psychopy)
word_text = visual.TextStim(win, text='', pos=(0.0, 0.25), alignHoriz='center', color=(1.0, 1.0, 1.0))  # text set later
timer_text = CountdownTimerStim(1111, win, pos=(0.0, -0.4), color=(0.0, 1.0, 0.0))  # Random time, set later.


# Create Trial Variables (
stim_order = [{'pedal_time': 10,
               'rest_time': 8}]
trials = data.TrialHandler(stim_order, nReps=2, method='sequential')


# Create a function for updating everything (so we can just call the function instead of typing things up every time)
def update_everything():
    timer_text.draw()
    word_text.draw()
    win.flip()

    # Check the keyboard to see if anything was pressed recently.
    if 'escape' in event.getKeys():  # Check if 'escape' key pressed, for window close ("hard exit")
        core.quit()

# Run the Trials (this is the main experiment loop)
for trial in trials:

    ###############
    # Pedal Phase #
    ###############
    timer_text.reset(trial['pedal_time'])
    while timer_text.getTime() > 0:

        # Decide which message to show, based on the time remaining on the timer.
        if timer_text.getTime() > 3:
            word_text.setText('Gleich geht es los!')
        else:
            word_text.setText('Fast fertig!')  # For all other times not included in above cases

        # Update the onscreen text and check the keyboard events
        update_everything()

    ##############
    # Rest Phase #
    ##############
    timer_text.reset(trial['rest_time'])
    while timer_text.getTime() > 0:

        # Decide which message to show, based on the time remaining on the timer.
        if timer_text.getTime() > 4:
            word_text.setText('Gleich beginnt die Ruheaufzeichnung')
        elif timer_text.getTime() > 0:  # Another way for specifying times. elif means "else if" and works the same as "if" statements
            word_text.setText('Gleich beginnt das naechste Zeitfahren')

        # Update the onscreen text and check the keyboard events
        update_everything()


# Once everything has completed, close the window!
win.close()






