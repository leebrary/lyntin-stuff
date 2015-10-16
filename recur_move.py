from lyntin import exported
from lyntin.modules import modutils

current = (0,0)
coords = [current]
no_go = False

commands_dict = {}
def mud_filter(args):
    global no_go
    text = args['data']
    if 'alas' in text:
        no_go = True
    else:
        no_go = False
    return args['data']


def recur(direc):
    global current,coords,no_go
    exported.write_message('going to move:'+direc)
    exported.lyntin_command(direc)
    if no_go:
        no_go = False
        with open('path_text.txt','a') as phile:
            phile.write(coords)
            coords.pop()
        return
    else:
        if direc == 'n':
            current = (coords[-1][0],coords[-1][1]+1)
        if direc == 'e':
            current = (coords[-1][0]+1,coords[-1][1])
        if direc == 'w':
            current = (coords[-1][0]-1,coords[-1][1])
        if direc == 's':
            current = (coords[-1][0],coords[-1][1]-1)
    for move in 'nesw':
        recur(move)


def command_recur(ses,args,input):
    val = args['value']
    if val == 'go':
        recur('n')

commands_dict['start_recur']=(command_recur,'value=')

def load():
    modutils.load_commands(commands_dict)
    exported.hook_register('mud_filter_hook',mud_filter)

def unload():
    modutils.unload_commands(commands_dict)
    exported.unhook_register('mud_filter_hook',mud_filter)


