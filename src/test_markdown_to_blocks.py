from markdown_to_blocks import (
    markdown_to_blocks
)

import unittest


class TestMarkdownToBlocks(unittest.TestCase):
    def test_no_blanklines(self):
        markdown = "Line 1\nLine 2\nLine 3"
        expected = [
            "Line 1\nLine 2\nLine 3"
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_single_block(self):
        markdown = "This is a single block"
        expected = [
            "This is a single block"
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_multiple_blocks(self):
        markdown = "Block 1\n\nBlock 2\n\nBlock 3"
        expected = [
            "Block 1",
            "Block 2",
            "Block 3"
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_multiple_blanklines(self):
        markdown = "Block 1\n\n\n\nBlock 2"
        expected = [
            "Block 1",
            "Block 2"
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_empty_input(self):
        markdown = ""
        expected = []
        self.assertEqual(markdown_to_blocks(markdown), expected)


if __name__ == "__main__":
    unittest.main()
