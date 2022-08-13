import unittest
import os

from main import checkDate

class ColNumUnitTest(unittest.TestCase):
      #Tests for the main module

      def test_cd1(self):
          #test purpose: check filenames array contains the correct filenames
          #run CheckDate function
          checkDate()

          #go through the directory that checkDate references, count the number of csv files <- indicates howmany file names you should have in the filenames array
          x = 0 #will count the number of csv files present in checkDate referenced directory
          for filename in os.listdir(checkDate.path):
              if filename.endswith('.csv'):
                 x += 1

          #compare the expeted number of filenames with actual number.
          self.assertEqual(x,len(checkDate.filenames))
          #passes 13/08/2022

      def test_cd2(self):
          #test purpose: check dates array contains the correct dates
          #run CheckDate function
          checkDate()

          #go through the directory that checkDate references, count the number of csv files <- indicates howmany dates you should have in the dates array
          x = 0 #will count the number of csv files present in checkDate referenced directory
          for filename in os.listdir(checkDate.path):
              if filename.endswith('.csv'):
                 x += 1

          #compare the expeted number of filenames with actual number.
          self.assertEqual(x,len(checkDate.dates))
          #passes 13/08/2022


if __name__ == '__main__':
   unittest.main()