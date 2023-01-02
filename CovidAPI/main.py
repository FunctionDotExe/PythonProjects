import requests
import json
import matplotlib.pyplot as plt

package1 = requests.get('https://api.covid19api.com/summary')
k = package1.json()
print(k)


print("Global Summary:\n", k['Global'])

countryi = ["Afghanistan", "Albania","Algeria","Andorra","Angola","Argentina"]
countries_data = {}

for country_info in k['Countries']:
    current = country_info['Country']
    if current in countryi :
        countries_data[current] = country_info

t = []
for country in countryi:
    current = countries_data[country]['TotalDeaths']
    t.append(current)


x = [i for i, _ in enumerate(countryi)]
 
plt.bar(countryi,t, color = 'blue')
plt.xlabel("Countries")
plt.ylabel("Total Deaths")
plt.title("Total Deaths per Country")

# plt.xticks(x, countryi) 

plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)

plt.show()