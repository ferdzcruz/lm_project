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
        print(Databackup.exclude_data_backup.__doc__)

    if params["Strategy"] == "precopy" and params["Tool"] == "sql" and params["EnvType"]=="target":
        print(Databackup.env_backup.__doc__)
        print(environment_backup,'\n')
        print(Databackup.exclude_data_backup.__doc__)
        print(excluded_backup)

    
    elif params["Strategy"] == "precopy" and params["Tool"] == "lm" and params ["backupType"] == "full":
        #run(full_backup, shell=True)
        print(lm_full_backup)

    elif params["Strategy"] == "precopy" and params["Tool"] == "lm" and params ["backupType"] == "noworkunits":
        #run(lm_nowu_backup, shell=True)
        print(lm_no_wu_backup)

    # elif params["Strategy"] == "precopy" and params["Tool"] == "sql" and params ["backupType"] == "noworkunits":
    #     #run(lm_nowu_backup, shell=True)
    #     print(lm_no_wu_backup)

    else:
        print("Error!!====Check your parameters====")

for validation in data_val:
    print('\n',validation)
# print(rolesec_backup)
# print(roamiuprof_backup)
# print(cd_backup)
# print(cdsec_backup)










