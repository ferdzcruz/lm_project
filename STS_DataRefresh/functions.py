from subprocess import call as run
#from variables import pfworkunits,pflows,excluded_table_list,pficonfig, admin_apps
from variables import *
from parameters import dataset as params
import datetime, time, errno, os


now = datetime.datetime.now()
info_time = now.strftime("%Y-%m-%d %H:%M:%S")

#Functions outside class
#create folder
def create_folder(wrkdir):
    try:
        os.makedirs(wrkdir)
        print("SUCCESS: Folder " + wrkdir + " is created.\n")
    except OSError as fileexist:
        if fileexist.errno == errno.EEXIST:
            print("Folder " + wrkdir + " already exists.Cleanup the files if you wish to use the same directory!\n")
        else:
            raise
    os.chdir(wrkdir)

#Stop/Start Apps

def admin_mode():
    print('='*50)
    print('|',info_time, '@@Running admin mode.......|')
    print('='*50)
    for am in admin_apps:
        run(am, shell=True)
    time.sleep(2)

def start_mode():
    print('='*23)
    print('|System Restart.......|')
    print('='*23)
    for sm in start_apps:
        run(sm, shell=True)
    time.sleep(2)

def pause():
    print('')
    os.system("pause")
    print('')


def completed_note():
    print('='*35)
    print(f'|{info_time} ==> completed|')
    print('='*35)

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

#creating object
cmd_backup = Databackup(params["EnvType"], params["SourceProductline"] or params['TargetProductline'])

# backup Type
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
        run(sql_gen_backup, shell=True)

def lm_default_backups():
    '''Run the usual backups'''
    print('='*75)
    print(f"|{info_time} == @@Export pflows, pficonfig, Gen-Secdata and cddata|")
    print('='*75)
    time.sleep(2)
    for lm_gen_backup in lm_def_data_backups:
        run(lm_gen_backup, shell=True)

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
comp_data_validations = Datavalidations(params["EnvType"], params["TargetProductline"])
cmd_dbverify = data_validations.cmd_dbverify()
cmd_cdverify = data_validations.cmd_dbverify()
cmd_dbcount_gen = data_validations.cmd_dbcount_gen()
cmd_dbcount_pl =  data_validations.cmd_dbcount_pl()

final_cmd_dbverify = comp_data_validations.cmd_dbverify()
final_cmd_cdverify = comp_data_validations.cmd_dbverify()
final_cmd_dbcount_gen = comp_data_validations.cmd_dbcount_gen()
final_cmd_dbcount_pl =  comp_data_validations.cmd_dbcount_pl()
final_dbcount_pl = comp_data_validations.cmd_dbcount_pl()

data_validation = (cmd_dbverify,cmd_cdverify,cmd_dbcount_gen,cmd_dbcount_pl)
comp_data_validation = (final_cmd_dbverify,final_cmd_cdverify,final_cmd_dbcount_gen,final_dbcount_pl)
def Default_data_validations():
    '''@@validating gen and pl'''
    for data_val in data_validation:
        run(data_val, shell=True)

def Default_after_data_validations():
    '''@@validating gen and pl'''
    for comp_data_val in comp_data_validation:
        run(comp_data_val, shell=True)

#====================End of Backup

class DataRestore:
    '''Will run daimport command'''
    def __init__(self, bkpsrc, src, tgt):
        self.bkpsrc = bkpsrc
        self.src = src
        self.tgt = tgt

    def daimport_data_env(self):
        '''|@@daimport env only....|'''

        return f'daimport --sameenv -ot 12 -w --deletedata -I {self.bkpsrc}source.{self.src}.dadata.env.zip {self.src}={self.tgt} | tee {self.tgt}.env.daimport.txt'

    def daimport_full(self):
        '''|daimport full data and no cleanup of workunits....|'''
        return f'daimport --sameenv -ot 12 -w --deletedata -I {self.bkpsrc}source.{self.src}.dadata.full.zip {self.src}={self.tgt} | tee {self.tgt}.daimport.txt'

    def daimport_noWU(self):
        '''|daimport where workunits are not included....|'''
        return f'daimport --sameenv -ot 12 -w --deletedata -I {self.bkpsrc}source.{self.src}.dadata.NoWU.zip {self.src}={self.tgt} | tee {self.tgt}.daimport.txt'

