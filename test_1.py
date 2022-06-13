import unittest
import io
import sys
from sales_tax import sales_object

class test_1(unittest.TestCase):
    
    
    def test_input1(self):
        compare_string=["1 book: 12.49","1 music CD: 16.49","1 chocolate bar: 0.85","Sales Taxes: 1.50","Total: 29.83"]
        self.assertEqual (sales_object.sales_tax_calculator(["1 book at 12.49","1 music CD at 14.99","1 chocolate bar at 0.85"]),compare_string,"failed test")
    def test_input2(self):
         compare_string=["1 imported box of chocolates: 10.50","1 imported bottle of perfume: 54.65","Sales Taxes: 7.65","Total: 65.15"]
         self.assertEqual (sales_object.sales_tax_calculator(["1 imported box of chocolates at 10.00","1 imported bottle of perfume at 47.50"]),compare_string,"failed test")
    def test_input3(self):
        compare_string=["1 imported bottle of perfume: 32.19","1 bottle of perfume: 20.89","1 packet of headache pills: 9.75","1 box of imported chocolates: 11.85","Sales Taxes: 6.70","Total: 74.68"]
        self.assertEqual (sales_object.sales_tax_calculator(["1 imported bottle of perfume at 27.99","1 bottle of perfume at 18.99","1 packet of headache pills at 9.75","1 box of imported chocolates at 11.25"]),compare_string,"failed test")



if __name__ == '__main__':
    unittest.main()

