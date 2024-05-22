import requests
import json
from datetime import datetime

def api_conn(base_url, start_page=1):
    
    all_data = []
    current_page = start_page
    hold = 1
    
    try:
        while hold == 1:
            
            url = f"{base_url}{current_page}&per_page=50"
            response = requests.get(url)
            data = response.json()
            
            if len(data[1]) == 0:
                hold = 0
            
            if current_page == start_page:
                data_0 = data[0] 
                all_data.append(data_0)
                
            current_date = datetime.now()

            log_json = {
                'date_conn': str(current_date),
                'status_code': response.status_code,
                'url': url,
                'encoding': response.encoding,
                'method': response.request.method,
                'error': response.reason if not response.ok else None
            }
            
            log_save = f"api-log-{current_date.date()}.json"
            
            with open(log_save, 'a') as f:
                json.dump(log_json, f, indent=4)
                f.write('\n')
                
            if response.status_code == 200:
                print(f"elablished connection, code: {response.status_code}")
                
                if len(data) > 1 and data[1]:
                    all_data.append(data[1])
                    print("extraction well successed")
            else:
                print(f"connection error, code: {response.status_code}, motivo: {response.reason}")
            
            current_page += 1
            
            print(f"page: {current_page}")
            
    except:
            print("Process finished with a exception")
    
    print("Process finished")
    return all_data 

#base_url = "https://api.worldbank.org/v2/country/ARG;BOL;BRA;CHL;COL;ECU;GUY;PRY;PER;SUR;URY;VEN/indicator/NY.GDP.MKTP.CD?format=json&page="
#data = api_conn(base_url)
#print(f"Total records fetched: {len(data)}") 