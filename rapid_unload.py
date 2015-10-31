from lyntin import exported
from lyntin.modules import modutils
module = ''
command_dict = {}
def test_load(ses,args,input):
    global module
    module = args['value']
    exported.lyntin_command('-load '+ module)

def remove(ses,args,input):
    global module
    exported.lyntin_command('-unload '+module)

command_dict['xx'] = remove
command_dict['tload'] = (test_load,'value=')
def load():
    modutils.load_commands(command_dict)
def unload():
    modutils.unload_commands(command_dict)
