#!/usr/bin/env python3
""" Test file for the console.py module """
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand  # Assuming console.py is in the same directory


class TestConsole(unittest.TestCase):
    """Unit tests for the HBNBCommand class methods"""

    def setUp(self):
        """Set up the test environment"""
        self.console = HBNBCommand()

    def test_show_command(self):
        """Test the show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(
                "User.show(38f22813-2753-4d42-b37c-57a17f1e4f88)")
            output = f.getvalue().strip()
            # Perform assertions on the output
            self.assertIn("User", output)
            self.assertIn("38f22813-2753-4d42-b37c-57a17f1e4f88", output)
            # Add more assertions as needed


if __name__ == "__main__":
    unittest.main()
