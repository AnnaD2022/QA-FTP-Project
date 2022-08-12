import unittest
import pandas as pd

from os.path import exists
from validate_file import remove_empty

class EmptyUnitTest(unittest.TestCase):
      #Tests for the validate_file module
      def test_re1(self):
          # should return without issue as its is testing a file without any missing values
          self.assertFalse(remove_empty(pd.read_csv('./tests/testDoc1Valid.csv'),"testDoc1Valid.csv"))
          #Passes 12/08/2022  

      def test_re2(self):
          # should produce a log file, etc as file being tested has missing values
          remove_empty(pd.read_csv('./tests/testDoc2invalid.csv'),"testDoc2invalid.csv")
          self.assertTrue(exists('testDoc2invalid_log.txt'))  
          #Passes 12/08/2022   

if __name__ == '__main__':
   unittest.main()