from lyntin import exported
import random
import re
check = 0


targets = []
taking_inputs = 'yes'
exits = []
combat = 0
#with open('/home/devin/lyntin-4.2/my_stuff/my_tars.txt','r') as phile:
#    targets = phile.readline().split()
immd_tars = []
fled = 0
def find_nmes(args):
    global targets,immd_tars,taking_inputs,exits,combat
    text= args['data']
    if taking_inputs == 'yes':
        for tar in targets:
            if tar in text:
                immd_tars.append(tar)
    if ">" in text and taking_inputs == 'yes':
        exported.write_message('\n these are my current targs'+ str(immd_tars))
        taking_inputs = 'no'
    if 'Exits' in text:
        found = re.search('\[ Exits: ([\w\s]+) \]',text)

        if found:
            exported.write_message('found exits are ' +found.group(0))
            exits.extend(found.group(1).split())
    health =re.search('(\d+/\d+)hp',text)
    if health:
        health = int(health.group(1).split('/')[0])

    if 'Fighting:' in text:
        if random.choice(range(3)) == 1:
            exported.lyntin_command('kick' if random.choice('kb')== 'k' else 'bash')
            exported.lyntin_command('dirt' if random.choice('es') == 'e' else 'stun')
        if random.choice(range(4)) == 1:
            exported.lyntin_command('intimidate')
        if health < 300 :
            exported.write_message('trying to flee \n')
            exported.lyntin_command('fle')
    return args['data']

def get_targs():
    global immd_tars,taking_inputs,exits
    if immd_tars:
        exported.lyntin_command('kill '+ immd_tars.pop())
        exported.write_message('\nthese are current tars '+ str(immd_tars))
    else:
        if exits:
            exported.lyntin_command(random.choice(exits))
            taking_inputs = 'yes'
            exits = []
        else:
            exported.lyntin_command(random.choice('eswn'))
            taking_inputs = 'yes'


def timer(args):
    global check
    if args['tick'] > check + random.choice(range(5,9)):
        get_targs()
        check = args['tick']
    return args['tick']

def treat():
    exported.lyntin_command('-4 treat')

def load():
    exported.hook_register('timer_hook',timer)
    exported.hook_register('mud_filter_hook',find_nmes)

def unload():
    exported.hook_unregister('timer_hook',timer)
    exported.hook_unregister('mud_filter_hook',find_nmes)
