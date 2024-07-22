import json
import re
import pandas as pd
import math

def read_file(file_path):
    global mang
    mang=[]
    with open(file_path, 'r', encoding='utf-8') as file:
        parsed_data = json.load(file)
        df1 = pd.json_normalize(parsed_data)
    return df1   
    # Tách thành phố
# def extract_thanh_pho(address):
#     parts = address.split(", ")
#     if len(parts) > 1:
#         thanh_pho = parts[-1]
#         if thanh_pho.endswith("."):
#             thanh_pho = thanh_pho[:-1]
#         if thanh_pho == "Bà Rịa Vũng Tàu":
#             thanh_pho = "Bà Rịa - Vũng Tàu"
#         return thanh_pho
#     return None
    
    # Tách quận
# def extract_quan(address):
#     parts = address.split(", ")
#     if len(parts) > 1:
#         return parts[-2]
#     return None
def split_address():
    # Read the file to get addresses (assuming `read_file` function and `mang` variable are defined elsewhere)
    
    # Define a more robust pattern for Ward
    patterns = {
        "Ward": r"(Phường|Xã)\s[\w\s\u00C0-\u017F]+(?:,|$)",  # Capture until comma or end of string
    }
    
    wards = []
    
    # Process each address and extract the Ward
    for index,row in df.iterrows():
        # Assume the address column is named 'DiaChi'
        address = row['DiaChi']
        
        # Check if address is a string, otherwise set it to an empty string
        if not isinstance(address, str):
            address = ''  # Or handle NaN/float cases as needed        
        # Check for Ward
        ward_match = re.search(patterns["Ward"], address)
        if ward_match:
            matched_ward = ward_match.group().strip().rstrip(',')
            wards.append(matched_ward)
        else:
            wards.append(None)  # No match found, append None    
    return wards

def read_json_file():
    dvhcvn_file="../../data/donvihanhchinhvn/dvhcvn.json"
    with open(dvhcvn_file, 'r', encoding='utf-8') as file:
        data_dict = json.load(file)
    return data_dict
    # Tìm kiếm ID của thành phố
def normalize_ward_name(ward_name):
    # Chuyển đổi phường 1-9 thành phường 01-09, giữ nguyên phường 10 trở lên
    match = re.search(r'(Phường|Xã)\s(\d+)', ward_name)
    if match:
        number = int(match.group(2))
        if number < 10:
            normalized_number = f'0{number}'
            return f'{match.group(1)} {normalized_number}'
    return ward_name
def find_city_id(city_name, data):
    if city_name is None or (isinstance(city_name, float) and math.isnan(city_name)):  # Kiểm tra nếu city_name là None hoặc NaN
        return float('nan')
    for item in data.get('data', []):
        name = item.get('name', '')
        if name and city_name in name:  # Kiểm tra nếu name không phải là None và city_name có trong name
            return item.get('level1_id')  # Trả về ID của thành phố 
    return float('nan')  # Trả về None nếu không tìm thấy
def find_district_id(city_id,district_name,data):
    if city_id is None or (isinstance(city_id, float) and math.isnan(city_id)) or \
       district_name is None or (isinstance(district_name, float) and math.isnan(district_name)):
        return float('nan')
    for item in data.get('data', []):
        # Duyệt qua các quận trong mỗi thành phố
        city_name = item.get('level1_id', '')
        if city_id in city_name:  # Kiểm tra nếu city_id có trong city_name
            for district in item.get('level2s', []):
                name = district.get('name', '')
                if name and district_name in name:  # Kiểm tra nếu name không phải là None và district_name có trong name
                    return district.get('level2_id')  # Trả về ID của quận    
    return float('nan')  # Trả về None nếu không tìm thấy
def find_ward_id(city_id, district_id, ward_name,data):
    """Tìm ID của phường dựa trên tên phường, ID thành phố và ID quận."""
    if city_id is None or (isinstance(city_id, float) and math.isnan(city_id)) or \
       district_id is None or (isinstance(district_id, float) and math.isnan(district_id)) or \
       ward_name is None or (isinstance(ward_name, float) and math.isnan(ward_name)):
        return float('nan')  
    for item in data.get('data', []):
        city_name = item.get('level1_id', '')
        if city_id in city_name:  # Kiểm tra nếu city_id có trong city_name
            for district in item.get('level2s', []):
                district_name = district.get('level2_id', '')
                if district_id in district_name:  # Kiểm tra nếu district_id có trong district_name
                    tmp1=ward_name
                    for ward in district.get('level3s', []):
                        ward_name_in_data = ward.get('name', '')
                        if(city_id=='79'):
                            tmp=normalize_ward_name(ward_name)
                            ward_name=tmp
                        if ward_name == ward_name_in_data or tmp1==ward_name_in_data:  # Kiểm tra nếu ward_name có trong ward_name_in_data
                            return ward.get('level3_id')    
                        if('Hòa'in ward_name):
                            ward_name=ward_name.replace('Hòa','Hoà')
                            if ward_name == ward_name_in_data:  # Kiểm tra nếu ward_name có trong ward_name_in_data
                                return ward.get('level3_id')                      
    return float('nan')  # Trả về None nếu không tìm thấy 
def normalize_address(file_path):
    data=read_json_file()
    rows = []
    array_city_ID=[]
    array_District_ID=[]
    array_Ward_ID=[]
    global df
    df=read_file(file_path)
    df["Ward"]=split_address()
    count=0
    for index, row in df.iterrows():
        city_id = find_city_id(row['City'],data)
        district_id = find_district_id(city_id,row['District'],data)
        ward_id = find_ward_id(city_id, district_id, row['Ward'],data)
        array_city_ID.append(city_id)
        array_District_ID.append(district_id)
        array_Ward_ID.append(ward_id)
    df["City ID"] = array_city_ID
    df["District ID"] = array_District_ID
    df["Ward ID"] = array_Ward_ID
    return df
