import unittest

from validate_file import verify_data

class verifDataUnitTest(unittest.TestCase):
      #Tests for the validate_file module

      def test_vd1(self):     
          self.assertTrue(check_header(pd.read_csv('./tests/testDoc2Invalid.csv'),"testDoc2Invalid.csv"))

      def test_vd2(self): 
          self.assertTrue(check_header(pd.read_csv('./tests/testDoc1Valid.csv'),"testDoc1Valid.csv"))

      def test_vd3(self): 
          self.assertTrue(check_header(pd.read_csv('./tests/testDoc7.3Invalid.csv'),"testDoc7.3Invalid.csv"))

      def test_vd4(self): 
          self.assertTrue(check_header(pd.read_csv('./tests/testDoc7.4Invalid.csv'),"testDoc7.4Invalid.csv"))

      def test_vd5(self): 
          self.assertTrue(check_header(pd.read_csv('./tests/testDoc7.51Invalid.csv'),"testDoc7.51Invalid.csv"))

      def test_vd5.2(self): 
          self.assertTrue(check_header(pd.read_csv('./tests/testDoc7.52Invalid.csv'),"testDoc7.52Invalid.csv"))

      def test_vd5.3(self): 
          self.assertTrue(check_header(pd.read_csv('./tests/testDoc7.53Invalid.csv'),"testDoc7.53Invalid.csv"))

      def test_vd6(self): 
          self.assertTrue(check_header(pd.read_csv('./tests/testDoc7.6Invalid.csv'),"testDoc7.6Invalid.csv"))

      def test_vd7(self): 
          self.assertTrue(check_header(pd.read_csv('./tests/testDoc7.71Invalid.csv'),"testDoc7.71Invalid.csv"))

      def test_vd7.2(self): 
          self.assertTrue(check_header(pd.read_csv('./tests/testDoc7.72nvalid.csv'),"testDoc7.72nvalid.csv"))

if __name__ == '__main__':
   unittest.main()