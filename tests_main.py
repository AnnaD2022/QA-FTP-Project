import unittest
import os 

#main.py functions through interactions between the main body of this code and the date_logic function. To test I will run the entire script and interact with the GUI. The test will pass if the expected responses are returned and fail if not.

class mainUnitTest(unittest.TestCase):
      #Tests for the main

      def test_m1(self):
          #run the main.py script, select todays date
          os.system('python main.py')
          #test passed 18/08/2022

      def test_m2(self):
          #run the main.py script, select yesterdays date
          os.system('python main.py')
          #test passed 18/08/2022

      def test_m3(self):
          #run the main.py script, select tomorrows date
          os.system('python main.py')
          #test failed 18/08/2022 -> incorrect definition of 'messagebox'
          #test passed 18/08/2022 -> 'from tkinter import message box' added to main.py to enable message box to be displayed.


if __name__ == '__main__':
   unittest.main()