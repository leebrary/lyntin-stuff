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
        found = re.search('A (\w+ )',text)
        if found:
            targets.append(found.group(1))


    if '>' in text:
        exported.write_message('my targets: '+''.join(targets))
        exits_line = 0
    if '[Fighting: ' in text:
        exported.lyntin_command('kick' if random.choice('kb')== 'k' else 'bash')
    return args['data']

def get_targs():
    global targets
    if targets:
        exported.lyntin_command('kill '+ targets.pop())
    else:
        exported.lyntin_command(random.choice('eswn'))


def timer(args):
    global check
    if args['tick'] > check + random.choice(range(5,9)):
        get_targs()
        check = args['tick']
    return args['tick']


def load():
    exported.hook_register('timer_hook',timer)
    exported.hook_register('mud_filter_hook',find_nmes)

def unload():
    exported.hook_unregister('timer_hook',timer)
    exported.hook_unregister('mud_filter_hook',find_nmes)
