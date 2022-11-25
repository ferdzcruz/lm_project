from functions import Databackup, DataRestore, lm_default_backups,sql_default_backups, info_time,Default_data_validations,admin_mode,start_mode,daimport_l_full,daimport_l_noWU,daimport_l_env
from functions import *
import os,sys
from parameters import dataset as params
import subprocess as run

# 1 : Create directory
chg = params["WorkingDirectory"]
subdir = params["EnvType"].upper()
workdir = os.path.join('D:\\', 'lmsops', 'working', chg,subdir)
create_folder(workdir)
os.chdir(workdir)
####backup
cmd_backup = Databackup(params["EnvType"], params["SourceProductline"] or params['TargetProductline'])
bckpsrc = os.path.join('D:\\', 'lmsops', 'working',params["WorkingDirectory"],'SOURCE\\')
restore_data = DataRestore(bckpsrc,params["SourceProductline"], params["TargetProductline"])

#SQL Tool
def backup_main():
    '''Data backup Part'''

    if params["Tool"] == 'sql':
        params["backupType"] == 'env'
        print('='*52)
        print('|',info_time, cmd_backup.env_backup.__doc__,'|')
        print('='*52)
        run(cmd_backup.env_backup(), shell=True)
        print(cmd_backup.env_backup())
        print('\n')
        sql_default_backups()

    #LM tool
    elif params["Tool"] == 'lm' and params["backupType"] == 'full':
        print('='*51)
        print('|',info_time, cmd_backup.full_backup.__doc__,'|')
        print('='*51)
        run(cmd_backup.full_backup, shell=True)
        print('\n')
        lm_default_backups()
    elif params["Tool"] == 'lm' and params["backupType"] == 'nowu':
        print('='*52)
        print('|',info_time,cmd_backup.nowu_backup.__doc__,'|')
        print('='*52)
        run(cmd_backup.nowu_backup ,shell=True)
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
    '''Data Restore part'''
    admin_mode()
    print("@@verifying data backup")


    if params["Tool"] == 'sql':
        params["backupType"] == 'env'
        run(daimport_l_env, shell=True)
        pause()
        print('='*47)
        print('|',info_time,restore_data.daimport_data_env.__doc__)
        print('='*47)
        run(restore_data.daimport_data_env(),shell=True)
        completed_note()
        revert_table_list()

    if params["Tool"] == 'lm' and params["backupType"] == 'full':
        run(daimport_l_full,shell=True)
        pause()
        print('='*74)
        print('|',info_time,restore_data.daimport_full.__doc__)
        print('='*74)
        run(restore_data.daimport_full(),shell=True)
        completed_note()

    if params["Tool"] == 'lm' and params["backupType"] == 'nowu':
        run(daimport_l_noWU,shell=True)
        pause()
        print('='*68)
        print('|',info_time,restore_data.daimport_noWU.__doc__)
        print('='*68)
        run(restore_data.daimport_noWU(), shell=True)
        completed_note()
        cleanup_workunits()

    dbimport_pfconfig()
    dbimport_pflows()
    cdimport_data()
    Default_after_data_validations()
    start_mode()
    completed_note()
    print(f"Note: You may find all the logs in D:\lmsops\working\{chg}")
    time.sleep(2)

if __name__ == '__main__':
    if params["Strategy"] == 'restore':
        restore_main()
        sys.exit(0)
    elif params["Strategy"] == 'backup':
        backup_main()
        sys.exit(0)
    else:
        print("Invalid Options")