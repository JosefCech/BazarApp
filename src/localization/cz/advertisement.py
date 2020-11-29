class LangObject:
    def __init__(self, items):
        self._items = items

    def get(self, item, **kwargs):

        return self._items.get(item).format(**kwargs) if self._items.get(item) else item


lang = LangObject(items={
    'created': 'Vytvořen',
    'published': 'Publikován',
    'reserved': 'Rezervováno',
    'sold': "Prodáno",
    'swapped': "Vyměněno",
    "boy": "Kluci",
    'girl': "Holky",
    "unisex": "Unisex",
    'women': "Ženy",
    'men': "Muži",
    'not-applicable': "N/A",
    'clothes': "Oblečení",
    'shoes': 'Boty',
    'toys': "Hračky",
    'other': "Ostatní",
    'winter': "Zimní",
    'summer': "Letní",
    'whole-year': "Celoroční",
    'undefined': "N/A",
    'name': "Název",
    'description': 'Popis inzerátu',
    'longName': 'Popisek',
    'categorySex': 'Určení',
    'categoryType': "Kategorie",
    'categorySubtype': 'Podkategorie',
    'brand': 'Značka',
    'season': 'Pro obdobi',
    'size': 'Velikost',
    "originalPrice": "Původní cena",
    "boughtPrice": "Nákupní cena",
    "publishedDate": "Datum publikování",
    "soldDate": "Datum prodeje",
    "postage": 'Poštovné',
    "advertisedPrice": "Inzerovaná cena",
    "givenPrice": 'Zaplaceno',
    "submit": "Odeslat",
    "purchasePrice": "Zaplaceno",
    "advertisementInfo": "Inzerát",
    "soldInfo": "Prodej",
    "item_extend_info": "{key} - rozšiřující informace"

})
