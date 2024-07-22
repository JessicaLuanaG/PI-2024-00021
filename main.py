import unittest

def contPalavras(string):
    pass
def contFrases(string):
    pass
def KMP(palavra,string):
    pass

class testeStrings(unittest.TestCase):
    def test_contPalavras(self):
        self.assertEqual(contPalavras("Hello World"), 2)
        self.assertEqual(contPalavras("            "), 0)
        self.assertEqual(contPalavras("   Eu prefiro Java   "), 3)
        self.assertEqual(contPalavras(""), 0)
        self.assertEqual(contPalavras("http://www.google.com"), 1)

    def test_contFrases(self):
        self.assertEqual(contFrases("Hello World"), 1)
        self.assertEqual(contFrases("Hello World. Hello world"), 2)
        self.assertEqual(contFrases("Hello World. Hello world."), 2)
        self.assertEqual(contFrases(""), 0)
        self.assertEqual(contFrases("            "), 0)

    def test_KMP(self):
        self.assertEqual(KMP("abracadabra", "abracadabra"), 0)
        self.assertEqual(KMP("world", "hello world"), 6)
        self.assertEqual(KMP("universe", "hello world"), -1)
        self.assertEqual(KMP("a", "hello world"), -1)
        self.assertEqual(KMP("hello world", "hello world hello world"), 0)