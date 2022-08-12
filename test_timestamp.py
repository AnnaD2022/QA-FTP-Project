import unittest
import pandas as pd

from os.path import exists
from validate_file import check_timestamp

class colNumUnitTest(unittest.TestCase):
      #Tests for the validate_file module
      def test_cts1(self):
          # False should be returned as the file being checked contains all valid time stamps
          self.assertFalse(check_timestamp(pd.read_csv('./tests/testDoc1Valid.csv'),"testDoc1Valid.csv"))
          #Passes 12/08/2022

      def test_cts2(self):
          # A log file, etc should be generated as the file being used for testing contains invalid time stamp values
          check_timestamp(pd.read_csv('./tests/testDoc5InvalidTS.csv'),"testDoc5InvalidTS.csv")
          self.assertTrue(exists('testDoc5InvalidTS_log.txt'))
          # Passed 12/08/2022

if __name__ == '__main__':
   unittest.main()