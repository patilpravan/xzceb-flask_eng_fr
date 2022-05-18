import unittest
from translator import englishToFrench, frenchToEnglish


class TestTranslator(unittest.TestCase):
    def test1_englishToFrench(self):
        self.assertNotEqual(englishToFrench('None'),'')

    def test2_englishToFrench(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')

    def test1_frenchToEnglish(self):
        self.assertNotEqual(englishToFrench('None'),'')     

    def test2_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
unittest.main()