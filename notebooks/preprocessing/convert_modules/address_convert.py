import json
import re
import pandas as pd
import os
from unidecode import unidecode


def __get_place_name(full_name):
    """
    ## Return a lowercase non-accent plain name of a location in Viet Nam
    E.g.:
    - 'Thành phố Hồ Chí Minh' -> hochiminh
    - 'Tỉnh Nam Định' -> namdinh
    - 'Thủ Đức (Quận 9 cũ)' -> thuduc
    """
    if pd.isna(full_name):
        return pd.NA
    # Remove parentheses
    if "(" in full_name:
        full_name = re.sub(r"\(.*?\)", "", full_name)
    # Replace administrative unit strings
    no_unit_name = re.sub(
        r"\A(thành phố|tp|tỉnh|huyện|quận|thị xã|xã|phường|thị trấn|xả|tĩnh)",
        "",
        full_name.strip().lower(),
    )
    plain = re.sub(r"[^a-z0-9]", "", unidecode(no_unit_name))
    # Convert 009 -> 9, 0003->3
    if plain.isnumeric():
        return str(int(plain))
    return plain


def __extract_ward(address: str):
    """
    Extract the ward, ward, or commune from the given address.
    E.g.:
    - 'Dự án Vinhomes Green Bay Mễ Trì, Đường Đại lộ Thăng Long, Phường Mễ Trì, Nam Từ Liêm, Hà Nội'
      -> 'Phường Mễ Trì'
    - 'Dự án Vinhomes Green Bay Mễ Trì, Đường Đại lộ Thăng Long, Nam Từ Liêm, Hà Nội'
      -> None
    """
    if pd.isna(address):
        return pd.NA
    match = re.search(r"\b(Phường|Xã|Thị trấn)\s+[^,]+", address, re.IGNORECASE)

    if match:
        return match.group(0).strip()
    return pd.NA


def __region_to_id_convert(raw_name, dvhc_json):
    """
    Convert region (Tỉnh, thành phố ~ level 1) to id (string)
    """
    new_name = __get_place_name(raw_name)
    if pd.isna(raw_name):
        return pd.NA, pd.NA

    for idx, level_1 in enumerate(dvhc_json):
        if new_name == level_1["name"]:
            return idx, level_1["level1_id"]
    return pd.NA, pd.NA


def __area_to_id_convert(region_idx, raw_name, dvhc_json):
    """
    Convert area (Quận, Huyện, thị xã ~ level 2) to id (string)
    """
    new_name = __get_place_name(raw_name)
    if pd.isna(raw_name):
        return pd.NA, pd.NA

    for idx, level_2 in enumerate(dvhc_json[region_idx]["level2s"]):
        if new_name == level_2["name"]:
            return idx, level_2["level2_id"]
    return pd.NA, pd.NA


def __ward_to_id_convert(region_idx, area_idx, raw_name, dvhc_json):
    """
    Convert ward (Phường, xã, thị trấn ~ level 3) to id (string)
    """
    new_name = __get_place_name(__extract_ward(raw_name))
    if pd.isna(new_name):
        return pd.NA

    for level_3 in dvhc_json[region_idx]["level2s"][area_idx]["level3s"]:
        if new_name == level_3["name"]:
            return level_3["level3_id"]

    return pd.NA


def address_convert_all(df: pd.DataFrame):
    """Convert Region, area, ward to id"""

    def convert_row(row, dvhc_json):
        region_idx, region_id = __region_to_id_convert(row["City"], dvhc_json)
        if pd.isna(region_idx):
            return pd.Series({"City": pd.NA, "District": pd.NA, "Ward": pd.NA})

        area_idx, area_id = __area_to_id_convert(region_idx, row["District"], dvhc_json)
        if pd.isna(area_idx):
            return pd.Series({"City": region_id, "District": pd.NA, "Ward": pd.NA})

        ward_id = __ward_to_id_convert(region_idx, area_idx, row["DiaChi"], dvhc_json)
        return pd.Series({"City": region_id, "District": area_id, "Ward": ward_id})

    def convert_row_hybrid(row):
        res = convert_row(row, __dvhc_json_2020)
        if res.isna().any():
            # Retry with another version
            res = convert_row(row, __dvhc_json_2024)
        return res.astype(pd.Int32Dtype())

    if "Ward" not in df:
        df["Ward"] = pd.NA

    df[["City", "District", "Ward"]] = df.apply(convert_row_hybrid, axis=1)


#################################################### Load dvhc ####################################################
# Get the absolute path
current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = (
    "/".join(i for i in current_dir.split("\\")[:-3]) + "/data/donvihanhchinhvn/"
)


def load_dvhc_file(file_name):
    with open(json_path + file_name, "r", encoding="utf8") as dvhc_file:
        dvhc_json = json.load(dvhc_file)["data"]
        for level_1 in dvhc_json:
            # Rename all level 1s
            level_1["name"] = __get_place_name(level_1["name"])
            # Rename all level 2s
            for level_2 in level_1["level2s"]:
                level_2["name"] = __get_place_name(level_2["name"])
                # Rename all level 3s
                for level_3 in level_2["level3s"]:
                    level_3["name"] = __get_place_name(level_3["name"])
    return dvhc_json


__dvhc_json_2024 = load_dvhc_file("dvhcvn_2024.json")
__dvhc_json_2020 = load_dvhc_file("dvhcvn_2020.json")
