from datetime import datetime

class Extractor:

    # This method locates the start and end of generic data in a page given a starting keyword
    # A specifier for start and end brackets of the data could be added
    def __find_data(self, keyword, data):
        section_index = data.find(keyword)
        data_start = data.find("[", section_index) + 1
        data_end = data.find("]", data_start)

        return data[data_start:data_end]

    def extract(self, x_axis_keyword, y_axis_keyword, data):

        x = self.__find_data(x_axis_keyword, data)
        y = self.__find_data(y_axis_keyword, data)

        #Process string-bound data
        x = x.split('","')
        x[0]  = x[0].replace("\"","")
        x[len(x)-1] = x[len(x)-1].replace("\"","")

        #Process integer-bound data
        y = y.replace("null", "0")
        y = y.split(',')
        y = [eval(value) for value in y]

        x = [datetime.strptime(date, '%b %d, %Y').date() for date in x]

        return x, y