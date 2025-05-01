import unittest
from unittest.mock import patch
from utils import nfc_tools

class TestNFCTools(unittest.TestCase):

    def test_hash_uid(self):
        uid = "AA-BB-CC"
        hashed = nfc_tools.hash_uid(uid)
        self.assertEqual(len(hashed), 64)
        self.assertIsInstance(hashed, str)

    @patch("utils.nfc_tools.pn532.read_passive_target")
    def test_read_card_no_card(self, mock_read):
        mock_read.return_value = None
        result = nfc_tools.read_card()
        self.assertIsNone(result)

    def test_write_card_stub(self):
        # Can't test without hardware – placeholder
        self.assertTrue(hasattr(nfc_tools, "write_card"))

    def test_clone_card_stub(self):
        # Can't test without hardware – placeholder
        self.assertTrue(hasattr(nfc_tools, "clone_card"))

    def test_dump_all_blocks_stub(self):
        # Can't test without card – placeholder
        self.assertTrue(hasattr(nfc_tools, "dump_all_blocks"))

if __name__ == "__main__":
    unittest.main()
