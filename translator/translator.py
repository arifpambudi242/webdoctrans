'''
author 	: Arif Pambudi
email	: arifpambudi242@gmail.com

'''

from docx import Document
import time
from googletrans import Translator
from autocorrect import Speller


trans = Translator()
spell = Speller(lang="en")


class Translator:
	def __init__(self):
		self._targetlang = 'id'
		self._document = None
		self._paragraphs = None
		self._filepath = None

	# buka file & baca file
	def openFile(self, filepath):
		self._filepath = filepath
		self._document = Document(filepath)
		self._paragraphs = self._document.paragraphs

	# translate paragraph
	def transDoc(self):
		for para in enumerate(self._paragraphs):
			try:
				if para.text:
					inline = para.runs
					for i, v in enumerate(inline):
						corrected = spell.autocorrect_sentence(v.text)
						# translating
						translated = trans.translate(corrected, dest=self._targetlang).text
						# set paragraph text
						if translated:
							v.text = translated
				time.sleep(0.1)
			except:
				continue
		return True
	
	def SaveFile(self, filename=None):
		filename = self._filepath.split(".docx", 1)[0] if not filename else filename
		self._document.save(f"{filename}-{self._targetlang}-{round(time.time())}.docx")
