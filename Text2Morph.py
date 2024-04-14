from manim import *
import sys

# get input and output text from terminal arguments
input_text = sys.argv[1]
output_text = sys.argv[2]

class Morph(Scene):
	def construct(self):
		# create text
		text1 = Text("Hello World")
		text2 = Text("Goodbye World")
		self.play(Transform(text1, text2), run_time=3)