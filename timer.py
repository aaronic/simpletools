# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 09:06:57 2018

@author: ASUS
"""

from datetime import datetime
from datetime import timedelta
import time

def date(fmt='%Y-%m-%d'):
    return datetime.strftime(datetime.today(), fmt)

def now(fmt='%Y-%m-%d %H:%M:%S'):
    return datetime.strftime(datetime.now(), fmt)

def h_m_s(fmt='%H:%M:%S'):
    return datetime.strftime(datetime.now(), fmt)

def ticktock(seconds=1):
    time.sleep(seconds)
        
class hourReminder:
    ''' accept a list of string time composed of hour/minute/second
        so every day once the time reach the user defined hour/min/sec, it will return true
    '''
    def __init__(self, times=[]):
        self.reminderTimes = times
        self.now = datetime.today()
    
    def refresh(self):
        self.now = datetime.today()
        
    def getDate(self, fmt='%Y-%m-%d'):
        self.refresh()
        return datetime.strftime(self.now, fmt)
    
    def monitor(self, times=[], deltaHours=0, deltaMinutes=0, deltaSeconds=0, dateFmt='%Y-%m-%d', timeFmt='%H:%M:%S'):
        ''' monitor if the current time reach the time in the times[] list
            intervalSeconds - if it is not 0, will monitor times[] + intervalSeconds
            e.g. times=['09:00:00'], intervalSeconds=60, it will return True for 09:01:00,09:02:00....
        '''
        if times:
            self.reminderTimes = times
        elif self.reminderTimes:
            pass
        else:
            raise Exception('Need a check time')
        date = self.getDate(dateFmt)
        for t in self.reminderTimes:
            time_check = date + ' ' + t
            time_check = datetime.strptime(time_check, dateFmt+' '+timeFmt)
            time_check +=timedelta(hours=deltaHours, minutes=deltaMinutes, seconds=deltaSeconds)
            self.refresh()
            diff = self.now - time_check
            diff_sec = diff.seconds
            if diff.days < 0:
                diff_sec = diff.days*3600*24 + diff.seconds
            #print('TIME_CHECK - {} , NOW - {}'.format(time_check, datetime.strftime(self.now, '%Y-%m-%d %H:%M:%S')))
            if 1 >= diff_sec >= 0:
                print('ALERT: TIME_CHECK - {} , NOW - {}'.format(time_check, self.now))
                return True
        return False
    
'''
start_1 = '11:37:00'
start_2 = '11:38:12'
end = '11:08:00'
hr = hourReminder()
cnt = 0
while(1):
    if hr.monitor(times=[start_1, start_2]):
        cnt = 0
    if hr.monitor(times=[start_1, start_2],deltaSeconds=5*cnt):
        cnt +=1
        pass
    
    time.sleep(1)
    if hr.monitor(times=[start_1], deltaMinutes=1):
        cnt = 0
    if hr.monitor(times=[start_1], deltaMinutes=3):
        break
'''