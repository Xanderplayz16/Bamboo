from ursina import *
from ursina.shaders.lit_with_shadows_shader import lit_with_shadows_shader
from ursina.prefabs.checkbox import CheckBox
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton

class OperatorNode(Draggable):
    def __init__(self, text = 'Operator', position = (0, 0), scale = .3, color = color.black50):
        super().__init__(
            text = text,
            text_origin = (0, .4),
            position = position,
            scale = scale,
            color = color,
            highlight_color = color)

        self.a_attachment = Button(model = 'circle', position = (-.5, 0, -.01), scale = .07, parent = self)
        self.b_attachment = Button(model = 'circle', position = (-.5, -.2, -.01), scale = .07, parent = self)
        self.output_attachment = Button(model = 'circle', position = (.5, -.1, -.01), scale = .07, parent = self)

        self.value = InputField(default_value = 'value', limit_content_to = "+-*/%", character_limit = 13, position = (0, .2, -.01), scale = (.9, .15), parent = self)
        self.aText = Text(text = 'a', position = (-.425, .04, -.01), scale = 3.25, parent = self)
        self.bText = Text(text = 'b', position = (-.425, -.16, -.01), scale = 3.25, parent = self)
        self.outputText = Text(text = 'output', position = (.163, -.06, -.01), scale = 3.25, parent = self)

    def make(self):
        if not self.value.text is self.value.default_value:
            pass

class VariableNode(Draggable):
    def __init__(self, text = 'Variable', position = (0, 0), scale = .3, color = color.black50):
        super().__init__(
            text = text,
            text_origin = (0, .4),
            position = position,
            scale = scale,
            color = color,
            highlight_color = color)

        self.value_attachment = Button(model = 'circle', position = (.5, .2, -.01), scale = .07, parent = self)

        self.value = InputField(default_value = 'value', limit_content_to = "'()[],./0123456789abcdefghijklmnopqrstuvwxyzFT", character_limit = 13, position = (0, .2, -.01), scale = (.9, .15), parent = self)

    def make(self):
        if not self.value.text is self.value.default_value:
            self.var = float(self.value.text)

class ModelNode(Draggable):
    def __init__(self, text = 'Model', position = (0, 0), scale = .3, color = color.black50):
        super().__init__(
            text = text,
            text_origin = (0, .4),
            position = position,
            scale = scale,
            color = color,
            highlight_color = color)

        self.texture_attachment = Button(model = 'circle', position = (-.5, 0, -.01), scale = .07, parent = self)

        self.path = InputField(default_value = 'path', limit_content_to = '_./abcdefghijklmnopqrstuvwxyz', character_limit = 13, position = (0, .2, -.01), scale = (.9, .15), parent = self)
        self.textureText = Text(text = 'Texture', position = (-.43, .04, -.01), scale = 3.25, parent = self)

        self.shadows = Entity(position = (-.03, -.33, -.01), parent = self)
        self.shadowsText = Text(text = 'shadows', position = (-.4, .035), scale = 3, parent = self.shadows)
        self.shadowsBox = CheckBox(scale = .08, parent = self.shadows)

    def make(self):
        model = Entity(model = self.path.text)
        if self.shadowsBox.state:
            model.shader = lit_with_shadows_shader

class TextureNode(Draggable):
    def __init__(self, text = 'Texture', position = (0, 0), scale = .3, color = color.black50):
        super().__init__(
            text = text,
            text_origin = (0, .4),
            position = position,
            scale = scale,
            color = color,
            highlight_color = color)

        self.output_attachment = Button(model = 'circle', position = (.5, .2, -.01), scale = .07, parent = self)

        self.path = InputField(default_value = 'path', limit_content_to = '_./abcdefghijklmnopqrstuvwxyz', character_limit = 13, position = (0, .2, -.01), scale = (.9, .15), parent = self)

    def make(self):
        load_texture(self.path.text)

class AudioNode(Draggable):
    def __init__(self, text = 'Audio', position = (0, 0), scale = .3, color = color.black50):
        super().__init__(
            text = text,
            text_origin = (0, .4),
            position = position,
            scale = scale,
            color = color,
            highlight_color = color)

        self.path_attachment = Button(model = 'circle', position = (-.5, .2, -.01), scale = .07, parent = self)

        self.path = InputField(default_value = 'path', limit_content_to = '_./abcdefghijklmnopqrstuvwxyz', character_limit = 13, position = (0, .2, -.01), scale = (.9, .15), parent = self)

        self.autoplay = Entity(y = -.025, z = -.01, parent = self)
        self.autoplayText = Text(text = 'autoplay', position = (-.4, .035), scale = 3, parent = self.autoplay)
        self.autoplayBox = CheckBox(x = .1, scale = .08, parent = self.autoplay)

        self.loop = Entity(y = -.14, z = -.01, parent = self)
        self.loopText = Text(text = 'loop', position = (-.4, .035), scale = 3, parent = self.loop)
        self.loopBox = CheckBox(x = .1, scale = .08, parent = self.loop)

    def make(self):
        Audio(self.path.text, autoplay = self.autoplayBox.state, loop = self.loopBox.state)

class DirectionalLightNode(Draggable):
    def __init__(self, text = 'Directional Light', position = (0, 0), scale = .3, color = color.black50):
        super().__init__(
            text = text,
            text_origin = (0, .4),
            position = position,
            scale = scale,
            color = color,
            highlight_color = color)

        self.shadows = Entity(y = .15, z = -.01, parent = self)
        self.shadowsText = Text(text = 'shadows', position = (-.4, .035), scale = 3, parent = self.shadows)
        self.shadowsBox = CheckBox(scale = .08, parent = self.shadows)

    def make(self):
        self.sun = DirectionalLight(shadows = self.shadowsBox.state)
        self.sun.look_at(Vec3(1,-1,-1))
