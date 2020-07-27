from tkinter import *
root = Tk()

search = "<script>+-+-1-+-+alert(1)</script>" #that's the given search

#username entry
search_entry = Entry(root)
search_entry.pack()


def trylogin():
    if search == search_entry.get():
        print("alert(vcgrdkajdvnciccndiancpdunsancmckdh)")
    else:
        print("Wrong way..!!")


button = Button(root, text="check", command = trylogin)
button.pack()


root.mainloop()
