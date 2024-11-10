import unittest

from textnode import (
    TextNode,
    TextType
)

from text_to_textnode import (
    text_to_textnodes
)


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes_plaintext(self):
        text = "This is plain text"
        expected = [TextNode("This is plain text", TextType.TEXT.value)]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_text_to_textnodes_boldtext(self):
        text = "This is **bold** text"
        expected = [
            TextNode("This is ", TextType.TEXT.value),
            TextNode("bold", TextType.BOLD.value),
            TextNode(" text", TextType.TEXT.value)
        ]

        self.assertEqual(text_to_textnodes(text), expected)

    def test_text_to_textnodes_codetext(self):
        text = "This is a `Python` course"
        expected = [
            TextNode("This is a ", TextType.TEXT.value),
            TextNode("Python", TextType.CODE.value),
            TextNode(" course", TextType.TEXT.value)
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_text_to_textnodes_italictext(self):
        text = "This is *italic* text"
        expected = [
            TextNode("This is ", TextType.TEXT.value),
            TextNode("italic", TextType.ITALIC.value),
            TextNode(" text", TextType.TEXT.value)
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_text_to_textnodes_image(self):
        text = "This is a fast cat ![image](https://i.imgur.com/fastcat.jpg) in text"
        expected = [
            TextNode("This is a fast cat ", TextType.TEXT.value),
            TextNode("image", TextType.IMAGE.value, "https://i.imgur.com/fastcat.jpg"),
            TextNode(" in text", TextType.TEXT.value),
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_text_to_textnodes_link(self):
        text = "This is a [link](https://www.example.com) in text"
        expected = [
            TextNode("This is a ", TextType.TEXT.value),
            TextNode("link", TextType.LINK.value, "https://www.example.com"),
            TextNode(" in text", TextType.TEXT.value),
        ]

        self.assertEqual(text_to_textnodes(text), expected)

    def test_text_to_textnodes_combinationofelements(self):
        text = ("This is **text** with an *italic* word and a `code block` and an ![obi wan image]("
                "https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        expected = [
            TextNode("This is ", TextType.TEXT.value),
            TextNode("text", TextType.BOLD.value),
            TextNode(" with an ", TextType.TEXT.value),
            TextNode("italic", TextType.ITALIC.value),
            TextNode(" word and a ", TextType.TEXT.value),
            TextNode("code block", TextType.CODE.value),
            TextNode(" and an ", TextType.TEXT.value),
            TextNode("obi wan image", TextType.IMAGE.value, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT.value),
            TextNode("link", TextType.LINK.value, "https://boot.dev"),
        ]

        self.assertEqual(text_to_textnodes(text), expected)



if __name__ == "__main__":
    unittest.main()
