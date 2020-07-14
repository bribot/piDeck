# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:24:25 2020

@author: Bri
"""

import pyglet

pyglet.resource.path = ["resources"]
pyglet.resource.reindex()

square = pyglet.resource.image("square.jpg")