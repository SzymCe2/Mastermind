import tkinter as tk
from tkinter import ttk, messagebox, font
from generator_kodu import KodGenerator
from porownywanie_odp import porownywanie_odp


class MastermindGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Mastermind")
        self.geometry("850x500")
        self.resizable(False, False)
        self.configure(bg="#1e1e2f")

        self.generator = KodGenerator()

        self.styl_czcionki = font.Font(family="Comic Sans MS", size=12)
        self.styl_naglowka = font.Font(family="Comic Sans MS", size=20, weight="bold")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TLabel", background="#1e1e2f", foreground="white", font=self.styl_czcionki)
        self.style.configure("TButton", font=self.styl_czcionki, padding=6)
        self.style.configure("TCombobox", font=self.styl_czcionki)

        self.create_widgets()

        self.kod = []
        self.porownywarka = None
        self.attempts = 0
        self.max_attempts = 10
        self.guess_vars = []

    def create_widgets(self):
        label_title = ttk.Label(self, text="🎮 Witaj w Mastermind!", font=self.styl_naglowka)
        label_title.pack(pady=20)

        label_instr = ttk.Label(self, text="Wybierz poziom trudności:")
        label_instr.pack(pady=(10, 5))

        radio_frame = ttk.Frame(self)
        radio_frame.pack(pady=5)

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

        self.guess_frame = ttk.Frame(self)
        self.guess_frame.pack(pady=10)

        self.btn_guess = tk.Button(
            self,
            text="Zgadnij",
            command=self.make_guess,
            font=self.styl_czcionki,
            bg="#66ccff",
            fg="#333333",
            activebackground="#5599dd",
            relief="raised",
            bd=2,
            padx=15,
            pady=5,
            state=tk.DISABLED
        )
        self.btn_guess.pack(pady=10)

        self.feedback_label = ttk.Label(self, text="", foreground="#b290fd")
        self.feedback_label.pack(pady=10)

        self.hint_label = ttk.Label(self, text="", foreground="#ffff66")
        self.hint_label.pack()

    def get_colors_for_difficulty(self, poziom):
        if poziom == 'latwy':
            return ['czerwony', 'zielony', 'niebieski', 'żółty', 'biały', 'czarny']
        elif poziom == 'sredni':
            return ['czerwony', 'zielony', 'niebieski', 'żółty', 'biały', 'czarny']
        elif poziom == 'trudny':
            return ['czerwony', 'zielony', 'niebieski', 'żółty', 'biały', 'czarny', 'fioletowy', 'pomarańczowy']
        else:
            return []

    def start_game(self):
        poziom = self.trudnosc_var.get()
        if not poziom:
            messagebox.showwarning("Błąd", "Wybierz poziom trudności.")
            return

        self.kod = self.generator.generuj_kod(trudnosc=poziom)
        self.porownywarka = porownywanie_odp(self.kod)
        self.attempts = 0
        self.feedback_label.config(text="")
        self.hint_label.config(text="")

        for widget in self.guess_frame.winfo_children():
            widget.destroy()
        self.guess_vars.clear()

        self.create_color_selectors(poziom)

        self.btn_guess.config(state=tk.NORMAL)
        self.feedback_label.config(text=f"🔐 Kod został wygenerowany! Masz {self.max_attempts} prób.")

    def create_color_selectors(self, poziom):
        kolory = self.get_colors_for_difficulty(poziom)

        for i in range(len(self.kod)):
            var = tk.StringVar(value=kolory[0])
            self.guess_vars.append(var)

            cb = ttk.Combobox(self.guess_frame, values=kolory, textvariable=var, state="readonly", width=12)
            cb.pack(side=tk.LEFT, padx=5)

    def make_guess(self):
        guess = [var.get() for var in self.guess_vars]
        try:
            self.attempts += 1
            dobra, dobry_kolor = self.porownywarka.porownanie(guess)
        except ValueError as e:
            messagebox.showerror("Błąd", str(e))
            return

        if dobra == len(self.kod):
            messagebox.showinfo("Gratulacje!", f"Udało się zgadnąć kod w {self.attempts} próbach!")
            self.btn_guess.config(state=tk.DISABLED)
            self.feedback_label.config(text="")
            return

        self.feedback_label.config(
            text=f"Próba {self.attempts}/{self.max_attempts}: "
                 f"{dobra} kolory na właściwych miejscach, {dobry_kolor} kolory na złych miejscach.")

        if self.attempts >= self.max_attempts:
            messagebox.showinfo("Koniec gry", f"Przegrałeś! Kod to: {', '.join(self.kod)}")
            self.btn_guess.config(state=tk.DISABLED)
