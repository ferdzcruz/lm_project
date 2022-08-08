from functions import *
import os
from parameters import dataset as params


# 1 : Create directory
chg = params["WorkingDirectory"]
subdir = params["EnvType"].upper()
workdir = os.path.join('D:\\', 'lmsops', 'working', chg,subdir)
create_folder(workdir)
os.chdir(workdir)