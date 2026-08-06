from game_loop import compare_stat, calculate_score_change, sum_stats, choose_cpu_card, cards_per_round, check_deck_capacity
from driver_class import Driver
from deck import Deck

def test_compare_stat_player_wins():
    result = compare_stat(10, 5)
    assert result == "player"

def test_compare_stat_cpu_wins():
    result = compare_stat(5, 10)
    assert result == "cpu"

def test_compare_stat_tie():
    result = compare_stat(3000, 3000)
    assert result == "tie"

def test_compare_stat_zero_values():
    result = compare_stat(0, 0)
    assert result == "tie"

def test_calculate_score_change_player_wins():
    result = calculate_score_change("player", 300, 100)
    assert result == 200

def test_calculate_score_change_cpu_wins():
    result = calculate_score_change("cpu", 100, 300)
    assert result == 200

def test_calculate_score_change_tie():
    result = calculate_score_change("tie", 300, 300)
    assert result == 0

def test_sum_stats():
    card = Driver("Test Guy", 1, 2, 3, 4, 5, 6)
    assert sum_stats(card) == 21

def test_choose_cpu_card_picks_highest_total():
    low = Driver("Low", 1, 1, 1, 1, 1, 1)
    high = Driver("High", 10, 10, 10, 10, 10, 10)
    assert choose_cpu_card([low, high]) is high

def test_choose_cpu_card_handles_ties():
    first = Driver("First", 5, 5, 5, 5, 5, 5)
    second = Driver("Second", 1, 1, 1, 1, 1, 25)
    assert choose_cpu_card([first, second]) is first

def test_cards_per_round_classic():
    assert cards_per_round("classic") == 2

def test_cards_per_round_draft():
    assert cards_per_round("draft") == 6

def test_check_deck_capacity_pass():
    deck = Deck([Driver(f"Driver {i}", 10, 10, 10, 10, 10, 10) for i in range(60)])
    assert check_deck_capacity(deck, "draft") == 60

def test_check_deck_capacity_too_small_for_draft():
    deck = Deck([Driver(f"Driver {i}", 10, 10, 10, 10, 10, 10) for i in range(59)])
    try:
        check_deck_capacity(deck, "draft")
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_check_deck_capacity_too_small_for_classic():
    deck = Deck([Driver(f"Driver {i}", 10, 10, 10, 10, 10, 10) for i in range(19)])
    try:
        check_deck_capacity(deck, "classic")
        assert False, "Expected ValueError"
    except ValueError:
        pass
