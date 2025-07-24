from typing import List
from MDB.components.MDComponet import MDComponent
import os


class ListItem(MDComponent):
    def __init__(self, value):
        super().__init__(value)

    def ToString(self):
        return f"  - {self.value} {os.linesep}"

class CheckListItem(MDComponent):
    def __init__(self, value, completed):
        self.completed = completed
        super().__init__(value)

    def ToString(self):
        bracketContent = 'x' if self.completed else f' '
        return f"  - [{bracketContent}] {self.value}{os.linesep}"

#TODO: this is a bit pesky to have to append MD, but python stdlib did get there first. 
class MDList(MDComponent):
    def __init__(self):
        super().__init__("") #TODO: Make the MDComponent value optional. 
        self.components: List[MDComponent] = list()
    
    def AddItem(self, value:str, completed: bool | None = None):
        if completed is None:
            li = ListItem(value)
            self.components.append(li) 
        else:
            cli = CheckListItem(value, completed)
            self.components.append(cli) 
            
    def ToString(self):
        st_arr = [comp.ToString() for comp in self.components] 
        str = "".join(st_arr) 
        return str
