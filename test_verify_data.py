import unittest
import pandas as pd

from validate_file import verify_data

class verifDataUnitTest(unittest.TestCase):
      #Tests for the validate_file module

      def test_vd1(self):   
          #tests a file with empty columns and invalid headings
          self.assertTrue(verify_data(pd.read_csv('./tests/testDoc2Invalid.csv'),"testDoc2Invalid.csv"))
          #Passes 16/08/2022

      def test_vd2(self): 
          #Should return false - this file is completely valid, check_Readings returns false if valid
          self.assertFalse(verify_data(pd.read_csv('./tests/testDoc1Valid.csv'),"testDoc1Valid.csv"))
          #Passes 16/08/2022

      def test_vd3(self): 
          self.assertTrue(verify_data(pd.read_csv('./tests/testDoc7.3Invalid.csv'),"testDoc7.3Invalid.csv"))
          #Passes 16/08/2022

      def test_vd4(self): 
          self.assertTrue(verify_data(pd.read_csv('./tests/testDoc7.4Invalid.csv'),"testDoc7.4Invalid.csv"))
          #Passes 16/08/2022

      def test_vd5(self): 
          #Testing checkID conditions are correctly applied
          self.assertTrue(verify_data(pd.read_csv('./tests/testDoc7.51Invalid.csv'),"testDoc7.51Invalid.csv"))
          #Passes 16/08/2022

      def test_vd52(self): 
          #Testing checkID conditions are correctly applied
          self.assertTrue(verify_data(pd.read_csv('./tests/testDoc7.52Invalid.csv'),"testDoc7.52Invalid.csv"))
          #Passes 16/08/2022

      def test_vd53(self):
          #checking checkID conditions are being correctly applied
          self.assertTrue(verify_data(pd.read_csv('./tests/testDoc7.53Invalid.csv'),"testDoc7.53Invalid.csv"))
          #Passes 16/08/2022

      def test_vd6(self): 
          self.assertTrue(verify_data(pd.read_csv('./tests/testDoc7.6Invalid.csv'),"testDoc7.6Invalid.csv"))
          #Passes 16/08/2022

      def test_vd7(self): 
          #Testing check readings conditions
          self.assertTrue(verify_data(pd.read_csv('./tests/testDoc7.71Invalid.csv'),"testDoc7.71Invalid.csv"))
          #Passes 16/08/2022

      def test_vd72(self): 
          #Testing check readings conditions
          self.assertTrue(verify_data(pd.read_csv('./tests/testDoc7.72nvalid.csv'),"testDoc7.72nvalid.csv"))
          #Passes 16/08/2022

if __name__ == '__main__':
   unittest.main()