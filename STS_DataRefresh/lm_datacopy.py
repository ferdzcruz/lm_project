from functions import Databackup, lm_default_backups,sql_default_backups, info_time,Default_data_validations
import os,sys
from parameters import dataset as params


# 1 : Create directory
# chg = params["WorkingDirectory"]
# subdir = params["EnvType"].upper()
# workdir = os.path.join('D:\\', 'lmsops', 'working', chg,subdir)
# create_folder(workdir)
# os.chdir(workdir)


#backup 
cmd_backup = Databackup(params["EnvType"], params["SourceProductline"] or params['TargetProductline'])
#SQL Tool
if params["Strategy"] == 'backup' and params["Tool"] == 'sql':
    params["backupType"] == 'env'
    print('='*52)
    print('|',info_time, cmd_backup.env_backup.__doc__,'|')
    print('='*52)
    print(cmd_backup.env_backup())
    print('\n')
    sql_default_backups()

#LM tool
elif params["Strategy"] == 'backup' and params["Tool"] == 'lm' and params["backupType"] == 'full':
    print('='*51)
    print('|',info_time, cmd_backup.full_backup.__doc__,'|')
    print('='*51)
    print(cmd_backup.full_backup())
    print('\n')
    lm_default_backups()
elif params["Strategy"] == 'backup' and params["Tool"] == 'lm' and params["backupType"] == 'nowu':
    print('='*52)
    print('|',info_time,cmd_backup.nowu_backup.__doc__,'|')   
    print('='*52)
    print(cmd_backup.nowu_backup())
    print('\n')
    lm_default_backups()

print('\n')
print('='*58)
print(f"|{info_time} == @@Data valdiation before the copy|")
print('='*58)
Default_data_validations()

