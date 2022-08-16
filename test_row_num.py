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
          #True should be returned as this file would be invalid
          self.assertTrue(check_num_rows(pd.read_csv('./tests/testDoc3InvalidRC.csv'),"testDoc3InvalidRC.csv"))

          # A log file containing error messages, etc should be produced as test file passed in has fewer rows then required.
          self.assertTrue(exists('testDoc3InvalidRC_info.txt'))
          # Passed 12/08/2022
          #Passes 16/08/2022 -> check of return value logic added, name of returned file to check against has also been modified to reflect change in main code from a '_log.txt' extension to '_text.info'

if __name__ == '__main__':
   unittest.main()