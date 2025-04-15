import pytest


from src.shared.domain.entities.purchase import Purchase
from src.shared.domain.enums.category_enum import CATEGORY
from src.shared.helpers.errors.domain_errors import EntityError


class Test_Purchase:
    def test_purchase(self):
        purchase = Purchase(user_id="3c0c67a5-2dc4-4b90-be13-73b7d29718f0", product_id="7aa45600-3e44-46ca-8064-aa90874288cf", 
                     category=CATEGORY.CLOTHES, price= 25.0, purchase_date= 1744644600)
        
        assert purchase.user_id == "3c0c67a5-2dc4-4b90-be13-73b7d29718f0"
        assert purchase.product_id == "7aa45600-3e44-46ca-8064-aa90874288cf"
        assert purchase.category == CATEGORY.CLOTHES
        assert purchase.price == 25.0
        assert purchase.purchase_date == 1744644600
    
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
            
    
