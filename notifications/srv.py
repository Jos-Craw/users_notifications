import paramiko

def sftp_get():
    local_path = 'D:/table/get_nf_direct'
    remote_path = '/netup/utm5/bin/get_nf_direct'

    t = paramiko.Transport('172.16.100.3', 22)
    t.connect(username='penovozhencev', password='admin')
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.get(remote_path, local_path)
    t.close()

if __name__ == '__main__':
    sftp_get()