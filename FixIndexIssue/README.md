This is utility will fix the issue on index mismatch
  1. varchar setting
  2. Charset setting

1. download the zip file from here : https://github.com/ferdzcruz/lm_project/archive/refs/heads/master.zip
2. extract it in D:\lmenv\scripts
3. Open Landmark Terminal, access D:\lmenv\scripts\lm_project-master\FixIndexIssue\
4. run FixIndexMismatch.py with the parameter 
ex : FixIndexMismatch.py -p pristine -o varchar -wd 11172021


Example Usage:
D:\lmenv\scripts\FixIndexMisMatch>FixIndexMismatch.py -h
usage: FixIndexMismatch.py [-h] -p  -wd  -o

To Fix the Index Mismatch

optional arguments:
  -h, --help            show this help message and exit
  -p , --prodline       Enter dataarea ex: lmghr
  -wd , --working_directory
                        Enter working directory ex: CHG12345
  -o , --option         Enter what is needed to fix


