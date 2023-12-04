from datetime import datetime

class Extractor:

    # This method locates the start and end of generic data in a page given a starting keyword
    # A specifier for start and end brackets of the data could be added
    def __FindData(self, keyword, data):
        sectionIndex = data.find(keyword)
        dataStart = data.find("[", sectionIndex) + 1
        dataEnd = data.find("]", dataStart)

        return data[dataStart:dataEnd]

    def Extract(self, xAxisKeyword, yAxisKeyword, data):

        xAxis = self.__FindData(xAxisKeyword, data)
        yAxis = self.__FindData(yAxisKeyword, data)

        #Process string-bound data
        xAxis = xAxis.split('","')
        xAxis[0]  = xAxis[0].replace("\"","")
        xAxis[len(xAxis)-1] = xAxis[len(xAxis)-1].replace("\"","")

        #Process integer-bound data
        yAxis = yAxis.replace("null", "0")
        yAxis = yAxis.split(',')
        yAxis = [eval(value) for value in yAxis]

        xAxis = [datetime.strptime(date, '%b %d, %Y').date() for date in xAxis]

        return xAxis, yAxis