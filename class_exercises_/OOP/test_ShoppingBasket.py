
import pytest
from class_exercises_.OOP.Item import Item
from class_exercises_.OOP.ShoppingBasket import ShoppingBasket

@pytest.fixture
def setup_items_and_basket():
    # Create items
    tomatoSoup = Item("Tomato Soup", "200mL can", 0.70, 20)
    spaghetti = Item("Spaghetti", "500g pack", 1.10, 20)
    blackOlives = Item("Black Olives Jar", "200g Jar", 2.10, 20)
    mozarella = Item("Mozarella", "100g", 1.50, 20)
    gratedCheese = Item("Grated Cheese", "100g", 2.20, 20)

    # Create basket and add items
    basket = ShoppingBasket()
    basket.addItem(tomatoSoup, 4)
    basket.addItem(blackOlives, 1)
    basket.addItem(mozarella, 2)
    basket.addItem(tomatoSoup, 6)

    return basket, tomatoSoup, spaghetti, blackOlives, mozarella, gratedCheese

def test_shopping_basket_setup(setup_items_and_basket):
    """ Test basket has been set up correctly """
    basket, tomatoSoup, *other = setup_items_and_basket
    assert basket.items[tomatoSoup] == 10
    assert tomatoSoup.stock == 10

def test_add_more_than_stock(setup_items_and_basket):
    """ Test adding more items than exist in stock"""
    basket, tomatoSoup, *other = setup_items_and_basket

    # Should add remaining stock of item to basket if requested amount > available stock
    basket.addItem(tomatoSoup, 20)
    assert tomatoSoup.stock == 0

def test_add_item(setup_items_and_basket):
    """test adding and item and invalid inputs"""
    basket, tomatoSoup, spaghetti, *other = setup_items_and_basket

    #tests invalid inputs of wrong data type
    with pytest.raises(TypeError):
        basket.addItem(spaghetti, -2)
    with pytest.raises(TypeError):
        basket.addItem(tomatoSoup, 'howdy')
    with pytest.raises(TypeError):
        basket.addItem(tomatoSoup, 2.5)

    #tests boundary data of 0
    with pytest.raises(Warning):
        basket.addItem(tomatoSoup, 0)
        assert basket.items[tomatoSoup] == 10

def test_remove_item(setup_items_and_basket):
    """test removing and item and invalid inputs"""
    basket, tomatoSoup, spaghetti, blackOlives, *other = setup_items_and_basket

    # tests invalid inputs of wrong data type
    with pytest.raises(TypeError):
        basket.removeItem(spaghetti, -2)
    with pytest.raises(TypeError):
        basket.removeItem(tomatoSoup, 'howdy')
    with pytest.raises(TypeError):
        basket.removeItem(tomatoSoup, 2.5)

    #tests if negative or 0 is entered, all of item is removed from basket
    basket.removeItem(tomatoSoup, -2)
    assert tomatoSoup.stock == 20
    basket.removeItem(blackOlives, 0)
    assert blackOlives.stock == 20

def test_update_item(setup_items_and_basket):
    """test updating item and invalid inputs"""
    basket, tomatoSoup, spaghetti, blackOlives, mozarella, *other = setup_items_and_basket

    #tests non existent items
    with pytest.raises(TypeError):
        basket.updateItem(spaghetti, -2)
    with pytest.raises(Warning):
        basket.updateItem(spaghetti, 0)
    with pytest.raises(TypeError):
        basket.updateItem(spaghetti, 2.5)
    with pytest.raises(TypeError):
        basket.updateItem(spaghetti, 'howdy')

    #tests items they want to add
    basket.addItem(spaghetti, 3)
    assert spaghetti.stock == 17

    #tests increasing amount of item
    basket.updateItem(tomatoSoup, 2)
    assert tomatoSoup.stock == 18

    #tests decreasing amount of item
    basket.updateItem(mozarella, 1)
    assert mozarella.stock == 19

    #tests removing item entirely
    basket.updateItem(blackOlives, 0)
    assert blackOlives.stock == 20
    assert blackOlives not in basket.items

    #tests invalid existing item errors
    with pytest.raises(TypeError):
        basket.updateItem(tomatoSoup, 'howdy')
    with pytest.raises(TypeError):
        basket.updateItem(tomatoSoup, 2.5)


def test_reset(setup_items_and_basket):
    basket, tomatoSoup, spaghetti, blackOlives, mozarella, gratedCheese = setup_items_and_basket

    #asserts stocks reset and no items left in basket after reset
    basket.reset()
    assert tomatoSoup.stock == 20
    assert gratedCheese not in basket.items
    assert tomatoSoup not in basket.items