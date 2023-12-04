import scraper
import matplotlib.pyplot as plt 

date, new_cases = scraper.scrape_data()

print("data received") 
plt.plot(date, new_cases) 
plt.xlabel('Date') 
plt.ylabel('Number of cases') 
plt.title('Total Covid Cases') 
plt.show() 