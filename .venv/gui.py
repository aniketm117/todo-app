import functions
import PySimpleGUI as sg

label = sg.Text('Type a to-do item')
input_box = sg.InputText(tooltip='To-do Item')

add_button = sg.Button("Dab")

win = sg.Window('To-do App', layout=[[label],[input_box, add_button]]) #window instance

win.read() #read method to display the run

win.close()