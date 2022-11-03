__author__ = 'nickdg'
from psychopy import visual, core
import pdb

class CountdownTimerStim(visual.TextStim):

    def __init__(self, start_time, *args, **kwargs):
        """
        Make visual.TextStim that is combined with a core.CountdownTimer.  Displays a timer that automatically updates.
        CountdownTimerStim(start_time, window, [optional arguments from TextStim])
         Example:
            from psychopy import visual
            from psytimer import CountdownTimerStim

            win = visual.Window()
            time_text = CountdownTimerStim(62, win)

            while time_text.getTime() > 0:
                time_text.draw()
                win.flip()
            win.close()
        """

        super(CountdownTimerStim, self).__init__(*args, **kwargs)

        self.__start_time = start_time
        self.__timer = core.CountdownTimer(self.__start_time)

    def draw(self, *args, **kwargs):
        """Draws the stimulus.  Can supply a Window if another window should be used."""
        secsleft = self.__timer.getTime()
        str_fmt = "%(mins)02d:%(secs)02d" % {'mins': secsleft // 60, 'secs': secsleft % 60}  # Make it look like a timer
        self.setText(str_fmt)
        super(CountdownTimerStim, self).draw(*args, **kwargs)

    def reset(self, *args, **kwargs):
        """Reset clock time."""
        self.__timer.reset(*args, **kwargs)

    def getTime(self, *args, **kwargs):
        """Returns the current time on the clock, in seconds."""
        return self.__timer.getTime(*args, **kwargs)
        #return aa

    def add(self, *args, **kwargs):
        """Add some time on the clock"""
        return self.__timer.add(*args, **kwargs)

