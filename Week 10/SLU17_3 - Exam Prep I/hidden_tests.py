import numpy as np


def test_exercise_1(answers):
    expected = {
        "question_1": 1,
        "question_2": 1,
        "question_3": 4,
        "question_4": 2,
        "question_5": 2,
        "question_6": 3,
        "question_7": 3,
        "question_8": 4,
        "question_9": 3,
        "question_10": 3,
        "question_11": 1,
        "question_12": 3,
    }

    assert isinstance(answers, dict)
    try:
        for k in answers.keys():
            q, n = k.split("_")
            assert q == "question"
            assert 1 <= int(n) <= 12
    except AssertionError:
        raise AssertionError("Answers dict has unexpected keys")

    score = 0
    for k in expected.keys():
        if k not in answers:
            continue
        if expected[k] == answers[k]:
            score += 1

    final_score = int(round(score * 6 / 12))
    if final_score == 0:
        raise AssertionError("Not enough correct answers to score points.")

    print(f"{score} / 12 correct answers. Your score is {final_score}.")
    
    return final_score
