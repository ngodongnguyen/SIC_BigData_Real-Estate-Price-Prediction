import json
import pandas as pd

# Đọc File
def Read_file(Path):
    with open(Path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    df1 = pd.json_normalize(data)
    df1.drop_duplicates(inplace=True)
    return df1

# Xử lý diện tích
def Area(df):
    df['DienTich'] = df['DienTich'].str.replace(' m²', '').str.replace('.', '').str.replace(',', '.').str.strip()
    df['DienTich'] = pd.to_numeric(df['DienTich'], errors='coerce')  # Chuyển đổi sang float và tạo NaN cho giá trị không hợp lệ
    median_area = df['DienTich'].median()  # Tính giá trị trung vị
    df['DienTich'].fillna(median_area, inplace=True)  # Thay thế NaN bằng giá trị trung vị
    return df

# Hàm chuyển đổi đơn vị giá -> đồng
def change_price(price, area):
    if isinstance(price, (float, int)):
        return price

    price = str(price)

    if 'triệu/m²' in price:
        price_value = float(price.replace(' triệu/m²', '').replace(',', '.').strip()) * 1000000
        return price_value * area
    elif 'nghìn/m²' in price:
        price_value = float(price.replace(' nghìn/m²', '').replace(',', '.').strip()) * 1000
        return price_value * area
    elif 'tỷ/m²' in price:
        price_value = float(price.replace(' tỷ/m²', '').replace(',', '.').strip()) * 1000000000
        return price_value * area
    elif 'triệu' in price:
        price_value = float(price.replace(' triệu', '').replace(',', '.').strip()) * 1000000
        return price_value
    elif 'tỷ' in price:
        price_value = float(price.replace(' tỷ', '').replace(',', '.').strip()) * 1000000000
        return price_value
    elif 'nghìn' in price:
        price_value = float(price.replace(' nghìn', '').replace(',', '.').strip()) * 1000
        return price_value

    return price

# Gán giá trị trung vị cho 'Thỏa thuận'
def Median_ThoaThuan(df):
    median_price = df[df['MucGia'] != 'Thỏa thuận']['MucGia'].astype(float).median()
    df['MucGia'] = df['MucGia'].replace('Thỏa thuận', median_price)
    return df

# Xử lý giá
def Price(df):
    df['MucGia'] = df.apply(lambda row: change_price(row['MucGia'], row['DienTich']), axis=1)
    df = Median_ThoaThuan(df)
    return df

# Xử lý diện tích mặt tiền
def Facade(df):
    df["MatTien"] = df["MatTien"].str.replace(' m', '').str.replace(',', '.').str.strip()
    return df

# Xử lý diện tích đường vào
def Way(df):
    df["DuongVao"] = df["DuongVao"].str.replace(' m', '').str.replace(',', '.').str.strip()
    return df

# Xử lý diện tích số phòng ngủ
def BedRoom(df):
    df["SoPhongNgu"] = df["SoPhongNgu"].str.replace(' phòng', '').str.strip()
    return df

# Xử lý số phòng Toilet
def Toilet(df):
    df["SoToilet"] = df["SoToilet"].str.replace(' phòng', '').str.strip()
    return df

# Xử lý số tầng
def Floor(df):
    df["SoTang"] = df["SoTang"].str.replace(' tầng', '').str.strip()
    return df

# Main Preprocess_Digit
def PreprocessDg(Path):
    df = Read_file(Path)
    df.dropna(how='all', inplace=True)  # Xóa các hàng có tất cả các cột bằng NaN
    df = Area(df)
    df = Price(df)
    df = Facade(df)
    df = Way(df)
    df = BedRoom(df)
    df = Toilet(df)
    df = Floor(df)
    return df