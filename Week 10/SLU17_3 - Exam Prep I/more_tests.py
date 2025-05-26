import numpy as np


def test_exercise_2_part_I(read_matches):
    matches_data = read_matches('champions_league_15_16_large.csv')
    
    assert isinstance(matches_data, list)
    assert all(isinstance(match_data, dict) for match_data in matches_data)
    assert len(matches_data) == 125

    match_data = matches_data[73]
    assert match_data["stage"] == "Group"
    assert match_data["date"] == "25 Nov 2015"
    assert match_data["team_1"] == "Shakhtar Donetsk"
    assert match_data["team_2"] == "Real Madrid CF"
    assert match_data["ft"] == "3-4"
    
    match_data = matches_data[102]
    assert match_data["stage"] == "Knockout"
    assert match_data["date"] == "24 Feb 2016"
    assert match_data["team_1"] == "PSV Eindhoven"
    assert match_data["team_2"] == "Atletico Madrid"
    assert match_data["ft"] == "0-0"


def test_exercise_2_part_II_a(get_goals_from_ft):
    matches_data = [
        {"stage": "Group", "date": "24 Nov 2015", "team_1": "BATE Borisov", "team_2": "Bayer 04 Leverkusen", "ft": "1-1"},
        {"stage": "Group", "date": "24 Nov 2015", "team_1": "FC Barcelona", "team_2": "AS Roma", "ft": "6-1"},
        {"stage": "Group", "date": "24 Nov 2015", "team_1": "Arsenal FC", "team_2": "Dinamo Zagreb", "ft": "3-0"},
        {"stage": "Group", "date": "24 Nov 2015", "team_1": "Bayern München", "team_2": "Olympiacos", "ft": "4-0"},
        {"stage": "Group", "date": "24 Nov 2015", "team_1": "FC Porto", "team_2": "Dinamo Kiev", "ft": "0-2"},
        {"stage": "Group", "date": "24 Nov 2015", "team_1": "Maccabi Tel Aviv", "team_2": "Chelsea FC", "ft": "0-4"},
        {"stage": "Group", "date": "24 Nov 2015", "team_1": "Olympique Lyon", "team_2": "KAA Gent", "ft": "1-2"},
        {"stage": "Group", "date": "24 Nov 2015", "team_1": "Zenit St. Petersburg", "team_2": "Valencia CF", "ft": "2-0"},
        {"stage": "Group", "date": "25 Nov 2015", "team_1": "Malmo FF", "team_2": "Paris Saint-Germain", "ft": "0-5"},
        {"stage": "Group", "date": "25 Nov 2015", "team_1": "Shakhtar Donetsk", "team_2": "Real Madrid CF", "ft": "3-4"},
        {"stage": "Group", "date": "25 Nov 2015", "team_1": "CSKA Moskva", "team_2": "VfL Wolfsburg", "ft": "0-2"},
        {"stage": "Group", "date": "25 Nov 2015", "team_1": "Manchester United FC", "team_2": "PSV Eindhoven", "ft": "0-0"},
        {"stage": "Group", "date": "25 Nov 2015", "team_1": "Astana", "team_2": "SL Benfica", "ft": "2-2"},
        {"stage": "Group", "date": "25 Nov 2015", "team_1": "Atletico Madrid", "team_2": "Galatasaray İstanbul AŞ", "ft": "2-0"},
        {"stage": "Group", "date": "25 Nov 2015", "team_1": "Juventus", "team_2": "Manchester City FC", "ft": "1-0"},
        {"stage": "Group", "date": "25 Nov 2015", "team_1": "Borussia Monchengladbach", "team_2": "Sevilla FC", "ft": "4-2"},
    ]
    
    matches_goals = get_goals_from_ft(matches_data)
    assert isinstance(matches_goals, list)
    assert all(isinstance(match_goals, int) for match_goals in matches_goals)
    assert len(matches_goals) == len(matches_data)
    assert matches_goals[3] == 4
    assert matches_goals[5] == 4
    assert matches_goals[9] == 7
    assert matches_goals[11] == 0
    assert matches_goals[14] == 1
    

def test_exercise_2_part_II_b(get_goals_stats):
    goals_list = [2, 7, 3, 4, 2, 4, 3, 2, 5, 7, 2, 0, 4, 2, 1, 6]
    
    goals_stats = get_goals_stats(goals_list)
    assert isinstance(goals_stats, tuple)
    assert len(goals_stats) == 2
    
    goals_average, goals_mode = goals_stats
    assert isinstance(goals_average, float)
    assert isinstance(goals_mode, int)
    np.testing.assert_almost_equal(goals_average, 3.4, decimal=1)
    assert goals_mode == 2
