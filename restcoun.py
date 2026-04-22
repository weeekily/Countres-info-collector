import requests
import json, csv
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter



URL = "https://restcountries.com/v3.1/all?"
fields = 'name,capital,languages,population,currencies'
retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 501, 502, 503,504]
)

adapter = HTTPAdapter(max_retries=retry_strategy)

session = requests.Session()
session.mount('https://', adapter)

try:
    response = session.get(f"{URL}fields={fields}", timeout=5)
except requests.exceptions.Timeout:
    print("SESSION TIMEOUT")
    exit()
    
    
all_countries = []
if response.status_code == 200:
    data = response.json()
    
    try:
        for country in data:
            
            name_data = country.get('name',{})
            if name_data:
                name = name_data.get('common','N/A')
                official = name_data.get('official','N/A')
            
            else:
                name = official = 'N/A'
                        
            currencies_data = country.get('currencies',{})
            if currencies_data:
                currency_code = list(currencies_data.keys())[0]
                currency_name = currencies_data[currency_code].get('name', 'N/A')
                currency_symbol = currencies_data[currency_code].get('symbol','N/A')
                
            else:
                currency_code = currency_name = currency_symbol = 'N/A'
                
                
            language_data = country.get('languages',{})
            if language_data:
                languages = ', '.join(language_data.values())
                
            else:
                languages = 'N/A'
                
            capital_data = country.get('capital', {})
            if capital_data:
                capital = capital_data[0]
                
            else:
                capital = 'N/A'
        
        
            population = country.get('population', 'N/A')
            
            
            
            section = {
                'name': name,
                'official': official,
                'currency_name': currency_name,
                'currency_symbol': currency_symbol,
                'languages': languages,
                'capital':capital,
                'population': population 
            }
            
            all_countries.append(section)

    except Exception as e:
        print(f"An error accured: {e}")        
        
 
        
        
    keys = ['name', 'official', 'currency_name', 'currency_symbol', 'languages', 'capital', 'population']
    
    jsonpath = 'restcountries.json'
    csvpath = 'restcountries.csv'
    try:
        with open(jsonpath, 'w', encoding='utf-8') as f:
            json.dump(all_countries, f, ensure_ascii=False, indent=4)
            print(f"Uspesno sacuvan JSON.")
            
            
        with open(csvpath, 'w', encoding='utf-8', newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(all_countries)
            print(f"Uspesno sacuvan CSV.")
    except Exception as e:
        print(f"Failed to save files: {e}")
        
        