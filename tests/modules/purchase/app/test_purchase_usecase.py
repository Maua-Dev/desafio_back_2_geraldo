import pytest


from src.shared.domain.entities.purchase import Purchase
from src.shared.domain.repositories.purchase_repository_mock import PurchaseRepositoryMock
from src.modules.purchase.app.purchase_usecase import PurchaseUsecase
from src.shared.domain.enums.category_enum import CATEGORY
from src.shared.helpers.errors.domain_errors import EntityError

class Test_PurchaseUsecase:

    def test_create_purchase(self):
        repo = PurchaseRepositoryMock()
        usecase = PurchaseUsecase(repo)

        purchase = usecase(user_id="e52bbdb7-aaa9-49a8-89be-f4ffd4bdc930", product_id="832ddff6-b83e-4759-ba88-0f683ac70fa3", 
                       category=CATEGORY.CLOTHES, price= 27.0, purchase_date= 1744637400)

        assert repo.purchase_list[-1] == purchase
    
    def test_purchase_user_id_str(self):
        with pytest.raises(EntityError):
            purchase = Purchase(user_id=10, product_id="7aa45600-3e44-46ca-8064-aa90874288cf", 
                        category=CATEGORY.CLOTHES, price= 25.0, purchase_date= 1744644600)
    
    def test_purchase_product_id_str(self):
        with pytest.raises(EntityError):
            purchase = Purchase(user_id="3c0c67a5-2dc4-4b90-be13-73b7d29718f0", product_id=10, 
                        category=CATEGORY.CLOTHES, price= 25.0, purchase_date= 1744644600)
            
    def test_purchase_category_ENUM(self):
        with pytest.raises(EntityError):
            purchase = Purchase(user_id="3c0c67a5-2dc4-4b90-be13-73b7d29718f0", product_id="7aa45600-3e44-46ca-8064-aa90874288cf", 
                        category=10, price= 25.0, purchase_date= 1744644600)
         
    def test_purchase_price_float(self):
        with pytest.raises(EntityError):
            purchase = Purchase(user_id="3c0c67a5-2dc4-4b90-be13-73b7d29718f0", product_id="7aa45600-3e44-46ca-8064-aa90874288cf", 
                        category=CATEGORY.CLOTHES, price= 25, purchase_date= 1744644600)
    
    def test_purchase_price_negative(self):
        with pytest.raises(EntityError):
            purchase = Purchase(user_id="3c0c67a5-2dc4-4b90-be13-73b7d29718f0", product_id="7aa45600-3e44-46ca-8064-aa90874288cf", 
                        category=CATEGORY.CLOTHES, price= -5, purchase_date= 1744644600)
            
    def test_purchase_purchase_date_int(self):
        with pytest.raises(EntityError):
            purchase = Purchase(user_id="3c0c67a5-2dc4-4b90-be13-73b7d29718f0", product_id="7aa45600-3e44-46ca-8064-aa90874288cf", 
                        category=CATEGORY.CLOTHES, price= 25.0, purchase_date= "1744644600")
            
    def test_purchase_purchase_date_positive(self):
        with pytest.raises(EntityError):
            purchase = Purchase(user_id="3c0c67a5-2dc4-4b90-be13-73b7d29718f0", product_id="7aa45600-3e44-46ca-8064-aa90874288cf", 
                        category=CATEGORY.CLOTHES, price= 25.0, purchase_date= -17446446000)