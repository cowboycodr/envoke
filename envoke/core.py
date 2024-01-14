import pyautogui
import time
import random

class Envoke:
    """ 
    A class to create and run keyboard macros with optional delays and randomness.
    """
    
    def __init__(self):
        """
        Initialize the Envoke macro creator.
        
        :param start_delay: Delay in seconds before the macro starts running.
        """
        self.sequence = []

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

    def run(self, repeat=1, continuous=False, start_delay=0):
        """
        Run the macro sequence.

        :param repeat: Number of times to repeat the sequence.
        :param continuous: If True, run the sequence continuously.
        :param start_delay: Delay in seconds before the macro starts running.
        """

        while True:
            for key, interval in self.sequence:
                time.sleep(interval)
                pyautogui.press(key)
            if not continuous:
                repeat -= 1
                if repeat <= 0:
                    break

def envoke():
    """
    Factory function to create a Envoke instance.

    :return: Instance of Envoke.
    """
    return Envoke()