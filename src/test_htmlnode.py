import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_default_end_none(self):
        node = HTMLNode()
        node2 = HTMLNode(None, None, None, None)
        self.assertEqual(repr(node), "HTMLNode(None, None, children: None, None)")
        self.assertEqual(repr(node2), "HTMLNode(None, None, children: None, None)")

    def test_eq_default_and_none(self):
        node = HTMLNode()
        node2 = HTMLNode(None, None, None, None)
        self.assertEqual(node, node2)

    def test_not_equal(self):
        node = HTMLNode()
        node2 = HTMLNode("p", "This is a paragraph")
        self.assertNotEqual(node, node2)

    def test_prop_to_html(self):
        node = HTMLNode(None,None,None,{"href":"https://fakesite.com/"})
        self.assertNotEqual(node.prop_to_html(), " href=https://fakeside.com/")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Hello, world!", {"target": "_blank"})
        self.assertEqual(node.to_html(), "<div target=\"_blank\">Hello, world!</div>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Link text", {"href": "https://fakelink.com/"})
        self.assertEqual(node.to_html(), "<a href=\"https://fakelink.com/\">Link text</a>")

if __name__ == "__main__":
    unittest.main()
