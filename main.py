from ursina import *

app = Ursina(title = 'Bamboo', borderless = False, fullscreen = False, development_mode = False, vsync = True)

from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton
from nodes import *
import os

# os.system('pip install https://github.com/pokepetter/ursina/archive/master.zip --upgrade --force-reinstall')

Text.default_font = 'assets/font.ttf'

nodes = []

def createNode(node):
    newNode = node()
    nodes.append(newNode)

def removeNode(node):
    nodes.remove(node)

# Title
nodeTitle = Text(text = 'Node Editor', position = window.top + (-.02, -.01))

# File
DropdownMenu(text = 'File', buttons = (
    DropdownMenuButton(text = 'New'),
    DropdownMenuButton(text = 'Open'),
    DropdownMenu(text = 'Open Recent', buttons = (
        DropdownMenuButton(text = 'Project 1'),
        DropdownMenuButton(text = 'Project 2'),
        )),
    DropdownMenuButton(text = 'Save'),
    DropdownMenu(text = 'Options', buttons = (
        DropdownMenuButton(text = 'Option a'),
        DropdownMenuButton(text = 'Option b'),
        )),
    DropdownMenuButton(text = 'Exit', color = color.rgb(75, 0, 0), on_click = application.quit),
    ))

# Add
addMenu = DropdownMenu(text = 'Add', buttons = (
    DropdownMenuButton(text = 'Operator', on_click = Func(createNode, OperatorNode)),
    DropdownMenuButton(text = 'Variable', on_click = Func(createNode, VariableNode)),
    DropdownMenuButton(text = 'Model', on_click = Func(createNode, ModelNode)),
    DropdownMenuButton(text = 'Texture', on_click = Func(createNode, TextureNode)),
    DropdownMenuButton(text = 'Audio', on_click = Func(createNode, AudioNode)),
    DropdownMenu(text = 'Lights', buttons = (
        DropdownMenuButton(text = 'Directional', on_click = Func(createNode, DirectionalLightNode)),
        #DropdownMenuButton(text = 'Point', on_click = Func(DirectionalLightNode, 'PointLight')),
        #DropdownMenuButton(text = 'Ambient', on_click = Func(DirectionalLightNode, 'AmbientLight')),
        #DropdownMenuButton(text = 'Spot', on_click = Func(DirectionalLightNode, 'SpotLight')),
        )),
    ))

def input(key):
    if not camera.ui.enabled and key == 'escape':
        for i in range(len(nodes)):
            nodes[i].undo()
        camera.ui.enable()

def update():
    addMenu.x = window.top_left.x + .25

def run():
    camera.ui.disable()
    for i in range(len(nodes)):
        nodes[i].make()
    EditorCamera()

runButton = Button(model = 'circle', icon = 'assets/run', position = window.top_right + (-.025, -.025), scale = .03, on_click = run)

app.run(info = False)