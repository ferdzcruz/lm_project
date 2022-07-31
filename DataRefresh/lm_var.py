from lm_functions import Databackup
from parameters import dataset as params

#env_backup
#Argument
cmd_backup = Databackup(params["EnvType"], params["SourceProductline"])

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

pl = params['SourceProductline'] or params['TargetProductline']
env = params['EnvType']
cmd_dbverify = 'dbverify -q ' + pl + ' | tee ' + pl + '.target.dbverify.txt'
cmd_cdverify = 'cdverify -ie ' + pl + ' | tee ' + pl + '.target.cdverify.txt'
cmd_dbcount_gen = 'dbcount gen | tee dbcount_gen.txt'
cmd_dbcount = 'dbcount ' + pl + ' | tee ' + pl + '.' + env + '.dcount.txt'
data_val = (cmd_dbverify,cmd_cdverify,cmd_dbcount_gen,cmd_dbcount)


    # dbcount_prodline = ''

# env_backup2 = env_cmd_backup.export_gen_rolesecclass_backup()
# env_backup3 = env_cmd_backup.export_gen_ruiprofile_backup()

# env_docstr1 = Env_backup.env_backup.__doc__
# env_docstr2 = Env_backup.export_gen_rolesecclass_backup.__doc__
# env_docstr3 = Env_backup.export_gen_ruiprofile_backup.__doc__

# backup_all = (env_docstr1, env_backup1,env_docstr2,env_backup2,env_docstr3,env_backup3)

# dbcount_gen = 'dbcount gen | tee dbcount_gen.txt'
# export_gen_ruiprofile = ('dbexport -Cz gen_' + pl + '_RoamingUIProfile.zip gen RoamingUIProfile -f' + '"DataArea=\\' + '"' + pl + '\\""' + ' | tee ' + pl + '.target.roaminguiprofile.txt')
# export_gen_rolesecclass = ('dbexport -Cz gen_' + pl + '_RoleSecurityClass.zip gen RoleSecurityClass -f' + '"DataArea=\\' + '"' + pl + '\\""' + ' | tee ' + pl + '.target.rolesecurityclass.txt')
# dadata_{env} = 'daexport -t 12 -ez ' + env + '.' + pl + '.dadata.env.zip ' + pl + ' | tee ' + pl + '.' + env + '.env.dadata.txt'
# dadata_noWU = 'daexport -t 12 -z ' + env + '.' + pl + '.dadata.NoWU.zip ' + pfworkunits + pl + ' | tee ' + pl + '.' + env + '.noWU.dadata.txt'
# pfiflows = 'dbexport -Cz ' + env + '.' + pl + '.pflows.zip ' + pl + pflows + ' | tee ' + pl + '.' + env + '.pfiflow.txt'
# pfconfig = 'dbexport -Cz ' + env + '.' + pl + '.pficonfig.zip ' + pl + pficonfig + ' | tee ' + pl + '.' + env + '.pficonfig.txt'
# excluded_tables = 'dbexport -Cz ' + env + '.' + pl + '.excluded_tables.zip ' + pl + excluded_table_list + ' | tee ' + pl + '.excluded_tables.txt'
# chp_export = 'dbexport -Cz ' + env + '.' + pl + '.CHP.zip ' + pl + ' CHP ' + ' | tee ' + pl + '.' + env + '.chp.txt'
# u_apvenmast_export = 'dbexport -Cz ' + env + '.' + pl + '.u_apvenmast.zip ' + pl + ' u_apvenmast ' + ' | tee ' + pl + '.' + env + '.u_apvenmast.txt'
# cddata = 'cdexport -z ' + env + '.' + pl + '.cddata.zip ' + pl + ' | tee ' + pl + '.' + env + '.' + 'cddata.txt'
# cddatasec = 'cdexport -z ' + env + '.' + pl + '.cddata.security.zip --authsecurity ' + pl + ' | tee ' + pl + '.' + env + '.' + 'cddata.security.txt'
# dbcount = 'dbcount ' + pl + ' | tee ' + pl + '.' + env + '.dcount.txt'
# dbverify = 'dbverify -q ' + pl + ' | tee ' + pl + '.target.dbverify.txt'
# cdverify = 'cdverify -ie ' + pl + ' | tee ' + pl + '.target.cdverify.txt'