#command as variable
bckpsrc = os.path.join('D:\\', 'lmsops', 'working',params["WorkingDirectory"],'SOURCE\\')
src_pl = params["SourceProductline"]
tgt_pl = params["TargetProductline"]
pflow = params["pfdata"]
cd_data = params["cddata"]
daimport_l_full = f'daimport -l {bckpsrc}source.{src_pl}.dadata.full.zip'
daimport_l_noWU = f'daimport -l {bckpsrc}source.{src_pl}.dadata.NoWU.zip'
daimport_l_env = f'daimport -l {bckpsrc}source.{src_pl}.dadata.env.zip'


def dbimport_pfconfig():
    dbdeletedata_data_pfconfig = f'dbdeletedata {tgt_pl} {pficonfig} -Y'
    pficonfig_revert = f'dbimport -Cz {bckpsrc}target.{tgt_pl}.pficonfig.zip {tgt_pl} | tee {tgt_pl}.pficonfig.revert.txt'
    print('\n@@Reverting PFI configurations...............\n')
    run(dbdeletedata_data_pfconfig, shell=True)
    run(pficonfig_revert, shell=True)
    completed_note()


def dbimport_pflows():
    dbdeletedata_data_flow = f'dbdeletedata {tgt_pl} {pflows} -Y'
    pflows_overwrite = f'dbimport -Cz {bckpsrc}source.{src_pl}.pflows.zip {tgt_pl} | tee {tgt_pl}.pflows.overwrite.txt'
    pflows_revert = f'dbimport -Cz {bckpsrc}target.{tgt_pl}.pflows.zip {tgt_pl} | tee {tgt_pl}.pflows.revert.txt'
    run(dbdeletedata_data_flow, shell=True)

    if pflow == 'y':
        print('\n@@Overwriting the Pflows Data...............\n')
        run(pflows_overwrite, shell=True)
        completed_note()
    elif pflow == 'n':
        print('\n@@Reverting the Pflows Data.................\n')
        run(pflows_revert, check=True,shell=True)
        completed_note()

def cdimport_data():
    cdimport_overwrite = f'cdimport -oI {bckpsrc}source.{src_pl}.cddata.zip --keepactor {tgt_pl} | tee {tgt_pl}.cdoverwrite.txt'
    cdimport_revert_sec = f'cdimport -oI {bckpsrc}target.{tgt_pl}.cddata.security.zip --keepactor {tgt_pl} | tee {tgt_pl}.cdrevert.security.txt'
    cdimport_revert = f'cdimport -oI {bckpsrc}target.{tgt_pl}.cddata.zip --keepactor {tgt_pl} | tee {tgt_pl}.cdrevert.txt'
    if cd_data == 'n':
        print('\n@@Reverting the Configuration Data...................\n')
        run(cdimport_revert, shell=True)
        completed_note()
    elif cd_data == 'y':
        print('\n@@Overwriting the Configuration Data...................\n')
        run(cdimport_overwrite, shell=True)
        run(cdimport_revert_sec, shell=True)
        completed_note()


def revert_table_list():
    dbdeletedata_data_excludedtables = f'dbdeletedata {tgt_pl} {excluded_table_list} -Y'
    table_list_revert = f'dbimport -Cz{bckpsrc}target.{tgt_pl}.excluded_tables.zip {tgt_pl} | tee {tgt_pl}.table_list.revert.txt'
    print('\n@@Reverting Configuration Data...................\n')
    run(dbdeletedata_data_excludedtables, shell=True)
    run(table_list_revert, shell=True)
    completed_note()

def cleanup_workunits():
    delete_workunits = f'dbdeletedata {tgt_pl} {workunits_tables} | tee {tgt_pl}.delete.workunits.data.txt'
    backup_async_actionrequest = 'dbexport -Cz gen_AsyncActionRequest.zip gen AsyncActionRequest -f' + '"DataArea=\\' + '"' + tgt_pl + '\\""'
    delete_async_actionrequest = 'dbdeletedata gen AsyncActionRequest -f' + '"DataArea=\\' + '"' + tgt_pl + '\\"" -Y'
    print('\n@@Running Cleanup of WorkUnits......\n')
    run(delete_workunits, shell=True)
    #run(backup_async_actionrequest, shell=True)- Enabled this if you need backup ActionRequest before deleting
    run(delete_async_actionrequest, shell=True)
    completed_note()