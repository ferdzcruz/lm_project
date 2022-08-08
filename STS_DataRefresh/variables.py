from functions import Databackup
from parameters import dataset as backup_params


#global vars
#Group of PfiTables
pfworkunits = '--ignore PfiWorkUnitInputData,AsyncActionRequest,ActionRequest,PfiActivity,PfiActivityVariable,PfiMetrics,PfiMetricsSummary,PfiQueue,PfiQueueAction,PfiQueueAssignment,PfiQueueReminder,PfiQueueTask,PfiWorkunit,PfiWorkunitFolder,PfiWorkunitState,PfiWorkunitVariable,PfiErrorMessage'
pflows = 'PfiFlowDefinition PfiFlowVersion PfiServiceDefinition PfiServiceFlowDefinition PfiServiceVariable PfiTrigger PfiTriggerFolder PfiTriggerVariable'
pficonfig = 'PfiChannel PfiConfiguration PfiConfigurationProperty PfiClassicConnection PfiFTPConnection PfiFrontOfficeConnection PfiJDBCConnection PfiJMSConnection PfiLandmarkConnection PfiM3Connection PfiMQConnection PfiSystemCommandConnection PfiTXConnection PfiWebRunConnection'

#Excluded Tables
excluded_table_list = 'SecurityClass ContextProperty ConfigurationParameter OAuth PfiChannel PfiChannelField PfiClassicConnection PfiCloverleafConnection PfiComparisonActivity PfiComparisonWorkunit PfiConfiguration PfiConfigurationProperty PfiEDICarrier PfiEDIWorkFile PfiEmailConnection PfiEventHubConnection PfiFTPConnection PfiFileActivityConnection PfiFrontOfficeConnection PfiIONConnection PfiJDBCConnection PfiJMSConnection PfiLandmarkConnection PfiLdapConnection PfiM3Connection PfiMQConnection PfiReceiver PfiSMSConnection PfiServer PfiSystemCommandConnection PfiTXConnection PfiWebRunConnection PfiWebServiceConnection PfiWorkunitState Ping ProfileLog ProfileLogEntry ProfileLogIntermediateEntry'


#data validations
val_docstr = "@@Data and Table valditions"
pl = backup_params['SourceProductline'] or backup_params['TargetProductline']
env = backup_params['EnvType']
cmd_dbverify = f"dbverify -q {pl} | tee {pl}.{env}.dbverify.txt"
cmd_cdverify =f"cdverify -ie {pl} | tee {pl}.{env}.cdverify.txt"
cmd_dbcount_gen = 'dbcount gen | tee dbcount_gen.txt'
cmd_dbcount = f"dbcount {pl} | tee {pl}.{env}.dcount.txt"
data_val = (cmd_dbverify,cmd_cdverify,cmd_dbcount_gen,cmd_dbcount)

#docstring


    

#selected data
chp_export = f"dbexport -Cz {env}.{pl}.CHP.zip {pl} CHP | tee {pl}.{env}.chp.txt"
u_apvenmast_export = f"dbexport -Cz {env}.{pl}.u_apvenmast.zip {pl} u_apvenmast | tee {pl}.{env}.u_apvenmast.txt"


