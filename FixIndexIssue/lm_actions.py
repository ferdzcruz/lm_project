import os
from lm_var import working_directory


def setadmin(prodline) -> str:
    '''@@setting prodline to admin mode'''
    return f"manageda --set admin {prodline}"

def stagelandmark(prodline) -> str:
    '''@@staging the target productline'''
    return f"stagelandmark --upgradeflags=\"--skipall\" {prodline}"

def activatelandmark(prodline):
    '''@@activating the prodline'''
    return f"activatelandmark --avoidadmin {prodline}"

def dbverify(prodline):
    '''@@verifying the tables'''
    return f"dbverify -q {prodline}"

def manageda(prodline):
    '''@@setting the prodline to enabled'''
    return f"manageda --set enabled {prodline}"

def pause():
    print('')
    os.system("pause")
    print('')

def move_logs(wd):
    '''@@moving the logs to the working directory'''
    return f"move *.txt {working_directory}\\{wd}"