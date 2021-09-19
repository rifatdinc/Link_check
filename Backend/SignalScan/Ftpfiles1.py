#!/usr/bin/python3
from ftplib import FTP
from datetime import datetime
import os
from pathlib import Path



def ftpDownload(filesname,ip):
    ftp = FTP(ip)
    ftp.login('admin','mc4152')

    # Get All Files
    files = ftp.nlst(filesname)
    getcurend = os.path.realpath(__file__)
    path = Path(getcurend)

    # Print out the files
    for file in files:

        
        ftp.retrbinary("RETR " + file ,open(os.path.dirname(path.parent.absolute())+'/'+ file, 'wb').write)

    ftp.close()

