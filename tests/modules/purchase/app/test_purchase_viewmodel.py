import pytest


from src.modules.purchase.app.purchase_viewmodel import PurchaseViewmodel
from src.shared.domain.entities.purchase import Purchase
from src.shared.domain.enums.category_enum import CATEGORY

class Test_PurchaseViewmodel:

    def test_purchase_viewmodel_to_dict(self):
        purchase = Purchase(
                        user_id="e52bbdb7-aaa9-49a8-89be-f4ffd4bdc930", 
                        product_id="832ddff6-b83e-4759-ba88-0f683ac70fa3", 
                        category=CATEGORY.CLOTHES, 
                        price= 27.0, 
                        purchase_date= 1744637400
                        )
        purchaseViewmodel = PurchaseViewmodel(purchase=purchase).to_dict()
        expected = {
            "purchase": {
                'user_id': "e52bbdb7-aaa9-49a8-89be-f4ffd4bdc930",
                'product_id': '832ddff6-b83e-4759-ba88-0f683ac70fa3',
                'category': CATEGORY.CLOTHES,
                'price': 27.0,
                'purchase_date': 1744637400,
            },
            'message': 'the purchase has been created'
        }

        assert expected == purchaseViewmodel
