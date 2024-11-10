"""
author: Gary Louis Stewart, gary-stewart@outlook.com
date: 10/11/2024
"""


from markdown_block_to_block import (
    block_to_block_type
)

import unittest


class TestMarkdownBlockToBlock(unittest.TestCase):
    # test markdown quotes
    def test_single_line_quote(self):
        markdown = "> Difficulties strengthen the mind, as labor does the body."
        expected = "quote"
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_multi_line_quote(self):
        markdown = ("> To live is to risk it all\n>Otherwise you're just an inert chunk of randomly assembled "
                    "molecules drifting wherever the universe blows you")
        expected = "quote"
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_mixed_context(self):
        markdown = "> I am a quote\nThis is not part of the quote"
        expected = "paragraph"
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_empty_quote_block(self):
        markdown = ">"
        expected = "quote"
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_leading_quote_character(self):
        markdown = "Test > not a quote"
        expected = "paragraph"
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_quote_multiple_lines(self):
        markdown = "> First line\n> Second Line"
        expected = "quote"
        self.assertEqual(block_to_block_type(markdown), expected)

    # test Markdown code blocks

    def test_code_block(self):
        markdown = "```\nthis is a code block\n```"
        expected = "code"
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_code_block_multiple_lines(self):
        markdown = "```\n1st line of this code block\n2nd line of this code block\n```"
        expected = "code"
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_code_block_unmatched_backticks(self):
        markdown = "```\nI am a code block, hello!\n``"
        expected = "paragraph"
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_code_block_incomplete_backticks(self):
        markdown = "```\n I am incomplete"
        expected = "paragraph"
        self.assertEqual(block_to_block_type(markdown), expected)

    # test ordered lists

    def test_ordered_list(self):
        markdown = "1. First item\n2. Second item"
        expected = "ordered_list"
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_ordered_list_increment(self):
        markdown = "1. Item 1\n2. Item 2\n3. Item 3"
        expected = "ordered_list"
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_wrong_increment_list(self):
        markdown = "1. Item 1\n3. Item 3"
        expected = "paragraph"  # should not return ordered_list
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_non_numeric_start_ordered_list(self):
        markdown = "a. Item\ba. Another"
        expected = "paragraph"
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_non_starting_one_ordered_list(self):
        markdown = "5. Not starting at one\n 6. Improper start"
        expected = "paragraph"
        self.assertEqual(block_to_block_type(markdown), expected)

    # unordered lists

    def test_unordered_list_asterisk(self):
        markdown = "* First  item\n* Second item"
        expected = "unordered_list"
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_unordered_list_dash(self):
        markdown = "- First item\n- Second item"
        expected = "unordered_list"
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_mixed_unordered_list(self):
        markdown = "* First item\n- Second item"
        expected = "paragraph"
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_unordered_list_incorrect_format(self):
        markdown = "*No space detected after marker"
        expected = "paragraph"
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_text_starting_with_asterisk_or_dash(self):
        markdown = "*This is not a list item\n-Dash text with improper format"
        expected = "paragraph"
        self.assertEqual(block_to_block_type(markdown), expected)

    # finally test paragraphs

    def test_paragraph(self):
        markdown = ("This is a paragraph\nThis is the second line of the paragraph\n This is the third line of the "
                    "paragraph")
        expected = "paragraph"
        self.assertEqual(block_to_block_type(markdown), expected)


if __name__ == "__main__":
    unittest.main()
