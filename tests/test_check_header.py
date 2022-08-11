import unittest
import pandas

from validate_file import check_header

class HeaderUnitTest(unittest.TestCase):
      ""Tests for the validate_file module""
#need to check
      def test_return_type(self):
          ""should return a boolean""
          self.assertIsInstance(check_header(pandas.read_csv(testDoc1Valid.csv),testDoc1Valid),bool)
          

if _name_ == 'main':
   unittest.main(verebosity=2)