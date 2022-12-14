# -*- coding: utf-8 -*-
"""assgg.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dZ9I5x6z8tY2If4WOPkXc5g7l0_lOs2x

Is there a relation between a country's Gross Domestrict Product (GDP) and its income inequality?
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
# %load_ext google.colab.data_table

import matplotlib.pyplot as plt

df_gini = pd.read_csv("/content/economic-inequality-gini-index.csv")
df_gini. head()

df_gdp = pd.read_csv("/content/gdp-per-capita-maddison-2020.csv")
df_gdp.head()

df_gdp_1 = df_gdp.astype({"Year": "Int32"})
df_gdp_1 .head()

df_gidp=pd.merge(df_gini, df_gdp, how="outer", on=['Entity','Year'])

df_gidp_1 =df_gidp.drop([ 'Code_x', 'Code_y',
        '417485-annotations'], axis='columns')

df_gidp_2 = df_gidp_1.dropna()

from scipy.stats import pearsonr
pearsonr(df_gidp_2['GDP per capita'], df_gidp_2['Gini coefficient'])

fig, ax = plt.subplots(figsize=(8,6))

ax.scatter(y=df_gidp_2['GDP per capita'], x=df_gidp_2['Gini coefficient']);

ax.set_ylabel('GDP per capita')
ax.set_xlabel('Gini coefficient')
ax.set_title('GDP vs Gini');

"""Er was sprake van een niet-significante, lage negatieve correlatie tussen GDP en GINI (r = .04; p = 2,2...-82)
De Pearson-correlatie wees uit dat er een niet-significant verband bestaat tussen GDP en GINI r = -0,4; p = 2.2...-82.
Uit de scatterplot lijkt het alsof er toch een redelijk verband is tussen GDP en Gini
"""