__author__ = 'ella'

from psychopy import visual, core
from psychopy import data

win = visual.Window(fullscr=False)

word_text = visual.TextStim(win, text='Gleich geht es los!', pos=(0.0, 0.25), alignHoriz='center',
                            color=(1.0, 1.0, 1.0))
word_text2 = visual.TextStim(win, text='Gleich beginnt die Ruheaufzeichnung', pos=(0.0, 0.25), alignHoriz='center',
                            color=(1.0, 1.0, 1.0))
word_text3 = visual.TextStim(win, text='Gleich beginnen die nächsten 9 Minuten Zeitfahren', pos=(0.0, 0.25), alignHoriz='center',
                            color=(1.0, 1.0, 1.0))

time_text = CountdownTimerStim(10, win, pos=(0.0, -0.4), color=(0.5, 1.0, 0.0))

stim_order = [{'time': 540, 'message': 'X', 'message2':True, 'message3':False},
              {'time': 60, 'message': 'X', 'message2':False, 'message3':False},
                {'time':10,'message': 'X', 'message2':False, 'message3':True}]

trials = data.TrialHandler(stim_order, nReps=5, method='sequential')

for trial in trials:

    word_text.setText(trial['message'])
    time_text.reset(trial['time'])

    while time_text.getTime() > 0:

        # Draw the sentence onscreen.  (won't display until win.flip() is called)
        word_text.draw()

        # Draw the timer. (Will automatically update and format itself correctly)
        time_text.draw()

        if time_text.getTime() < 30 and trial['message2'] == True:
            word_text2.draw()

            if time_text.getTime() <10 and trial['message3'] == True:
                word_text3.draw()

        # Update the window, so everything is drawn onscreen!
        win.flip()

win.close()



