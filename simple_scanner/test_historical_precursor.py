import sqlite3
import unittest
from simple_scanner.historical_precursor import crypto_pair, rank_precursors, evaluate_precursor

class PrecursorTests(unittest.TestCase):
    def test_excludes_fiat_and_stable(self):
        for pair in ('ZEURZUSD','ZGBPZUSD','USDTUSD','USDCUSD'):
            self.assertFalse(crypto_pair(pair))
        self.assertTrue(crypto_pair('XXBTZUSD'))
        self.assertTrue(crypto_pair('TAOUSD'))

    def test_early_acceleration_and_budget(self):
        rows=[('EARLYUSD',1,10,100000,100,101,100),('LATEUSD',30,10,100000,100,101,100),('ZEURZUSD',1,1,1000000,100,101,100)]
        result=rank_precursors(rows,limit=1)
        self.assertEqual([x['pair'] for x in result],['EARLYUSD'])

    def test_missing_history_fails_closed(self):
        con=sqlite3.connect(':memory:')
        self.assertFalse(evaluate_precursor(con)['promotion_eligible'])
        con.close()

    def test_missing_prior_prices_does_not_invent_signal(self):
        self.assertEqual(rank_precursors([('TESTUSD',1,10,100000,None,100,None)]),[])

if __name__=='__main__': unittest.main()
