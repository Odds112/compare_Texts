import unittest
import compare as comp

class TestTextComparison(unittest.TestCase):

    def test_similarity_between_identical_texts(self):
        text = "Это текст для сравнения."
        similarity = comp.compare_texts(text, text)
        self.assertEqual(similarity, 1.0, "Ожидается полное сходство для идентичных текстов")

    def test_similarity_between_different_texts(self):
        text1 = "Это первый текст для сравнения."
        text2 = " "
        similarity = comp.compare_texts(text1, text2)
        self.assertEqual(similarity, 0.1, "Ожидается нулевое сходство для различных текстов")

    def test_similarity_with_similar_texts(self):
        text1 = "Это текст с похожим содержанием."
        text2 = "Это текст с схожим содержанием, но другой."
        similarity = comp.compare_texts(text1, text2)
        self.assertGreater(similarity, 0.7, "Ожидается высокое сходство для схожих текстов")

    def test_similarity_with_dissimilar_texts(self):
        text1 = "Это текст с определенной темой."
        text2 = "Случайное предложение."
        similarity = comp.compare_texts(text1, text2)
        self.assertLess(similarity, 0.3, "Ожидается низкое сходство для различных текстов")

if __name__ == '__main__':
    unittest.main()
