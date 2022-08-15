import unittest
import pandas as pd

from os.path import exists
from validate_file import check_header

class HeaderUnitTest(unittest.TestCase):
      #Tests for the validate_file module
      def test_ch1(self):
          # should return without issue as its is testing a file with valid headings
          self.assertFalse(check_header(pd.read_csv('./tests/testDoc1Valid.csv'),"testDoc1Valid.csv"))
           # Passed 12/08/2022
     
      def test_ch2(self):
          # check the correct value is returned
          self.assertFalse(check_header(pd.read_csv('./tests/testDoc2invalid.csv'),"testDoc2invalid.csv"))

          # checks log file is generated following incorrect heading inclusion
          self.assertTrue(exists('testDoc2invalid_log.txt'))
          # Passed 12/08/2022

      def test_ch3(self):
          #check true is returned
          self.assertTrue(check_header(pd.read_csv('./tests/testDoc2.1Invalid.csv'),"testDoc2.1Invalid.csv"))

          #checks log file is generated following identification of an additional heading
          self.assertTrue(exists('testDoc2.1Invalid_log.txt'))

      def test_ch4(self):
          #False should be returned in this instance
          self.assertFalse(check_header(pd.read_csv('./tests/testDoc3InvalidRC.csv'),"testDoc3InvalidRC.csv"))

           #checks log file is generated following identification of a deleted heading
          self.assertTrue(exists('testDoc3InvalidRC_log.txt'))         
      # Passed 12/08/2022

if __name__ == '__main__':
   unittest.main()