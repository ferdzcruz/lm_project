# -------------------------------------------------------module
import subprocess
import os
import argparse


# --------------------------------------------------------Parsing
parser = argparse.ArgumentParser(description='Landmark Data Refresh')
parser.add_argument('-c', '--chg', required=True, help="CHG number")
parser.add_argument('-sp', '--sp', required=True, help="SOURCE productline")
parser.add_argument('-tp', '--tp', required=True, help="TARGET productline")
parser.add_argument('-pf', '--pf', required=True, help="Overwrite PFlows", choices=["Y", "N"])
parser.add_argument('-cd', '--cd', required=True, help="Overwrite Configuration Data", choices=["Y", "N"])
parser.add_argument('-cw', '--cw', required=True, help="Cleanup WorkUnits", choices=["Y", "N"])
parser.add_argument('-o', '--options', required=True, help="Options", choices=["lm-tool", "sql-tool"])
args = parser.parse_args()

# --------------------------------------------------------function

def dbimport_chp():
    import_chp = 'dbimport -oCz ' + backup_tp + 'target.' + sp + '.CHP.zip ' + tp + ' | tee ' + tp + '.chp.revert.txt'

def dbimport_uapvenmast():
    import_uapvenmast = 'dbimport -oCz ' + backup_sp + 'source.' + sp + '.u_apvenmast.zip ' + tp + ' | tee ' + tp + '.u_apvenmast.overwrite.txt'


def admin_mode():
    print('\n Running admin mode.......\n')
    ibm_app_stop = 'call D:\IBM\WebSphere\AppServer\profiles\lmenv\\bin\stopServer.bat lmapp -username wasadmin -password L@wson123'
    ibm_node_stop = 'call D:\IBM\WebSphere\AppServer\profiles\lmenv\\bin\stopNode.bat'
    ibm_dmg_stop = 'call D:\IBM\WebSphere\AppServer\profiles\Dmgr01\\bin\stopManager.bat'
    lm_adminlaw = 'call adminlaw'
    subprocess.call(ibm_app_stop, shell=True)
    subprocess.call(ibm_node_stop, shell=True)
    subprocess.call(ibm_dmg_stop, shell=True)
    subprocess.call(lm_adminlaw, shell=True)


def running_mode():
    print('\n System Restart.......\n')
    lm_stoplaw = 'call stoplaw'
    lm_startlaw = 'call startlaw'
    ping30 = 'ping -n 30 localhost'
    ping = 'ping -n 500 localhost'
    ibm_dmg_start = 'call D:\IBM\WebSphere\AppServer\profiles\Dmgr01\\bin\startManager.bat'
    ibm_node_start = 'call D:\IBM\WebSphere\AppServer\profiles\lmenv\\bin\startNode.bat'
    ibm_app_start = 'call D:\IBM\WebSphere\AppServer\profiles\lmenv\\bin\startServer.bat lmapp'
    subprocess.call(lm_stoplaw, shell=True)
    subprocess.call(ping30, shell=True)
    subprocess.call(lm_startlaw, shell=True)
    subprocess.call(ping, shell=True)
    subprocess.call(ibm_dmg_start, shell=True)
    subprocess.call(ibm_node_start, shell=True)
    subprocess.call(ibm_app_start,shell=True)


def completed_note():
    print('\n ...................completed...................\n')

def pause():
    print('')
    os.system("pause")
    print('')

def dbimport_pflows(pf):
    dbdeletedata_data_flow = 'dbdeletedata ' + tp + ' PfiFlowDefinition PfiFlowVersion PfiServiceDefinition PfiServiceFlowDefinition PfiServiceVariable PfiTrigger PfiTriggerFolder PfiTriggerVariable -Y'
    pflows_overwrite = 'dbimport -Cz ' + backup_sp + 'source.' + sp + '.pflows.zip ' + tp + ' | tee ' + tp + '.pflows.overwrite.txt'
    pflows_revert = 'dbimport -Cz ' + backup_tp + 'target.' + tp + '.pflows.zip ' + tp + ' | tee ' + tp + '.pflows.revert.txt'
    subprocess.call(dbdeletedata_data_flow, shell=True)
    
    if pf == 'Y':
        print('\nOverwriting the Pflows Data...............\n')
        subprocess.call(pflows_overwrite, shell=True)
        completed_note()
    elif pf == 'N':
        print('\nReverting the Pflows Data.................\n')
        subprocess.call(pflows_revert, shell=True)
        completed_note()

def dbimport_pfconfig():
    dbdeletedata_data_pfconfig = 'dbdeletedata ' + tp + ' PfiChannel PfiConfiguration PfiConfigurationProperty PfiClassicConnection PfiFTPConnection PfiFrontOfficeConnection PfiJDBCConnection PfiJMSConnection PfiLandmarkConnection PfiM3Connection PfiMQConnection PfiSystemCommandConnection PfiTXConnection PfiWebRunConnection -Y'
    pficonfig_revert = 'dbimport -Cz ' + backup_tp + 'target.' + tp + '.pficonfig.zip ' + tp + ' | tee ' + tp + '.pficonfig.revert.txt'
    print('\nReverting PFI configurations...............\n')
    subprocess.call(dbdeletedata_data_pfconfig, shell=True)
    print('')
    subprocess.call(pficonfig_revert, shell=True)
    completed_note()

