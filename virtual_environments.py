# Virtual environments

# By default packages are installed globally
# Here version management becomes a challenge

# Virtual Environements can be use to contain and manage packages collections
# Just like folder behind the scenes with all your packages

# Creating a virtual environment

# Install virtual environment
# pip install vritualenv

# windows systems
# python -m venv <folder_name>

# OSX/Linux (Bash)
# virtualenv <folder_name>

# Using virtual environment

# Windows systems
# cmd.exe
# <folder_name>\Scripts\Activate.bat

# Powershell
# <folder_name>\Scripts\Activate.ps1

# bash shell
# . ./<folder_name>/Scripts/activate

# OSX/Linux (bash)
# <folder_name>/bin/activate

# Installing package in a virtual environment 
# Its exactly same as the default case

# Install an individual package
# pip install colorama

# install from a list of packages
# pip install -r requirements.txt

# requiremets.txt
# colorama

# PRO TIP
# To create virtual env in windows in vs code type this 'virtualenv venv'

# To get out of the venv just type deactivate in the terminal