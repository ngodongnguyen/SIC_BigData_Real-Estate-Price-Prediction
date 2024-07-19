import json
import re
import pandas as pd

def normalize_address(file_path, dvhc_path):
    mang = []
    
    # Đọc file
    def read_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            parsed_data = json.load(file)
        for item in parsed_data:
            if isinstance(item, dict):
                mang.append(item.get("DiaChi"))
     # Tách thành phố
    def extract_thanh_pho(address):
       
        parts = address.split(", ")
        if len(parts) > 1:
            return parts[-1]
        return None
    # Tách quận
    def extract_quan(address):
        parts = address.split(", ")
        if len(parts) > 1:
            return parts[-2]
        return None
    
    read_file(file_path)

    #Đưa các dữ liệu tách được vào dataframe
    patterns = {
        "Phường": r"Phường\s[\w\s]+",#Tách dữ liệu khi gặp Phường + space
        "Xã": r"Xã\s[\w\s]+", #Tách dữ liệu khi gặp Xã + space
        "Huyện": r"Huyện\s[\w\s]+", #Tách dữ liệu khi gặp Huyện + space
    }
    rows = []

    # Process each address and populate the rows list
    for address in mang:
        row = {}  # Initialize row with the address
        row["Thành phố"] = extract_thanh_pho(address)
        row["Quận"] = extract_quan(address)
        for key, pattern in patterns.items():
            match = re.search(pattern, address)
            if match:
                row[key] = match.group().strip()  # Add matched value to row
            else:
                row[key] = None  # No match found, set value to None

        # Add the row to the list of rows
        rows.append(row)

    # Create a DataFrame from the list of rows
    df = pd.DataFrame(rows, columns=["Thành phố", "Quận", "Phường", "Xã", "Huyện"])
    #Mở file cần chuẩn hóa dữ liệu
    with open(dvhc_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Khởi tạo từ điển ánh xạ
    city_mapping = {}
    district_mapping = {}
    ward_mapping = {}

    # Tạo ánh xạ cho Thành phố
    for item in data.get('data', []):
        city_id = item.get('level1_id')
        city_name = item.get('name')
        # city_mapping[city_name] = city_id
        # Tạo ánh xạ cho Quận
        for district in item.get('level2s', []):
            district_id = district.get('level2_id')
            district_name = district.get('name')
            # district_mapping[district_name] = district_id

            # Tạo ánh xạ cho Phường
            for ward in district.get('level3s', []):
                ward_id = ward.get('level3_id')
                ward_name = ward.get('name')
                # ward_mapping[ward_name] = ward_id

    # Tìm kiếm ID của thành phố
    def find_city_id(city_name):
        if not city_name:  # Kiểm tra nếu city_name là None hoặc chuỗi rỗng
            return None
        for item in data.get('data', []):
            name = item.get('name', '')
            if name and city_name in name:  # Kiểm tra nếu name không phải là None và city_name có trong name
                return item.get('level1_id')  # Trả về ID của thành phố 
        return None  # Trả về None nếu không tìm thấy

    def find_district_id(district_name):
        if not district_name:  # Kiểm tra nếu district_name là None hoặc chuỗi rỗng
            return None
        for item in data.get('data', []):
            # Duyệt qua các quận trong mỗi thành phố
            for district in item.get('level2s', []):
                name = district.get('name', '')
                if name and district_name in name:  # Kiểm tra nếu name không phải là None và district_name có trong name
                    return district.get('level2_id')  # Trả về ID của quận    
        return None  # Trả về None nếu không tìm thấy

    def find_ward_id(city_id, district_id, ward_name):
        """Tìm ID của phường dựa trên tên phường, ID thành phố và ID quận."""
        if not city_id or not district_id or not ward_name:  # Kiểm tra nếu bất kỳ tham số nào là None hoặc chuỗi rỗng
            return None  
        for item in data.get('data', []):
            city_name = item.get('name', '')
            if city_id in city_name:  # Kiểm tra nếu city_id có trong city_name
                for district in item.get('level2s', []):
                    district_name = district.get('name', '')
                    if district_id in district_name:  # Kiểm tra nếu district_id có trong district_name
                        for ward in district.get('level3s', []):
                            ward_name_in_data = ward.get('name', '')
                            if ward_name in ward_name_in_data:  # Kiểm tra nếu ward_name có trong ward_name_in_data
                                return ward.get('level3_id')  
        return None  # Trả về None nếu không tìm thấy

    def find_commune_id(city_id, district_id, commune_name):
        """Tìm ID của xã dựa trên tên xã, ID thành phố và ID quận."""
        if not city_id or not district_id or not commune_name:  # Kiểm tra nếu bất kỳ tham số nào là None hoặc chuỗi rỗng
            return None   
        for item in data.get('data', []):
            city_name = item.get('name', '')
            if city_id in city_name:  # Kiểm tra nếu city_id có trong city_name
                for district in item.get('level2s', []):
                    district_name = district.get('name', '')
                    if district_id in district_name:  # Kiểm tra nếu district_id có trong district_name
                        for commune in district.get('level3s', []):
                            commune_name_in_data = commune.get('name', '')
                            if commune_name in commune_name_in_data:  # Kiểm tra nếu commune_name có trong commune_name_in_data
                                return commune.get('level3_id')   
        return None  # Trả về None nếu không tìm thấy

    def find_county_id(county_name):
        """Tìm ID của huyện dựa trên tên huyện."""
        if not county_name:  # Kiểm tra nếu tham số huyện là None hoặc chuỗi rỗng
            return None
        for item in data.get('data', []):
            # Duyệt qua các huyện trong mỗi thành phố
            for district in item.get('level2s', []):
                for county in district.get('level3s', []):
                    county_name_in_data = county.get('name', '')
                    if county_name in county_name_in_data:  # Kiểm tra nếu county_name có trong county_name_in_data
                        return county.get('level3_id')
        return None  # Trả về None nếu không tìm thấy

    # Khởi tạo danh sách hàng
    def address_normalization():
        rows = []
        for index, row in df.iterrows():
            city_id = find_city_id(row['Thành phố'])
            district_id = find_district_id(row['Quận'])
            ward_id = find_ward_id(row['Thành phố'], row['Quận'], row['Phường'])
            commune_id = find_commune_id(row['Thành phố'], row['Quận'], row['Xã'])
            county_id = find_county_id(row['Huyện'])

            rows.append({
                "Thành phố ID": city_id,
                "Quận ID": district_id,
                "Phường ID": ward_id,
                "Xã ID": commune_id,
                "Huyện ID": county_id
            })
        result_df = pd.DataFrame(rows, columns=["Thành phố ID", "Quận ID", "Phường ID", "Xã ID", "Huyện ID"])
        return result_df

    return address_normalization()

