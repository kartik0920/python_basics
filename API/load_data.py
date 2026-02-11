import pandas as pd
from get_data import get_data
import matplotlib.pyplot as plt
daily_data=get_data()

df=pd.DataFrame(
{    "date":daily_data['time'],
    "max_temp":daily_data["temperature_2m_max"],
    "min_temp":daily_data["temperature_2m_min"]
}
)

df["date"]=pd.to_datetime(df['date'])


# visualize Data

x,y1,y2=df["date"],df["min_temp"],df["max_temp"] 
def show_plot(x=x,y1=y1,y2=y2):
    plt.plot(x,y2,marker='.')
    plt.plot(x,y1,marker='.')
    plt.xlabel("Day")
    plt.ylabel("Minimum temparature")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


show_plot()