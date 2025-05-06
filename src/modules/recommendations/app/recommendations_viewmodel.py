class RecommendationsViewmodel:
    recommended_categories: list[str]


    def __init__(self, recommended_categories: list[str]):
        self.recommended_categories = recommended_categories

    def to_dict(self) -> dict:
        return {
            "recommended_categories": self.recommended_categories
        }
