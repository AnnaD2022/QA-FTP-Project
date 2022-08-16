import unittest
import pandas as pd

from os.path import exists
from validate_file import check_timestamp

class timeStampUnitTest(unittest.TestCase):
      #Tests for the validate_file module
      def test_cts1(self):
          # False should be returned as the file being checked contains all valid time stamps
          self.assertFalse(check_timestamp(pd.read_csv('./tests/testDoc1Valid.csv'),"testDoc1Valid.csv"))
          #Passes 12/08/2022

      def test_cts2(self):
          # True should be returned as the file being checked would be invalid.
          self.assertTrue(check_timestamp(pd.read_csv('./tests/testDoc5InvalidTS.csv'),"testDoc5InvalidTS.csv"))

          # A log file, etc should be generated as the file being used for testing contains invalid time stamp values
          self.assertTrue(exists('testDoc5InvalidTS_info.txt'))
          # Passed 12/08/2022
          #Passed 16/08/2022, check of return value in the instance of an invalid file added and name of returned file to check against modified to reflect change in code main code from '_log.txt' to '_info.txt' extension.

if __name__ == '__main__':
   unittest.main()