from os import mkdir, chdir
import os, errno
from lm_var import pfworkunits

def Completed_note():
    print('\n ...................completed...................\n')


def create_folder(wrkdir):
    try:
        os.makedirs(wrkdir)
        print("Folder " + wrkdir + " created.")
    except OSError as fileexist:
        if fileexist.errno == errno.EEXIST:
            print("Folder " + wrkdir + " already exists.")
        else:
            raise
    os.chdir(wrkdir)


# Backup
def env_backup(env,pl)->str:
    return f"daexport -t 12 -ez {env}.{pl}.dadata.env.zip {pl}  | tee {pl}.{env}.env.dadata.txt"

def lm_full_backup(env,pl)->str:
    return f"daexport -t 12 -z {env}.{pl}.dadata.full.zip {pl} | tee {pl}.{env}.full.dadata.txt"

def lm_nowu_backup(env,pl)->str:
    return f"daexport -t 12 -z {env}.{pl}.dadata.NoWU.zip {pfworkunits} {pl} | tee {pl}.{env}.noWU.dadata.txt"


def cddata_backup(env,pl)->str:
    return f"cdexport -z {env}.{pl}.cddata.zip {pl} | tee {pl}.{env}.cddata.txt"

def cddatasec_backup(env,pl)->str:
    return f"cdexport -z {env}.{pl}.cddata.security.zip --authsecurity {pl} | tee {pl}.{env}.cddata.security.txt"

def export_gen_ruiprofile_backup(pl)->str:
    return f'dbexport -Cz gen_{pl}_RoamingUIProfile.zip gen RoamingUIProfile -f "DataArea=\\"{pl}\\"" | tee {pl}.target.roaminguiprofile.txt'
def export_gen_rolesecclass_backup(pl)->str:
    return f'dbexport -Cz gen_{pl}_RoleSecurityClass.zip gen RoleSecurityClass -f "DataArea=\\"{pl}\\"" | tee {pl}.target.rolesecurityclass.txt'


class Env_backup:


    def __init__(self, env, pl, wrkdir):
        self.env = env
        self.pl = pl
        self.wrkdir =wrkdir


    def create_folder(self):
        try:
            os.mkdir(self.wrkdir)
            print (f"Folder {self.wrkdir} created.")
        except OSError as fileexist:
            if fileexist.errno == errno.EEXIST:
                print(f"Folder {self.wrkdir} already exists.")
            else:
                raise
        os.chdir(self.wrkdir)


    def env_backup(self):
        return f"daexport -t 12 -ez {self.env}.{self.pl}.dadata.env.zip {self.pl} | tee env.{self.pl}.{self.env}.dadata.txt"
    def export_gen_ruiprofile_backup(self):
        return f'dbexport -Cz gen_{self.pl}_RoamingUIProfile.zip gen RoamingUIProfile -f "DataArea=\\"{self.pl}\\"" | tee {self.pl}.target.roaminguiprofile.txt'
    def export_gen_rolesecclass_backup(self):
        return f'dbexport -Cz gen_{self.pl}_RoleSecurityClass.zip gen RoleSecurityClass -f "DataArea=\\"{self.pl}\\"" | tee {self.pl}.target.rolesecurityclass.txt'





   


# def export_gen_ruiprfile_rolesecclass_backup(pl):
#     export_gen_rolesecclass_backup()
#     export_gen_ruiprofile_backup()



# dbcount_gen = 'dbcount gen | tee dbcount_gen.txt'
# 
# 
# dadata_{env} = 'daexport -t 12 -ez ' + env + '.{pl}.dadata.env.zip {pl} | tee {pl}.' + env + '.env.dadata.txt'
# dadata_noWU = 'daexport -t 12 -z ' + env + '.{pl}.dadata.NoWU.zip ' + pfworkunits + pl + ' | tee {pl}.' + env + '.noWU.dadata.txt'
# pfiflows = 'dbexport -Cz ' + env + '.{pl}.pflows.zip ' + pl + pflows + ' | tee {pl}.' + env + '.pfiflow.txt'
# pfconfig = 'dbexport -Cz ' + env + '.{pl}.pficonfig.zip ' + pl + pficonfig + ' | tee {pl}.' + env + '.pficonfig.txt'
# excluded_tables = 'dbexport -Cz ' + env + '.{pl}.excluded_tables.zip ' + pl + excluded_table_list + ' | tee {pl}.excluded_tables.txt'
# chp_export = 'dbexport -Cz ' + env + '.{pl}.CHP.zip {pl} CHP ' + ' | tee {pl}.' + env + '.chp.txt'
# u_apvenmast_export = 'dbexport -Cz ' + env + '.{pl}.u_apvenmast.zip {pl} u_apvenmast ' + ' | tee {pl}.' + env + '.u_apvenmast.txt'
# cddata = 'cdexport -z ' + env + '.{pl}.cddata.zip {pl} | tee {pl}.' + env + '.' + 'cddata.txt'
# cddatasec = 'cdexport -z ' + env + '.{pl}.cddata.security.zip --authsecurity {pl} | tee {pl}.' + env + '.' + 'cddata.security.txt'
# dbcount = 'dbcount {pl} | tee {pl}.' + env + '.dcount.txt'
# dbverify = 'dbverify -q {pl} | tee {pl}.target.dbverify.txt'
# cdverify = 'cdverify -ie {pl} | tee {pl}.target.cdverify.txt'
