import matplotlib.pyplot as plt
import pandas as pd

d={"Name":["Karthick","Kishore","Pavithran","Vignhesh"],
   "Sal":[25000,30000,40000,45000]}
df = pd.DataFrame(d)
print(df)

plt.bar(df["Name"],df["Sal"],color="red")
plt.title("Name By Salary")
plt.xlabel("Name")
plt.ylabel("Salary")
plt.show()


plt.plot(df["Name"],df["Sal"],color="red")
plt.title("Name By Salary")
plt.xlabel("Name")
plt.ylabel("Salary")
plt.show()