def dbimport_pflows(pf):
    dbdeletedata_data_flow = 'dbdeletedata ' + tp + ' PfiFlowDefinition PfiFlowVersion PfiServiceDefinition PfiServiceFlowDefinition PfiServiceVariable PfiTrigger PfiTriggerFolder PfiTriggerVariable -Y'
    pflows_overwrite = 'dbimport -Cz ' + backup_sp + 'source.' + sp + '.pflows.zip ' + tp + ' | tee ' + tp + '.pflows.overwrite.txt'
    pflows_revert = 'dbimport -Cz ' + backup_tp + 'target.' + tp + '.pflows.zip ' + tp + ' | tee ' + tp + '.pflows.revert.txt'
    subprocess.call(dbdeletedata_data_flow, shell=True)
    if pf == 'Y':
        print('\nOverwriting the Pflows Data...............\n')
        subprocess.call(pflows_overwrite, shell=True)
        completed_note()
    elif pf == 'N':
        print('\nReverting the Pflows Data.................\n')
        subprocess.call(pflows_revert, shell=True)
        completed_note()

def cdimport_data(cd):
    cdimport_overwrite = 'cdimport -oI ' + backup_sp + 'source.' + sp + '.cddata.zip --keepactor ' + tp + ' | tee ' + tp + '.cdoverwrite.txt'
    cdimport_revert_sec = 'cdimport -oI ' + backup_tp + 'target.' + tp + '.cddata.security.zip --keepactor ' + tp + ' | tee ' + tp + '.cdrevert.security.txt'
    cdimport_revert = 'cdimport -oI ' + backup_tp + 'target.' + tp + '.cddata.zip --keepactor ' + tp + ' | tee ' + tp + '.cdrevert.txt'
    if cd == 'N':
        print('\nReverting the Configuration Data...................\n')
        subprocess.call(cdimport_revert, shell=True)
        completed_note()
    elif cd == 'Y':
        print('\nOverwriting the Configuration Data...................\n')
        subprocess.call(cdimport_overwrite, shell=True)
        subprocess.call(cdimport_revert_sec, shell=True)
        completed_note()

def revert_table_list():
    table_list = ' SecurityClass ContextProperty ConfigurationParameter OAuth PfiChannel PfiChannelField PfiClassicConnection PfiCloverleafConnection PfiComparisonActivity PfiComparisonWorkunit PfiConfiguration PfiConfigurationProperty PfiEDICarrier PfiEDIWorkFile PfiEmailConnection PfiEventHubConnection PfiFTPConnection PfiFileActivityConnection PfiFrontOfficeConnection PfiIONConnection PfiJDBCConnection PfiJMSConnection PfiLandmarkConnection PfiLdapConnection PfiM3Connection PfiMQConnection PfiReceiver PfiSMSConnection PfiServer PfiSystemCommandConnection PfiTXConnection PfiWebRunConnection PfiWebServiceConnection PfiWorkunitState Ping ProfileLog ProfileLogEntry ProfileLogIntermediateEntry '
    dbdeletedata_data_excludedtables = 'dbdeletedata ' + tp + table_list + '-Y'
    table_list_revert = 'dbimport -Cz ' + backup_tp + 'target.' + tp + '.excluded_tables.zip ' + tp + table_list + ' | tee ' + tp + '.table_list.revert.txt'
    print('\nReverting Configuration Data...................\n')
    subprocess.call(dbdeletedata_data_excludedtables, shell=True)
    print('')
    subprocess.call(table_list_revert, shell=True)
    completed_note()

def cleanup_workunits():
    workunits_tables = ' PfiWorkUnitInputData ActionRequest PfiActivity PfiActivityVariable PfiMetrics PfiMetricsSummary PfiQueue PfiQueueAction PfiQueueAssignment PfiQueueReminder PfiQueueTask PfiWorkunit PfiWorkunitFolder PfiWorkunitState PfiWorkunitVariable PfiErrorMessage -Y'
    delete_workunits = 'dbdeletedata ' + tp + workunits_tables + ' | tee ' + tp + '.delete.workunits.data.txt'
    backup_async_actionrequest = 'dbexport -Cz gen_AsyncActionRequest.zip gen AsyncActionRequest -f' + '"DataArea=\\' + '"' + tp + '\\""'
    delete_async_actionrequest = 'dbdeletedata gen AsyncActionRequest -f' + '"DataArea=\\' + '"' + tp + '\\"" -Y'
    print('\nRunning Cleanup of WorkUnits......\n')
    subprocess.call(delete_workunits, shell=True)
    print('')
    subprocess.call(backup_async_actionrequest, shell=True)
    print('')
    subprocess.call(delete_async_actionrequest, shell=True)
    completed_note()

