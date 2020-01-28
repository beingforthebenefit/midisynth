from Tkinter import *
window = Tk()
label = Label(window, text="Which device would you like to use?", font = ('Veranda', 12))
label.grid(column = 0, row = 0)
window.title("Welcome to a MIDI interpretor. Please select you device.")
window.geometry('400x400')
window.mainloop()
