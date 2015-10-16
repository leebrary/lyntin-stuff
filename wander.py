from lyntin.modules import modutils
from lyntin import exported
import random
#import time
movement_list = ['e','w','n','s']
#command_dir = {}

current = 0
lyntin_tick = 0

def select_and_move():
    movement_choice = random.choice(movement_list)
    exported.write_message(movement_choice)
    exported.lyntin_command('exits')
#    start_wander = time.time()
    exported.lyntin_command(movement_choice)

def handle_timer(args):
    global current,lyntin_tick
    current = args['tick']
    if current > lyntin_tick + 5:
        lyntin_tick = current
        select_and_move()

#def wander(ses,args,input):
#    whether_wander = args ['value']
#    if whether_wander == 'go':
#        start = time.time()
#    while whether_wander == 'go':
#        if time.time() > start +10:
#            exported.write_message('somewhere new now')
#            select_and_move()
#            whether_wander = raw_input('keep wandering?')
#
#command_dir['wander']=(wander,'value=')

def load():
#modutils.load_commands(command_dir)
    exported.hook_register('timer_hook',handle_timer)

def unload():
    exported.hook_unregister('timer_hook',handle_timer)
#    modutils.unload_commands(command_dir)


