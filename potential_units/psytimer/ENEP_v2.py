__author__ = 'ella'

from psychopy import visual, core
from psychopy import data
from psytimer import CountdownTimerStim

win = visual.Window(color=(-1,-1,-1),colorSpace='rgb', fullscr=False)

word_text = visual.TextStim(win, text='Gleich geht es los!', pos=(0.0, 0.25), alignHoriz='center',
                            color=(1.0, 1.0, 1.0))
word_text2 = visual.TextStim(win, text='Gleich beginnt die Ruheaufzeichnung', pos=(0.0, 0.25), alignHoriz='center',
                            color=(1.0, 1.0, 1.0))
word_text3 = visual.TextStim(win, text='X', pos=(0.0, 0.25), alignHoriz='center',
                            color=(1.0, 1.0, 1.0))							
word_text4 = visual.TextStim(win, text='Gleich beginnt das naechste Zeitfahren', pos=(0.0, 0.25), alignHoriz='center',
                            color=(1.0, 1.0, 1.0))

time_text = CountdownTimerStim(62, win, pos=(0.0, -0.4), color=(0.0, 1.0, 0.0))
time_text2 = CountdownTimerStim(62, win, pos=(0.0, -0.4), color=(-1.0, -1.0, -1.0))

window_timer = core.CountdownTimer(6)


stim_order = [{'time': 35, 'message':'', 'message2': True, 'message3': False, 'message4':False},
			{'time': 20, 'message':'', 'message2': False, 'message3': True, 'message4':False},
			{'time': 10,'message':'', 'message2': False, 'message3': False, 'message4':True}]

trials = data.TrialHandler(stim_order, nReps=1, method='sequential')

for trial in trials:
	word_text.setText(trial['message'])
	word_text2.setText(trial['message2'])
	word_text3.setText(trial['message3'])
	word_text4.setText(trial['message4'])
	time_text.reset(trial['time'])
	time_text2.reset(trial['time'])

	while time_text.getTime() > 0:
        # Draw the sentence onscreen.  (won't display until win.flip() is called)
		word_text.draw()
			# Draw the timer. (Will automatically update and format itself correctly)
		time_text.draw()
	
		if time_text.getTime() < 30 and trial['message2'] == True:
			word_text2.draw()
			time_text2.draw()
		
			if time_text.getTime() <20 and trial['message3'] == True:
				word_text3.draw()
				time_text2.draw()
			
				if time_text.getTime() <10 and trial['message4'] == True:
					word_text4.draw()
					time_text2.draw()
	
        # Update the window, so everything is drawn onscreen!

win.flip()

win.close()



