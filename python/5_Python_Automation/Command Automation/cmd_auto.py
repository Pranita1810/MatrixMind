# COMMAND TERMINAL AUTOMATION 

# import subprocess
# subprocess.run("docker ps -a", shell=True) # Run any command 
# r = subprocess.run("docker ps -a", shell=True, capture_output=True) # Capture the output in a variable
# subprocess.Popen("docker images") # This run any command in backgroung
# subprocess.run(["python" , "xcmd_auto.py"]) # We can also run python from python it self, but this will create an infinite loop.

"""
Task : Create a automated process that will chekc if the docker is running or not if not than run  the docker 
also if there is no container also run the container
"""

import subprocess
import time


class AutoDockerProcesser:

    def __init__(self):
        self.check_docker()

    def check_docker(self):
        result = subprocess.run(
            ["docker", "info"],
            capture_output=True,
            text=True)
        if result.returncode != 0:
            print("Docker is not running.")
            self.start_docker()
        else:
            print("Docker is running.")

    def start_docker(self):
        subprocess.Popen(
            [
                "C:\\Program Files\\Docker\\Docker\\Docker Desktop.exe"
            ]
        )
        print("Starting Docker Desktop...")
        # Docker Desktop needs time to start
        time.sleep(10)
        self.check_docker()

x = AutoDockerProcesser()