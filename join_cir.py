from lyntin import exported
from lyntin.modules import modutils

commands_dir = {}
def join_cir(ses,args,input):
    name = args ['value']
    exported.lyntin_command('#session {} localhost 4000'.format(name))


commands_dir['join_cir']=(join_cir,'value=')

def load():
    modutils.load_commands(commands_dir)

def unload():
    modutils.unload_commands(commands_dir)

