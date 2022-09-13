import os
import sys
import shutil

current_folder = str(os.path.dirname(os.path.abspath(sys.argv[0]))).replace('\\', "/") + "/"
appdata_folder = os.path.expandvars('%appdata%').replace(r"\Roaming", "").replace('\\', "/") + "/"
python_folder = appdata_folder + "Local/Programs/Python/"


for file in os.listdir(python_folder):
    if "Python" in file:
        python_folder = python_folder + file + "/Lib/"

 
shutil.move(current_folder + "userfiles.py", python_folder + "userfiles.py")

input("Installed package")
