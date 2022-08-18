import unittest
import os
import client
from client import download_files
#NOTE: server.py must be running in background

class downFilesUnitTest(unittest.TestCase):
      #tests for the client download_files function

      def test_cl1(self):
          #Check that a valid input returns a value that is not '-1'
          assert(download_files(2022,8,17) >= 0)
          #Passes 18/08/2022

      def test_cl2(self):
          #Check that a valid input returns a '-1' 
          #alter username
          client.user = "bob"

          #check error indicator is returned.
          self.assertEqual(download_files(2022,8,17),-1)

          #return username to valid version
          client.user = "user"
          #Passes 18/08/2022

      def test_cl3(self):
          #Check that a valid input returns a '-1' 
          #alter password
          client.password = "tempPassword"

          #check error indicator is returned.
          self.assertEqual(download_files(2022,8,17),-1)

          #return password to valid
          client.password = "verysecure123"
          #Passes 18/08/2022

      def test_cl4(self):
          #Check that an ivalid input returns a '0' as this function believes only valid inputs are being passed in - it would be called following date logic resolution 
          self.assertEqual(download_files(2093,8,17),0)
          #Passes 18/08/2022

if __name__ == '__main__':
   unittest.main()