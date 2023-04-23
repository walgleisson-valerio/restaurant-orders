from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    carne = Ingredient("Carne")
    carne2 = Ingredient("Carne")
    ovo = Ingredient("Ovo")
    assert carne.name == "Carne"
    assert repr(carne) == "Ingredient('Carne')"
    assert carne == carne != ovo
    assert hash(carne) == hash(carne2) != hash(ovo)
    assert len(carne.restrictions) == 0
