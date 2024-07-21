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
    return df

# Hàm chuyển đổi đơn vị giá -> đồng
def change_price(price, area):
    if isinstance(price, (float, int)):
        return price

    price = str(price)

    per_m2 = False
    if "m²" in price:
        price = price.replace("/m²", "")
        per_m2 = True

    if "nghìn" in price:
        price_value = 1_000 * float(price.replace(" nghìn", "").replace('.','').replace(",", "."))
        return (price_value * area) if per_m2 else price_value
    if "triệu" in price:
        price_value = 1_000_000 * float(price.replace(" triệu", "").replace('.','').replace(",", "."))
        return (price_value * area) if per_m2 else price_value
    if "tỷ" in price:
        price_value = 1_000_000_000 * float(price.replace(" tỷ", "").replace('.','').replace(",", "."))
        return (price_value * area) if per_m2 else price_value

    return pd.NA

# Xử lý giá
def Price(df):
    df['MucGia'] = df.apply(lambda row: change_price(row['MucGia'], row['DienTich']), axis=1)
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
    df = Area(df)
    df = Price(df)
    df = Facade(df)
    df = Way(df)
    df = BedRoom(df)
    df = Toilet(df)
    df = Floor(df)
    return df
