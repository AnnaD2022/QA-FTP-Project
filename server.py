import os

from pyftpdlib import authorizers
from pyftpdlib.handlers import FTPHandler
from pyftpdlib import servers

##!!Change username and password before running for security
user = "user"
password = "verysecure123"

##Server function
def main(user, password):
    ##DummyAuthorizer is used for managing users that can connect
    authorizer = authorizers.DummyAuthorizer()

    ##Create a basic user with permissions to list files/folders and
    ##read/download them. Folder shown is ./files
    authorizer.add_user(user, password, './server_files', perm='lr')

    ##Initialises Handler, allows client to run FTP commands
    handler = FTPHandler
    handler.authorizer = authorizer

    ##Create FTP server and set to listen on 0.0.0.0:2121 -- allows
    ##local network connections
    address = ('0.0.0.0', 2121)
    server = servers.FTPServer(address, handler)

    ##Start server, listens indefinitely
    server.serve_forever()

##Run server
if __name__ == '__main__':
    main(user, password)
