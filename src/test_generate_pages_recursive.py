"""
author: Gary Louis Stewart, gary-stewart@outlook.com
date: 10/11/2024
"""


import unittest
import tempfile
import os
from pathlib import Path
from generate_page import generate_pages_recursive


class TestGeneratePagesRecursive(unittest.TestCase):
    def setUp(self):
        # Create temporary directories for content and public
        self.content_dir = tempfile.TemporaryDirectory()
        self.public_dir = tempfile.TemporaryDirectory()

        # Create a markdown file in the content directory
        self.md_path = os.path.join(self.content_dir.name, 'example.md')
        with open(self.md_path, 'w') as f:
            f.write("# Sample Content\n\nThis is a test.")

        # Create a simple template file
        self.template_path = os.path.join(self.content_dir.name, 'template.html')
        with open(self.template_path, 'w') as f:
            f.write("<html><head></head><body>{{ Content }}</body></html>")

    def test_generate_pages_recursive(self):
        # Run the function
        generate_pages_recursive(self.content_dir.name, self.template_path, self.public_dir.name)

        # Check if the corresponding HTML file exists
        html_path = Path(self.public_dir.name).joinpath('example.html')
        self.assertTrue(html_path.is_file())

        # Optionally read and check the contents to match expectation
        with open(html_path, 'r') as f:
            content = f.read()
            self.assertIn('<html>', content)
            self.assertIn('<body>', content)
            self.assertIn('Sample Content', content)

    def tearDown(self):
        # Clean up temporary directories
        self.content_dir.cleanup()
        self.public_dir.cleanup()


if __name__ == '__main__':
    unittest.main()
