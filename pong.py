# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 10:59:48 2015

@author: shashank
"""

from kivy.app import App
from kivy.uix.widget import Widget


class PongGame(Widget):
    pass


class PongApp(App):
    def build(self):
        return PongGame()


if __name__ == '__main__':
    PongApp().run()