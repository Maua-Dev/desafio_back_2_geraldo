from src.shared.domain.entities.purchase import Purchase
from src.shared.domain.repositories.challenge_repository_interface import IChallengeRepository
from collections import defaultdict
from typing import Dict, Any

class PurchaseSummaryUsecase:
    def __init__(self, repo: IChallengeRepository):
        self.repo = repo

    def __call__(self, user_id: str, start_date: int, end_date: int) -> Dict[str, Any]:
        # Recupera as compras do repositório para o intervalo de tempo especificado
        result = self.repo.get_purchase_from_user_id_and_interval(
            user_id=user_id, 
            start_date=start_date, 
            end_date=end_date
        )

        # Se não houver compras no intervalo, retorna uma resposta padrão com valores 0
        if not result:
            return {
                "user_id": user_id,
                "start_date": start_date,
                "end_date": end_date,
                "total_spent": 0.0,
                "total_purchases": 0,
                "category_breakdown": {},
                "last_purchase_date": 0
            }

        # Total gasto
        total_spent = result['total_spent']
        
        # Total de compras
        total_purchases = result['total_purchases']
        
        # Breakdown de categoria
        category_breakdown = result['category_breakdown']

        return {
            "user_id": user_id,
            "start_date": start_date,
            "end_date": end_date,
            "total_spent": total_spent,
            "total_purchases": total_purchases,
            "category_breakdown": category_breakdown,
        }
