from ftplib import FTP

# Connect and login at once
with FTP(host='ftp.scene.org', user='ftp', passwd='email@example.com') as ftp:
    print(ftp.getwelcome())
    ftp.dir()
    ftp.close()