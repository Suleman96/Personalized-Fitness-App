from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
<Check@MDCheckbox>:
    group: 'group'
    size_hint: None, None
    size: dp(48), dp(48)


MDFloatLayout:

    Check:
        text: '1 hour'
        active: True
        pos_hint: {'center_x': .4, 'center_y': .5}

    Check:
        text: '2 hour'
        pos_hint: {'center_x': .6, 'center_y': .5}
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()