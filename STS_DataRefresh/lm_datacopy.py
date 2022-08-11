
#from functions import Databackup, DataRestore, lm_default_backups,sql_default_backups, info_time,Default_data_validations,admin_mode,start_mode,daimport_l_full,daimport_l_noWU,daimport_l_env
from functions import *
import os,sys
from parameters import dataset as params


# 1 : Create directory
# chg = params["WorkingDirectory"]
# subdir = params["EnvType"].upper()
# workdir = os.path.join('D:\\', 'lmsops', 'working', chg,subdir)
# create_folder(workdir)
# os.chdir(workdir)


####backup 

cmd_backup = Databackup(params["EnvType"], params["SourceProductline"] or params['TargetProductline'])
bckpsrc = os.path.join('D:\\', 'lmsops', 'working',params["WorkingDirectory"],'SOURCE\\')
restore_data = DataRestore(bckpsrc,params["SourceProductline"], params["TargetProductline"])

#SQL Tool

def backup_main():

    if params["Tool"] == 'sql':
        params["backupType"] == 'env'
        print('='*52)
        print('|',info_time, cmd_backup.env_backup.__doc__,'|')
        print('='*52)
        print(cmd_backup.env_backup())
        print('\n')
        sql_default_backups()

    #LM tool
    elif params["Tool"] == 'lm' and params["backupType"] == 'full':
        print('='*51)
        print('|',info_time, cmd_backup.full_backup.__doc__,'|')
        print('='*51)
        print(cmd_backup.full_backup())
        print('\n')
        lm_default_backups()
    elif params["Tool"] == 'lm' and params["backupType"] == 'nowu':
        print('='*52)
        print('|',info_time,cmd_backup.nowu_backup.__doc__,'|')   
        print('='*52)
        print(cmd_backup.nowu_backup())
        print('\n')
        lm_default_backups()
    
    else:
        print("Please check your parameters!!")
        sys.exit(0)

    print('\n')
    print('='*58)
    print(f"|{info_time} == @@Data valdiation before the copy|")
    print('='*58)
    Default_data_validations()
    sys.exit(0)

###Restore


def restore_main():
#    if params["Strategy"] == 'restore' and params["Tool"] == 'sql':
    admin_mode()
    if params["Tool"] == 'sql':
        params["backupType"] == 'env'
        print(daimport_l_env)
        pause()
        print(restore_data.daimport_data_env())
        revert_table_list()

    if params["Tool"] == 'lm' and params["backupType"] == 'full':
        print(daimport_l_full)
        pause()
        print(restore_data.daimport_full())

    if params["Tool"] == 'lm' and params["backupType"] == 'nowu':
        print(daimport_l_noWU)
        pause()
        print(restore_data.daimport_noWU())
        cleanup_workunits()

    dbimport_pfconfig()
    dbimport_pflows()
    cdimport_data()
    Default_data_validations()
    start_mode()




if __name__ == '__main__':
    if params["Strategy"] == 'restore':
        restore_main()
        sys.exit(0)
    elif params["Strategy"] == 'backup':
        backup_main()
        sys.exit(0)
    else:   
        print("Invalid Options")
