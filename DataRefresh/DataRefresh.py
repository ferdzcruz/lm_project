import os
from parameters import dataset as params
from lm_functions import lm_nowu_backup, lm_full_backup, export_gen_ruiprofile_backup, export_gen_rolesecclass_backup, Env_backup, create_folder
from os import path


# print(params)
# print(params["Strategy"])
# print(params["WorkingDirectory"])
# print(params["SourceProductline"])

#Create directory
chg = params["WorkingDirectory"]
wrkdir = os.path.join('D:\\', 'lmsops', 'working', chg)
subdir = params["EnvType"].upper()
os.mkdir(wrkdir + '\\' + subdir)
os.chdir(wrkdir + '\\' + subdir)

#define object
env_cmd_backup = Env_backup(params["EnvType"], params["SourceProductline"], wrkdir)

# env_backup_sequence
backup1 = env_cmd_backup.env_backup()
backup2 = env_cmd_backup.export_gen_rolesecclass_backup()
backup3 = env_cmd_backup.export_gen_ruiprofile_backup()

if __name__ == '__main__':

    if params["Strategy"] == "precopy" and params["EnvType"] == "source" and params["Tool"] == "lm":
        # print(export_gen_ruiprofile_backup(params["SourceProductline"]))
        # print(export_gen_rolesecclass_backup(params["SourceProductline"]))
        print(backup1, '\n', backup2, '\n', backup3)
        print(wrkdir)
        print(chg)








