import unittest
import pandas as pd

from os.path import exists
from validate_file import check_num_rows

class RowNumUnitTest(unittest.TestCase):
      #Tests for the validate_file module""
      def test_cnr1(self):
          # False should be returned as the file being checked has the desired number of rows
          self.assertFalse(check_num_rows(pd.read_csv('./tests/testDoc1Valid.csv'),"testDoc1Valid.csv"))
          #Passes 12/08/2022

      def test_cnr2(self):
          # A log file containing error messages, etc should be produced as test file passed in has fewer rows then required.
          check_num_rows(pd.read_csv('./tests/testDoc3InvalidRC.csv'),"testDoc3InvalidRC.csv")
          self.assertTrue(exists('testDoc3InvalidRC_log.txt'))
          # Passed 12/08/2022

if __name__ == '__main__':
   unittest.main()