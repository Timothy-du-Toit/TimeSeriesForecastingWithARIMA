import Scraper
import matplotlib.pyplot as plt 

scraper = Scraper.Scraper()
date, newCases = scraper.ScrapeData()

print("data received") 
plt.plot(date, newCases) 
plt.xlabel('Date') 
plt.ylabel('Number of cases') 
plt.title('Total Covid Cases') 
plt.show() 