import numpy as np
from unidecode import unidecode


# Không sổ : 0
# Sổ đỏ + sổ hồng | đầy đủ | thổ cư : 1
# Sổ đỏ | Có sổ | sổ sẵn | chinh chu | phap ly ro rang: 2
# Sổ hồng | sổ riêng: 3
# viết tay | vi bằng | hợp đồng : 4
# đang chờ sổ: 5
def legal_document_convert(s) -> int:
    if s == np.nan:
        return 0

    s = unidecode(s.lower().replace(" ", ""))
    # Sổ đỏ + sổ hồng | đầy đủ | thổ cư : 1
    cri = ["sodo", "sohong"]
    if (
        "thocu" in s
        or all(i in s for i in cri)
        or ("daydu" in s and not any(i in s for i in cri))
    ):
        return 1

    # Sổ đỏ | Có sổ | sổ sẵn | chinh chu | phap ly ro rang: 2
    cri = [
        "sodo",
        "sd",
        "biado",
        "sosan",
        "sanso",
        "cosan",
        "chinhchu",
        "quyensudungdat",
        "phaplyrorang",
        "phaplirorang",
        "phaplychuan",
        "phaplysach",
        "phaplyminhbach",
        "sodep",
        "socongchung",
        "vuongdep",
        "sovuong",
        "sodat",
        "catket",
    ]
    if any(i in s for i in cri) or ("coso" in s and "sohong" not in s):
        return 2

    # Sổ hồng | sổ riêng | so huu lau dai: 3
    cri = ["sohong", "sh", "biahong", "sorieng", "hoancong", "laudai"]
    if any(i in s for i in cri):
        return 3

    # viết tay | vi bằng | hợp đồng : 4
    cri = ["viettay", "vibang", "hopdong", "giaytay", "hdmb", "thoathuan", "vb"]
    if any(i in s for i in cri):
        return 4

    cri = ["dangcho", "dangdoi", "chocap", "choso", "chuanbi", "dangra", "danglam"]
    # đang chờ sổ: 5
    if any(i in s for i in cri):
        return 5

    return 0


# Không: 0
# Cao cấp: 1
# Đầy đủ | hoàn thiện: 2
# Cơ bản: 3
def furnishings_convert(s) -> int:
    if s == np.nan:
        return 0

    s = unidecode(s.lower().replace(" ", ""))

    cri = [
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
    if any(i in s for i in cri):
        return 1

    # Đầy đủ | hoàn thiện: 2
    cri = [
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
    if any(i in s for i in cri):
        return 2

    # Cơ bản: 3
    cri = [
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
    if any(i in s for i in cri):
        return 3

    return 0
