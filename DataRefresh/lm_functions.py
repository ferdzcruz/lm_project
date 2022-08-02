from os import mkdir, chdir
import os, errno
from global_vars import *
import backup_parameters as args

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


#Backup


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
        return f"dbexport -Cz {self.env}.{self.pl}.excluded_tables.zip {self.pl} {excluded_table_list} | tee {self.pl}.excluded_tables.txt "




# def Completed_note():
#     print('\n ...................completed...................\n')

