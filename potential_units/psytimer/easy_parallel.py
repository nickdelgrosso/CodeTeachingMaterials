__author__ = 'nickdg'

import psychopy
import time

class ParallelPort(object):

    def __init__(self, address=0x0378, testing=False):
        """Makes an easier-to-use, if slightly less flexible, parallel port object for
        easy trigger sending (automatically sets things back to 0 and handles the pauses
        for good message sending!) and debugging (if testing=True, will simply print
        trigger messages to the console instead of connecting to the parallel port.
        """
        self.port = None
        self.testing = testing
        if not testing:
            self.port = psychopy.parallel.ParallelPort(address=address)

    def send_trigger(self, value, sleep_time=.02):
        """Sends a trigger via the parallel port. Does all resetting things back to 0 and pausing automatically."""

        if not self.testing:

            # Reset parallel port
            self.port.setData(0)
            time.sleep(sleep_time)  # Wait .02 seconds for parallel port to respond correctly

            # Set parallel port to trigger value
            self.port.setData(value)  # Set Parallel port to trigger value.
            time.sleep(sleep_time)  # Wait .02 seconds for parallel port to respond correctly

            # Reset parallel port again
            self.port.setData(0)

        print("Sent Trigger to Parallel Port: {0}".format(value))



