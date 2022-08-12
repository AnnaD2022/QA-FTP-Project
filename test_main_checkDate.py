import unittest

from main import checkDate

class ColNumUnitTest(unittest.TestCase):
      #Tests for the main module

      def cd1(self):
          #check filenames array contains the correct filenames
          checkDate()
          self.assertEqual(["20210701153942.csv","20210701153947.csv","20210701153948.csv", "20210701153952.csv", "20210701153954.csv", "20220803153918.csv", "20220803153920.csv", "20220803153921.csv", "20220803153922.csv", "20220803153923.csv", "20220803153925.csv", "20220803153927.csv", "20220803153928.csv", "20220803153929.csv", "20220803153931.csv", "20220803153932.csv", "20220803155851.csv", "20220803155852.csv" , "20220803155853.csv" , "20220803155854.csv" , "20220803155855.csv" , "20220803155856.csv" , "20220803155857.csv" , "20220803155858.csv" , "20220803155859.csv" , "20220803155900.csv" , "20220803155901.csv" , "20220803160722.csv" , "20220803160723.csv" , "20220803160724.csv" , "20220803160725.csv" , "20220803160726.csv" , "20220803160727.csv" , "20220803160728.csv" , "20220803160729.csv" , "20220803160730.csv", "20220803160731.csv", "20220803160732.csv"], main.filenames)

      def cd2(self):
          #check dates array contains the correct dates
          checkDate()
          self.assertEqual(["2021/07/01","2021/07/01","2021/07/01", "2021/07/01", "2021/07/01", "2022/08/03", "2022/08/03", "2022/08/03", "2022/08/03", "2022/08/03", "2022/08/03", "2022/08/03", "2022/08/03", "2022/08/03", "2022/08/03", "2022/08/03", "2022/08/03", "2022/08/03", "2022/08/03" , "2022/08/03" , "2022/08/03" , "2022/08/03" , "2022/08/03" ,"2022/08/03" , "2022/08/03","2022/08/03" , "2022/08/03" , "2022/08/03" , "2022/08/03" , "2022/08/03" , "2022/08/03" , "2022/08/03" , "2022/08/03" , "2022/08/03" , "2022/08/03" , "2022/08/03", "2022/08/03", "2022/08/03"], main.dates)


if _name_ == 'main':
   unittest.main(verebosity=2)