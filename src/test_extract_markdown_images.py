"""
author: Gary Louis Stewart, gary-stewart@outlook.com
date: 10/11/2024
"""

import unittest

from extract_markdown_elements import (
    extract_markdown_links,
    extract_markdown_images
)


class TestExtractMarkdown(unittest.TestCase):
    def test_markdown_image_eq(self):
        text = [("cat pictures", "https://cat-pictures.example.com/cats.gif")]
        text2 = extract_markdown_images("This is text with a ![cat pictures](https://cat-pictures.example.com/cats.gif)")
        self.assertEqual(text, text2)

    def test_markdown_image_false(self):
        text = [("cat picturez", "https://cat-pictures.example.com/cats.gif")]
        text2 = extract_markdown_images("This is text with a ![cat picturezzz]("
                                        "https://cat-pictures.example.com/batz.gif)")
        self.assertNotEqual(text, text2)

    def test_markdown_image_multiple(self):
        text = [
            ("cat pics", "https://cat-pics.example.com/cats.gif"),
            ("bat pics", "https://bat-pics.example.com/bats.gif")
        ]
        text2 = extract_markdown_images("Here are some images of animals: ![cat pics]("
                                        "https://cat-pics.example.com/cats.gif) and ![bat pics]("
                                        "https://bat-pics.example.com/bats.gif)")
        self.assertEqual(text, text2)

    def test_markdown_link_eq(self):
        text = [("to google uk", "https://google.co.uk")]
        text2 = extract_markdown_links("This is a link with text [to google uk](https://google.co.uk)")
        self.assertEqual(text, text2)

    def test_markdown_link_false(self):
        text = [("to yahoo", "https://yahoo.co.uk")]
        text2 = extract_markdown_links("This is a link with text [to google uk](https://google.co.uk)")
        self.assertNotEqual(text, text2)

    def test_markdown_link_multiple(self):
        text = [
            ("adrian cantrill", "https://learn.cantrill.io"),
            ("linux foundation", "https://trainingportal.linuxfoundation.org"),
            ("boot dev", "https://boot.dev")
        ]
        text2 = extract_markdown_links("here are some links to good websites for learning: [adrian cantrill]("
                                       "https://learn.cantrill.io) and [linux foundation]("
                                       "https://trainingportal.linuxfoundation.org) and [boot dev](https://boot.dev)")
        self.assertEqual(text, text2)


if __name__ == '__main__':
    unittest.main()