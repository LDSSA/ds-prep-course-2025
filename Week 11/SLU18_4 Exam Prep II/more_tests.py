import numpy as np


def test_exercise_2_part_I(read_movies):
    movies_data = read_movies('movies_large.csv')
    
    assert isinstance(movies_data, dict)
    assert len(movies_data) == 200

    assert 'tt1375666' in movies_data
    inception = movies_data['tt1375666']
    assert inception["title"] == "Inception"
    assert inception["year"] == 2010
    np.testing.assert_almost_equal(inception["rating"], 8.8, decimal=1)
    
    assert 'tt0078748' in movies_data
    alien = movies_data['tt0078748']
    assert alien["title"] == "Alien"
    assert alien["year"] == 1979
    np.testing.assert_almost_equal(alien["rating"], 8.5, decimal=1)


def test_exercise_2_part_II(average_movie_rating):
    movies_data = {
        "tt0071411": {"title": "Dersu Uzala", "year": 1975, "rating": 8.2},
        "tt0118799": {"title": "Life Is Beautiful", "year": 1997, "rating": 8.6},
        "tt0252487": {"title": "The Chaos Class", "year": 1975, "rating": 9.3},
        "tt0381681": {"title": "Before Sunset", "year": 2004, "rating": 8.1},
        "tt0466460": {"title": "Khosla Ka Ghosla!", "year": 2006, "rating": 8.3},
        "tt0075148": {"title": "Rocky", "year": 1976, "rating": 8.1},
        "tt0263975": {"title": "The Girl with the Red Scarf", "year": 1977, "rating": 8.5},
        "tt0109830": {"title": "Forrest Gump", "year": 1994, "rating": 8.8},
        "tt1954470": {"title": "Gangs of Wasseypur", "year": 2012, "rating": 8.2},
        "tt0074958": {"title": "Network", "year": 1976, "rating": 8.1},
        "tt0363163": {"title": "Downfall", "year": 2004, "rating": 8.2},
        "tt0347149": {"title": "Howl's Moving Castle", "year": 2004, "rating": 8.2},
        "tt2375605": {"title": "The Act of Killing", "year": 2012, "rating": 8.2},
        "tt0091763": {"title": "Platoon", "year": 1986, "rating": 8.1},
        "tt0114787": {"title": "Underground", "year": 1995, "rating": 8.1},
        "tt0214915": {"title": "Manichithrathazhu", "year": 1993, "rating": 8.7},
        "tt6966692": {"title": "Green Book", "year": 2018, "rating": 8.2},
        "tt3322420": {"title": "Queen", "year": 2013, "rating": 8.1},
        "tt6316138": {"title": "Ayla: The Daughter of War", "year": 2017, "rating": 8.3},
        "tt0468569": {"title": "The Dark Knight", "year": 2008, "rating": 9.0},
    }
                      
    average_movie_rating_1976 = average_movie_rating(movies_data, 1976)
    assert isinstance(average_movie_rating_1976, float)  
    np.testing.assert_almost_equal(average_movie_rating_1976, 8.1, decimal=2)
    
    average_movie_rating_2004 = average_movie_rating(movies_data, 2004)
    assert isinstance(average_movie_rating_2004, float)  
    np.testing.assert_almost_equal(average_movie_rating_2004, 8.1666, decimal=2)
    
    average_movie_rating_2005 = average_movie_rating(movies_data, 2005)
    assert isinstance(average_movie_rating_2005, float)  
    np.testing.assert_almost_equal(average_movie_rating_2005, -1, decimal=2)
    
    average_movie_rating_2023 = average_movie_rating(movies_data, 2023)
    assert isinstance(average_movie_rating_2023, float)  
    np.testing.assert_almost_equal(average_movie_rating_2023, -1, decimal=2)


def test_exercise_2_part_III(pearson_correlation_year_rating):
    
    movies_data = {
        "tt0071411": {"title": "Dersu Uzala", "year": 1975, "rating": 8.2},
        "tt0118799": {"title": "Life Is Beautiful", "year": 1997, "rating": 8.6},
        "tt0252487": {"title": "The Chaos Class", "year": 1975, "rating": 9.3},
        "tt0381681": {"title": "Before Sunset", "year": 2004, "rating": 8.1},
        "tt0466460": {"title": "Khosla Ka Ghosla!", "year": 2006, "rating": 8.3},
        "tt0075148": {"title": "Rocky", "year": 1976, "rating": 8.1},
        "tt0263975": {"title": "The Girl with the Red Scarf", "year": 1977, "rating": 8.5},
        "tt0109830": {"title": "Forrest Gump", "year": 1994, "rating": 8.8},
        "tt1954470": {"title": "Gangs of Wasseypur", "year": 2012, "rating": 8.2},
        "tt0074958": {"title": "Network", "year": 1976, "rating": 8.1},
        "tt0363163": {"title": "Downfall", "year": 2004, "rating": 8.2},
        "tt0347149": {"title": "Howl's Moving Castle", "year": 2004, "rating": 8.2},
        "tt2375605": {"title": "The Act of Killing", "year": 2012, "rating": 8.2},
        "tt0091763": {"title": "Platoon", "year": 1986, "rating": 8.1},
        "tt0114787": {"title": "Underground", "year": 1995, "rating": 8.1},
        "tt0214915": {"title": "Manichithrathazhu", "year": 1993, "rating": 8.7},
        "tt6966692": {"title": "Green Book", "year": 2018, "rating": 8.2},
        "tt3322420": {"title": "Queen", "year": 2013, "rating": 8.1},
        "tt6316138": {"title": "Ayla: The Daughter of War", "year": 2017, "rating": 8.3},
        "tt0468569": {"title": "The Dark Knight", "year": 2008, "rating": 9.0},
    }
    
    pearson_correlation = pearson_correlation_year_rating(movies_data)
    assert isinstance(pearson_correlation, float)
    np.testing.assert_almost_equal(pearson_correlation, -0.197, decimal=3)
