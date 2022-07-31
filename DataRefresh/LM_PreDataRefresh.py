# -------------------------------------------------------module
import subprocess
import os
import errno
import argparse
parser = argparse.ArgumentParser(description='Landmark Pre Data Refresh')
parser.add_argument('-c', '--chg', required=True, help="ServiceNow Change number/Working Directory")
parser.add_argument('-p', '--pl', required=True, help="SOURCE/TARGET productline")
parser.add_argument('-ip', '--ipaddress', help="TARGET ipaddress")
parser.add_argument('-o', '--options', required=True, help="Options", choices=["src-lm-nowu", "src-lm-full", "src-sql", "tgt-lm", "tgt-sql"])
args = parser.parse_args()

# --------------------------------------------------------Global Variables

pfworkunits = '--ignore PfiWorkUnitInputData,AsyncActionRequest,ActionRequest,PfiActivity,PfiActivityVariable,PfiMetrics,PfiMetricsSummary,PfiQueue,PfiQueueAction,PfiQueueAssignment,PfiQueueReminder,PfiQueueTask,PfiWorkunit,PfiWorkunitFolder,PfiWorkunitState,PfiWorkunitVariable,PfiErrorMessage '
pflows = ' PfiFlowDefinition PfiFlowVersion PfiServiceDefinition PfiServiceFlowDefinition PfiServiceVariable PfiTrigger PfiTriggerFolder PfiTriggerVariable '
pficonfig = ' PfiChannel PfiConfiguration PfiConfigurationProperty PfiClassicConnection PfiFTPConnection PfiFrontOfficeConnection PfiJDBCConnection PfiJMSConnection PfiLandmarkConnection PfiM3Connection PfiMQConnection PfiSystemCommandConnection PfiTXConnection PfiWebRunConnection '
excluded_table_list = ' SecurityClass ContextProperty ConfigurationParameter OAuth PfiChannel PfiChannelField PfiClassicConnection PfiCloverleafConnection PfiComparisonActivity PfiComparisonWorkunit PfiConfiguration PfiConfigurationProperty PfiEDICarrier PfiEDIWorkFile PfiEmailConnection PfiEventHubConnection PfiFTPConnection PfiFileActivityConnection PfiFrontOfficeConnection PfiIONConnection PfiJDBCConnection PfiJMSConnection PfiLandmarkConnection PfiLdapConnection PfiM3Connection PfiMQConnection PfiReceiver PfiSMSConnection PfiServer PfiSystemCommandConnection PfiTXConnection PfiWebRunConnection PfiWebServiceConnection PfiWorkunitState Ping ProfileLog ProfileLogEntry ProfileLogIntermediateEntry '

# --------------------------------------------------------function
def completed_note():
    print('\n ...................completed...................\n')

def pre_datarefresh(env, wrkdir, pl, tool, workunits):
    subdir = env.upper()
    os.mkdir(wrkdir + '\\' + subdir)
    os.chdir(wrkdir + '\\' + subdir)
    dbcount_gen = 'dbcount gen | tee dbcount_gen.txt'
    export_gen_ruiprofile = str('dbexport -Cz gen_' + pl + '_RoamingUIProfile.zip gen RoamingUIProfile -f' + '"DataArea=\\' + '"' + pl + '\\""' + ' | tee ' + pl + '.target.roaminguiprofile.txt')
    export_gen_rolesecclass = str('dbexport -Cz gen_' + pl + '_RoleSecurityClass.zip gen RoleSecurityClass -f' + '"DataArea=\\' + '"' + pl + '\\""' + ' | tee ' + pl + '.target.rolesecurityclass.txt')
    dadata_env = 'daexport -t 12 -ez ' + env + '.' + pl + '.dadata.env.zip ' + pl + ' | tee ' + pl + '.' + env + '.env.dadata.txt'
    dadata_noWU = 'daexport -t 12 -z ' + env + '.' + pl + '.dadata.NoWU.zip ' + pfworkunits + pl + ' | tee ' + pl + '.' + env + '.noWU.dadata.txt'
    dadata_full = 'daexport -t 12 -z ' + env + '.' + pl + '.dadata.full.zip ' + pl + ' | tee ' + pl + '.' + env + '.full.dadata.txt'
    pfiflows = 'dbexport -Cz ' + env + '.' + pl + '.pflows.zip ' + pl + pflows + ' | tee ' + pl + '.' + env + '.pfiflow.txt'
    pfconfig = 'dbexport -Cz ' + env + '.' + pl + '.pficonfig.zip ' + pl + pficonfig + ' | tee ' + pl + '.' + env + '.pficonfig.txt'
    excluded_tables = 'dbexport -Cz ' + env + '.' + pl + '.excluded_tables.zip ' + pl + excluded_table_list + ' | tee ' + pl + '.excluded_tables.txt'
    chp_export = 'dbexport -Cz ' + env + '.' + pl + '.CHP.zip ' + pl + ' CHP ' + ' | tee ' + pl + '.' + env + '.chp.txt'
    u_apvenmast_export = 'dbexport -Cz ' + env + '.' + pl + '.u_apvenmast.zip ' + pl + ' u_apvenmast ' + ' | tee ' + pl + '.' + env + '.u_apvenmast.txt'
    cddata = 'cdexport -z ' + env + '.' + pl + '.cddata.zip ' + pl + ' | tee ' + pl + '.' + env + '.' + 'cddata.txt'
    cddatasec = 'cdexport -z ' + env + '.' + pl + '.cddata.security.zip --authsecurity ' + pl + ' | tee ' + pl + '.' + env + '.' + 'cddata.security.txt'
    dbcount = 'dbcount ' + pl + ' | tee ' + pl + '.' + env + '.dcount.txt'
    dbverify = 'dbverify -q ' + pl + ' | tee ' + pl + '.target.dbverify.txt'
    cdverify = 'cdverify -ie ' + pl + ' | tee ' + pl + '.target.cdverify.txt'

    # main course
    print('\nSystem Current Version is :\n')
    subprocess.call(['univver', '-a'], shell=True)
    print('')
    os.system("pause")
    if env == 'source' and workunits == 'NO' and tool =='LANDMARK':
        print('\nRunning daexport with no workunits................')
        subprocess.call(dadata_noWU, shell=True)
        print('\nRunning export of u_apvenmast_export................')
