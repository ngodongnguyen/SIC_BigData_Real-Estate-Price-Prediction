import json
import re
import pandas as pd

def read_file(file_path):
    global mang
    mang=[]
    with open(file_path, 'r', encoding='utf-8') as file:
        parsed_data = json.load(file)
    for item in parsed_data:
        if isinstance(item, dict):
            mang.append(item.get("DiaChi"))
    
    # Tách thành phố
def extract_thanh_pho(address):
    parts = address.split(", ")
    if len(parts) > 1:
        thanh_pho = parts[-1]
        if thanh_pho.endswith("."):
            thanh_pho = thanh_pho[:-1]
        if thanh_pho == "Bà Rịa Vũng Tàu":
            thanh_pho = "Bà Rịa - Vũng Tàu"
        return thanh_pho
    return None
    
    # Tách quận
def extract_quan(address):
    parts = address.split(", ")
    if len(parts) > 1:
        return parts[-2]
    return None
def split_address(file_path):
    read_file(file_path)
    # Define patterns for different address components
    patterns = {
        "Ward": r"(Phường|Xã)\s[\w\s]+",  # Combined pattern for Phường and Xã
        "District": r"(Huyện)\s[\w\s]+",  # Combined pattern for Quận and Huyện
    }
    rows = []
    # Process each address and populate the rows list
    for address in mang:
        row = {}  # Initialize row with the address
        row["Region"] = extract_thanh_pho(address)
        row["Area"] = extract_quan(address)
        
        # Check for Ward and District
        ward_match = re.search(patterns["Ward"], address)
        district_match = re.search(patterns["District"], address)
        
        if ward_match:
            row["Ward"] = ward_match.group().strip()  # Add matched Ward value to row
        else:
            row["Ward"] = None  # No match found, set value to None
        
        if row["Area"]:
            rows.append(row)
            # If Area is not None or empty, try to find the District
            continue
        else:
            # If Area is None or empty, find the District
            if district_match:
                row["Area"] = district_match.group().strip()  # Add matched District value to row
            else:
                row["Area"] = None  # No match found, set value to None

        # Add the row to the list of rows
        rows.append(row)

    # Create a DataFrame from the list of rows
    df = pd.DataFrame(rows, columns=["Region", "Area", "Ward"])
    return df

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
def find_city_id(city_name,data):
    if not city_name:  # Kiểm tra nếu city_name là None hoặc chuỗi rỗng
        return None
    for item in data.get('data', []):
        name = item.get('name', '')
        if name and city_name in name:  # Kiểm tra nếu name không phải là None và city_name có trong name
            return item.get('level1_id')  # Trả về ID của thành phố 
    return None  # Trả về None nếu không tìm thấy

def find_district_id(city_id,district_name,data):
    if not district_name or not city_id:  # Kiểm tra nếu district_name là None hoặc chuỗi rỗng
        return None
    for item in data.get('data', []):
        # Duyệt qua các quận trong mỗi thành phố
        city_name = item.get('level1_id', '')
        if city_id in city_name:  # Kiểm tra nếu city_id có trong city_name
            for district in item.get('level2s', []):
                name = district.get('name', '')
                if name and district_name in name:  # Kiểm tra nếu name không phải là None và district_name có trong name
                    return district.get('level2_id')  # Trả về ID của quận    
    return None  # Trả về None nếu không tìm thấy

def find_ward_id(city_id, district_id, ward_name,data):
    """Tìm ID của phường dựa trên tên phường, ID thành phố và ID quận."""
    if not city_id or not district_id or not ward_name:  # Kiểm tra nếu bất kỳ tham số nào là None hoặc chuỗi rỗng
        return None  

    for item in data.get('data', []):
        city_name = item.get('level1_id', '')
        if city_id in city_name:  # Kiểm tra nếu city_id có trong city_name
            for district in item.get('level2s', []):
                district_name = district.get('level2_id', '')
                if district_id in district_name:  # Kiểm tra nếu district_id có trong district_name
                    for ward in district.get('level3s', []):
                        ward_name_in_data = ward.get('name', '')
                        if(city_id=='79'):
                            tmp=normalize_ward_name(ward_name)
                            ward_name=tmp
                        if('Hòa'in ward_name):
                            ward_name=ward_name.replace('Hòa','Hoà')
                            if ward_name == ward_name_in_data:  # Kiểm tra nếu ward_name có trong ward_name_in_data
                                return ward.get('level3_id') 
                        if ward_name == ward_name_in_data:  # Kiểm tra nếu ward_name có trong ward_name_in_data
                            return ward.get('level3_id') 
                         
    return None  # Trả về None nếu không tìm thấy 
def normalize_address(file_path):
    data=read_json_file()
    rows = []
    df=split_address(file_path)
    count=0
    for index, row in df.iterrows():
        city_id = find_city_id(row['Region'],data)
        district_id = find_district_id(city_id,row['Area'],data)
        ward_id = find_ward_id(city_id, district_id, row['Ward'],data)
        rows.append({
            "Region ID": city_id,
            "Area ID": district_id,
            "Ward ID": ward_id
        })
    
    result_df = pd.DataFrame(rows, columns=["Region ID", "Area ID", "Ward ID"])
    return result_df
