
from cx_Freeze import setup, Executable
import sys

path = sys.path
includefiles = []
includes = []
excludes = []
packages = ["module/"]

base = "Win32GUI" # pour application graphique sous Windows

options = {
    'include_files': includefiles,
    'includes': includes,
    'excludes': excludes,
    'packages': packages
}

setup(
    name = "Convertisseur de PDF",
    options = {'build_exe': options},
    version = "0.1",
    description = "Convertisseur de fichier tif ou jpeg en pdf avec  choix du format",
    executables = [Executable("main.py", base=base)])

# python setup.py build     
