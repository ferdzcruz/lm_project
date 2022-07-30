#Group of PfiTables
pfworkunits = '--ignore PfiWorkUnitInputData,AsyncActionRequest,ActionRequest,PfiActivity,PfiActivityVariable,PfiMetrics,PfiMetricsSummary,PfiQueue,PfiQueueAction,PfiQueueAssignment,PfiQueueReminder,PfiQueueTask,PfiWorkunit,PfiWorkunitFolder,PfiWorkunitState,PfiWorkunitVariable,PfiErrorMessage '
pflows = ' PfiFlowDefinition PfiFlowVersion PfiServiceDefinition PfiServiceFlowDefinition PfiServiceVariable PfiTrigger PfiTriggerFolder PfiTriggerVariable '
pficonfig = ' PfiChannel PfiConfiguration PfiConfigurationProperty PfiClassicConnection PfiFTPConnection PfiFrontOfficeConnection PfiJDBCConnection PfiJMSConnection PfiLandmarkConnection PfiM3Connection PfiMQConnection PfiSystemCommandConnection PfiTXConnection PfiWebRunConnection '

#Excluded Tables
excluded_table_list = ' SecurityClass ContextProperty ConfigurationParameter OAuth PfiChannel PfiChannelField PfiClassicConnection PfiCloverleafConnection PfiComparisonActivity PfiComparisonWorkunit PfiConfiguration PfiConfigurationProperty PfiEDICarrier PfiEDIWorkFile PfiEmailConnection PfiEventHubConnection PfiFTPConnection PfiFileActivityConnection PfiFrontOfficeConnection PfiIONConnection PfiJDBCConnection PfiJMSConnection PfiLandmarkConnection PfiLdapConnection PfiM3Connection PfiMQConnection PfiReceiver PfiSMSConnection PfiServer PfiSystemCommandConnection PfiTXConnection PfiWebRunConnection PfiWebServiceConnection PfiWorkunitState Ping ProfileLog ProfileLogEntry ProfileLogIntermediateEntry '

#




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
