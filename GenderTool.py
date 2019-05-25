
import nltk, random, os
import tkinter as tk
import PIL
import base64, urllib
from urllib.request import Request, urlopen
from tkinter import filedialog
import pickle



class GUI(object):

  def __init__(self):

    root = tk.Tk()
    root.title("GenderTool")
    root.geometry("292x195")


    #Logos
    bckgrnd_photo = tk.PhotoImage(file=os.path.join(os.path.dirname("GenderTool App"), "gendersymbols.gif"))
    bckgrnd = tk.Label(root, image = bckgrnd_photo)
    bckgrnd.grid(row=0, column=2, columnspan=2)
    bckgrnd.image = bckgrnd_photo

    jlu_logo_photo = tk.PhotoImage(file=os.path.join(os.path.dirname("GenderTool App"), "jlu-logo.gif"))
    jlulogo = tk.Label(root, image = jlu_logo_photo)
    jlulogo.grid(row=3, column=2, columnspan=2)
    jlulogo_image = jlu_logo_photo


    #Load file field
    self.var = tk.StringVar()
    entryfield = tk.Entry(root, textvariable=self.var)
    entryfield.grid(row=1, column=2)

    #Button for file selection action
    loadfile = tk.Button(root, text="Select a File", command=self.file)
    loadfile.grid(row=1, column=3)

    #Run button
    filename = self.file()
    runbutton = tk.Button(root, text="Run", command=self.get_human_names(filename))
    runbutton.grid(row=2, column=2, columnspan=2)

    root.update()
    root.mainloop()

  #Action for pop-up file selection

  def file(self):
    options = {
        'defaultextension': '.txt',
        'filetypes': [('text files', '.txt')]
    }

    filename = filedialog.askopenfilename(title='Choose a file', initialdir="/", **options)

    if filename:
      directory = os.path.split(filename)[-1]
      self.var.set(directory)
      return filename



  #method to extract human names from file
  def get_human_names(self, text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sent = nltk.ne_chunk(pos, binary=False)
    person_list = []
    person = []
    name = ""
    for subtree in sent.subtrees(filter=lambda t: t.label() == "PERSON"):
      for leaf in subtree.leaves():
        person.append(leaf[0])
      if len(person) > 1:
        for part in person:
          name += part + ' '
        if name[:-1] not in person_list:
          person_list.append(name[:-1])
        name = ''
      person = []

    return pickle.dump(person_list, open("dumped_data.txt", "wb"))




















GUI()



















