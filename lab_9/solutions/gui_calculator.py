import string
import tkinter as tk
from functools import partial

from lab_9.tools.calculator import Calculator, EmptyMemory


class CalculatorGUI(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.variables = {}
        self.state = tk.BooleanVar(value=True)
        self.calculator = Calculator()
        self._init_variables()

        screen, self.memory, self.screen = self._init_screen()
        screen.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.bottom_pad = self._init_bottom_pad()
        self.bottom_pad.pack(side=tk.BOTTOM)

        self.focus_set()
        self.bind("<Key>", self.input_from_keyboard)

    def _init_variables(self):
        self.variables['var_1'] = ''
        self.variables['var_2'] = ''
        self.variables['operator'] = ''
        self.state.set(True)
        self.operations = set(self.calculator.operations.keys())

    def _init_screen(self):
        screen = tk.Frame(self)
        memory_screen = tk.Label(screen, bg='white', width=4)
        memory_screen.pack(side=tk.LEFT)
        main_screen = tk.Label(screen, bg='white')
        main_screen.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        return screen, memory_screen, main_screen

    def _init_bottom_pad(self):
        bottom_pad = tk.Frame(self)

        # memory pad
        memory_pad = tk.Frame(bottom_pad)
        memory_pad.pack(side=tk.LEFT)
        for ii, (label, command) in enumerate([
            ('MC', self.clean_memory),
            ('MR', self.use_memory),
            ('M+', self.memorize),
            ('C', self.clear),
        ]):
            tk.Button(
                memory_pad, text=label, width=5,
                command=command
            ).grid(row=ii, column=0)

        # num pad
        num_pad = tk.Frame(bottom_pad)
        num_pad.pack(side=tk.LEFT)
        ii = 0
        for ii, num in enumerate(range(9, 0, -1)):
            tk.Button(
                num_pad, text=num, width=5,
                command=partial(self.update_var, num)
            ).grid(row=ii // 3, column=(2-ii) % 3)

        for ii, (label, command) in enumerate([
            ('0', partial(self.update_var, 0)),
            ('.', partial(self.update_var, '.')),
            ('=', self.calculate_result),
        ], ii+1):
            tk.Button(
                num_pad, text=label, width=5,
                command=command
            ).grid(row=ii // 3, column=ii % 3)

        # operation pad
        operation_pad = tk.Frame(bottom_pad)
        operation_pad.pack(side=tk.RIGHT)
        for ii, operation in enumerate(self.operations):
            tk.Button(
                operation_pad, text=operation, width=5,
                command=partial(self.set_operator, operation),
            ).grid(row=ii, column=0)

        return bottom_pad

    # region printing
    def update_screen(self):
        text = f"{self.variables['var_1']}"
        if self.variables['operator']:
            text += f" {self.variables['operator']}"
        if self.variables['var_2']:
            text += f" {self.variables['var_2']}"
        self.screen['text'] = text

    def clear(self):
        key = self._get_var_key()
        self.variables[key] = ''
        self.update_screen()
    # endregion printing

    # region operation
    def _get_var_key(self):
        return 'var_1' if self.state.get() else 'var_2'

    def update_var(self, char):
        key = self._get_var_key()
        if char != '.' or char not in self.variables[key]:
            self.variables[key] += str(char)
            self.variables[key] = self.variables[key].lstrip('0')
            self.update_screen()

    @staticmethod
    def _to_value(var):
        try:
            return float(var)
        except ValueError:
            return

    def set_operator(self, operator):
        if self.state.get():
            self.variables['operator'] = operator
            self.state.set(not self.state.get())
            self.update_screen()

    def calculate_result(self):
        var_1 = self._to_value(self.variables['var_1'])
        var_2 = self._to_value(self.variables['var_2'])
        if var_1 is not None and var_2 is not None:
            self.screen['text'] = self.calculator.run(
                self.variables['operator'], var_1, var_2
            )
            self._init_variables()

    def input_from_keyboard(self, event):
        print(event.keycode)
        if event.char in string.digits + '.':
            self.update_var(event.char)
        elif event.char in self.operations:
            self.set_operator(event.char)
        elif event.char in '\r=':
            self.calculate_result()
    # endregion operation

    # region memory
    def _get_memory(self):
        try:
            value = str(self.calculator.memory)
        except EmptyMemory:
            value = ''
        return value

    def memorize(self):
        self.calculator.memorize()
        if self._get_memory():
            self.memory['text'] = 'M'

    def clean_memory(self):
        self.calculator.clean_memory()
        self.memory['text'] = ''

    def use_memory(self):
        key = self._get_var_key()
        value =self._get_memory()
        self.variables[key] = value
        self.update_screen()
    # endregion memory


if __name__ == '__main__':
    root = tk.Tk()
    CalculatorGUI(root).pack()
    root.mainloop()