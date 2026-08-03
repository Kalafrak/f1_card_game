from game_loop import compare_stat, calculate_score_change

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
