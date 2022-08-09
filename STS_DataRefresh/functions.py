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
        '''This data should be imported when TARGET configuration data is overwritter by SOURCE'''
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
    def chp_export(self)->str:
        '''@export CHP data. This is for LMGHR only'''
        return f"dbexport -Cz {self.env}.{self.pl}.CHP.zip {self.pl} CHP | tee {self.pl}.{self.env}.chp.txt"
    def u_apvenmast_export(self)->str:
        '''This is for MSCM and when LM tool is used'''
        return f"dbexport -Cz {self.env}.{self.pl}.u_apvenmast.zip {self.pl} u_apvenmast | tee {self.pl}.{self.env}.u_apvenmast.txt"



#selected data



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

#specific tables
u_apvenmast_data = cmd_backup.u_apvenmast_export()
chp_data = cmd_backup.chp_export()

#general backup to restore
pfi_docstr = "@@Running pfidata export"
sql_def_data_backups = (cmd_pflow,cmd_pfconfig,excluded_backup,roamiuprof_backup,rolesec_backup,cd_backup,cdsec_backup,chp_data)
lm_def_data_backups =(cmd_pflow,cmd_pfconfig,roamiuprof_backup,rolesec_backup,cd_backup,cdsec_backup,u_apvenmast_data)
def sql_default_backups():
    '''Run the usual backups'''
    print('='*75)
    print(f"|{info_time} == @@Export pflows, pficonfig, Gen-Secdata and cddata|")
    print('='*75)
    time.sleep(2)
    for sql_gen_backup in sql_def_data_backups:
        print(sql_gen_backup)


def lm_default_backups():
    '''Run the usual backups'''
    print('='*75)
    print(f"|{info_time} == @@Export pflows, pficonfig, Gen-Secdata and cddata|")
    print('='*75)
    time.sleep(2)
    for lm_gen_backup in lm_def_data_backups:
        print(lm_gen_backup)

class Datavalidations:
    '''validates before and after'''
    def __init__(self,env,pl) -> None:
        self.env = env
        self.pl = pl
    
    def cmd_dbverify(self):
        '''@@table verification'''
        return f"dbverify -q {self.pl} | tee {self.pl}.{self.env}.dbverify.txt"

    def cmd_cdverify(self):
        '''@@cd data verification'''
        return f"cdverify -ie {self.pl} | tee {self.pl}.{self.env}.cdverify.txt"
    
    def cmd_dbcount_gen(self):
        '''@@dbcount of gen'''
        return f"dbcount gen | tee dbcount_gen.txt"

    def cmd_dbcount_pl(self):
        return f"dbcount {self.pl} | tee {self.pl}.{self.env}.dcount.txt"


data_validations = Datavalidations(params["EnvType"], \
    params["SourceProductline"] or params["TargetProductline"])
cmd_dbverify = data_validations.cmd_dbverify() 
cmd_cdverify = data_validations.cmd_dbverify()
cmd_dbcount_gen = data_validations.cmd_dbcount_gen()
cmd_dbcount_pl =  data_validations.cmd_dbcount_pl()
data_validation = (cmd_dbverify,cmd_cdverify,cmd_dbcount_gen,cmd_dbcount_pl)


def Default_data_validations():
    '''@@validating gen and pl'''
    for data_val in data_validation:
        print(data_val)



