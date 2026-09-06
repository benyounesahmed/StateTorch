# test_statetorch.py
"""
Tests for StateTorch module.
"""

import unittest
from statetorch import StateTorch

class TestStateTorch(unittest.TestCase):
    """Test cases for StateTorch class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StateTorch()
        self.assertIsInstance(instance, StateTorch)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StateTorch()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
