from IPython.core.magic import Magics, magics_class, line_magic
from IPython.core import magic_arguments

@magics_class
class ReverseMagic(Magics):
    @magic_arguments.magic_arguments()
    @magic_arguments.argument('input_text', type=str, help='Text to reverse')
    @line_magic
    def reverse(self, line):
        """Reverse the input text."""
        args = magic_arguments.parse_argstring(self.reverse, line)
        reversed_text = args.input_text[::-1]
        self.shell.set_next_input(reversed_text, replace=True)

def load_ipython_extension(ipython):
    ipython.register_magics(ReverseMagic)
