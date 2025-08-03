# test_animecore.py
"""
Tests for AnimeCore module.
"""

import unittest
from animecore import AnimeCore

class TestAnimeCore(unittest.TestCase):
    """Test cases for AnimeCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AnimeCore()
        self.assertIsInstance(instance, AnimeCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AnimeCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
