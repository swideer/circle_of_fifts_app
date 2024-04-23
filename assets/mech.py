from tkinter import *
from ttkbootstrap import Style
from tkinter import ttk
from assets.data import scales_chords, options_base_major, options_base_minor, options_mode

class app:
    def __init__(self):
        self.root = Tk()
        style = Style(theme='darkly')
        style.configure('title.TLabel', font=('Verdana', 24))
                        
        self.root.title("Music app")
        self.root.geometry("1250x500+100+100")
        self.options_mode = options_mode
        self.options_base_major = options_base_major
        self.options_base_minor = options_base_minor

        self.label_title = ttk.Label(self.root, text="Circle of Fifts", style='title.TLabel')
        self.label_title.place(relx=.5, anchor="center")
        self.label_title.pack(side=TOP, pady=20)

        #MODES FRAME
        self.modes_frm = ttk.Frame(self.root)
        self.modes_frm.place(relx=.5, anchor="center")
        self.modes_frm.pack()
        self.mode_value = StringVar(self.root, '0')

        #MODE Buttons
        i = 0
        for (text, value) in self.options_mode.items():
            ttk.Radiobutton(self.modes_frm, text = text, variable = self.mode_value, 
                        value = value, style='primary.Toolbutton',
                        command=self.select_mode, width=15).grid(row=0,column=i, padx=20)
            i+=1

        #BASES FRAME
        self.bases_frm = ttk.Frame(self.root)
        self.bases_frm.place(relx=.5, anchor="center")
        self.bases_frm.pack()

        #CHORDS FRAME
        self.chords_frame = ttk.Frame(self.root)
        self.chords_frame.place(relx=.5, anchor="center")
        self.chords_frame.pack()

        #SINGLE CHORD FRAME
        self.single_chord_frame = ttk.Frame(self.root)
        self.single_chord_frame.place(relx=.5, anchor="center")
        self.single_chord_frame.pack()

        #QUIT BUTTON
        self.button_quit = ttk.Button(self.root, text="Quit", style='primary.Outline.TButton', command=self.root.destroy)
        self.button_quit.place(relx=.5, anchor="center")
        self.button_quit.pack(side=BOTTOM, pady=20)

        #SELF ADVERTISEMENT
        self.self_label = ttk.Label(self.root, text="by swDEVr", style='primary.TLabel')
        self.self_label.place(relx=.5, anchor="center")
        self.self_label.pack(side=BOTTOM, pady=3)

        self.root.mainloop()
        
    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def select_mode(self):
        self.clear_frame(self.bases_frm)
        self.clear_frame(self.chords_frame)
        self.clear_frame(self.single_chord_frame)
        if self.mode_value.get() == 'major':
            self.base_value_major = StringVar(self.root, '0')
            i=0
            for (text, value) in self.options_base_major.items():
                ttk.Radiobutton(self.bases_frm, text = text, variable = self.base_value_major, 
                            value = text, style='primary.Toolbutton',
                            command=self.base_selection, width=7).grid(row=0, column=i, pady=10, padx=5)
                i+=1
        elif self.mode_value.get() == 'minor':
            self.base_value_minor = StringVar(self.root, '0')
            i=0
            for (text, value) in self.options_base_minor.items():
                ttk.Radiobutton(self.bases_frm, text = text, variable = self.base_value_minor, 
                            value = text, style='primary.Toolbutton',
                            command=self.base_selection, width=7).grid(row=0, column=i, pady=10, padx=5)
                i+=1
        
    def provide_chords(self, scale, base):
        return scales_chords[scale][base]
    
    def base_selection(self):
        self.chord_selected = StringVar(self.root, '0')
        self.clear_frame(self.chords_frame)
        self.clear_frame(self.single_chord_frame)
        #POPULATE CHORDS FRAME
        if self.mode_value.get() == 'major':
            scale_sel = self.provide_chords(self.mode_value.get(), self.base_value_major.get())
            i=0
            for text in scale_sel:
                ttk.Radiobutton(self.chords_frame, text = text, variable = self.chord_selected, 
                            value = text, style='primary.Toolbutton',
                            command=self.chord_selection, width=14).grid(row=0, column=i, pady=10, padx=5)
                i+=1
        elif self.mode_value.get() =='minor':
            scale_sel = self.provide_chords(self.mode_value.get(), self.base_value_minor.get())
            i=0
            for text in scale_sel:
                ttk.Radiobutton(self.chords_frame, text = text, variable = self.chord_selected, 
                            value = text, style='primary.Toolbutton',
                            command=self.chord_selection, width=14).grid(row=0, column=i, pady=10, padx=5)
                i+=1
    
    def chord_selection(self):
        self.clear_frame(self.single_chord_frame)
        self.chord_diagram = ttk.Label(self.single_chord_frame, text=f'Chord diagram test: {self.chord_selected.get()}')
        self.chord_diagram.pack()
    
if __name__=='__main__':
    app()