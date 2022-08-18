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
          #Passes 13/08/2022 - type check in validate_file fixed

      def test_cr2(self):
          #True should be returned
          self.assertTrue(check_readings(pd.read_csv('./tests/testDoc6.1notfloar.csv'),"testDoc6.1notfloar.csv"))

          # A log file containing error messages, etc should be produced as test file passed in has vlues of the wrong type.
          self.assertTrue(exists('testDoc6.1notfloar_info.txt'))

          #Passed 12/08/2022
          #Passed 16/08/2022 - name of returned file altered to match the change in main code from '_log.txt' to '_info.txt'

      def test_cr3(self):
          #True should be returned
          self.assertTrue(check_readings(pd.read_csv('./tests/testDoc6.2RangeDP.csv'),"testDoc6.2RangeDP.csv"))

          # A log file containing error messages, etc should be produced as test file passed in has incorrectly rounded readings.
          self.assertTrue(exists('testDoc6.2RangeDP_info.txt'))

          #Passed 12/08/2022
          #Passed 16/08/2022 - name of returned file altered to match the change in main code from '_log.txt' to '_info.txt'


if __name__ == '__main__':
   unittest.main()