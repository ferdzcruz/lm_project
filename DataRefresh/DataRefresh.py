import os
from subprocess import run
from parameters import dataset as params
from lm_functions import Databackup
from os import path
from lm_var import *


# print(params)
# print(params["Strategy"])
# print(params["WorkingDirectory"])
# print(params["SourceProductline"])



#path = "D:\lmsops\working\"

#subdir = params["EnvType"].upper()
#workdir = os.path.join(path,chg,subdir)
#subdir = params["EnvType"].upper()
#os.mkdir(wrkdir)
#os.chdir(wrkdir)



# # 1 : Create directory
# chg = params["WorkingDirectory"]
# subdir = params["EnvType"].upper()
# workdir = os.path.join('D:\\', 'lmsops', 'working', chg,subdir)
# create_folder(workdir)
# os.chdir(workdir)

if __name__ == '__main__':

# Backup type

    if params["Strategy"] == "precopy" and params["Tool"] == "sql" and params["EnvType"]=="source":
        print(Databackup.env_backup.__doc__)
        print(environment_backup,'\n')

    if params["Strategy"] == "precopy" and params["Tool"] == "sql" and params["EnvType"]=="target":
        print(Databackup.env_backup.__doc__)
        print(environment_backup,'\n')
        print(Databackup.exclude_data_backup.__doc__)
        print(excluded_backup)
        print(chp_export)
        print(u_apvenmast_export)
    
    elif params["Strategy"] == "precopy" and params["Tool"] == "lm" and params ["backupType"] == "full":
        #run(full_backup, shell=True)
        print(lm_full_backup)

    elif params["Strategy"] == "precopy" and params["Tool"] == "lm" and params ["backupType"] == "noworkunits":
        #run(lm_nowu_backup, shell=True)
        print(lm_no_wu_backup)

    elif params["Strategy"] == "precopy" and params["Tool"] == "sql" and params ["backupType"] == "noworkunits":
        #run(lm_nowu_backup, shell=True)
        print(lm_no_wu_backup)

    # else:
    #     print("Error!!====Check your parameters====")

#general backup
print(pfi_docstr)
print(cmd_pflows)
print(cmd_pfconfig)
print(Databackup.export_gen_ruiprofile_backup.__doc__)
print(rolesec_backup)
print(roamiuprof_backup)
print(Databackup.cddata_backup.__doc__)
print(cd_backup)
print(cdsec_backup)

#data validation

print(val_docstr)
for validation in data_val:
    print(validation)









