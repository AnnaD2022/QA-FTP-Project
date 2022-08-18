import unittest
import os
import client
from client import download_files

class downFilesUnitTest(unittest.TestCase):
      #tests for the client download_files function

      def test_cl1(self):
          #Check that a valid input returns a value that is not '-1'
          self.assertEqual(download_files(2022,8,17), 0)

      def test_cl2(self):
          #Check that a valid input returns a '-1' 
          #alter username
          client.user = "bob"

          #check error indicator is returned.
          self.assertEqual(download_files(2022,8,17),-1)

          #return username to valid version
          client.user = "user"

      def test_cl3(self):
          #Check that a valid input returns a '-1' 
          #alter password
          client.password = "tempPassword"

          #check error indicator is returned.
          self.assertEqual(download_files(2022,8,17),-1)

          #return password to valid
          client.password = "verysecure123"

      def test_cl4(self):
          #Check that a valid input returns a '-1' 
          self.assertEqual(download_files(2023,8,17),-1)

if __name__ == '__main__':
   unittest.main()