from lm_functions import Databackup
from parameters import dataset as params
from global_vars import pflows, pficonfig

#env_backup
#Argument
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

#excluded_tables_for SQL
excluded_backup = cmd_backup.exclude_data_backup()



#data validations

val_docstr = "@@Data and Table valditions"
pl = params['SourceProductline'] or params['TargetProductline']
env = params['EnvType']
cmd_dbverify = f"dbverify -q {pl} | tee {pl}.target.dbverify.txt"
cmd_cdverify =f"cdverify -ie {pl} | tee {pl}.target.cdverify.txt"
cmd_dbcount_gen = 'dbcount gen | tee dbcount_gen.txt'
cmd_dbcount = f"dbcount {pl} | tee {pl}.{env}.dcount.txt"
data_val = (cmd_dbverify,cmd_cdverify,cmd_dbcount_gen,cmd_dbcount)

#pfdata
pfi_docstr = "@@Running pfidata export" 
cmd_pflows = f"dbexport -Cz {env}.{pl}.pflows.zip {pl} {pflows} | tee {pl}.{env}.pfiflow.txt"
cmd_pfconfig = f"dbexport -Cz {env}.{pl}.pficonfig.zip {pl} {pficonfig} | tee {pl}.{env}.pficonfig.txt"
    

#selected data
chp_export = f"dbexport -Cz {env}.{pl}.CHP.zip {pl} CHP | tee {pl}.{env}.chp.txt"
u_apvenmast_export = f"dbexport -Cz {env}.{pl}.u_apvenmast.zip {pl} u_apvenmast | tee {pl}.{env}.u_apvenmast.txt"
