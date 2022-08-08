from subprocess import call as run
from variables import pfworkunits,pflows,excluded_table_list,pficonfig
from parameters import dataset as params
import datetime, time, errno, os


now = datetime.datetime.now()
info_time = now.strftime("%Y-%m-%d %H:%M:%S")


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



#main command
class Databackup:
    '''Types of Backups'''

    def __init__(self, env, pl):
        self.env = env
        self.pl = pl

    def env_backup(self):
        '''@@exporting environment data'''
        return f"daexport -t 12 -ez {self.env}.{self.pl}.dadata.env.zip {self.pl} | tee env.{self.pl}.{self.env}.dadata.txt"

    def full_backup(self):
        '''@@exporting fullbackup data'''
        return f"daexport -t 12 -z {self.env}.{self.pl}.dadata.full.zip {self.pl} | tee {self.pl}.{self.env}.full.dadata.txt"

    def nowu_backup(self):
        '''@@exporting no workunit data'''
        return f"daexport -t 12 -z {self.env}.{self.pl}.dadata.NoWU.zip {pfworkunits} {self.pl} | tee {self.pl}.{self.env}.noWU.dadata.txt"
      
    def export_gen_ruiprofile_backup(self):
        '''@@exporting Identities'''
        return f'dbexport -Cz gen_{self.pl}_RoamingUIProfile.zip gen RoamingUIProfile -f "DataArea=\\"{self.pl}\\"" | tee {self.pl}.{self.env}.roaminguiprofile.txt'
    def export_gen_rolesecclass_backup(self):
        '''@@exporting Role SecurityClass'''
        return f'dbexport -Cz gen_{self.pl}_RoleSecurityClass.zip gen RoleSecurityClass -f "DataArea=\\"{self.pl}\\"" | tee {self.pl}.{self.env}.rolesecurityclass.txt'

    def cddata_backup(self)->str:
        '''@@export configuration data'''
        return f"cdexport -z {self.env}.{self.pl}.cddata.zip {self.pl} | tee {self.pl}.{self.env}.cddata.txt"

    def cddatasec_backup(self)->str:
        return f"cdexport -z {self.env}.{self.pl}.cddata.security.zip --authsecurity {self.pl} | tee {self.pl}.{self.env}.cddata.security.txt"

    def exclude_data_backup(self)->str:
        '''@@exporting tables for Post Steps'''
        return f"dbexport -Cz {self.env}.{self.pl}.excluded_tables.zip {self.pl} {excluded_table_list} | tee {self.pl}.excluded_tables.txt"
    def cmd_pflows(self)->str:
        '''@@exporting pflow data'''
        return f"dbexport -Cz {self.env}.{self.pl}.pflows.zip {self.pl} {pflows} | tee {self.pl}.{self.env}.pfiflow.txt"
    def cmd_pfconfig(self)->str:
        '''@export pficonfig data'''
        return f"dbexport -Cz {self.env}.{self.pl}.pficonfig.zip {self.pl} {pficonfig} | tee {self.pl}.{self.env}.pficonfig.txt"


#creating object
cmd_backup = Databackup(params["EnvType"], params["SourceProductline"] or params['TargetProductline'])

#backup Type
environment_backup = cmd_backup.env_backup()
lm_full_backup = cmd_backup.full_backup()
lm_no_wu_backup = cmd_backup.nowu_backup()

#Gen Role/Roaming backup
rolesec_backup = cmd_backup.export_gen_rolesecclass_backup()
roamiuprof_backup = cmd_backup.export_gen_ruiprofile_backup()

#configuration data backup
cd_backup = cmd_backup.cddata_backup()
cdsec_backup = cmd_backup.cddatasec_backup()

#pflows and pficonfig data
cmd_pflow = cmd_backup.cmd_pflows()
cmd_pfconfig = cmd_backup.cmd_pfconfig()

#excluded_tables_for SQL
excluded_backup = cmd_backup.exclude_data_backup()

#general backup
pfi_docstr = "@@Running pfidata export"
gen_backups = (cmd_pflow,cmd_pfconfig,roamiuprof_backup,rolesec_backup,cd_backup,cdsec_backup)
def default_backups():
    '''Run the usual backups'''
    print(f"{info_time} == @@Export pflows, pficonfig, Gen-Secdata and cddata\n")
    time.sleep(2)
    for gen_backup in gen_backups:
        print(gen_backup)



#     print(pfi_docstr,'\n')
#     run(cmd_pflow, check = True, shell = True)
#     run(cmd_pfconfig, check = True, shell = True)
#     print(roamiuprof_backup.__doc__,'\n')
#     run(rolesec_backup, check = True, shell = True)
#     run(roamiuprof_backup, check = True, shell = True)
#     print(Databackup.cddata_backup.__doc__,'\n')
#     run(cd_backup, check = True, shell = True)
#     run(cdsec_backup, check = True, shell = True)
