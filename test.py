import main
import unittest
import cv2

class main_functions_testing(unittest.TestCase):

    def test_case(self):
        pass

    def test_image_compression(self):
        pass

    def test_image_pixel_toarray_conversion(self):
        pass

    def test_out_put_from_the_Representational_function(self):
        self.assertEqual(main.Representational(1.2, 2.5, 4.3) ,  1.5664999999999998)
    
    def test_out_type_from_the_Represenatational(self):
        self.assertTrue(type(main.Representational(1.2, 2.5, 4.3)) == float)
    



if __name__ == '__main__':
    unittest.main()                   
    