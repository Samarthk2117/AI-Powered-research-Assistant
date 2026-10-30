import unittest
from unittest.mock import patch
from agent import create_research_brief

class AgentTests(unittest.TestCase):
    def test_requires_topic(self):
        with self.assertRaises(ValueError):
            create_research_brief("")

    @patch.dict("os.environ", {}, clear=True)
    def test_requires_api_key(self):
        with self.assertRaises(RuntimeError):
            create_research_brief("Artificial intelligence")

if __name__ == "__main__":
    unittest.main()
