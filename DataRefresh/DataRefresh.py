import os, time, sys
from subprocess import run
from backup_parameters import dataset as backup_params
from lm_functions import Databackup
from os import path
from lm_var import *



# print(backup_params)
# print(backup_params["Strategy"])
# print(backup_params["WorkingDirectory"])
# print(backup_params["SourceProductline"])



#path = "D:\lmsops\working\"

#subdir = backup_params["EnvType"].upper()
#workdir = os.path.join(path,chg,subdir)
#subdir = backup_params["EnvType"].upper()
#os.mkdir(wrkdir)
#os.chdir(wrkdir)



# # 1 : Create directory
# chg = backup_params["WorkingDirectory"]
# subdir = backup_params["EnvType"].upper()
# workdir = os.path.join('D:\\', 'lmsops', 'working', chg,subdir)
# create_folder(workdir)
# os.chdir(workdir)

if __name__ == '__main__':

# Backup type

    if  backup_params["Tool"] == "sql" and backup_params["EnvType"]=="source":
        print(Databackup.env_backup.__doc__)
        print(environment_backup,'\n')

    if  backup_params["Tool"] == "sql" and backup_params["EnvType"]=="target":
        print(Databackup.env_backup.__doc__)
        print(environment_backup,'\n')
        print(Databackup.exclude_data_backup.__doc__)
        print(excluded_backup)
        print(chp_export)
        print(u_apvenmast_export)
    
    elif backup_params["Tool"] == "lm" and backup_params ["backupType"] == "full":
        #run(full_backup, shell=True)
        print(lm_full_backup)

    elif backup_params["Tool"] == "lm" and backup_params ["backupType"] == "noworkunits":
        #run(lm_nowu_backup, shell=True)
        print(lm_no_wu_backup)

    elif backup_params["Tool"] == "sql" and backup_params ["backupType"] == "noworkunits":
        #run(lm_nowu_backup, shell=True)
        print(lm_no_wu_backup)

    else:
        print("Failed!!Check your parameters. The tool doesn't match with the backup type. Rerun the script!")
        time.sleep(2)
        sys.exit(1)

#general backup
# print(pfi_docstr)
# print(cmd_pflows)
# print(cmd_pfconfig)
# print(Databackup.export_gen_ruiprofile_backup.__doc__)
# print(rolesec_backup)
# print(roamiuprof_backup)
# print(Databackup.cddata_backup.__doc__)
# print(cd_backup)
# print(cdsec_backup)

for std_backup in strd_backup:
    print(std_backup)

#general

#data validation
print(val_docstr)
for validation in data_val:
    print(validation)









