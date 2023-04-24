import pandas as pd
from src.models.ingredient import Ingredient
from src.models.dish import Dish


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.set_menu(source_path)

    def set_menu(self, path: str) -> set:
        df = pd.read_csv(path)
        dishes = {}
        for dish, price, ingr, amount in df.itertuples(index=False):
            if dish not in dishes:
                dishes[dish] = Dish(dish, price)
            dishes[dish].add_ingredient_dependency(Ingredient(ingr), amount)
        return set(dishes.values())
