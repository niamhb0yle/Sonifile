from IPython.core.magic import Magics, magics_class, line_magic
from IPython.core import magic_arguments
import sounddevice as sd
import numpy as np
import time

@magics_class
class Sonifile(Magics):
    @magic_arguments.magic_arguments()
    @magic_arguments.argument('input_text', type=str, help='Text to reverse')
    @line_magic
    def reverse(self, line):
        """Reverse the input text."""
        args = magic_arguments.parse_argstring(self.reverse, line)
        reversed_text = args.input_text[::-1]
        self.shell.set_next_input(reversed_text, replace=True)
    def play_file_size(file_size_mbytes):
        sd.play(file_size_mbytes * np.sin(0.1*np.arange(176400/3)), 44100)
    
    
    

def load_ipython_extension(ipython):
    ipython.register_magics(Sonifile)
