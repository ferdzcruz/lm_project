from parameters import dataset as backup_params


#global vars
#Group of PfiTables
pfworkunits = '--ignore PfiWorkUnitInputData,AsyncActionRequest,ActionRequest,PfiActivity,PfiActivityVariable,PfiMetrics,PfiMetricsSummary,PfiQueue,PfiQueueAction,PfiQueueAssignment,PfiQueueReminder,PfiQueueTask,PfiWorkunit,PfiWorkunitFolder,PfiWorkunitState,PfiWorkunitVariable,PfiErrorMessage'
pflows = 'PfiFlowDefinition PfiFlowVersion PfiServiceDefinition PfiServiceFlowDefinition PfiServiceVariable PfiTrigger PfiTriggerFolder PfiTriggerVariable'
pficonfig = 'PfiChannel PfiConfiguration PfiConfigurationProperty PfiClassicConnection PfiFTPConnection PfiFrontOfficeConnection PfiJDBCConnection PfiJMSConnection PfiLandmarkConnection PfiM3Connection PfiMQConnection PfiSystemCommandConnection PfiTXConnection PfiWebRunConnection'
workunits_tables = 'PfiWorkUnitInputData ActionRequest PfiActivity PfiActivityVariable PfiMetrics PfiMetricsSummary PfiQueue PfiQueueAction PfiQueueAssignment PfiQueueReminder PfiQueueTask PfiWorkunit PfiWorkunitFolder PfiWorkunitState PfiWorkunitVariable PfiErrorMessage'
#Excluded Tables
excluded_table_list = 'SecurityClass ContextProperty ConfigurationParameter OAuth PfiChannel PfiChannelField PfiClassicConnection PfiCloverleafConnection PfiComparisonActivity PfiComparisonWorkunit PfiConfiguration PfiConfigurationProperty PfiEDICarrier PfiEDIWorkFile PfiEmailConnection PfiEventHubConnection PfiFTPConnection PfiFileActivityConnection PfiFrontOfficeConnection PfiIONConnection PfiJDBCConnection PfiJMSConnection PfiLandmarkConnection PfiLdapConnection PfiM3Connection PfiMQConnection PfiReceiver PfiSMSConnection PfiServer PfiSystemCommandConnection PfiTXConnection PfiWebRunConnection PfiWebServiceConnection PfiWorkunitState Ping ProfileLog ProfileLogEntry ProfileLogIntermediateEntry'

#was_variables
secret = 'L@wson123'
was_path = 'D:\IBM\WebSphere\AppServer\profiles\lmenv\\bin\\'
ibm_app_stop = f'call {was_path}stopServer.bat lmapp -username wasadmin -password {secret}'
ibm_node_stop = f'call {was_path}stopNode.bat'
ibm_dmg_stop = f'call {was_path}stopManager.bat'
ibm_dmg_start = f'call {was_path}startManager.bat'
ibm_node_start = f'call {was_path}startNode.bat'
ibm_app_start = f'call {was_path}startServer.bat lmapp'
lm_adminlaw = 'call adminlaw'
lm_stoplaw = 'call stoplaw'
lm_startlaw = 'call startlaw'
ping30 = 'ping -n 30 localhost'
ping500 = 'ping -n 500 localhost'
admin_apps = (ibm_app_stop,ibm_node_stop,ibm_dmg_stop,lm_adminlaw)
start_apps = (lm_stoplaw,ping30,lm_startlaw,ping500,ibm_dmg_start,ibm_node_start,ibm_app_start)


