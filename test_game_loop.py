from game_loop import compare_stat

def test_compare_stat_player_wins():
    result = compare_stat(10, 5)
    assert result == "player"