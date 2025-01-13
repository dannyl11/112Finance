class dateButton: #class for graph date buttons
    def __init__(self, weeks, months, x, y, width, height, selected=-1):
        self.weeksBack = weeks
        self.monthsBack = months
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill = None
        self.selected = selected

class statButton: #class for RSI and MACD buttons for analysis screen
    def __init__(self, x, y, metric):
        self.x = x
        self.y = y
        self.width = 200
        self.height = 70
        self.metric = metric
        self.selected = -1