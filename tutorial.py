from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
#from kivy.uix.floatlayout import Floatlayout
class TutorialApp(App):
	def build(self):
		#f= Floatlayout()
		s= Scatter()
		l= Label(text="Hello!",font_size=150)
		#f.add_widget(s)
		s.add_widget(l)
		return s
if __name__=="__main__":
	TutorialApp().run()

