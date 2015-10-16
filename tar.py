from lyntin.modules import modutils
from lyntin import exported
presence = 'no'
target = None
def set_target():
    global target
    target = raw_input('whom shall we pursue? ')

def mud_filter(args):
    global presence
    text = args['data']
    if target != None:
        if target in text:
            presence = 'yes'
        else:
            presence = 'no'
    return args['data']

def go_getem(ses,args,input):
    if presence == 'yes' and target != None:
        exported.lyntin_command('kill '+target)







