"""
author: Gary Louis Stewart, gary-stewart@outlook.com
date: 10/11/2024
"""

from extract_title import extract_title
import unittest


class TestExtractTitle(unittest.TestCase):
    def test_extract_markdown_h1_header(self):
        markdown = "# This is a heading"
        expected_result = "This is a heading"
        self.assertEqual(extract_title(markdown), expected_result)

    def test_extract_markdown_no_h1(self):
        markdown = "## This is a H2 header"
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_extract_markdown_no_trailing_space(self):
        markdown = "#No trailing space"
        with self.assertRaises(Exception):
            extract_title(markdown)


if __name__ == "__main__":
    unittest.main()
