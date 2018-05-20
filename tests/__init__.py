import os
import sys
import unittest

base_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
sys.path.append(base_path)


import apertium as a # noqa: E402

class TestAnalyze(unittest.TestCase):
    def test_en(self):
        # TODO: test the LexicalUnit object instead! (see streamparser tests)
        self.assertEqual(str(a.analyze('cats', 'en')), 'cats/cat<n><pl>')

class TestGenerate(unittest.TestCase):
    def test_en(self):
        # TODO: test the LexicalUnit object instead! (see streamparser tests)
        self.assertEqual(str(a.generate('cat<n><pl>', 'en')), 'cats')