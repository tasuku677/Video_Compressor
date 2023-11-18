import tkinter
class Application(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root, borderwidth=1, relief='groove')
        self.root = root
        self.pack()
        self.pack_popagate(0)
        self.create_widgets()

    def create_widgets(self):
        upload_btn = tkinter.Button(self, text='upload', command=self.upload)
        upload_btn.pack()
    def upload():
        '''add uploading process'''
        print('uploading...')

root = tkinter.Tk()
root.title('video_compressor')
app = Application(root=root)
app.mainloop()

