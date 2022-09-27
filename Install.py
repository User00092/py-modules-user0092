import os
import sys
import shutil
os.system("pip install dload")
import dload

class Paths:
    current_folder = str(os.path.dirname(os.path.abspath(sys.argv[0]))).replace('\\', "/") + "/"
    app_data = (str(os.path.expandvars("%APPDATA%")).replace(r"\Roaming", "")).replace('\\', '/') + '/'
    python_lib = app_data + "Local/Programs/Python/"

    for file in os.listdir(python_lib):
        if "Python" in file:
            python_lib = python_lib + file + "/Lib/"
            
            
def get_userfiles():
    python_path = Paths.python_lib
    dload.save_unzip("https://codeload.github.com/User00092/py-modules-user0092/zip/refs/heads/main", Paths.current_folder)
    shutil.move(Paths.current_folder + "py-modules-user0092-main/userfiles.py", Paths.python_lib)
    shutil.rmtree(Paths.current_folder + "py-modules-user0092-main")
    os.remove(Paths.current_folder + "main")


if __name__ == "__main__":
    get_userfiles()
