import tkinter as tk
from tkinter import ttk

from constants import *

class NautilusParams:
    def __init__(self):
        self.mass = tk.IntVar()
        self.volume = tk.IntVar()
        self.phaseDuration = tk.IntVar()
        self.maxYPower = tk.IntVar()
        self.maxXPower = tk.IntVar()
        self.minYPower = tk.IntVar()
