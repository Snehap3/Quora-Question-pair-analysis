# -*- coding: utf-8 -*-
"""Translate.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FPXy-_HTEYGUe4o56l9xlRR1mkUejUBL
"""

import deep_translator

def translate_any():
  from deep_translator import GoogleTranslator
  to_translate = input('what do you want to translate?')
  translated = GoogleTranslator(source='auto', target='english').translate(to_translate)
  return translated

translate_any()

