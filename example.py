import os
from typing import List

from MDB.MDBuilder import MDBuilder
from MDB.components.Headings import Heading1, Heading2, Heading3
from MDB.components.List import MDList
from MDB.components.Text import Paragraph

# This file will generate the Readme.md

document = MDBuilder()
document.AddComponent(Heading1("Markdown Document Builder ( mdb.py )"))
document.AddComponent(Paragraph("A python library for building markdown documents, is it a good idea to do it like this, probably not. but this was created because I wanted to play around with python OOP and inheritance."))
document.AddComponent(Paragraph("The aim is to provide a simple library which can be used to build up  a markdown document in code, without having to write giant strings yourself."))
document.AddComponent(Paragraph("see `example.py` for an example of using the library to build this document."))

document.AddComponent(Heading2("TODO"))
todoList = MDList()
todoList.AddItem("Implement builder pattern")
todoList.AddItem("Add better type safety")
todoList.AddItem("Unit Tests")
document.AddComponent(todoList)

document.AddComponent(Heading2("Markdown Spec Coverage"))
document.AddComponent(Heading3("Standard Features"))

standardTodoList = MDList()
standardTodoList.AddItem("Headings", True)
standardTodoList.AddItem("Paragraphs", True)
standardTodoList.AddItem("Line break", False)
standardTodoList.AddItem("Blockquotes", False)
standardTodoList.AddItem("Lists", True)
standardTodoList.AddItem("Images", True)
standardTodoList.AddItem("Image Links", False)
standardTodoList.AddItem("Code", False)
standardTodoList.AddItem("Horizontal Rule", True)
standardTodoList.AddItem("Links", False)

document.AddComponent(standardTodoList)
document.AddComponent(Heading3("Non standard Features"))

nonStandardTodoList = MDList()
nonStandardTodoList.AddItem("Checkbox lists", True)
nonStandardTodoList.AddItem("Tables", False)
document.AddComponent(nonStandardTodoList)

output = document.Write("Readme-gen.md")