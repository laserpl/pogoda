#from services.openweather_api import get_weather
#from services.excel_files import save_to_excel,read_excel
from services.dashbard import render_dashboard
#from config import Config
#import time


render_dashboard("lisbon.xlsx")

# file = read_excel(Config.excel_path)
# print(file.describe())

# while True:
#     weather = get_weather()
#     save_to_excel([weather])
#     print("Pobrano i zapisano dane")
#     time.sleep(5)
