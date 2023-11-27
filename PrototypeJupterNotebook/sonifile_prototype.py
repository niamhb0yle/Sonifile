import sounddevice as sd
import numpy as np
import time
import os
from IPython.core.magic import Magics, magics_class, line_magic
fileDict = {}

@magics_class
class HelloMagics(Magics):
    @line_magic
    def play_file_size(self,file_size_mbytes):
        sd.play(file_size_mbytes * np.sin(0.1*np.arange(176400/3)), 44000) #the second parameter is the pitch
        
    fileDict = {}
    @line_magic
    def list_directory_tree_with_indentation(self,directory, indent=0):
        global fileDict
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                counter = 0
                print(f"{'  ' * indent}File: {item}")
                #fileDict[item] = item_path#.split('\\')
                try:
                    f = open(item_path, "r")
                    fileDict[item] = item_path
                except:
                    pass
    #             fileList = item_path.split('\\')
    #             fileDict[fileList[-1]] = 0
            elif os.path.isdir(item_path):
                print(f"{'  ' * indent}Directory: {item}")
                HelloMagics.list_directory_tree_with_indentation(self, item_path, indent+1)

                
    #list_directory_tree_with_indentation("C:")
    #print(fileDict)
    @line_magic
    def select_from_dummy_folder(self, init):
        global fileDict
        HelloMagics.list_directory_tree_with_indentation(self,os.getcwd(), 0)
        file_size_dict = {}
        for i in fileDict:
            counter = 0 
            f = open(fileDict[i], 'r')
            try:

                while f.readline() != "":
                    counter = counter +1
                    try:
                        f.readline()
                    except:
                        break
            except:
                #print("file wont open")
                pass
            file_size_dict[i] = counter
            print(i)#,fileDict[i], counter)
        user_input = input("Select a file")
        while user_input != "stop":
            if user_input in fileDict:
                size = (file_size_dict[user_input]) / 100
                if (len(fileDict[user_input].split('\\'))) == 1:
                    HelloMagics.play_file_size(self,size)
                else:
                    for x in range (len(fileDict[user_input].split(os.getcwd())[1].split('\\'))):
                        print(fileDict[user_input].split(os.getcwd())[1].split('\\')[x])
                        HelloMagics.play_file_size(self,size)
                        time.sleep(0.3)
            else:
                print("File not found. Please try again.")
            user_input = input("Select a file")


def load_ipython_extension(ipython):
    """Load the extension in IPython."""
    ipython.register_magics(HelloMagics)