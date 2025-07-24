
import os
from MDB.components.MDComponet import MDComponent


class Heading1(MDComponent):
    def __init__(self, value):
        super().__init__(value)

    def ToString(self):
        return f'# {self.value}{os.linesep}'

class Heading2(MDComponent):
    def __init__(self, value):
        super().__init__(value)

    def ToString(self):
        return f'## {self.value}{os.linesep}'
    
class Heading3(MDComponent):
    def __init__(self, value):
        super().__init__(value)

    def ToString(self):
        return f'### {self.value}{os.linesep}'

class Heading4(MDComponent):
    def __init__(self, value):
        super().__init__( value)

    def ToString(self):
        return f'#### {self.value}{os.linesep}'
    
class Heading5(MDComponent):
    def __init__(self, value):
        super().__init__( value)

    def ToString(self):
        return f'##### {self.value}{os.linesep}'
    
class Heading6(MDComponent):
    def __init__(self, value):
        super().__init__( value)

    def ToString(self):
        return f'###### {self.value}{os.linesep}'
