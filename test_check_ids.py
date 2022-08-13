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
          #True will be returned as an invalid batch id is present in the test file
          self.assertTrue(check_ids(pd.read_csv('./tests/testDoc4DupBID.csv'),"testDoc4DupBID.csv"))

          # A log file should be created as test file used has duplicate batch ID's          
          self.assertTrue(exists('testDoc4DupBID_log.txt'))
           # Passed 12/08/2022
           # Passed 13/08/2022 - checking returned value logic added

      def test_cid3(self):
          #True will be returned as an invalid batch id is present in the test file
          self.assertTrue(check_ids(pd.read_csv('./tests/testDoc4NegBID.csv'),"testDoc4NegBID.csv"))        
          # A log file, etc should be created as test file used contains a negative batch ID's
          self.assertTrue(exists('testDoc4NegBID_log.txt'))
           # Passed 12/08/2022
           # Passed 13/08/2022 - checking returned value logic added

      def test_cid4(self):
          #True will be returned as an invalid batch id is present in the test file
          self.assertTrue(check_ids(pd.read_csv('./tests/testDoc4StrBID.csv'),"testDoc4StrBID.csv"))
         
          # A log file, etc should be created as test file used contains a batch ID of type string
          self.assertTrue(exists('testDoc4StrBID_log.txt'))
           # Passed 12/08/2022
           # Passed 13/08/2022 - checking returned value logic added

if __name__ == '__main__':
   unittest.main()