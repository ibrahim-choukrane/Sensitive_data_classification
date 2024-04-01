import tkinter as tk
from tkinter import ttk  # for notebook widget
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3

# Database connection and table creation (if not exists)
conn = sqlite3.connect('gas_consumption.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS consumption (
             vehicle text,
             date text,
             consumption real
             )''')
conn.commit()


class VehiclePage(tk.Frame):
    def __init__(self, root, vehicle_name):
        super().__init__(root)
        self.vehicle_name = vehicle_name
        self.date_var = tk.StringVar()
        self.consumption_var = tk.DoubleVar()

        # Entry fields for date and consumption
        date_label = tk.Label(self, text="Date (YYYY-MM-DD):")
        date_label.pack()
        date_entry = tk.Entry(self, textvariable=self.date_var)
        date_entry.pack()

        consumption_label = tk.Label(self, text="Consumption (Liters):")
        consumption_label.pack()
        consumption_entry = tk.Entry(self, textvariable=self.consumption_var)
        consumption_entry.pack()

        # Button to save data and update graph
        save_button = tk.Button(self, text="Save and Update Graph", command=self.save_data)
        save_button.pack()

        # Frame for the graph (initially empty)
        self.graph_frame = tk.Frame(self, width=500, height=300)
        self.graph_frame.pack()
        self.update_graph()

    def save_data(self):
        date = self.date_var.get()
        consumption = self.consumption_var.get()

        # Insert data into database
        c.execute("INSERT INTO consumption VALUES (?, ?, ?)", (self.vehicle_name, date, consumption))
        conn.commit()

        # Clear entry fields
        self.date_var.set("")
        self.consumption_var.set(0.0)

        # Update graph
        self.update_graph()

    def update_graph(self):
        # Fetch data from database for this vehicle
        c.execute(f"SELECT date, consumption FROM consumption WHERE vehicle = '{self.vehicle_name}'")
        data = c.fetchall()

        # Extract dates and consumptions for plotting
        dates = [row[0] for row in data]
        consumptions = [row[1] for row in data]

        # Create a Matplotlib figure
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.plot(dates, consumptions, marker='o', linestyle='-')
        ax.set_xlabel("Date")
        ax.set_ylabel("Consumption (Liters)")
        ax.set_title(f"{self.vehicle_name} Gas Consumption")

        # Clear previous graph (if any)
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        # Embed the Matplotlib figure into the Tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gas Consumption Tracker")

        # Create a notebook to hold different vehicle pages
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create pages for different vehicles
        self.car_page = VehiclePage(self.notebook, "Car")
        self.motorcycle_page = VehiclePage(self.notebook, "Motorcycle")
        self.truck_page = VehiclePage(self.notebook, "Truck")
        self.bus_page = VehiclePage(self.notebook, "Bus")
        self.other_page = VehiclePage(self.notebook, "Other")

        # Add pages to the notebook
        self.notebook.add(self.car_page, text="Car")
        self.notebook.add(self.motorcycle_page, text="Motorcycle")
        self.notebook.add(self.truck_page, text="Truck")
        self.notebook.add(self.bus_page, text="Bus")
        self.notebook.add(self.other_page, text="Other")
        
        # Start the main event loop
        self.mainloop()

if __name__ == "__main__":
    app = MainApp()
