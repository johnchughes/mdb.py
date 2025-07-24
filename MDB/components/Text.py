
import os
from MDB.components.MDComponet import MDComponent

#Q: How to handle bold / italics / inline text within a paragraph ? 
#Short and dirty make users write it into the value ? 
class Paragraph(MDComponent):
    def __init__(self, value):
        super().__init__(value)

    def ToString(self):
        return f'{self.value}{os.linesep}'
    
