#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_b.question_b import get_most_likely_ancestor_consensus

class Test_Config(unittest.TestCase):

    def test_question_b_config(self):

        anything  = get_most_likely_ancestor_consensus( "GATATATGCATATACTT", "ATAT" )
        varible1 = anything[0] 
        varible2 = anything[1]
        varible3 = anything[2]

        self.assertEqual(varible1, 2)
        self.assertEqual(varible2, 4)
        self.assertEqual(varible3, 10)
        
        

