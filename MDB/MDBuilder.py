#It would be nicer to use the builder pattern here, so method calls can be chaind  mdb.AddComponet(x).AddComponent(y).Build()
from typing import List

from MDB.components.MDComponet import MDComponent

class MDBuilder:
    def __init__(self):
        self.components: List[MDComponent] = list()
    
    def AddComponent(self, component:MDComponent) -> None:
        self.components.append(component)

    def Build(self) -> str:
        st_arr = [comp.ToString() for comp in self.components]
        str = "".join(st_arr) # type: ignore # TODO: fix this! 
        return str
    
    def Write(self, path):
        markdown_string = self.Build()
        with open(path, 'w') as f:
            f.write(markdown_string)