from deck import Card, Deck  # remplace `your_module` par le nom de ton fichier (sans .py)

def test_card_str_and_repr():
    card = Card(Card.Color.HEART, 7)
    assert str(card) == "7 of Color.HEART"
    assert repr(card) == "7 of Color.HEART"

def test_deck_has_52_cards():
    deck = Deck()
    assert len(deck.cards) == 52

def test_deck_contains_all_colors():
    deck = Deck()
    colors = {card.color for card in deck.cards}
    assert colors == set(Card.Color)

def test_deck_contains_numbers_1_to_13():
    deck = Deck()
    numbers = {card.number for card in deck.cards}
    assert numbers == set(range(1, 14))

def test_no_duplicate_cards():
    deck = Deck()
    seen = set()
    for card in deck.cards:
        key = (card.color, card.number)
        assert key not in seen, f"Duplicate card found: {card}"
        seen.add(key)