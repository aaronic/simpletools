import os
import argparse

command_runner = argparse.ArgumentParser(description='Traverse current path and run the specific command')
command_runner.add_argument('--cmd', dest='cmd',action='store',help='user command')
args = command_runner.parse_args()
print('CMD: {}'.format(args.cmd))

current_path = os.getcwd()
folders = [folder for folder in os.listdir(current_path) if os.path.isdir(folder)]

for folder in folders:
    os.chdir(os.path.join(current_path, folder))
    os.system(args.cmd)
    #print(os.getcwd())
