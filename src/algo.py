
from datetime import datetime, timedelta

from src.results import Results


class Algo:

    def __init__(self, gui):
        self._gui = gui
        self._filename= 'history.txt'
        self._data=None
        self._results = None

    def read_last_line(self):
        try:
            with open(self._filename, 'r') as file:
                lines = file.readlines()
                if lines:
                    last_line = lines[-1].strip()
                    return last_line
                else:
                    return "The file is empty."
        except FileNotFoundError:
            return "File not found."

    def write_to_history(self,number):
        try:
            with open(self._filename, 'a') as file:
                file.write('\n' + str(number))
        except Exception as e:
            print("An error occurred:", e)

    def kk(self):
        pass

    def calculate(self):
        kWh = float(self._gui.entry_kWh.get())
        MkWh = float(self._gui.entry_MkWh.get())
        kVA = round(float(self._gui.entry_kVA.get()) / 2, 1)
        fixed_payment = round(float(self._gui.entry_fixed_payment.get()) / 2, 1)
        debits_credits = round(float(self._gui.entry_debits_credits.get()) / 2, 1)
        NkWh = float(self._gui.entry_NkWh.get())

        history_NkWh = float(self.read_last_line())
        total_NkWh = round(NkWh - history_NkWh, 1)
        self.write_to_history(NkWh)
        MNkWh = round(total_NkWh * (MkWh / kWh), 1)
        water_heater = round((float(self._gui.entry_water_heater.get()) / 5) * 2, 1)
        total_without_VAT = round(MNkWh + kVA + fixed_payment + debits_credits, 1)
        VAT = round(total_without_VAT * 0.17, 1)
        total_with_VAT = round(total_without_VAT + VAT, 1)
        total = round(total_with_VAT + water_heater, 1)

        today = datetime.now()
        one_week_later = today + timedelta(weeks=1)

        # Format the date in numbers
        formatted_date = today.strftime("%d-%m-%y")
        formatted_one_week_later = one_week_later.strftime("%d-%m-%y")
        NIS = '₪'
        self._gui.result_text.set(
            f"חשבון חשמל דו-חודשי עמית ועדן\n"
            f"{'=' * 40}\n"
            f"תאריך עריכת החשבון: {formatted_date}\n"
            f"עד תאריך: {self._gui.entry_until_date.get()}\t מתאריך: {self._gui.entry_date.get()}\n"
            f"קריאה נוכחית: {NkWh}\t קריאה קודמת: {history_NkWh}\n"
            f"סה\"כ קוט\"ש: {total_NkWh}\n"
            f"חיוב בגין צריכה: {NIS}{MNkWh}\n"
            f"תשלום בגין הספק: {NIS}{kVA}\n"
            f"תשלום קבוע: {NIS}{fixed_payment}\n"
            f"חיובים וזיכויים שונים: {NIS}{debits_credits}\n"
            f"{'~' * 20}\n"
            f"סה\"כ ללא מע\"מ: {NIS}{total_without_VAT}\n"
            f"מע\"מ 17%: {NIS}{VAT}\n"
            f"{'~' * 20}\n"
            f"סה\"כ כולל מע\"מ: {NIS}{total_with_VAT}\n"
            f" +\n"
            f"תוספת דוד שמש כולל מע\"מ: {NIS}{water_heater}\n"
            f"{'-' * 40}\n"
            f"סה\"כ לתשלום: {NIS}{total}\n"
            f"{'-' * 40}\n"
            f":נתונים לחישוב\n"
            f"מחיר לקוט\"ש 1 אחרי מע\"מ: {NIS}{round((MkWh / kWh) * 1.17, 3)}\t מע\"מ 17%: {NIS}{round((MkWh / kWh) * 0.17, 3)}\tמחיר לקוט\"ש 1 לפני מע\"מ: {NIS}{round((MkWh / kWh), 3)}\n"
            f":אפשרויות לתשלום\n"
            f"לתשלום לא יאוחר מתאריך: {formatted_one_week_later}"

        )
        self._data = self._gui.result_text.get().split('\n')
        self._results = Results(self._data)

