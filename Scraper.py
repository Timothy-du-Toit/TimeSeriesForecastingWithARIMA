import requests
from bs4 import BeautifulSoup
import extractor

def scrape_data():
    data_source = "https://www.worldometers.info/coronavirus/country/south-africa/"
    response = requests.get(data_source)
    print("Request made to data source: ", data_source)
    print(f"Server Response: {response.status_code}")

    graph_name = "coronavirus-cases-linear"

    soup = BeautifulSoup(response.text, "html.parser")
    script_sections = soup.find_all("script")
    for script in script_sections:
        if(script.get("type") == "text/javascript"):
            if graph_name in script.text:
                graph = script.text
                
    graph_data = graph[43:len(graph)-3]
    
    data_extractor = extractor.Extractor()
    return data_extractor.extract("categories","data", graph_data)



