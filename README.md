# Sonifile
This is the repository for our HCI coursework.

# How to run the code
Users must have the sounddevice library installed - pip install sounddevice

The sonifile_prototype.py file has all the relevant functions in the class HelloMagics.  

The below commands must be executed in a Jupyter Notebook cell:


%load_ext autoreload

%autoreload 2

%run sonifile_prototype.py

%reload_ext sonifile_prototype

%select_from_dummy_folder


These can also be found in testing_env.IPYNB.  We have supplied a dummy folder structure, TestProject, a user is able to demo our implementation by opening testing_env in a Jupyter Notebook.  They then must run the first cell, once they input a suitable file, they will be returned with an audio cue indicating the file size and the distance it is form the current file. The user must enter "stop" if they want to close the application.
