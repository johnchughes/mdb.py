from MDB.components.MDComponet import MDComponent


class BlockQuote(MDComponent):
    def __init__(self, value):
        super().__init__(value)

    def ToString(self):
        return f'```{self.value}```'

#This poses an interesting problem, a single tick quote can be displayed inline within a paragraph.
#So does a component need an internal list of components so you can slice quotes into a paragraph.
#Might help solve the table conundrum.
class Quote(MDComponent):
    def __init__(self, value):
        super().__init__(value)

    def ToString(self):
        return f'`{self.value}`'