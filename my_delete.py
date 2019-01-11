import os
import time
path = r'C:\Users\22222\ProgramFile\SogouInput\8.9.0.2130'
while(True):
    files = os.listdir(path)
    for file_ in files:
        #print(file_)
        if 'SGDownload.exe' in file_:
            print('found and delete {}'.format(file_))
            os.remove(os.path.join(path,file_))
        if 'SohuNews.exe' in file_:
            print('found and delete {}'.format(file_))
            os.remove(os.path.join(path,file_))
    time.sleep(5)
