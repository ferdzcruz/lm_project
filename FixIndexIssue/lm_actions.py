import os


def setadmin(prodline) -> str:
    '''set prodline to admin mode'''
    return f"manageda --set admin {prodline}"

def stagelandmark(prodline) -> str:
    '''staging the target productline'''
    return f"stagelandmark --upgradeflags=\"--skipall\" {prodline}"

def activatelandmark(prodline):
    '''activate the prodline'''
    return f"activatelandmark --avoidadmin {prodline}"

def dbverify(prodline):
    '''verify the tables'''
    return f"dbverify -q {prodline}"

def manageda(prodline):
    '''set the prodline to enabled'''
    return f"manageda --set enabled {prodline}"