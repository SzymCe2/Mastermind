import tkinter as tk
from tkinter import ttk, messagebox, font
from generator_kodu import KodGenerator


class MastermindGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Mastermind 🎮")
        self.geometry("450x350")
        self.resizable(False, False)
        self.configure(bg="#1e1e2f")  

        self.generator = KodGenerator()

        self.styl_czcionki = font.Font(family="Comic Sans MS", size=12)
        self.styl_naglowka = font.Font(family="Comic Sans MS", size=20, weight="bold")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TLabel", background="#1e1e2f", foreground="white", font=self.styl_czcionki)
        self.style.configure("TButton", font=self.styl_czcionki, padding=6)
        self.style.configure("TRadiobutton", 
                            background="#1e1e2f", 
                            foreground="white", 
                            font=self.styl_czcionki,
                            indicatorcolor="#ffd966")  

    def create_widgets(self):
        label_title = ttk.Label(self, text="🎮 Witaj w grze Mastermind!", font=self.styl_naglowka)
        label_title.pack(pady=20)

        label_instr = ttk.Label(self, text="Wybierz poziom trudności:")
        label_instr.pack(pady=(10, 5))

        radio_frame = ttk.Frame(self)
        radio_frame.pack(pady=5)
        radio_frame.configure(style="TLabel")

        self.trudnosc_var = tk.StringVar(value="latwy")
        radio_latwy = ttk.Radiobutton(
            radio_frame, 
            text="Łatwy", 
            variable=self.trudnosc_var, 
            value="latwy"
        )
        radio_latwy.pack(side=tk.LEFT, padx=10)
        
        radio_sredni = ttk.Radiobutton(
            radio_frame, 
            text="Średni", 
            variable=self.trudnosc_var, 
            value="sredni"
        )
        radio_sredni.pack(side=tk.LEFT, padx=10)
        
        radio_trudny = ttk.Radiobutton(
            radio_frame, 
            text="Trudny", 
            variable=self.trudnosc_var, 
            value="trudny"
        )
        radio_trudny.pack(side=tk.LEFT, padx=10)

        btn_start = tk.Button(
            self, 
            text="Rozpocznij grę", 
            command=self.start_game,
            font=self.styl_czcionki,
            bg="#ffd966",  
            fg="#333333",  
            activebackground="#e6c252", 
            relief="raised",
            bd=2,
            padx=15,
            pady=5
        )
        btn_start.pack(pady=20)

        self.output_label = ttk.Label(self, text="", foreground="#66ff66")
        self.output_label.pack(pady=10)

    def start_game(self):
        poziom = self.trudnosc_var.get()
        if not poziom:
            messagebox.showwarning("Błąd", "Wybierz poziom trudności.")
            return

        kod = self.generator.generuj_kod(trudnosc=poziom)
        self.output_label.config(text=f"🔐 Kod został wygenerowany: {kod}")  

#TODODdokończyć

if __name__ == "__main__":
    app = MastermindGUI()
    app.create_widgets()
    app.mainloop()
