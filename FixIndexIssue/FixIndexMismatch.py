import argparse
from lm_var import *
from lm_actions import setadmin, stagelandmark, activatelandmark, dbverify, manageda, pause, move_logs
from subprocess import call
import os

# parsing of parameters
parser = argparse.ArgumentParser(description="To Fix the Index Mismatch")
parser.add_argument(
    "-p", "--prodline", type=str, required=True, metavar="", help="Enter dataarea ex: lmghr"
)
parser.add_argument(
    "-wd", "--working_directory", type=str, required=True, metavar="", help="Enter working directory ex: CHG12345"
)
parser.add_argument(
    "-o", "--option", type=str, required=True, metavar="", help="Enter what is needed to fix", choices=["varchar", "charset"]
)

args = parser.parse_args()

# 2
class Changeda():
    '''This will create the object for changeda command'''
    
    def __init__(self, prodline, option):
        self.prodline = prodline
        self.option = option

    def changeda_varchar(self) -> str:
        '''Fix varchar issue'''
        return f"{varchar} {self.prodline} | tee {self.prodline}.{varchar_log}"

    def changeda_charset(self) -> str:
        '''Fix charset issue'''
        return f" {charset_s} {self.prodline} msf | tee {self.prodline}.{char_s_log}"
    
    def changeda_charset_d(self) -> str:
        '''Set charset default'''
        return f"{charset_d} {self.prodline} | tee {self.prodline}.{char_d_log}"

command = Changeda(args.prodline, args.option)

if __name__ == '__main__':
    action_varchar = command.changeda_varchar()
    action1_charset_set = command.changeda_charset()
    action2_charset_default = command.changeda_charset_d()
    phase1 = setadmin(args.prodline)
    phase2 = stagelandmark(args.prodline)
    phase3 = activatelandmark(args.prodline)
    phase4 = dbverify(args.prodline)
    phase5 = manageda(args.prodline)
    cleanup_logs = move_logs(args.working_directory)
    if args.option == "varchar":
        call(action_varchar, shell=True)

    elif args.option == "charset":
        call(action1_charset_set, shell=True)
        call(action2_charset_default,shell=True)

print('\n',setadmin.__doc__,'\n')
call(phase1, shell=True)
print('\n',stagelandmark.__doc__,'\n')
call(phase2, shell=True)
pause()
print('\n',activatelandmark.__doc__,'\n')
call(phase3, shell=True)
pause()
print('\n',dbverify.__doc__,'\n')
call(phase4, shell=True)
print('\n',manageda.__doc__,'\n')
call(phase5, shell=True)
print('\n',move_logs.__doc__,'\n')
call(cleanup_logs,shell=True)








