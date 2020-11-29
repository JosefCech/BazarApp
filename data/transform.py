import csv
from uuid import uuid4

import requests

from src.data.models.business.store_item import StoreItemDocument
from src.data.models.business.store_item_resource import StoreItemResourceRequest
from src.data.models.transform.csv_import import _transformation_size, _transformation_price, _transformation_int, \
    _transformation_size_request

# class StoreItemResourceRequest(BaseModel):
#     id: str
#     name: str
#     longName: Optional[str]
#     originalPrice: Optional[float]
#     purchasePrice: Optional[float]
#     categorySex: CategorySex = CategorySex.NA
#     categoryType: CategoryType = CategoryType.OTHER
#     categorySubtype: Optional[str]
#     brand: Optional[str]
#     advertisementInfo: Optional[AdvertisementRequest]
#     soldInfo: Optional[SoldItemRequest]
#     createAt: Optional[str]
from src.data.models.transform.transform_db_model_to_resource import transform_resquest_to_business_model


def transformation(file_name: str):
    with open(file_name, 'r', encoding="utf-8") as file:
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
                data_row = {"id": str(uuid4())}
                for i in range(len(fields)):
                    if fields[i] == "size":
                        data_row[fields[i]] = _transformation_size_request(size=_transformation_size(row[i].strip())) if \
                        row[i].strip() != '' else None
                    elif fields[i] in ["purchasePrice", "originalPrice"]:
                        data_row[fields[i]] = _transformation_price(row[i].strip())
                    elif fields[i] in ["givenPrice", "postage"]:
                        if data_row.get('soldInfo') is None:
                            data_row['soldInfo'] = {}
                        data_row['soldInfo'][fields[i]] = _transformation_price(row[i].strip())
                    elif fields[i] == "pieces":
                        if not row[i].strip():
                            row[i] = '1'
                        data_row[fields[i]] = _transformation_int(row[i].strip())
                    else:
                        data_row[fields[i]] = row[i].strip()
                data.append(StoreItemResourceRequest(**data_row))
                row_id = row_id + 1
            except Exception as e:
                print(f"Row id {row_id} field {i} failed due  {e}  on  {row}")
    return data


data = transformation('data.csv')
print([x.json(ensure_ascii=False) for x in data])

for item in data:
    response = requests.post(url="https://jgfnvpor2j.execute-api.eu-west-1.amazonaws.com/v0/store-items",
                             data=item.json(), headers={})

    print(response.json())
