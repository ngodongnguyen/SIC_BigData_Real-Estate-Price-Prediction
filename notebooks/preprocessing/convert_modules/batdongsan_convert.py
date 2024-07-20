import numpy as np
import pandas as pd
from unidecode import unidecode


def legal_document_convert(s) -> int:
    """
    # Convert property legal document to integer
    Không sổ : 0
    Đã có sổ: 1
    Đang chờ sổ: 2
    Sổ chung | công chứng vi bằng: 3
    viết tay: 4
    """
    if pd.isna(s):
        return np.nan

    s = unidecode(s.lower().replace(" ", ""))

    # Đang chờ sổ: 2
    trait = [
        "dangcho",
        "dangdoi",
        "chocap",
        "choso",
        "chuanbi",
        "dangra",
        "danglam",
        "dangnop",
        "cholam",
        "doilam",
    ]
    if any(i in s for i in trait):
        return 2

    # Sổ chung | công chứng vi bằng : 3
    trait = [
        "sochung",
        "vibang",
        "vb",
        "dongsohuu",
        "shc",
        "sdc",
        "sodochung",
        "sohongchung",
    ]
    exc = ["shcc", "sdcc", "chinhchu"]
    if any(i in s for i in trait) and not any(i in s for i in exc):
        return 3

    # Đã có sổ: 1
    trait = [
        "coso",
        "sodo",
        "sd",
        "biado",
        "quyensudungdat",
        "giayphepxaydung",
        "gpxd",
        "sohong",
        "sh",
        "biahong",
        "sosan",
        "sanso",
        "cosan",
        "sodep",
        "socongchung",
        "vuongdep",
        "vuongvan",
        "sovuong",
        "sodat",
        "catket",
        "sorieng",
        "sohongrieng",
        "sonet",
        "chinhchu",
        "hoancong",
        "laudai",
        "thocu",
        "daydu",
        "sangten",
        "vinhvien",
        "hople",
        "hopphap",
        "phaplychuan",
        "phaplysach",
        "minhbach",
        "rorang",
        "sodenganhang",
    ]
    exc = ["chuaco", "chuaso", "khongso", "seraso", "secapso"]
    if any(i in s for i in trait) and not any(i in s for i in exc):
        return 1
    if len(s) <= 3 and s == "so":
        return 1

    # viết tay: 4
    trait = ["viettay", "giaytay", "hopdong", "hdmb", "thoathuan", "hdm"]
    exc = []
    if any(i in s for i in trait) and not any(i in s for i in exc):
        return 4

    return 0


def furnishings_convert(s) -> int:
    """
    # Convert furnishing status to integer
    Không: 0
    Cao cấp: 1
    Đầy đủ | hoàn thiện: 2
    Cơ bản: 3
    """
    if pd.isna(s):
        return np.nan

    s = unidecode(s.lower().replace(" ", ""))

    trait = [
        "caocap",
        "sangtrong",
        "xin",
        "5*",
        "dangcap",
        "chuyennghiep",
        "quy",
        "vip",
        "namsao",
        "chauau",
        "nhap",
        "sangtrong",
        "datvang",
        "tienty",
        "dattien",
        "lim",
    ]
    # Cao cấp: 1
    if any(i in s for i in trait):
        return 1

    # Đầy đủ | hoàn thiện: 2
    trait = [
        "daydu",
        "hoanthien",
        "du",
        "full",
        "toanbo",
        "hiendai",
        "dep",
        "san",
        "delai",
        "tang",
        "chatluongcao",
    ]
    if any(i in s for i in trait):
        return 2

    # Cơ bản: 3
    trait = [
        "coban",
        "binhdan",
        "cu",
        "conoithat",
        "condep",
        "chuan",
        "maylanh",
        "dieuhoa",
        "tulanh",
        "giuong",
        "tivi",
        "tv",
        "sofa",
        "sopha",
        "nhumoi",
        "nonglanh",
        "noithatdinhtuong",
        "moitinh",
        "tot",
        "lientuong",
        "nhuhinh",
        "trangbi",
        "dinhtuong",
    ]
    if any(i in s for i in trait):
        return 3

    return 0


def direction_convert(s) -> int:
    """
    # Convert direction to integer
    Đông: 1
    Tây: 2
    Nam: 3
    Bắc: 4
    Đông - Bắc: 5
    Đông - Nam: 6
    Tây - Bắc: 7
    Tây - Nam: 8
    """
    if pd.isna(s):
        return np.nan
    if "Đông" == s:
        return 1
    if "Tây" == s:
        return 2
    if "Nam" == s:
        return 3
    if "Bắc" == s:
        return 4
    if "Đông - Bắc" == s:
        return 5
    if "Đông - Nam" == s:
        return 6
    if "Tây - Bắc" == s:
        return 7
    if "Tây - Nam" == s:
        return 8


def legal_document_deconvert(num) -> str:
    """
    # Deconvert property legal document to string
    0: Uncertified
    1: Certified
    2: Awaiting certification
    3: Shared/notarized certification
    4: Handwritten document
    """
    if pd.isna(num):
        return np.nan
    if num == 0:
        return "Uncertified"
    if num == 1:
        return "Certified"
    if num == 2:
        return "Awaiting certification"
    if num == 3:
        return "Shared/notarized certification"
    if num == 4:
        return "Handwritten document"


def furnishings_deconvert(num) -> str:
    """
    # Deconvert furnishing status to string
    0: No furnishings
    1: High-end furnishings
    2: Adequate furnishings
    3: Decent furnishings
    """
    if pd.isna(num):
        return np.nan
    if num == 0:
        return "No furnishings"
    if num == 1:
        return "High-end furnishings"
    if num == 2:
        return "Adequate furnishings"
    if num == 3:
        return "Decent furnishings"


def direction_deconvert(num) -> str:
    """
    # Deconvert direction to string
    East: 1
    West: 2
    South: 3
    North: 4
    North - East: 5
    South - East: 6
    North - West: 7
    South - West: 8
    """
    if pd.isna(num):
        return np.nan
    if num == 1:
        return "East"
    if num == 2:
        return "West"
    if num == 3:
        return "South"
    if num == 4:
        return "North"
    if num == 5:
        return "North - East"
    if num == 6:
        return "South - East"
    if num == 7:
        return "North - West"
    if num == 8:
        return "South - West"
