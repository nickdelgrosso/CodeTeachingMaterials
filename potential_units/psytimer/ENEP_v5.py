__author__ = 'ella'

from psychopy import visual, core, event, data#, parallel
from psytimer import CountdownTimerStim

# Connect to parallel port
#port = parallel.ParallelPort(address=0x0378)

# Create Window
win = visual.Window(color=(-1, -1, -1), colorSpace='rgb', fullscr=False)

# Create Text Stimuli (visual.TextStim, from psychopy)
word_text = visual.TextStim(win, text='', pos=(0.0, 0.25), alignHoriz='center', color=(1.0, 1.0, 1.0))  # text set later
timer_text = CountdownTimerStim(1111, win, pos=(0.0, -0.4), color=(0.0, 1.0, 0.0))  # Random time, set later.


# Create Trial Variables (
stim_order = [{'pedal_time': 10,
               'rest_time': 8,
               'start_pedal_trig': 50,
               'start_rest_trig': 60}]

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


def send_trigger(value):
    """Sends a trigger via the parallel port. Does all resetting things back to 0 and pausing automatically."""
    #port.setData(0)  # Reset parallel port
    #time.sleep(.02)  # Wait .02 seconds for parallel port to respond correctly
    #port.setData(value)  # Set Parallel port to trigger value.
    print("Sent Trigger to Parallel Port: {0}".format(value))
    #time.sleep(.02)  # Wait .02 seconds for parallel port to respond correctly
    #port.setData(0)  # Reset parallel port again (the first time was probably unnecessary, but caution is nice to have.)



# Run the Trials (this is the main experiment loop)
for trial in trials:

    # Send a trigger to the EEG system with the current trial number (could be useful for later)
    send_trigger(trials.thisN + 1)  # Send trial number as a trigger.

    ###############
    # Pedal Phase #
    ###############
    timer_text.reset(trial['pedal_time'])
    beginning_of_phase = True
    while timer_text.getTime() > 0:

        if beginning_of_phase:
            send_trigger(trial['start_pedal_trig'])
            beginning_of_phase = False

        # Decide which message to show, based on the time remaining on the timer.
        if timer_text.getTime() > 3:
            word_text.setText('Gleich geht es los!')
        else:
            word_text.setText('Fast fertig!')  # For all other times not included in above cases

        # Update the onscreen text and check the keyboard events
        update_window_and_keyboard()


    ##############
    # Rest Phase #
    ##############
    timer_text.reset(trial['rest_time'])
    beginning_of_phase = True
    while timer_text.getTime() > 0:

        if beginning_of_phase:
            send_trigger(trial['start_rest_trig'])
            beginning_of_phase = False

        # Decide which message to show, based on the time remaining on the timer.
        if timer_text.getTime() > 4:
            word_text.setText('Gleich beginnt die Ruheaufzeichnung')
        elif timer_text.getTime() > 0:  # Another way for specifying times. elif means "else if" and works the same as "if" statements
            word_text.setText('Gleich beginnt das naechste Zeitfahren')

        # Update the onscreen text and check the keyboard events
        update_window_and_keyboard()


# Once everything has completed, close the window!
win.close()






