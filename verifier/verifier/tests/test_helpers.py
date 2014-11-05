import unittest

from pprint import pprint
from verifier.modules import helpers



class TestHelpers(unittest.TestCase):

    def  test_get_value(self):
        x = {"test":1}
        
        self.assertEqual(helpers.get_value(x, "test", "default"), 1)

        self.assertEqual(helpers.get_value(x, "test1", "default"), "default")

        self.assertEqual(helpers.get_value(None, "test1", "default"), 
                         "default")


 

if __name__ == "__main__":
    unittest.main()

    
    