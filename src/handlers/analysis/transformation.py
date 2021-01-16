import csv
from typing import List, Dict
from uuid import uuid4

from src.data.models.business.advertisement_resource import SoldPieceOfClothing
from src.data.models.business.clothing_size import ClothingSizeByHeight, ClothingSizeByWeight


def _transformation_size(size_str: str):
    size_type = ClothingSizeByHeight
    if 'kg' in size_str:
        size_type = ClothingSizeByWeight
        size_str = size_str.replace('kg', '').strip()

    size = None
    if size_str.find("-") != -1:
        size = size_str.split("-")
    if size_str.find("/") != -1:
        size = size_str.split("/")
    if size:
        return size_type(min=int(size[0]), max=int(size[1]))
    else:
        return size_type(min=int(size_str), max=int(size_str))


def _transformation_price(price_str: str):
    try:
        return float(price_str)
    except Exception:
        return None


def _transformation_int(int_str):
    try:
        return int(int_str)
    except Exception:
        return None


def transformation(file_name: str):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        data = []
        first_row = True
        row_id = 0
        for row in reader:
            try:
                if len(row) == 0:
                    continue
                if first_row:
                    fields = row
                    first_row = False
                    continue
                data_row = {"id": uuid4()}
                for i in range(len(fields)):
                    if fields[i] == "size":
                        data_row[fields[i]] = _transformation_size(row[i].strip()) if row[i].strip() != '' else None
                    elif fields[i] in ["purchase_price", "original_price", "selling_price", "post_fee"]:
                        data_row[fields[i]] = _transformation_price(row[i].strip())
                    elif fields[i] == "pieces":
                        if not row[i].strip():
                            row[i] = '1'
                        data_row[fields[i]] = _transformation_int(row[i].strip())
                    else:
                        data_row[fields[i]] = row[i].strip()
                if data_row["selling_price"] is not None:
                    data.append(SoldPieceOfClothing(**data_row))
                row_id = row_id + 1
            except Exception as e:
                print(f"Row id {row_id} field {i} failed due  {e}  on  {row}")
    return data


def _filter(item, filter_data):
    for filter in filter_data:
        value = getattr(item, filter)
        if  value and value != filter_data[filter]:
            return False
    return True


def make_analysis(data: List, filter_data: Dict):
    filter_data = [item for item in data if _filter(item, filter_data)]
    print(f"items : {len(filter_data)}")
    analysis = {"gifts": 0}
    CALC_FIELDS = ["purchase_price", "original_price", "selling_price", "post_fee"]
    for item in filter_data:
        for field in CALC_FIELDS:
            field_value = getattr(item, field)
            if field_value is not None:
                if f"{field}_total" in analysis:
                    analysis[f"{field}_total"] += field_value
                else:
                    analysis[f"{field}_total"] = field_value
                if field == "selling_price" and field_value == 0:
                    analysis["gifts"] += 1

    analysis["total_discount"] = analysis['purchase_price_total'] - analysis['original_price_total']
    analysis["total_discount_percent"] = 1 - analysis['purchase_price_total'] / analysis['original_price_total']
    analysis["total_reward"] = analysis['selling_price_total'] - analysis["post_fee_total"]
    analysis["total_reward_percent"] = analysis['selling_price_total'] / (
            analysis["post_fee_total"] + analysis["purchase_price_total"])
    analysis["total_real_price"] = analysis['purchase_price_total'] - analysis["total_reward"]
    analysis["total_discount_against_original"] = 1 - analysis["total_real_price"] / analysis['original_price_total']
    return analysis
