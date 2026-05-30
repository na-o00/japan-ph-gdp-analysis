import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("real_gdp.csv")
print(df.head())

plt.figure(figsize = (10,8))

#GDP
plt.subplot(3,1,1)
plt.plot(df["Years"], df["Japan"], label = "Japan")
plt.plot(df["Years"], df["Philippines"], label = "Philippines")
plt.xlabel("Years")
plt.ylabel("GDP ($)")
plt.title("GDP Comparison: Japan vs Philippines")
plt.legend()
plt.grid()

#Difference
plt.subplot(3,1,2)
df["Difference"] = df["Japan"] - df["Philippines"]
plt.plot(df["Years"], df["Difference"], label = "GDP difference")
plt.xlabel("Years")
plt.ylabel("GDP Gap ($)")
plt.title("GDP Gap: Japan - Philippines")
plt.grid()

#GDP growth
plt.subplot(3,1,3)
df["Japan Growth"] = df["Japan"].pct_change()
plt.plot(df["Years"], df["Japan Growth"], label = "Japan Growth")
df["Philippines Growth"] = df["Philippines"].pct_change()
plt.plot(df["Years"], df["Philippines Growth"], label = "Philippines Growth")
plt.xlabel("Years")
plt.ylabel("GDP Growth ($)")
plt.title("GDP Growth")
plt.legend()
plt.grid()

plt.tight_layout()
plt.savefig("gdp_analysis.png")
plt.show()

#GDP Comparison Analysis: Japan vs Philippines (World Bank Data)
#Using real-world data from the World Bank, Japan has a significantly higher GDP than the Philippines throughout the observed period.
#The GDP Growth graph shows that both countries experienced fluctuations over time
#However, the Philippines tends to have more consistent growth, while Japan shows more volatility, especially during economic downturns.
#The GDP gap widened rapidly from the 1960s to the 1990s, reflecting Japan’s rapid economic expansion. However, in recent years, the gap has stabilized and shows slight signs of narrowing, suggesting gradual convergence.
#Overall, while Japan remains a much larger and more mature economy, the Philippines demonstrates steady growth potential as an emerging economy.