#for lmscm product
        subprocess.call(u_apvenmast_export, shell=True)
        completed_note()

    elif env == 'source' and workunits == 'YES' and tool =='LANDMARK':
        print('\nRunning full daexport................')
        subprocess.call(dadata_full, shell=True)
        print('\nRunning export of u_apvenmast_export................')
        subprocess.call(u_apvenmast_export, shell=True)
        completed_note()

    elif env == 'source' and tool == 'SQL':
        print('\nRunning daexport environment................')
        subprocess.call(dadata_env, shell=True)
        completed_note()

    elif env == 'target' and tool == 'LANDMARK':
        print('\nRunning full daexport................')
        subprocess.call(dadata_full, shell=True)
        completed_note()
        print('\nRunning pficonfig export................')
        subprocess.call(pfconfig, shell=True)
        print('\nRunning dbverify................')
        subprocess.call(dbverify, shell=True)
        print('\nRunning cdverify................')
        subprocess.call(cdverify, shell=True)
        print('\nRunning export of RoleSecClass and RoamingUIProfile................')
        subprocess.call(export_gen_rolesecclass, shell=True)
        subprocess.call(export_gen_ruiprofile, shell=True)
        print('\nRunning dbcount................')
        subprocess.call(dbcount_gen, shell=True)

    elif env == 'target' and tool == 'SQL':
        print('\nRunning daexport environment................')
        subprocess.call(dadata_env, shell=True)
        completed_note()
        print('\nRunning export of excluded tables................')
        subprocess.call(excluded_tables, shell=True)
        print('\nRunning pficonfig export................')
        subprocess.call(pfconfig, shell=True)
        print('\nRunning dbverify................')
        subprocess.call(dbverify, shell=True)
        print('\nRunning cdverify................')
        subprocess.call(cdverify, shell=True)
        print('\nRunning export of RoleSecClass and RoamingUIProfile................')
        subprocess.call(export_gen_rolesecclass, shell=True)
        subprocess.call(export_gen_ruiprofile, shell=True)
        print('\nRunning dbcount................')
        subprocess.call(dbcount_gen, shell=True)
# To revert different prodline name
        print('\nRunning export of CHP................')
        subprocess.call(chp_export, shell=True)

    print('\nRunning cdexport................')
    subprocess.call(cddata, shell=True)
    print('\nRunning cdexport security only................')
    subprocess.call(cddatasec, shell=True)
    print('\nRunning pflows export................')
    subprocess.call(pfiflows, shell=True)
#    print('\nRunning dbcount................')
#   subprocess.call(dbcount, shell=True)
#    print('\nRunning export of identities................')
#    subprocess.call(gen_identities, shell=True)
    completed_note()

def create_folder(wrkdir):
    try:
        os.makedirs(wrkdir)
        print("Folder " + wrkdir + " created.")
    except OSError as fe:
        if fe.errno == errno.EEXIST:
            print("Folder " + wrkdir + " already exists.")
        else:
            raise
    os.chdir(wrkdir)

def transfer_files(wrkdir,ipaddress):
    copy_files = 'xcopy /S /I /E *.* ' + '\\\\' + ipaddress + '\D$\lmsops\working\\' + chg + '\\SOURCE'
    subprocess.call(copy_files, shell=True)

# ---------------------------------------------------------main program
chg = args.chg
pl = args.pl
wrkdir = os.path.join('D:\\', 'lmsops', 'working', chg)
choice = args.options
create_folder(wrkdir)
ipaddress = args.ipaddress

# -----------Menu

def main():
    if choice == 'src-lm-nowu':
        env = 'source'
        workunits = 'NO'
        tool = 'LANDMARK'
        pre_datarefresh(env, wrkdir, pl, tool, workunits)
        transfer_files(wrkdir, ipaddress)

    elif choice == 'src-lm-full':
        env = 'source'
        workunits = 'YES'
        tool = 'LANDMARK'
        pre_datarefresh(env, wrkdir, pl, tool, workunits)
        transfer_files(wrkdir, ipaddress)

    elif choice == 'src-sql':
        workunits = 'YES'
        env = 'source'
        tool = 'SQL'
        pre_datarefresh(env, wrkdir, pl, tool, workunits)
        transfer_files(wrkdir, ipaddress)
    elif choice == 'tgt-lm':
        workunits = 'YES'
        env = 'target'
        tool = 'LANDMARK'
        pre_datarefresh(env, wrkdir, pl, tool, workunits)
    elif choice == 'tgt-sql':
        workunits = 'YES'
        env = 'target'
        tool = 'SQL'
        pre_datarefresh(env, wrkdir, pl, tool, workunits)
    else:
        print("Invalid option. You may use -h for references.")
    print("\nLog files are stored in: " + wrkdir)






