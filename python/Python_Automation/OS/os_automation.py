# OS AUTOMATION PROJECT
"""
Task : Create a folder x and backup all csv file as they arrive in a folder y 

"""
import os 
import shutil
import time

source_x = "From"
backup_y = "To"

os.makedirs(source_x, exist_ok=True)
os.makedirs(backup_y, exist_ok=True)

while True:
    for file in os.listdir(source_x):
        if file.endswith(".csv"):
            source_file = os.path.join(source_x, file)
            backup_file = os.path.join(source_x, file)

            shutil.copy(source_file, backup_file)

            print(f"Backup File Created : {file}")
    time.sleep(5)