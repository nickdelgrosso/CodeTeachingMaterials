__author__ = 'ella'

from psychopy import visual, core, event
from psychopy import data
from psytimer import CountdownTimerStim

# Create Window
win = visual.Window(color=(-1,-1,-1), colorSpace='rgb', fullscr=False)

# Create Text Stimuli (visual.TextStim, from psychopy)
word_text = visual.TextStim(win, text='', pos=(0.0, 0.25), alignHoriz='center', color=(1.0, 1.0, 1.0))  #text set later.
timer_text = CountdownTimerStim(1111, win, pos=(0.0, -0.4), color=(0.0, 1.0, 0.0))  #Random time, set later.


# Create Trial Variables (
stim_order = [{'pedal_time': 10,
               'rest_time': 8}]
trials = data.TrialHandler(stim_order, nReps=1, method='sequential')

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

        # Update the onscreen text
        timer_text.draw()
        word_text.draw()
        win.flip()



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

        # Update the onscreen text
        timer_text.draw()
        word_text.draw()
        win.flip()


win.close()



