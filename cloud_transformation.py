import json

def transform_data(data):
    
    country_data = []
    gpd_data = []

    for key in range(1, len(data)):   
        table = data[key]
     
        for aux_table in table:
        
            country_id = aux_table['country']['id']
            country_name = aux_table['country']['value']
            iso3_code = aux_table['countryiso3code']
            
            
            country_values = {
                'id': country_id,
                'name': country_name,
                'iso3_code': iso3_code
            }
            
            country_data.append(country_values)
            
            year = aux_table['date']
            value = aux_table['value']
            
            gpd_values = {
                'country_id': country_id,
                'year': year,
                'value': value
            }
            
            gpd_data.append(gpd_values)
            
            
    with open('country_data.json', 'w') as f:
        json.dump(country_data, f, indent=4)
        
    with open('gpd_data.json', 'w') as f:
        json.dump(gpd_data, f, indent=4)
        


#transform_data(data)