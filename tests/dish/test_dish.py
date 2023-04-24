from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest

# Req 2
def test_dish():
    pizza = Dish("Pizza", 35.99)
    pizza2 = Dish("Pizza", 35.99)
    macarrao = Dish("Macarrão", 27.99)

    assert repr(pizza) == "Dish('Pizza', R$35.99)"
    assert repr(macarrao) == "Dish('Macarrão', R$27.99)"
    assert pizza.name == "Pizza"

    assert pizza == pizza2
    assert pizza != macarrao

    assert hash(pizza) == hash(pizza2)
    assert hash(pizza) != hash(macarrao)

    macarrao.add_ingredient_dependency("Carne moída", 200)
    assert macarrao.get_ingredients() == { "Carne moída" }

    assert len(pizza.get_restrictions()) == 0

    with pytest.raises(TypeError):
        Dish("Pizza", "30")
    with pytest.raises(ValueError):
        Dish("Pizza", -30)

