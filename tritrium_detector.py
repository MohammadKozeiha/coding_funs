import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

class TritiumSensorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tritium Particle Sensor")

        # Simulated data
        self.tritium_data = [random.uniform(0, 10) for _ in range(50)]

        # GUI components
        self.create_widgets()

    def create_widgets(self):
        # Data plot
        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.plot = self.figure.add_subplot(1, 1, 1)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Start button
        self.start_button = ttk.Button(self.root, text="Start", command=self.start_sensor)
        self.start_button.pack(side=tk.LEFT, padx=10)

        # Stop button
        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop_sensor)
        self.stop_button.pack(side=tk.LEFT, padx=10)

    def start_sensor(self):
        # Simulate real-time data acquisition
        for _ in range(10):
            new_data_point = random.uniform(0, 10)
            self.tritium_data.append(new_data_point)
            self.update_plot()
            self.root.after(1000)  # Simulated delay (1 second)

    def stop_sensor(self):
        # Stop the sensor or perform cleanup if needed
        pass

    def update_plot(self):
        self.plot.clear()
        self.plot.plot(self.tritium_data, marker='o', linestyle='-')
        self.plot.set_xlabel("Time")
        self.plot.set_ylabel("Tritium Concentration")
        self.plot.set_title("Tritium Particle Sensor Data")
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = TritiumSensorApp(root)
    root.mainloop()
