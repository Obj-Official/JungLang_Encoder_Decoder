from tkinter import *
from Encode_Decode_Module import EncodeMsg
from Encode_Decode_Module import DecodeMsg
import tkinter.messagebox


class EncodeDecodeGUI:
    def __init__(self):
        window = Tk()
        self.window = window
        window.title("Jung-Lang Scramber")
        window.geometry("500x400")
        #window.configure(bg = 'light gray')
        self.copiedData = ""
        self.doubleClickedWidget = 0
        
        #menubar
        menubarX = Menu(window)
        window.config(menu = menubarX)
        #menuoption1
        settingsmenu = Menu(menubarX, tearoff = 0)
        menubarX.add_cascade(label = "Settings", menu = settingsmenu)
        settingsmenu.add_command(label = "Change button color", command = self.changeBtn)
        settingsmenu.add_command(label = "Change font color", command = self.changeFontColor)
        settingsmenu.add_command(label = "Reset", command = self.reset)
        settingsmenu.add_command(label = "About", command = self.relayMessage)
        #menuoption2
        closemenu = Menu(menubarX, tearoff = 0)
        menubarX.add_cascade(label = "Close", menu = closemenu)
        closemenu.add_command(label = "Close this window", command = window.quit)
        #popupmenu
        self.popupmenu1 = Menu(window, tearoff=0)
        self.popupmenu1.add_command(label = "Copy", command = self.copyClipboard)
        self.popupmenu1.add_command(label = "Paste", command = self.pasteClipboard)
        self.popupmenu1.add_command(label = "Export", command = self.export)
        self.popupmenu1.add_command(label = "Clear all", command = self.clearAll)
        self.popupmenu1.add_command(label = "Close", command = window.quit)
        
        '''#images in this window
        encodeMsgImg = PhotoImage(file="EncodeImg.gif")
        decodeMsgImg = PhotoImage(file="DecodeImg.gif")'''
        
        #Create widgets
        label1 = Label(window, text = "Scramble message")
        frame1 = Frame(window)
        self.msg1 = StringVar()
        self.encodeTextbox = Entry(frame1, textvariable = self.msg1)
        self.encodeButton = Button(frame1, text = "Encode Message", command = self.processEncode)
        self.msg2 = StringVar()
        self.decodeTextbox = Entry(frame1, textvariable = self.msg2)
        self.decodeButton = Button(frame1, text = "Decode Message", command = self.processDecode)
        self.text = Text(window, height = 10, width = 40, wrap = WORD)
        self.messagew = Message(window, text="")

        #place, arrange and align all widgets accordingly
        self.encodeTextbox.grid(row = 1, column = 1, padx = 5)
        self.encodeButton.grid(row = 2, column = 1, pady = 10)
        self.decodeTextbox.grid(row = 1, column = 2, padx = 5)
        self.decodeButton.grid(row = 2, column = 2, pady = 10)
        label1.pack()
        frame1.pack()
        self.text.pack(pady = 5)  
        self.messagew.pack()
        self.text.bind("<Button-3>", self.popup1)
        self.encodeTextbox.bind("<Button-3>", self.popup2)
        self.decodeTextbox.bind("<Button-3>", self.popup3)
  
        window.mainloop()
        
    def processEncode(self):
         self.message = EncodeMsg(self.msg1.get())
         self.text.insert(END, self.message.processEncode())
         self.text.insert(END, "\n")
         
    def processDecode(self):
         self.message = DecodeMsg(self.msg2.get())
         self.text.insert(END, self.message.processDecode())
         self.text.insert(END, "\n")
         
    def changeBtn(self):
        self.encodeButton["bg"] = "dodgerblue"
        self.decodeButton["bg"] = "maroon"
        self.encodeButton["fg"] = "whitesmoke"
        self.decodeButton["fg"] = "white"
        
    def changeFontColor(self):
        self.encodeTextbox["fg"] = "maroon" 
        self.decodeTextbox["fg"] = "maroon"
        self.text["fg"] = "blue"
        
    def reset(self):
        self.encodeButton["bg"] = "lightgray"
        self.decodeButton["bg"] = "lightgray"
        self.encodeButton["fg"] = "black"
        self.decodeButton["fg"] = "black"
        self.encodeTextbox["fg"] = "black" 
        self.decodeTextbox["fg"] = "black"
        self.text["fg"] = "black"
        self.messagew["text"] = ""
        self.clearAll()
        
    def clearAll(self):
        self.encodeTextbox.delete(0,END)
        self.decodeTextbox.delete(0,END)
        self.text.delete("1.0","end")
        
    def popup1(self, event):
        self.popupmenu1.post(event.x_root, event.y_root)
        self.doubleClickedWidget = 1

    def popup2(self, event):
        self.popupmenu1.post(event.x_root, event.y_root)
        self.doubleClickedWidget = 2

    def popup3(self, event):
        self.popupmenu1.post(event.x_root, event.y_root)
        self.doubleClickedWidget = 3
        
    def copyClipboard(self):
        if self.doubleClickedWidget == 1:
            self.copiedData = self.text.selection_get()
        elif self.doubleClickedWidget == 2:
            self.copiedData = self.encodeTextbox.selection_get()
        elif self.doubleClickedWidget == 3:
            self.copiedData = self.decodeTextbox.selection_get()  
        self.window.clipboard_clear()
        self.window.clipboard_append(self.copiedData)
        
    def pasteClipboard(self):
        data = self.window.clipboard_get()
        if self.doubleClickedWidget == 1:
            self.text.insert(END, data)
        elif self.doubleClickedWidget == 2:
            self.encodeTextbox.insert(END, data)
        elif self.doubleClickedWidget == 3:
            self.decodeTextbox.insert(END, data)

    def export(self):
        msg = self.text.get("1.0",END)
        exportmsg = open("encodedecodemsg.txt", "w")  
        exportmsg.write(msg)
        exportmsg.close()
        tkinter.messagebox.showinfo("Data Exported", "Check external file \"encodedecodemsg.txt\" for export")

    def relayMessage(self):
        self.messagew["text"] = "Scrambler v1.0.1 \nSoftware created by OBJ \nLanguage Code based on Tunrayo's Jungle Encoding Language \n©OBJ PRIME"
        self.messagew["justify"] = "center"
        tkinter.messagebox.showinfo("About", "Scrambler v1.0.1 by OBJ\nJungle Language Encoder/Decoder")
EncodeDecodeGUI()
