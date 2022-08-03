import os

from pyftpdlib import authorizers
from pyftpdlib.handlers import FTPHandler
from pyftpdlib import servers

def main():
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = authorizers.DummyAuthorizer()

    # Define a new user having full r/w permissions and a read-only
    # anonymous user
    authorizer.add_user('user', '12345', '.', perm='elradfmwMT')

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "hello client!"

    # Specify a masquerade address and the range of ports to use for
    # passive connections.  Decomment in case you're behind a NAT.
    #handler.masquerade_address = '151.25.42.11'
    #handler.passive_ports = range(60000, 65535)

    # Instantiate FTP server class and listen on 0.0.0.0:2121
    address = ('0.0.0.0', 2121)
    server = servers.FTPServer(address, handler)

    # start ftp server
    server.serve_forever()

if __name__ == '__main__':
    main()