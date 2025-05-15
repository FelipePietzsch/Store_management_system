import pytest
from programm_modules.product import Product
from programm_modules.promotion import PercentDiscount, SecondHalfPrice, ThirdOneFree

# Test für PercentDiscount
def test_percent_discount():
    # Promotion: 20% Rabatt
    promotion = PercentDiscount("20% off", 20)

    # Erstellen eines Produkts
    product = Product("Book", 10.0, 5, promotion_class=promotion)

    # Berechne den Preis nach der Promotion
    final_price = product.buy(3)  # Wir bestellen 3 Produkte

    # Erwarteter Preis: 3 * 10.0 = 30.0, dann 20% Rabatt: 30.0 * 0.20 = 6.0
    # Endpreis: 30.0 - 6.0 = 24.0
    assert final_price == 24.0


# Test für SecondHalfPrice
def test_second_half_price():
    # Erstellen eines Produkts
    product = Product("Book", 10.0, 5)

    # Promotion: Zweites Produkt zum halben Preis
    promotion = SecondHalfPrice("Second Half Price")

    # Berechne den Preis nach der Promotion
    final_price = promotion.apply_promotion(product, 4)  # Wir bestellen 4 Produkte

    # Erwarteter Preis: 2 Produkte zum vollen Preis und 2 Produkte zum halben Preis
    # Endpreis: 2 * 10.0 + 2 * 5.0 = 20.0 + 10.0 = 30.0
    assert final_price == 30.0


# Test für ThirdOneFree
def test_third_one_free():
    # Erstellen eines Produkts
    product = Product("Book", 10.0, 5)

    # Promotion: Jedes dritte Produkt ist kostenlos
    promotion = ThirdOneFree("Third One Free")

    # Berechne den Preis nach der Promotion
    final_price = promotion.apply_promotion(product, 6)  # Wir bestellen 6 Produkte

    # Erwarteter Preis: 4 Produkte zum vollen Preis (6 - 2 kostenlose Produkte)
    # Endpreis: 4 * 10.0 = 40.0
    assert final_price == 40.0


# Test für ungültige Prozentwerte im PercentDiscount
def test_invalid_percent_discount():
    with pytest.raises(ValueError):
        # Promotion: Ungültiger Prozentwert (mehr als 100%)
        promotion = PercentDiscount("Invalid Percent", 150)


def test_negative_percent_discount():
    with pytest.raises(ValueError):
        # Promotion: Ungültiger Prozentwert (negativ)
        promotion = PercentDiscount("Invalid Percent", -20)