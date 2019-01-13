# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 16:47:16 2018

@author: ASUS
"""


import sys

"""
text = None
if len(sys.argv) > 1:
    text = ' '.join(sys.argv[1:])
else:
    text = 'Please input the text'

''' not so good choice
'''
import win32com.client
speaker = win32com.client.Dispatch('SAPI.SpVoice')
speaker.Speak(text)




'''
import pyttsx3
engine = pyttsx3.init() # get engine
engine.say(text)
engine.runAndWait()
'''
"""

import win32com.client

class sayer:
    def __init__(self):
        self.speaker = win32com.client.Dispatch('SAPI.SpVoice')
    def say(self, msg, repeat=1, logger=None):
        for i in range(repeat):
            if logger:
                logger.info('Say "{}"'.format(msg))
            self.speaker.Speak(msg)

def say(msg, repeat=1):
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    for i in range(repeat):
        speaker.Speak(msg)