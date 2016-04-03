# -*- coding: utf-8 -*-
__author__ = 'Valeriy'

from qwt.qt.QtGui import QApplication
from qwt import QwtPlot, QwtPlotCurve
import numpy as np

app = QApplication([])

# x = [1,2,3,4,5,6,7,8,9]
# y1 = [3.2, 5.1 ,7.0, 4.24, 4.41, 8.34, 2.21, 5.657, 6.1]


x = []
y1 = []


my_plot = QwtPlot("Two curves")
curve1 = QwtPlotCurve("Curve 1")
my_plot.resize(600, 300)

curve1.setData(x, y1)
curve1.attach(my_plot)
# my_plot.replot()
my_plot.show()

app.exec_()

# SELECT PrepData FROM= Pdata WHERE ((PNameId=2) AND (SNameId = 14) AND (YearId=2012))
