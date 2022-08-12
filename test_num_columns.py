import unittest
import pandas as pd

from os.path import exists
from validate_file import check_num_columns

class ColNumUnitTest(unittest.TestCase):
      #Tests for the validate_file module
      def test_cnc1(self):
          # False should be returned as the file being checked has the desired number of columns
          self.assertFalse(check_num_columns(pd.read_csv('./tests/testDoc1Valid.csv'),"testDoc1Valid.csv"))
          #Passes 12/08/2022

      def test_cnc2(self):
          # A log file containing error messages, etc should be produced as test file passed in has unwanted additional comlumns
          check_num_columns(pd.read_csv('./tests/testDoc2.1Invalid.csv'),"testDoc2.1Invalid.csv")
          self.assertTrue(exists('testDoc2.1Invalid_log.txt'))
          #Passes 12/08/2022

if __name__ == '__main__':
   unittest.main()