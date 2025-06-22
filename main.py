import generator_kodu
from interfejs import MastermindGUI


def mastermind():
    ukryty_kod = generator_kodu.KodGenerator().generuj_kod(4, unikalne=False)
    app = MastermindGUI()
  #  app.create_widgets()
    app.mainloop()


mastermind()