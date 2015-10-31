from lyntin import exported
import random
import re
check = 0

exits_line = 0
targets = []
def find_nmes(args):
    global exits_line,targets
    text= args['data']
    if "[ Exits:" in text:
        exits_line = 1
    if exits_line == 1:
        found = re.search('[A|An] (\w+) ',text)
        if found:
            exported.write_message(targets)
            targets.append(found.group(1))


    if '>' in text:
        exits_line = 0
        try:
            if health< 500:
                exported.lyntin_command('treat')
        except:
            pass
    health =re.search('(\d+/\d+)hp',text)
    if health:
        health = int(health.group(1).split('/')[0])

    if 'Fighting:' in text:
        if random.choice(range(7)) == 1:
            exported.lyntin_command('kick' if random.choice('kb')== 'k' else 'bash')
            exported.lyntin_command('dirt' if random.choice('es') == 'e' else 'stun')
        if random.choice(range(7)) == 1:
            exported.lyntin_command('intimidate')
        if health < 300 :
            exported.write_message('trying to flee \n')
            exported.lyntin_command('flee')
        if health < 100 :
            exported.lyntin_command('fle')
    return args['data']

#def get_targs():
#    global targets
#    if targets:
#        exported.lyntin_command('kill '+ targets.pop())
#    else:
#        exported.lyntin_command(random.choice('eswn'))


def timer(args):
    global check
    if args['tick'] > check + random.choice(range(5,9)):
        #get_targs()
        check = args['tick']
    return args['tick']


def load():
    exported.hook_register('timer_hook',timer)
    exported.hook_register('mud_filter_hook',find_nmes)

def unload():
    exported.hook_unregister('timer_hook',timer)
    exported.hook_unregister('mud_filter_hook',find_nmes)
