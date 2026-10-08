import unittest
from scanner import rank

class ShadowScannerTests(unittest.TestCase):
    def test_valid_quote(self):
        t={"c":["10"],"o":"10","v":["0","10000"],"t":[0,500],"b":["9.99"],"a":["10.01"]}
        self.assertGreater(rank(t)["score"],0)
    def test_crossed_quote_rejected(self):
        t={"c":["10"],"o":"10","v":["0","10000"],"t":[0,500],"b":["10.02"],"a":["10.01"]}
        with self.assertRaises(ValueError):
            rank(t)
    def test_zero_open_rejected(self):
        t={"c":["10"],"o":"0","v":["0","10000"],"t":[0,500],"b":["9.99"],"a":["10.01"]}
        with self.assertRaises(ValueError):
            rank(t)

if __name__=="__main__": unittest.main()
