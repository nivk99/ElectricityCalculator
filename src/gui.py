import tkinter as tk

from src.algo import Algo


class GUI:



    def __init__(self):
        self._root = tk.Tk()
        self.entry_water_heater = tk.Entry(self._root)
        self.entry_NkWh = tk.Entry(self._root)
        self.entry_debits_credits = tk.Entry(self._root)
        self.entry_fixed_payment = tk.Entry(self._root)
        self.entry_kVA = tk.Entry(self._root)
        self.entry_MkWh = tk.Entry(self._root)
        self.entry_kWh = tk.Entry(self._root)
        self.entry_until_date = tk.Entry(self._root)
        self.entry_date = tk.Entry(self._root)
        self.result_text = tk.StringVar()
        self.run()



    def run(self):
        self._root.title("מחשבון חשבונות")

        # Create and place the labels and entry fields
        tk.Label(self._root, text="מתאריך:").grid(row=0, column=0)
        self.entry_date.grid(row=0, column=1)

        # Create and place the labels and entry fields
        tk.Label(self._root, text="עד תאריך:").grid(row=1, column=0)
        self.entry_until_date.grid(row=1, column=1)

        # Create and place the labels and entry fields
        tk.Label(self._root, text="סה\"כ צריכה של קוט\"ש:").grid(row=2, column=0)
        self.entry_kWh.grid(row=2, column=1)

        # Create and place the labels and entry fields
        tk.Label(self._root, text="סה\"כ חיוב צריכת כסף קוט\"ש:").grid(row=3, column=0)
        self.entry_MkWh.grid(row=3, column=1)

        # Create and place the labels and entry fields
        tk.Label(self._root, text="תשלום בגין הספק:").grid(row=4, column=0)
        self.entry_kVA.grid(row=4, column=1)

        # Create and place the labels and entry fields
        tk.Label(self._root, text="תשלום קבוע:").grid(row=5, column=0)
        self.entry_fixed_payment.grid(row=5, column=1)

        # Create and place the labels and entry fields
        tk.Label(self._root, text="חיובים וזיכויים שונים:").grid(row=6, column=0)
        self.entry_debits_credits.grid(row=6, column=1)

        # Create and place the labels and entry fields
        tk.Label(self._root, text="הקלד קריאה נוכחית של דיירים:").grid(row=7, column=0)
        self.entry_NkWh.grid(row=7, column=1)

        # Create and place the labels and entry fields
        tk.Label(self._root, text="סה\"כ דוד שמש:").grid(row=8, column=0)
        self.entry_water_heater.grid(row=8, column=1)

        result_label = tk.Label(self._root, textvariable=self.result_text, justify="right")
        result_label.grid(row=12, columnspan=2)

        calculate_button = tk.Button(self._root, text="חשב", command=Algo(self).calculate)
        calculate_button.grid(row=13, columnspan=2)

        self._root.mainloop()

