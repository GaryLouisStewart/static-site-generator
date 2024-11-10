"""
author: Gary Louis Stewart, gary-stewart@outlook.com
date: 10/11/2024
"""

import unittest
import os
from generate_page import generate_page


class TestGeneratePage(unittest.TestCase):
    def setUp(self):
        self.from_path = "testdata/content.md"
        self.template_path = "testdata/template.html"
        self.dest_path = "output/index.html"

        os.makedirs('testdata', exist_ok=True)
        with open(self.from_path, 'w') as f:
            f.write("# Test Page\nContent goes here.")

        with open(self.template_path, 'w') as t:
            t.write("<html><head><title>{{ Title }}</title></head>"
                    "<body>{{ Content }}</body></html>")

    def tearDown(self):
        os.remove(self.from_path)
        os.remove(self.template_path)
        if os.path.exists(self.dest_path):
            os.remove(self.dest_path)
            os.rmdir(os.path.dirname(self.dest_path))

    def test_generate_page(self):
        generate_page(self.from_path, self.template_path, self.dest_path)

        with open(self.dest_path, 'r') as output_file:
            content = output_file.read()
            self.assertIn("<title>Test Page</title>", content)
            self.assertIn("<h1>Test Page", content)
            self.assertIn("Content goes here.</h1>", content)


if __name__ == '__main__':
    unittest.main()
