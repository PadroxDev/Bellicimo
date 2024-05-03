import tkinter as tk
from tkinter import ttk
from tkinter import IntVar
import os

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from hermite import DrawPlot
from hermite_params import HermiteParams
from nautilus import MoveNautilus
from nautilus_params import NautilusParams
from constants import *

class App(tk.Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.width = DEFAULT_WIDTH
		self.height = DEFAULT_HEIGHT

		self.initWindow()

		self.hermiteParams = HermiteParams()
		self.xPointVar = tk.StringVar()
		self.yPointVar = tk.StringVar()
		self.xPenteVar = tk.StringVar()
		self.yPenteVar = tk.StringVar()

		self.nautilusParams = NautilusParams()

	def initWindow(self):
		x, y = self.getCenterPos(DEFAULT_WIDTH, DEFAULT_HEIGHT)
		self.geometry('%dx%d+%d+%d' % (DEFAULT_WIDTH, DEFAULT_HEIGHT, x, y))

		self.title(DEFAULT_TITLE)
		self.iconbitmap("res/images/gtech.ico")

	def run(self):
		self.draw()
		# self.update()
		self.mainloop()

	# def update(self):
	#     self.after(REFRESH_RATE, self.update)

	def draw(self):
		self.config(bg=C_SEPARATION_LINE)

		self.sidebarFrame = tk.Frame(self, width=SIDEBAR_WIDTH, bg=C_SECONDARY, bd=0, highlightthickness=0)
		self.sidebarFrame.pack(side="left", fill="y")
		self.sidebarFrame.pack_propagate(0)

		self.renderFrame = tk.Frame(self, width=DEFAULT_WIDTH - SIDEBAR_WIDTH - SEPARATION_LINE_WIDTH, bg=C_MAIN, bd=0, highlightthickness=0)
		self.renderFrame.pack(side="right", fill="y")
		self.renderFrame.pack_propagate(0)

		self.big_text_label = tk.Label(self.renderFrame, text="Blob", font=F_TITLE, bg=C_MAIN, fg=C_TEXT)
		self.big_text_label.pack(side="top", pady= (50,0))

		self.nautilusVar = IntVar()


		# self.fig.set_facecolor("none")
		# self.ax.set_facecolor("none")



		# ICI Y FAUT LE TRUC POUR METTRE LE NAUTILUS

		self.choose()


		self.versionLabel = tk.Label(self.renderFrame, text='Version {}'.format(CURRENT_VERSION), fg=C_TEXT, bg=C_MAIN, font=F_CALIBRI)
		self.versionLabel.place(rely=1.0, relx=1.0, x=0, y=0, anchor="se")

	def updatePointValues(self):
		points = self.hermiteParams.points
		values = [str(points[i]) for i in range(len(points))]
		self.pointsCombobox.config(values=values)

	def drawButtonNautilus(self):
		self.nautilusCheckbox = tk.Checkbutton(self.sidebarFrame, text="Blob", variable=self.nautilusVar, font=F_CALIBRI, fg=C_MAIN, bg=C_SECONDARY, selectcolor=C_MAIN, activebackground=C_SECONDARY, onvalue=0, offvalue=1, indicatoron=False)
		self.nautilusCheckbox.pack(side="top", pady=(20, 5))
		self.nautilusCheckbox.config(command=self.choose)

		self.nautilusParams.mass.set(DEFAULT_MASS)

		mass = tk.Frame(self.sidebarFrame, bg=C_SECONDARY)
		mass.pack(fill="x", padx=15, pady=(20, 5))

		tk.Label(mass, text="Mass", font=F_CALIBRI, fg=C_MAIN, bg=C_SECONDARY, width=PARAM_WIDTH).pack(
			side="left", padx=(0, SIDEBAR_WIDTH*0.05))

		massEntry = tk.Entry(mass, font=F_CALIBRI, bg=C_SECONDARY, bd=0,  highlightcolor=C_ACCENT, highlightthickness=2,
			highlightbackground=C_MAIN, fg=C_MAIN, textvariable=self.nautilusParams.mass)
		massEntry.bind("<Return>", lambda event: self.drawNautilus(), lambda event: self.drawNautilus())
		massEntry.pack(side="right", fill="x")

		self.nautilusParams.volume.set(DEFAULT_VOLUME)

		volume = tk.Frame(self.sidebarFrame, bg=C_SECONDARY)
		volume.pack(fill="x", padx=15, pady=(20, 5))

		tk.Label(volume, text="Volume", font=F_CALIBRI, fg=C_MAIN, bg=C_SECONDARY, width=PARAM_WIDTH).pack(
			side="left", padx=(0, SIDEBAR_WIDTH*0.05))

		volumeEntry = tk.Entry(volume, font=F_CALIBRI, bg=C_SECONDARY, bd=0,  highlightcolor=C_ACCENT, highlightthickness=2,
			highlightbackground=C_MAIN, fg=C_MAIN, textvariable=self.nautilusParams.volume)
		volumeEntry.bind("<Return>", lambda event: self.drawNautilus(), lambda event: self.drawNautilus())
		volumeEntry.pack(side="right", fill="x")

		self.nautilusParams.phaseDuration.set(DEFAULT_PHASE_DURATION)

		phaseDuration = tk.Frame(self.sidebarFrame, bg=C_SECONDARY)
		phaseDuration.pack(fill="x", padx=15, pady=(20, 5))

		tk.Label(phaseDuration, text="Phase Duration", font=F_CALIBRI, fg=C_MAIN, bg=C_SECONDARY, width=PARAM_WIDTH).pack(
			side="left", padx=(0, SIDEBAR_WIDTH*0.05))

		phaseDurationEntry = tk.Entry(phaseDuration, font=F_CALIBRI, bg=C_SECONDARY, bd=0,  highlightcolor=C_ACCENT, highlightthickness=2,
			highlightbackground=C_MAIN, fg=C_MAIN, textvariable=self.nautilusParams.phaseDuration)
		phaseDurationEntry.bind("<Return>", lambda event: self.drawNautilus(), lambda event: self.drawNautilus())
		phaseDurationEntry.pack(side="right", fill="x")

		self.nautilusParams.maxYPower.set(DEFAULT_MAX_Y_POWER)

		maxYPower = tk.Frame(self.sidebarFrame, bg=C_SECONDARY)
		maxYPower.pack(fill="x", padx=15, pady=(20, 5))

		tk.Label(maxYPower, text="MaxYPower", font=F_CALIBRI, fg=C_MAIN, bg=C_SECONDARY, width=PARAM_WIDTH).pack(
			side="left", padx=(0, SIDEBAR_WIDTH*0.05))

		maxYPowerEntry = tk.Entry(maxYPower, font=F_CALIBRI, bg=C_SECONDARY, bd=0,  highlightcolor=C_ACCENT, highlightthickness=2,
			highlightbackground=C_MAIN, fg=C_MAIN, textvariable=self.nautilusParams.maxYPower)
		maxYPowerEntry.bind("<Return>", lambda event: self.drawNautilus(), lambda event: self.drawNautilus())
		maxYPowerEntry.pack(side="right", fill="x")

		self.nautilusParams.maxXPower.set(DEFAULT_MAX_X_POWER)

		maxXPower = tk.Frame(self.sidebarFrame, bg=C_SECONDARY)
		maxXPower.pack(fill="x", padx=15, pady=(20, 5))

		tk.Label(maxXPower, text="MaxXPower", font=F_CALIBRI, fg=C_MAIN, bg=C_SECONDARY, width=PARAM_WIDTH).pack(
			side="left", padx=(0, SIDEBAR_WIDTH*0.05))

		maxXPowerEntry = tk.Entry(maxXPower, font=F_CALIBRI, bg=C_SECONDARY, bd=0,  highlightcolor=C_ACCENT, highlightthickness=2,
			highlightbackground=C_MAIN, fg=C_MAIN, textvariable=self.nautilusParams.maxXPower)
		maxXPowerEntry.bind("<Return>", lambda event: self.drawNautilus(), lambda event: self.drawNautilus())
		maxXPowerEntry.pack(side="right", fill="x")

		self.nautilusParams.minYPower.set(DEFAULT_MIN_Y_POWER)

		minYPower = tk.Frame(self.sidebarFrame, bg=C_SECONDARY)
		minYPower.pack(fill="x", padx=15, pady=(20, 5))

		tk.Label(minYPower, text="MinYPower", font=F_CALIBRI, fg=C_MAIN, bg=C_SECONDARY, width=PARAM_WIDTH).pack(
			side="left", padx=(0, SIDEBAR_WIDTH*0.05))

		minYPowerEntry = tk.Entry(minYPower, font=F_CALIBRI, bg=C_SECONDARY, bd=0,  highlightcolor=C_ACCENT, highlightthickness=2,
			highlightbackground=C_MAIN, fg=C_MAIN, textvariable=self.nautilusParams.minYPower)
		minYPowerEntry.bind("<Return>", lambda event: self.drawNautilus(), lambda event: self.drawNautilus())
		minYPowerEntry.pack(side="right", fill="x")

	def drawButtonBlob(self):
		self.nautilusCheckbox = tk.Checkbutton(self.sidebarFrame, text="Nautilus", variable=self.nautilusVar, font=F_CALIBRI, fg=C_MAIN, bg=C_SECONDARY, selectcolor=C_MAIN, activebackground=C_SECONDARY, onvalue=1, offvalue=0, indicatoron=False)
		self.nautilusCheckbox.pack(side="top", pady=(20, 5))
		self.nautilusCheckbox.config(command=self.choose)
		self.pointsContainer = tk.Frame(self.sidebarFrame, bg=C_SECONDARY, height=SIDEBAR_POINTS_HEIGHT)
		self.pointsContainer.pack(fill="x", padx=10, pady=40)
		self.pointsContainer.pack_propagate(0)

		self.addBtnImg = tk.PhotoImage(file="res/images/add_button.png")
		self.addButton = tk.Button(self.pointsContainer, image=self.addBtnImg, bg=C_SECONDARY, bd=0, highlightthickness=0,
			activebackground=C_SECONDARY, command=self.addNewPoint)
		self.addButton.pack(side="right", padx=5)

		self.deleteBtnImg = tk.PhotoImage(file="res/images/bin_button.png")
		self.deleteButton = tk.Button(self.pointsContainer, image=self.deleteBtnImg, bg=C_SECONDARY, bd=0, highlightthickness=0,
			activebackground=C_SECONDARY, command=self.deleteSelectedPoint)
		self.deleteButton.pack(side="right", padx=5)

		self.pointsCombobox = ttk.Combobox(self.pointsContainer, background=C_ACCENT, foreground=C_TEXT, font=F_POINTS_COMBOBOX,
			state="readonly")
		self.updatePointValues()
		self.pointsCombobox.current(0)
		self.pointsCombobox.pack(fill='x', pady=5)

		self.hermiteParams.centerX.set(DEFAULT_CENTER_X)
		self.hermiteParams.centerY.set(DEFAULT_CENTER_Y)

		centerPointX = tk.Frame(self.sidebarFrame, bg=C_SECONDARY)
		centerPointX.pack(fill="x", padx=15, pady=(20, 5))

		tk.Label(centerPointX, text="Center x", font=F_CALIBRI, fg=C_MAIN, bg=C_SECONDARY, width=PARAM_WIDTH).pack(
			side="left", padx=(0, SIDEBAR_WIDTH*0.05))

		centerPointXEntry = tk.Entry(centerPointX, font=F_CALIBRI, bg=C_SECONDARY, bd=0,  highlightcolor=C_ACCENT, highlightthickness=2,
			highlightbackground=C_MAIN, fg=C_MAIN, textvariable=self.hermiteParams.centerX)
		centerPointXEntry.bind("<Return>", lambda event: self.drawBlob())
		centerPointXEntry.pack(side="right", fill="x")

		centerPointY = tk.Frame(self.sidebarFrame, bg=C_SECONDARY)
		centerPointY.pack(fill="x", padx=15, pady=(20, 5))

		tk.Label(centerPointY, text="Center y", font=F_CALIBRI, fg=C_MAIN, bg=C_SECONDARY, width=PARAM_WIDTH).pack(
			side="left", padx=(0, SIDEBAR_WIDTH*0.05))

		centerPointYEntry = tk.Entry(centerPointY, font=F_CALIBRI, bg=C_SECONDARY, bd=0,  highlightcolor=C_ACCENT, highlightthickness=2,
			highlightbackground=C_MAIN, fg=C_MAIN, textvariable=self.hermiteParams.centerY)
		centerPointYEntry.bind("<Return>", lambda event: self.drawBlob(), lambda event: self.drawBlob())
		centerPointYEntry.pack(side="right", fill="x")

		self.hermiteParams.precision.set(50)
		self.hermiteParams.intervalLength.set(30)

		precision = tk.Frame(self.sidebarFrame, bg=C_SECONDARY)
		precision.pack(fill="x", padx=15, pady=(20, 5))

		tk.Label(precision, text="Precision", font=F_CALIBRI, fg=C_MAIN, bg=C_SECONDARY, width=PARAM_WIDTH).pack(
			side="left", padx=(0, SIDEBAR_WIDTH*0.05))

		precisionEntry = tk.Entry(precision, font=F_CALIBRI, bg=C_SECONDARY, bd=0,  highlightcolor=C_ACCENT, highlightthickness=2,
			highlightbackground=C_MAIN, fg=C_MAIN, textvariable=self.hermiteParams.precision)
		precisionEntry.bind("<Return>", lambda event: self.drawBlob())
		precisionEntry.pack(side="right", fill="x")

		intervalLength = tk.Frame(self.sidebarFrame, bg=C_SECONDARY)
		intervalLength.pack(fill="x", padx=15, pady=(20, 5))

		tk.Label(intervalLength, text="Interval Length", font=F_CALIBRI, fg=C_MAIN, bg=C_SECONDARY, width=PARAM_WIDTH).pack(
			side="left", padx=(0, SIDEBAR_WIDTH*0.05))

		intervalLengthEntry = tk.Entry(intervalLength, font=F_CALIBRI, bg=C_SECONDARY, bd=0,  highlightcolor=C_ACCENT, highlightthickness=2,
			highlightbackground=C_MAIN, fg=C_MAIN, textvariable=self.hermiteParams.intervalLength)
		intervalLengthEntry.bind("<Return>", lambda event: self.drawBlob())
		intervalLengthEntry.pack(side="right", fill="x")

		self.hermiteParams.drawPoints.set(1)
		self.hermiteParams.drawSlopes.set(0)
		self.hermiteParams.drawCenteredReplica.set(0)
		self.hermiteParams.interpolateAbscissas.set(0)
		self.hermiteParams.symmetry.set(0)
		self.hermiteParams.xSymmetry.set(0)
		self.hermiteParams.ySymmetry.set(0)

		drawPoints = tk.Frame(self.sidebarFrame, bg=C_SECONDARY)
		drawPoints.pack(fill="x", padx=15, pady=(20, 5))

		tk.Label(drawPoints, text="Draw points", font=F_CALIBRI, fg=C_MAIN, bg=C_SECONDARY, width=PARAM_WIDTH).pack(
			side="left", padx=(0, SIDEBAR_WIDTH*0.05))

		tk.Checkbutton(drawPoints, text="", variable=self.hermiteParams.drawPoints, bg=C_SECONDARY, activebackground=C_SECONDARY,
			highlightcolor=C_ACCENT, command=self.drawBlob).pack(side="left")

		drawSlopes = tk.Frame(self.sidebarFrame, bg=C_SECONDARY)
		drawSlopes.pack(fill="x", padx=15, pady=(20, 5))

		tk.Label(drawSlopes, text="Draw slopes", font=F_CALIBRI, fg=C_MAIN, bg=C_SECONDARY, width=PARAM_WIDTH).pack(
			side="left", padx=(0, SIDEBAR_WIDTH*0.05))

		tk.Checkbutton(drawSlopes, text="", variable=self.hermiteParams.drawSlopes, bg=C_SECONDARY, activebackground=C_SECONDARY,
			highlightcolor=C_ACCENT, command=self.drawBlob).pack(side="left")

		drawCenteredReplica = tk.Frame(self.sidebarFrame, bg=C_SECONDARY)
		drawCenteredReplica.pack(fill="x", padx=15, pady=(20, 5))

		tk.Label(drawCenteredReplica, text="Draw centered replica", font=F_CALIBRI, fg=C_MAIN, bg=C_SECONDARY, width=PARAM_WIDTH).pack(
			side="left", padx=(0, SIDEBAR_WIDTH*0.05))

		tk.Checkbutton(drawCenteredReplica, text="", variable=self.hermiteParams.drawCenteredReplica, bg=C_SECONDARY, activebackground=C_SECONDARY,
			highlightcolor=C_ACCENT, command=self.drawBlob).pack(side="left")

		interpolateAbscissas = tk.Frame(self.sidebarFrame, bg=C_SECONDARY)
		interpolateAbscissas.pack(fill="x", padx=15, pady=(20, 5))

		tk.Label(interpolateAbscissas, text="Interpolate abscissas", font=F_CALIBRI, fg=C_MAIN, bg=C_SECONDARY, width=PARAM_WIDTH).pack(
			side="left", padx=(0, SIDEBAR_WIDTH*0.05))

		tk.Checkbutton(interpolateAbscissas, text="", variable=self.hermiteParams.interpolateAbscissas, bg=C_SECONDARY, activebackground=C_SECONDARY,
			highlightcolor=C_ACCENT, command=self.drawBlob).pack(side="left")

		symmetry = tk.Frame(self.sidebarFrame, bg=C_SECONDARY)
		symmetry.pack(fill="x", padx=15, pady=(20, 5))

		tk.Label(symmetry, text="Symmetry", font=F_CALIBRI, fg=C_MAIN, bg=C_SECONDARY, width=PARAM_WIDTH).pack(
			side="left", padx=(0, SIDEBAR_WIDTH*0.05))

		tk.Checkbutton(symmetry, text="", variable=self.hermiteParams.symmetry, bg=C_SECONDARY, activebackground=C_SECONDARY,
			highlightcolor=C_ACCENT, command=self.drawBlob).pack(side="left")

		xSymmetry = tk.Frame(self.sidebarFrame, bg=C_SECONDARY)
		xSymmetry.pack(fill="x", padx=15, pady=(20, 5))

		tk.Label(xSymmetry, text="Axis-x symmetry", font=F_CALIBRI, fg=C_MAIN, bg=C_SECONDARY, width=PARAM_WIDTH).pack(
			side="left", padx=(0, SIDEBAR_WIDTH*0.05))

		tk.Checkbutton(xSymmetry, text="", variable=self.hermiteParams.xSymmetry, bg=C_SECONDARY, activebackground=C_SECONDARY,
			highlightcolor=C_ACCENT, command=self.drawBlob).pack(side="left")

		ySymmetry = tk.Frame(self.sidebarFrame, bg=C_SECONDARY)
		ySymmetry.pack(fill="x", padx=15, pady=(20, 5))

		tk.Label(ySymmetry, text="Axis-y symmetry", font=F_CALIBRI, fg=C_MAIN, bg=C_SECONDARY, width=PARAM_WIDTH).pack(
			side="left", padx=(0, SIDEBAR_WIDTH*0.05))

		tk.Checkbutton(ySymmetry, text="", variable=self.hermiteParams.ySymmetry, bg=C_SECONDARY, activebackground=C_SECONDARY,
			highlightcolor=C_ACCENT, command=self.drawBlob).pack(side="left")

	def clearFrames(self):
		for widget in self.sidebarFrame.winfo_children():
			widget.destroy()
		if hasattr(self, 'pltWidget'):
			self.pltWidget.destroy()

	def choose(self):
		self.clearFrames()
		if self.nautilusVar.get() == 0:
			self.drawButtonBlob()
			self.drawBlob()
		elif self.nautilusVar.get() == 1:
			self.drawButtonNautilus()
			self.drawNautilus()

	def drawBlob(self):
		self.updateBlobPlt()

		if hasattr(self, 'pltWidget'):
			self.pltWidget.destroy()

		self.fig.set_facecolor("none")
		self.ax.set_facecolor("none")
		pltCanvas = FigureCanvasTkAgg(self.fig, master=self.renderFrame)
		self.pltWidget = pltCanvas.get_tk_widget()

		figW, figH = self.fig.get_size_inches()
		ratio = figW / figH
		self.pltWidget.configure(bg=C_MAIN, width=(1920-SIDEBAR_WIDTH)*0.8, height=(1920-SIDEBAR_WIDTH) * ratio*0.8)
		self.pltWidget.pack()

	def updateNautilusPlt(self):
		masse = self.nautilusParams.mass.get()
		volume = self.nautilusParams.volume.get()
		duree_phase = self.nautilusParams.phaseDuration.get()
		puissance_max_y = self.nautilusParams.maxYPower.get()
		puissance_max_x = self.nautilusParams.maxXPower.get()
		puissance_min_y = self.nautilusParams.minYPower.get()
		self.fig, self.ax = MoveNautilus(masse, volume, duree_phase, puissance_max_y, puissance_max_x, puissance_min_y)

	def drawNautilus(self):
		self.updateNautilusPlt()
		self.big_text_label.config(text="Nautilus")
		self.nautilusCheckbox.config(text="Blob")

		if hasattr(self, 'pltWidget'):
			self.pltWidget.destroy()

		# Convertir la figure en widget Tkinter
		pltCanvas = FigureCanvasTkAgg(self.fig, master=self.renderFrame)
		figW, figH = self.fig.get_size_inches()
		ratio = figW / figH
		self.pltWidget = pltCanvas.get_tk_widget()
		self.pltWidget.configure(bg=C_MAIN, width=(1920 - SIDEBAR_WIDTH) * 0.8, height=(1920 - SIDEBAR_WIDTH) * ratio * 0.8)
		self.pltWidget.pack()

	def updateBlobPlt(self):
		print("Update")
		self.big_text_label.config(text="Blob")
		p = self.hermiteParams.points
		points = [[p[i].x, p[i].y] for i in range(len(p))]
		slopes = [[p[i].slopeX, p[i].slopeY] for i in range(len(p))]
		centerPoint = [self.hermiteParams.centerX.get(), self.hermiteParams.centerY.get()]
		precision = self.hermiteParams.precision.get()
		intervalLength = self.hermiteParams.intervalLength.get()
		drawPoints = bool(self.hermiteParams.drawPoints.get())
		drawSlopes = bool(self.hermiteParams.drawSlopes.get())
		drawCenteredReplica = bool(self.hermiteParams.drawCenteredReplica.get())
		interpolateAbscissas = bool(self.hermiteParams.interpolateAbscissas.get())
		symmetry = bool(self.hermiteParams.symmetry.get())
		xSymmetry = bool(self.hermiteParams.xSymmetry.get())
		ySymmetry = bool(self.hermiteParams.ySymmetry.get())
		self.fig, self.ax = DrawPlot(points, slopes, precision, drawPoints, drawSlopes, drawCenteredReplica, centerPoint, intervalLength, interpolateAbscissas,symmetry,xSymmetry,ySymmetry)
		self.addPointWindow = None

	def deleteSelectedPoint(self):
		currentIndex = self.pointsCombobox.current()
		if(currentIndex < 0): return
		del self.hermiteParams.points[currentIndex]
		self.updatePointValues()

		pointsCount = len(self.hermiteParams.points)
		if(pointsCount > 0):
			self.pointsCombobox.current(currentIndex if (pointsCount > currentIndex) else currentIndex-1)
		else:
			self.pointsCombobox.set('')
		self.drawBlob()

	def validateNewPoint(self):
		x = float(self.xPointVar.get())
		y = float(self.yPointVar.get())
		xp = float(self.xPenteVar.get())
		yp = float(self.yPenteVar.get())
		p = Point(x, y, xp, yp)
		self.hermiteParams.points.append(p)
		self.updatePointValues()
		self.pointsCombobox.current(len(self.hermiteParams.points)-1)
		self.addPointWindow.destroy()
		self.drawBlob()

	def addNewPoint(self):
		if(self.addPointWindow is not None): self.addPointWindow.destroy()

		self.addPointWindow = tk.Toplevel(self, bg=C_MAIN)
		self.addPointWindow.title(ADD_POINT_WINDOW)

		x, y = self.getCenterPos(ADD_POINT_WIDTH, ADD_POINT_HEIGHT)
		self.addPointWindow.geometry('%dx%d+%d+%d' % (ADD_POINT_WIDTH, ADD_POINT_HEIGHT, x, y))

		self.xPointVar.set("0.0")
		self.yPointVar.set("0.0")
		self.xPenteVar.set("0.0")
		self.yPenteVar.set("0.0")

		xFrame = tk.Frame(self.addPointWindow, bg=C_MAIN)
		xFrame.pack(fill="x", padx=15, pady=(20, 5))

		tk.Label(xFrame, text="x", font=F_CALIBRI, fg=C_TEXT, bg=C_MAIN, width=10).pack(
			side="left", padx=(ADD_POINT_WIDTH*0.1, 5))

		tk.Entry(xFrame, font=F_CALIBRI, bg=C_MAIN, bd=0,  highlightcolor=C_ACCENT, highlightthickness=2,
			highlightbackground=C_SECONDARY, fg=C_TEXT, textvariable=self.xPointVar).pack(side="right", fill="x", pady=10, padx=(0,ADD_POINT_WIDTH * 0.3))

		yFrame = tk.Frame(self.addPointWindow, bg=C_MAIN)
		yFrame.pack(fill="x", padx=15, pady=5)

		tk.Label(yFrame, text="y", font=F_CALIBRI, fg=C_TEXT, bg=C_MAIN, width=10).pack(
			side="left", padx=(ADD_POINT_WIDTH*0.1, 5))

		tk.Entry(yFrame, font=F_CALIBRI, bg=C_MAIN, bd=0,  highlightcolor=C_ACCENT, highlightthickness=2,
			highlightbackground=C_SECONDARY, fg=C_TEXT, textvariable=self.yPointVar).pack(side="right", fill="x", pady=10, padx=(0,ADD_POINT_WIDTH * 0.3))

		xPenteFrame = tk.Frame(self.addPointWindow, bg=C_MAIN)
		xPenteFrame.pack(fill="x", padx=15, pady=5)

		tk.Label(xPenteFrame, text="x pente", font=F_CALIBRI, fg=C_TEXT, bg=C_MAIN, width=10).pack(
			side="left", padx=(ADD_POINT_WIDTH*0.1, 5))

		tk.Entry(xPenteFrame, font=F_CALIBRI, bg=C_MAIN, bd=0,  highlightcolor=C_ACCENT, highlightthickness=2,
			highlightbackground=C_SECONDARY, fg=C_TEXT, textvariable=self.xPenteVar).pack(side="right", fill="x", pady=10, padx=(0,ADD_POINT_WIDTH * 0.3))

		yPenteFrame = tk.Frame(self.addPointWindow, bg=C_MAIN)
		yPenteFrame.pack(fill="x", padx=15, pady=5)

		tk.Label(yPenteFrame, text="y pente", font=F_CALIBRI, fg=C_TEXT, bg=C_MAIN, width=10).pack(
			side="left", padx=(ADD_POINT_WIDTH*0.1, 5))

		tk.Entry(yPenteFrame, font=F_CALIBRI, bg=C_MAIN, bd=0,  highlightcolor=C_ACCENT, highlightthickness=2,
			highlightbackground=C_SECONDARY, fg=C_TEXT, textvariable=self.yPenteVar).pack(side="right", fill="x", pady=10, padx=(0,ADD_POINT_WIDTH * 0.3))

		tk.Button(self.addPointWindow, text="Add Point", bg=C_SECONDARY, fg=C_MAIN,
			font=F_CALIBRI, command=self.validateNewPoint).pack(fill="x", side="bottom", padx=ADD_POINT_WIDTH * 0.3, pady=30)

	def getCenterPos(self, width: int, height: int):
		ws = self.winfo_screenwidth() # width of the screen
		hs = self.winfo_screenheight() # height of the screen

		x = (ws/2) - (width/2)
		y = (hs/2) - (height/2)

		return (x, y)
