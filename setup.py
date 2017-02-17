from cx_Freeze import setup, Executable

buildOptions = dict(include_files = ['src/GUI'])
setup(
    name = "WoWTime" ,
    version = "0.1" ,
    description = " " ,
    executables = [Executable("src/main.py")] , )