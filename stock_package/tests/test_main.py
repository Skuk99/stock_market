import unittest
import sys
sys.path.append('../scripts')
from csv_reader import read_currency_data
import os


class TestMain(unittest.TestCase):

    def setUp(self):
        # note: this would be better done with tempfile
        self.temporary_file = "/tmp/emptyfile"
        f = open(self.temporary_file, 'w')
        f.close()

    def test_no_datafile(self):
        df = read_currency_data(path="/tmp/nonexistentfile-wewefwwe")
        self.assertFalse(df)

    def test_empty_datafie(self):
        df = read_currency_data(path=self.temporary_file)
        self.assertFalse(df)

    def test_file_is_not_csv(self):
        df = read_currency_data(path=self.temporary_file)
        self.assertFalse(df)

    def tearDown(self):
        os.remove(self.temporary_file)