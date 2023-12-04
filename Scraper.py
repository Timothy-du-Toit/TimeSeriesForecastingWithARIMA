import requests
import os
from bs4 import BeautifulSoup
import Extractor

class Scraper:
    
    def ScrapeData(self):
        data_source = "https://www.worldometers.info/coronavirus/country/south-africa/"
        response = requests.get(data_source)
        print(response.status_code)

        output_file = os.path.join("output.html")

        graph_name = "coronavirus-cases-linear"

        soup = BeautifulSoup(response.text, "html.parser")
        r = soup.find_all("script")
        for script in r:
            if(script.get("type") == "text/javascript"):
                if graph_name in script.text:
                    graph = script.text
                    
        graphData = graph[43:len(graph)-3] # Issue here is that the data is not JSON format and has been nested. We need 

        extractor = Extractor.Extractor()
        return extractor.Extract("categories","data", graphData)



