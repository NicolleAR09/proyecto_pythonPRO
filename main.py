import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style

#Create class 
class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter App")
        self.style = Style(theme='morph')
        self.root.geometry("600x350")
        
        self.create_widgets()

    def create_widgets(self):
        # set unit types to choose from 
        self.unit_types = ["Longitud", "Peso", "Masa", "Temperatura"]
        # set units according to the unit types 
        self.units = {
            "Longitud": [("Metro", 1.0), ("Kilómetro", 1000.0), ("Centímetro", 0.01), ("Milímetro", 0.001)],
            "Peso": [("Gramo", 1.0), ("Kilogramo", 1000.0), ("Miligramo", 0.001)],
            "Masa": [("Tonelada", 1000000.0), ("Kilogramo", 1000.0), ("Gramo", 1.0)],
            "Temperatura": [("Celsius", 1.0), ("Fahrenheit", 0.5555555555555556, 32), ("Kelvin", 1.0, -273.15)]
        }
        
        self.selected_unit_type = tk.StringVar(value=self.unit_types[0]) #select a unit type from the previous list
        self.selected_unit_from = tk.StringVar(value=self.units[self.unit_types[0]][0][0]) # select the unit according to the unit type 
        self.selected_unit_to = tk.StringVar(value=self.units[self.unit_types[0]][1][0]) # select the value of the unit according to the unit type
        
        #text tipo de unidad
        ttk.Label(self.root, text="Tipo de Unidad:").pack(pady=10)

        # deplegable unit type
        self.unit_type_menu = ttk.Combobox(self.root, textvariable=self.selected_unit_type, values=self.unit_types)
        self.unit_type_menu.pack()
        self.unit_type_menu.bind("<<ComboboxSelected>>", self.update_unit_options)
        
        # text convertir de 
        ttk.Label(self.root, text="Convertir de:").place(x=80, y=100)
        self.unit_from_menu = ttk.Combobox(self.root, textvariable=self.selected_unit_from)
        self.unit_from_menu.place(x=50, y=120)
        
        # text convertir a 
        ttk.Label(self.root, text="Convertir a:").place(x=440, y=100)
        self.unit_to_menu = ttk.Combobox(self.root, textvariable=self.selected_unit_to)
        self.unit_to_menu.place(x=400, y=120)
        
        # entry box for the number 
        ttk.Label(self.root, text="Ingresar valor:").place(x=80, y=180)
        self.value_entry = ttk.Entry(self.root)
        self.value_entry.place(x=50, y=200)
        
        # convert button
        self.convert_button = ttk.Button(self.root, text="Convertir", command=self.convert_units)
        self.convert_button.pack(pady=90)
        
        # result text 
        ttk.Label(self.root, text="Resultado:").place(x=440, y=180)
        self.result_label = ttk.Label(self.root, text="Resultado:")
        self.result_label.place(x=440, y=180)
        
        self.update_unit_options()
        
    def update_unit_options(self, event=None):
        unit_type = self.selected_unit_type.get()
        units = [unit[0] for unit in self.units[unit_type]]
        self.unit_from_menu['values'] = units
        self.unit_to_menu['values'] = units
        self.selected_unit_from.set(units[0])
        self.selected_unit_to.set(units[1])
    
    def convert_units(self):
        unit_type = self.selected_unit_type.get()
        from_unit = self.selected_unit_from.get()
        to_unit = self.selected_unit_to.get()
        
        try:
            value = float(self.value_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un valor numérico válido.")
            return
        
        if unit_type == "Temperatura":
            self.convert_temperature(from_unit, to_unit, value)
        else:
            self.convert_general(unit_type, from_unit, to_unit, value)
    
    def convert_general(self, unit_type, from_unit, to_unit, value):
        from_factor = next(unit[1] for unit in self.units[unit_type] if unit[0] == from_unit)
        to_factor = next(unit[1] for unit in self.units[unit_type] if unit[0] == to_unit)
        
        result = value * from_factor / to_factor
        self.result_label.config(text=f"{result:.4f} {to_unit}")
        self.result_label.place(x=420, y=210)

    def convert_temperature(self, from_unit, to_unit, value):
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result = (value * 9/5) + 32
            elif to_unit == "Kelvin":
                result = value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = (value - 32) * 5/9
            elif to_unit == "Kelvin":
                result = (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = value - 273.15
            elif to_unit == "Fahrenheit":
                result = (value - 273.15) * 9/5 + 32
        
        self.result_label.config(text=f"{result:.4f} {to_unit}")
        self.result_label.place(x=420, y=210)

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()