def validations_after_sql_restore(tp):
    target_dbcount = 'dbcount ' + tp + ' | tee ' + tp + '.target.dcount.after.restore.txt'
    target_dbverify = 'dbverify -q ' + tp + ' | tee ' + tp + '.target.dbverify.after.restore.txt'
    print('\nRunning dbcount after restore of ' + tp)
    subprocess.call(target_dbcount, shell=True)
    print('\nRunning dbverify after restore of ' + tp)
    subprocess.call(target_dbverify, shell=True)
    completed_note()

def validations_after_refresh(tp):
    target_dbcount = 'dbcount ' + tp + ' | tee ' + tp + '.target.dcount.after.refresh.txt'
    target_cdverify = 'cdverify -ie ' + tp + ' | tee ' + tp + '.target.cdverify.after.refresh.txt'
    target_dbverify = 'dbverify -q ' + tp + ' | tee ' + tp + '.target.dbverify.after.refresh.txt'
    print('\nRunning dbcount after refresh of ' + tp)
    subprocess.call(target_dbcount, shell=True)
    print('\nRunning cdverify after refresh of ' + tp)
    subprocess.call(target_cdverify, shell=True)
    print('\nRunning dbverify after refresh of ' + tp)
    subprocess.call(target_dbverify, shell=True)
    completed_note()

def daimport_data(wrkdir, sp, tp, tool, cw):
    daimport_full = 'daimport --sameenv -ot 12 -w --deletedata -I ' + backup_sp + 'source.' + sp + '.dadata.full.zip ' + sp + '=' + tp + ' | tee ' + tp + '.daimport.txt'
    daimport_noWU = 'daimport --sameenv -ot 12 -w --deletedata -I ' + backup_sp + 'source.' + sp + '.dadata.NoWU.zip ' + sp + '=' + tp + ' | tee ' + tp + '.daimport.txt'
    daimport_env = 'daimport --sameenv -ot 12 -w --deletedata -I ' + backup_sp + 'source.' + sp + '.dadata.env.zip ' + sp + '=' + tp + ' | tee ' + tp + '.env.daimport.txt'
    daimport_l_full = 'daimport -l ' + backup_sp + 'source.' + sp + '.dadata.full.zip'
    daimport_l_noWU = 'daimport -l ' + backup_sp + 'source.' + sp + '.dadata.NoWU.zip'
    daimport_l_env = 'daimport -l ' + backup_sp + 'source.' + sp + '.dadata.env.zip'


#    admin_mode()
    os.chdir(wrkdir)
    if tool == 'LM' and cw == 'Y':
        print('\nRunning backup validation................')
        subprocess.call(daimport_l_noWU, shell=True)
        pause()
        print('\nRunning daimport from ' + sp + ' to ' + tp + '................')
        subprocess.call(daimport_noWU, shell=True)
        pause()
        dbimport_uapvenmast()
        dbimport_pfconfig()
        cleanup_workunits()

    elif tool == 'LM' and cw == 'N':
        print('\nRunning backup validation................')
        subprocess.call(daimport_l_full, shell=True)
        pause()
        print('\nRunning daimport from ' + sp + ' to ' + tp + '................')
        subprocess.call(daimport_full, shell=True)
        os.system("pause")
        dbimport_uapvenmast()
        dbimport_pfconfig()

    elif tool == 'SQL' and cw == 'Y':
        print('\nRunning backup validation................')
        subprocess.call(daimport_l_env, shell=True)
        pause()
        validations_after_sql_restore(tp)
        print('\nRunning daimport env data only from ' + sp + ' to ' + tp + '................')
        subprocess.call(daimport_env, shell=True)
        os.system("pause")
        revert_table_list()
        cleanup_workunits()
        dbimport_chp()

    elif tool == 'SQL' and cw == 'N':
        print('\nRunning backup validation................')
        subprocess.call(daimport_l_env, shell=True)
        pause()
        validations_after_sql_restore(tp)
        print('\nRunning daimport env data only from ' + sp + ' to ' + tp + '................')
        subprocess.call(daimport_env, shell=True)
        os.system("pause")
        revert_table_list()
        dbimport_chp()

    dbimport_pflows(pf)
    cdimport_data(cd)
    validations_after_refresh(tp)
    print('\n................System Restart................\n')
    pause()
    running_mode()

#---------------------------------------------------------main program

chg = args.chg
sp = args.sp
tp = args.tp
pf = args.pf
cd = args.cd
cw = args.cw

wrkdir = os.path.join('D:\\', 'lmsops', 'working', chg)
backup_sp = wrkdir + '\\SOURCE\\'
backup_tp = wrkdir + '\\TARGET\\'
choice = args.options

def main():
# -----------Menu
    if choice == 'lm-tool':
        tool = 'LM'
        daimport_data(wrkdir, sp, tp, tool, cw)

    elif choice == 'sql-tool':
        tool = 'SQL'
        daimport_data(wrkdir, sp, tp, tool, cw)
    else:
        print("Invalid option. You may use -h for references.")
    print("\nLog files are stored in: " + wrkdir)

if __name__ == '__main__':
    main()
