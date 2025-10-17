
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

    #normal test for expected data
    basket.addItem(tomatoSoup, 1)
    assert tomatoSoup.stock == 9

def test_add_item_erroneous(setup_items_and_basket):
    """tests invalid inputs of wrong data type"""
    basket, tomatoSoup, spaghetti, *other = setup_items_and_basket

    with pytest.raises(TypeError):
        basket.addItem(spaghetti, -2)
    with pytest.raises(TypeError):
        basket.addItem(tomatoSoup, 'howdy')
    with pytest.raises(TypeError):
        basket.addItem(tomatoSoup, 2.5)

def test_add_item_boundary(setup_items_and_basket):
    """tests boundary data for adding (0)"""
    basket, tomatoSoup, spaghetti, *other = setup_items_and_basket

    with pytest.raises(Warning):
        basket.addItem(tomatoSoup, 0)
        assert basket.items[tomatoSoup] == 10

def test_remove_item(setup_items_and_basket):
    """test removing and item with expected data"""
    basket, tomatoSoup, spaghetti, blackOlives, gratedCheese, *other = setup_items_and_basket

    basket.removeItem(blackOlives, 1)
    assert blackOlives.stock == 20
    assert blackOlives not in basket.items

def test_remove_item_erroneous(setup_items_and_basket):
    """test removing and item with incorrect data type"""
    basket, tomatoSoup, spaghetti, blackOlives, gratedCheese, *other = setup_items_and_basket

    # tests invalid inputs of wrong data type
    with pytest.raises(TypeError):
        basket.removeItem(tomatoSoup, 'howdy')
    with pytest.raises(TypeError):
        basket.removeItem(tomatoSoup, 2.5)

def test_remove_items_all(setup_items_and_basket):
    """tests if negative or 0 is entered, all of item is removed from basket"""
    basket, tomatoSoup, spaghetti, blackOlives, gratedCheese, *other = setup_items_and_basket

    basket.removeItem(tomatoSoup, -2)
    assert tomatoSoup.stock == 20
    basket.removeItem(blackOlives, 0)
    assert blackOlives.stock == 20

def test_remove_item_more_than_there(setup_items_and_basket):
    """tests trying to remove more of item than in basket"""
    basket, tomatoSoup, spaghetti, blackOlives, gratedCheese, *other = setup_items_and_basket

    basket.addItem(blackOlives, 1)
    basket.removeItem(blackOlives, 10)
    assert blackOlives.stock == 20

def test_remove_item_not_there(setup_items_and_basket):
    """tests trying to remove non-existent items"""
    basket, tomatoSoup, spaghetti, blackOlives, gratedCheese, *other = setup_items_and_basket

    basket.removeItem(gratedCheese, 0)
    assert gratedCheese.stock == 20
    with pytest.raises(Warning):
        basket.removeItem(gratedCheese, 0)
        assert gratedCheese.stock == 20
    with pytest.raises(Warning):
        basket.removeItem(gratedCheese, 1)
        assert gratedCheese.stock == 20

def test_update_item(setup_items_and_basket):
    """test updating item and invalid inputs"""
    basket, tomatoSoup, spaghetti, blackOlives, mozarella, *other = setup_items_and_basket

    basket.updateItem(tomatoSoup, 1)
    assert tomatoSoup.stock == 19
    assert basket.items[tomatoSoup] == 1

def test_update_item_not_there_normal(setup_items_and_basket):
    """test updating items not there with normal data"""
    basket, tomatoSoup, spaghetti, blackOlives, mozarella, *other = setup_items_and_basket

    basket.addItem(spaghetti, 3)
    assert spaghetti.stock == 17

def test_update_item_not_there_erroneous(setup_items_and_basket):
    """test updating items not there with erroneous and normal data"""
    basket, tomatoSoup, spaghetti, blackOlives, mozarella, *other = setup_items_and_basket

    with pytest.raises(TypeError):
        basket.updateItem(spaghetti, -2)
    with pytest.raises(Warning):
        basket.updateItem(spaghetti, 0)
    with pytest.raises(TypeError):
        basket.updateItem(spaghetti, 2.5)
    with pytest.raises(TypeError):
        basket.updateItem(spaghetti, 'howdy')

def test_update_item_normal(setup_items_and_basket):
    """test updating items with normal data"""
    basket, tomatoSoup, spaghetti, blackOlives, mozarella, *other = setup_items_and_basket

    """tests increasing amount of item"""
    basket.updateItem(tomatoSoup, 2)
    assert tomatoSoup.stock == 18

    """tests decreasing amount of item"""
    basket.updateItem(mozarella, 1)
    assert mozarella.stock == 19

    """tests removing item entirely"""
    basket.updateItem(blackOlives, 0)
    assert blackOlives.stock == 20
    assert blackOlives not in basket.items

    basket.updateItem(tomatoSoup, -2)
    assert tomatoSoup.stock == 20
    assert tomatoSoup not in basket.items

def test_update_item_erroneous(setup_items_and_basket):
    """test updating items with erroneous data"""
    basket, tomatoSoup, spaghetti, blackOlives, mozarella, *other = setup_items_and_basket

    with pytest.raises(TypeError):
        basket.updateItem(tomatoSoup, 'howdy')
    with pytest.raises(TypeError):
        basket.updateItem(tomatoSoup, 2.5)


def test_reset(setup_items_and_basket):
    """test resetting basket and making sure it's empty afterwards"""
    basket, tomatoSoup, spaghetti, blackOlives, mozarella, gratedCheese = setup_items_and_basket

    basket.reset()
    assert tomatoSoup.stock == 20
    assert gratedCheese not in basket.items
    assert tomatoSoup not in basket.items