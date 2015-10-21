from lyntin import exported
from lyntin.modules import modutils
import time
import random
check = time.time()
command_dic = {}
target = 'None'

def look_fortarget(args):
    global target
    text = args['data']
    if target in text:
        if timed():
            exported.lyntin_command('kill '+target)
    return args['data']

def timer(args):
    tick = args['tick']
    if tick%15 == 0:
        exported.lyntin_command(random.choice('eswn'))
    return tick


def timed():
    global check
    if time.time() > 5+ check:
        check = time.time()
        return True
    return False

def pick_target(ses,args,input):
    global target
    target = args['value']

command_dic ['tar']=(pick_target,'value=')

def load():
    exported.hook_register('timer_hook',timer)
    exported.hook_register('mud_filter_hook',look_fortarget)
    modutils.load_commands(command_dic)

def unload():
    exported.hook_unregister('timer_hook',timer)
    exported.hook_unregister('mud_filter_hook',look_fortarget)
    modutils.unload_commands(command_dic)



