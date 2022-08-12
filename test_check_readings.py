import unittest
import pandas as pd

from os.path import exists
from validate_file import check_readings

class checkReadingUnitTest(unittest.TestCase):
      #Tests for the validate_file module
      def test_cr1(self):
          # False should be returned as the file being checked has the desired number of readings
          self.assertFalse(check_readings(pd.read_csv('./tests/testDoc1Valid.csv'),"testDoc1Valid.csv"))
          #Fails 12/08/2022

      def test_cr2(self):
          # A log file containing error messages, etc should be produced as test file passed in has integer values.
          check_readings(pd.read_csv('./tests/testDoc6.1notfloar.csv'),"testDoc6.1notfloar.csv")
          self.assertTrue(exists('testDoc6.1notfloar_log.txt'))
          #Passed 12/08/2022

      def test_cr3(self):
          # A log file containing error messages, etc should be produced as test file passed in has incorrectly rounded readings.
          check_readings(pd.read_csv('./tests/testDoc6.2RangeDP.csv'),"testDoc6.2RangeDP.csv")
          self.assertTrue(exists('testDoc6.2RangeDP_log.txt'))
          #Passed 12/08/2022


if __name__ == '__main__':
   unittest.main()