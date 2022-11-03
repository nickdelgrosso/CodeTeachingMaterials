__author__ = 'nickdg'
from psychopy import visual, core
from psytimer import CountdownTimerStim  # Make sure psytimer.py is in the same folder, for now.

# Create Window to display things in. Careful, if you set fullscr to True, you might not
# Be able to get rid of it!
win = visual.Window(fullscr=False)

# Create a Psychopy TextStim that displays your Text Sentence
word_text = visual.TextStim(win, text='Pedal!', pos=(0.0, 0.25), alignHoriz='center',
                            color=(1.0, 1.0, 1.0))

# Create your custom CountdownTimerStim.  This will automatically display a timer onscreen,
# and, except for putting the window as the second argument,
# works exactly the same as Psychopy's TextStim otherwise.
time_text = CountdownTimerStim(62, win, pos=(0.0, -0.4), color=(0.5, 1.0, 0.0))

# Start a timer.  We'll use this one to decide when to move on past the while loop.
window_timer = core.CountdownTimer(6)

# Start the loop
while window_timer.getTime() > 0:  # Check to see if the window_timer is negative yet.

    # Draw the sentence onscreen.  (won't display until win.flip() is called)
    word_text.draw()

    # Draw the timer. (Will automatically update and format itself correctly)
    time_text.draw()

    # Update the window, so everything is drawn onscreen!
    win.flip()


# Now that the while loop is finished, close the window.
win.close()