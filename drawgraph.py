    def drawMap(self, dbData)
        x = dbData[0]
        y = dbData[1]
        self.plot.autoFillBackground()
        self.plot.setTitle("A Simple Map Demonstration")
        self.plot.setCanvasBackground(Qt.white)
        self.plot.setAxisTitle(QwtPlot.xBottom, "серії")
        self.plot.setAxisTitle(QwtPlot.yLeft, "y")
        self.plot.setAxisScale(QwtPlot.xBottom, 0.0, 1.0)
        self.plot.setAxisScale(QwtPlot.yLeft, 0.54, 0.56)
        self.curve = QwtPlotCurve()
        self.curve.setData(x, y)
        self.curve.attach(self.plot)
        self.plot.replot()
        # self.plot.show()
        return None

    def clearDraw(self):
        self.curve.detach()
        self.plot.replot()
        return None

    # *************Перевизначення подій ***********************
    def resizeEvent(self, event):
        # self.ui.textBrowser.repaint()
        rect = self.ui.plotwidget.frameSize()
        self.plot.resize(rect)
