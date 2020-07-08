#!/usr/bin/python
# coding: utf-8
import unittest
import yandex_translate


class YandexTranslateTest(unittest.TestCase):

  def setUp(self):
    pass

  def test_translate_it(self):
    result = yandex_translate.translate_it("Hello", "en")
    self.assertEqual(result["text"][0], "Привет")
    self.assertEqual(result["code"], 200)

  def test_error_long_text(self):
    result = yandex_translate.translate_it("hi! "*4098, "en")
    self.assertEqual(result["code"], 413)

  def test_language_error(self):
    result = yandex_translate.translate_it("hi", "англ")
    self.assertEqual(result["code"], 502)


if __name__ == "__main__":
  unittest.main()