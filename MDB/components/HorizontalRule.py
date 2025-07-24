import os
from MDB.components.MDComponet import MDComponent


class HorizontalRule(MDComponent):
    def __init__(self):
        super().__init__("")

    def ToString(self):
        return f'{os.linesep}---{os.linesep}'
    
