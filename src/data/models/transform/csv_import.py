import csv
from uuid import uuid4

from src.data.models.business.store_item import ClothesSize, ClothesSizeEnum
from src.data.models.business.store_item_resource import ClothesSizeRequest


def _transformation_size_request(size: ClothesSize):
    return ClothesSizeRequest(min=size.min, max=size.max, typeSize=size.type_size)


def _transformation_size(size_str: str):
    size_type = ClothesSizeEnum.BY_HEIGHT
    if 'kg' in size_str:
        size_type = ClothesSizeEnum.BY_HEIGHT
        size_str = size_str.replace('kg', '').strip()

    size = None
    if size_str.find("-") != -1:
        size = size_str.split("-")
    if size_str.find("/") != -1:
        size = size_str.split("/")
    if size:
        return ClothesSize(min=int(size[0]), max=int(size[1]), type_size=size_type)
    else:
        return ClothesSize(min=int(size_str), max=int(size_str), type_size=size_type)


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

# def transformation(file_name: str):
#     with open(file_name, 'r') as file:
#         reader = csv.reader(file)
#         data = []
#         first_row = True
#         row_id = 0
#         for row in reader:
#             try:
#                 if len(row) == 0:
#                     continue
#                 if first_row:
#                     fields = row
#                     first_row = False
#                     continue
#                 data_row = {"id": uuid4()}
#                 for i in range(len(fields)):
#                     if fields[i] == "size":
#                         data_row[fields[i]] = _transformation_size(row[i].strip()) if row[i].strip() != '' else None
#                     elif fields[i] in ["purchase_price", "original_price", "selling_price", "post_fee"]:
#                         data_row[fields[i]] = _transformation_price(row[i].strip())
#                     elif fields[i] == "pieces":
#                         if not row[i].strip():
#                             row[i] = '1'
#                         data_row[fields[i]] = _transformation_int(row[i].strip())
#                     else:
#                         data_row[fields[i]] = row[i].strip()
#                 if data_row["selling_price"] is not None:
#                     data.append(SoldPieceOfClothing(**data_row))
#                 row_id = row_id + 1
#             except Exception as e:
#                 print(f"Row id {row_id} field {i} failed due  {e}  on  {row}")
#     return data
