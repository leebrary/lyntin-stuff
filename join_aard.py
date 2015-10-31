from lyntin.modules import modutils
from lyntin import exported

command_dict ={}
def join(ses,args,input):
    exported.lyntin_command('-session aard aardmud.org 23')

command_dict['join_aard'] = join

def load():
    modutils.load_commands(command_dict)
def unload():
    modutils.unload_commands(command_dict)
