import unittest
import pandas as pd

from os.path import exists
from validate_file import check_ids

class IdUnitTest(unittest.TestCase):
      #Tests for the validate_file module
      def test_cid1(self):
          # should return False as test file used has all valid ID's
          self.assertFalse(check_ids(pd.read_csv('./tests/testDoc1Valid.csv'),"testDoc1Valid.csv"))
           # Passed 12/08/2022

      def test_cid2(self):
          # A log file should be created as test file used has duplicate batch ID's
          check_ids(pd.read_csv('./tests/testDoc4DupBID.csv'),"testDoc4DupBID.csv")
          self.assertTrue(exists('testDoc4DupBID_log.txt'))
           # Passed 12/08/2022


      def test_cid3(self):
          # A log file, etc should be created as test file used contains a negative batch ID's
          check_ids(pd.read_csv('./tests/testDoc4NegBID.csv'),"testDoc4NegBID.csv")
          self.assertTrue(exists('testDocNegBID_log.txt'))
           # Passed 12/08/2022
      def test_cid4(self):
          # A log file, etc should be created as test file used contains a batch ID of type string
          check_ids(pd.read_csv('./tests/testDoc4StrBID.csv'),"testDoc4StrBID.csv")
          self.assertTrue(exists('testDoc4StrBID_log.txt'))
           # Passed 12/08/2022

if __name__ == '__main__':
   unittest.main()