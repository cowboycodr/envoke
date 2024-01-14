import pyautogui
import time
import random

class Conjure:
    """ 
    A class to create and run keyboard macros with optional delays and randomness.
    """
    
    def __init__(self, start_delay=0):
        """
        Initialize the Conjure macro creator.
        
        :param start_delay: Delay in seconds before the macro starts running.
        """
        self.sequence = []
        self.start_delay = start_delay

    def __getattr__(self, key):
        """
        Magic method to add a key with a delay to the macro sequence.
        Allows using attribute style for key names.

        :param key: Key name as a string.
        """
        return lambda interval=0.1, interval_diff=0: self._add_key(key, interval, interval_diff)

    def key(self, key_value, interval=0.1, interval_diff=0):
        """
        Method to add a single key press to the macro sequence.

        :param key_value: Key name as a string.
        :param interval: Time in seconds to wait after this key press.
        :param interval_diff: Random deviation for the interval.
        """
        self._add_key(key_value, interval, interval_diff)

    def keys(self, key_values, interval=0.1, interval_diff=0):
        """
        Method to add multiple key presses to the macro sequence.

        :param key_values: List of key names.
        :param interval: Time in seconds to wait after each key press.
        :param interval_diff: Random deviation for the interval.
        """
        for key_value in key_values:
            self._add_key(key_value, interval, interval_diff)

    def _add_key(self, key, interval, interval_diff):
        """
        Private method to add a key with interval and random deviation to the sequence.

        :param key: Key name as a string.
        :param interval: Time in seconds to wait after the key press.
        :param interval_diff: Random deviation for the interval.
        """
        actual_interval = max(0, interval + random.uniform(-interval_diff, interval_diff))
        self.sequence.append((key, actual_interval))
        return self

    def run(self, repeat=1, continuous=False):
        """
        Run the macro sequence.

        :param repeat: Number of times to repeat the sequence.
        :param continuous: If True, run the sequence continuously.
        """
        time.sleep(self.start_delay)
        while True:
            for key, interval in self.sequence:
                pyautogui.press(key)
                time.sleep(interval)
            if not continuous:
                repeat -= 1
                if repeat <= 0:
                    break

def conjure(start_delay=0):
    """
    Factory function to create a Conjure instance.

    :param start_delay: Delay in seconds before the macro starts running.
    :return: Instance of Conjure.
    """
    return Conjure(start_delay)