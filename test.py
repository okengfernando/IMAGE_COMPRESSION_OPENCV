import main
import unittest
import cv2

class main_functions_testing(unittest.TestCase):

    def test_case(self):
        pass

    def test_out_from_the_Representational_function(self):
        self.assertEqual(main.Representational(1.2, 2.5, 4.3) ,  1.5664999999999998)
    



if __name__ == '__main__':
    unittest.main()                   
    