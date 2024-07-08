import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.scraping.scraper import scrape

base_url = "https://tiendamia.com/ec/tendencias-laptops"

df = scrape(base_url)

df.head()

plt.figure(figsize=(10, 6))
sns.histplot(df['price'], bins=20)
plt.title('Distribución de Precios')
plt.xlabel('Precio')
plt.ylabel('Frecuencia')
plt.show()
