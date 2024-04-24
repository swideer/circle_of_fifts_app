from tkinter import *
from ttkbootstrap import Style
from tkinter import ttk
from PIL import ImageTk, Image 
import webbrowser
import os
import sys

class app:
    def __init__(self):
        self.root = Tk()
        style = Style(theme='darkly')
        style.configure('title.TLabel', font=('Verdana', 24))
        style.configure('chord.TLabel', font=('Courier', 20))
                        
        self.root.title("Music app")
        self.root.geometry("1250x900+10+10")
        self.root.resizable(width=True, height=True)
        self.options_mode = options_mode
        self.options_base_major = options_base_major
        self.options_base_minor = options_base_minor
        self.generate_chord = self.generate_chord

        self.label_title = ttk.Label(self.root, text="Circle of Fifths", style='title.TLabel')
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
        #Main for label
        self.single_chord_frame = ttk.Frame(self.root)
        self.single_chord_frame.place(relx=.5, anchor="center")
        self.single_chord_frame.pack()
        #Main for details
        self.chord_label = ttk.Frame(self.single_chord_frame)
        self.chord_label.grid(row=0,column=1)
        self.chord_label_options = ttk.Frame(self.single_chord_frame)
        self.chord_label_options.grid(row=1,column=1)
        #Guitar diagram
        self.chord_guitar = ttk.Frame(self.single_chord_frame)
        self.chord_guitar.grid(row=2,column=0)
        #Piano diagram
        self.chord_piano = ttk.Frame(self.single_chord_frame)
        self.chord_piano.grid(row=2, column=1)
        #Notes
        self.chord_notes = ttk.Frame(self.single_chord_frame)
        self.chord_notes.grid(row=2, column=2)

        #QUIT BUTTON
        self.button_quit = ttk.Button(self.root, text="Quit", style='primary.Outline.TButton', command=self.root.destroy)
        self.button_quit.place(relx=.5, anchor="center")
        self.button_quit.pack(side=BOTTOM, pady=20)

        #SELF ADVERTISEMENT
        self.self_label = ttk.Label(self.root, text="by swDEVr", style='primary.TLabel')
        self.self_label.place(relx=.5, anchor="center")
        self.self_label.pack(side=BOTTOM, pady=3)
        self.self_label.bind("<Button-1>", lambda e: self.callback('https://github.com/swideer/'))

        self.root.mainloop()

    def callback(self, url):
        webbrowser.open_new(url)

    def clear_frame(self, frame):
        '''
        Clears frame before populating it again. This way it prevents overlaping frames, with each user action.
        '''
        for widget in frame.winfo_children():
            widget.destroy()

    def select_mode(self):
        '''
        Populates frame with scales buttons from each mode.
        '''
        self.clear_frame(self.bases_frm)
        self.clear_frame(self.chords_frame)
        self.clear_frame(self.chord_guitar)
        self.clear_frame(self.chord_piano)
        self.clear_frame(self.chord_notes)
        self.clear_frame(self.chord_label)
        self.clear_frame(self.chord_label_options)
        self.scales_label1 = ttk.Label(self.bases_frm, text="Scales:", anchor='center')
        self.scales_label1.grid(row=0, columnspan=12)
        if self.mode_value.get() == 'major':
            self.base_value_major = StringVar(self.root, '0')
            i=0
            for (text, value) in self.options_base_major.items():
                ttk.Radiobutton(self.bases_frm, text = text, variable = self.base_value_major, 
                            value = text, style='primary.Toolbutton',
                            command=self.base_selection, width=7).grid(row=1, column=i, pady=10, padx=5)
                i+=1
        elif self.mode_value.get() == 'minor':
            self.base_value_minor = StringVar(self.root, '0')
            i=0
            for (text, value) in self.options_base_minor.items():
                ttk.Radiobutton(self.bases_frm, text = text, variable = self.base_value_minor, 
                            value = text, style='primary.Toolbutton',
                            command=self.base_selection, width=7).grid(row=1, column=i, pady=10, padx=5)
                i+=1
    
    def base_selection(self):
        '''
        Populates frame with chords buttons accordingly to chosen scale.
        '''
        self.chord_selected = StringVar(self.root, '0')
        self.clear_frame(self.chords_frame)
        self.clear_frame(self.chord_guitar)
        self.clear_frame(self.chord_piano)
        self.clear_frame(self.chord_notes)
        self.clear_frame(self.chord_label)
        self.clear_frame(self.chord_label_options)
        self.scales_label2 = ttk.Label(self.chords_frame, text="Chords:", anchor='center')
        self.scales_label2.grid(row=0, columnspan=7)
        #POPULATE CHORDS FRAME
        if self.mode_value.get() == 'major':
            scale_sel = scales_chords[self.mode_value.get()][self.base_value_major.get()]
            i=0
            for text in scale_sel:
                ttk.Radiobutton(self.chords_frame, text = text, variable = self.chord_selected, 
                            value = text, style='primary.Toolbutton',
                            command=self.chord_selection, width=14).grid(row=1, column=i, pady=10, padx=5)
                i+=1
        elif self.mode_value.get() =='minor':
            scale_sel = scales_chords[self.mode_value.get()][self.base_value_minor.get()]
            i=0
            for text in scale_sel:
                ttk.Radiobutton(self.chords_frame, text = text, variable = self.chord_selected, 
                            value = text, style='primary.Toolbutton',
                            command=self.chord_selection, width=14).grid(row=1, column=i, pady=10, padx=5)
                i+=1
    
    def chord_selection(self):
        '''
        Populates frame with chord details, including guitar tabulature, chord piano keys and notes.
        '''
        self.clear_frame(self.chord_guitar)
        self.clear_frame(self.chord_piano)
        self.clear_frame(self.chord_notes)
        self.clear_frame(self.chord_label)
        self.clear_frame(self.chord_label_options)
        #MAIN LABEL
        self.chord_label_label = ttk.Label(self.chord_label, text=f'Chord {self.chord_selected.get()} details', anchor='center')
        self.chord_label_label.grid(row=0, column=0)
        #OPTIONAL LABEL
        self.chord_options = ttk.Label(self.chord_label_options, text=f'{self.generate_chord(self.chord_selected.get(), True)}', anchor='center')
        self.chord_options.grid(row=0, column=0)
        #GUITAR TAB DIAGRAM
        self.guitar_label = ttk.Label(self.chord_guitar, text='Guitar tab', width=40, anchor='center')
        self.guitar_label.grid(row=0, column=0)
        self.configure_diagram(self.generate_chord(self.chord_selected.get(), False))
        #PPIANO KEYS
        self.piano_label = ttk.Label(self.chord_piano, text='Piano keys', anchor='center')
        self.piano_label.grid(row=0, column=0)
        self.configure_image(self.chord_selected.get() + ".jpeg", self.chord_piano, 1)
        self.piano_label_1st = ttk.Label(self.chord_piano, text='Piano 1st inversion', width=40, anchor='center')
        self.piano_label_1st.grid(row=2, column=0)
        self.configure_image(self.chord_selected.get() + " 1st.jpeg", self.chord_piano, 3)
        self.piano_label_2nd = ttk.Label(self.chord_piano, text='Piano 2nd inversion', anchor='center')
        self.piano_label_2nd.grid(row=4, column=0)
        self.configure_image(self.chord_selected.get() + " 2nd.jpeg", self.chord_piano, 5)
        #PIANO NOTES
        self.piano_label_notes = ttk.Label(self.chord_notes, text='Chord notes',width=40, anchor='center')
        self.piano_label_notes.grid(row=0, column=0)
        self.configure_image(self.chord_selected.get() + ".png", self.chord_notes, 1)

    def resource_path(self, relative_path):
        '''
        Provides absolute path to images. Needed for distribution to work.
        '''
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def configure_image(self, path, frame, row):
        '''
        Returns acccoridng images from assets forlder. Piano diagrams, and chord notes. 
        Images taken from https://www.scales-chords.com
        Accepts:
        1. file name consisting of capitalised full chord name with description (i.e. G diminished, C sharp minor)
        2. frame which should be populated
        3. row of frame to be populated, as chord details frame uses grid layout manager
        '''
        img = ImageTk.PhotoImage(Image.open(self.resource_path(f"assets/images/{path}")).resize((250,120) , resample=5))
        display = ttk.Label(frame)
        display.config(image=img)
        display.image = img
        display.grid(row=row, column=0, padx=10)

    def configure_diagram(self, chord):
        '''
        Populates frame with guitar chord tabulature. Accepts return of generate_chord(). 
        '''
        self.guitar_diagram = ttk.Label(self.chord_guitar, style='chord.TLabel', text=f'{chord}')
        self.guitar_diagram.grid(row=1, column=0)

    def generate_chord(self, chord, options):
        '''
        Returns guitar chord tabulature. Accepts:
        1. capitalised chord name with full description. Example: G diminished or C sharp minor
        2. options indicator (True or False) if the chord have additional description, like E sharp diminished.
        '''
        if options == False:
            base_chord = "E|--str1--\nB|--str2--\nG|--str3--\nD|--str4--\nA|--str5--\nE|--str6--"
            requested = chords[chord]
            for key in requested:
                base_chord = base_chord.replace(key, requested[key])
            return base_chord
        elif options==True:
            try:
                options_value = chords[chord]['options']
                return options_value
            except KeyError:
                return ""

if __name__=='__main__':
    from data import *
    app()
else:
    from assets.data import *