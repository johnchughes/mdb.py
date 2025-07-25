from MDB.components.MDComponet import MDComponent


class Image(MDComponent):
    def __init__(self, value, url):
        self.url = url
        super().__init__(value)

    def ToString(self):
        return f'![{self.value}]({self.url})'
    
