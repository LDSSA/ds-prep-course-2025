import numpy as np
import hashlib

def test_exercise_1(answers):
    expected = {
        "question_1": '8527a891e224136950ff32ca212b45bc93f69fbb801c3b1ebedac52775f99e61',
        "question_2": '785f3ec7eb32f30b90cd0fcf3657d388b5ff4297f2f9716ff66e9b69c05ddd09',
        "question_3": 'eb1e33e8a81b697b75855af6bfcdbcbf7cbbde9f94962ceaec1ed8af21f5a50f',
        "question_4": '71ee45a3c0db9a9865f7313dd3372cf60dca6479d46261f3542eb9346e4a04d6',
        "question_5": '2858dcd1057d3eae7f7d5f782167e24b61153c01551450a628cee722509f6529',
        "question_6": 'd029fa3a95e174a19934857f535eb9427d967218a36ea014b70ad704bc6c8d1c',
        "question_7": '96061e92f58e4bdcdee73df36183fe3ac64747c81c26f6c83aada8d2aabb1864',
        "question_8": 'bbb965ab0c80d6538cf2184babad2a564a010376712012bd07b0af92dcd3097d',
        "question_9": 'e3d6c4d4599e00882384ca981ee287ed961fa5f3828e2adb5e9ea890ab0d0525',
        "question_10": '5ef6fdf32513aa7cd11f72beccf132b9224d33f271471fff402742887a171edf',
    }

    assert isinstance(answers, dict)
    try:
        for k in answers.keys():
            q, n = k.split("_")
            assert q == "question"
            assert 1 <= int(n) <= 10
    except AssertionError:
        raise AssertionError("Answers dict has unexpected keys")

    score = 0
    for k in expected.keys():
        if k not in answers:
            continue
        if expected[k] == hashlib.sha256(str(answers[k]+10*int(k.split('_')[1])).encode()).hexdigest():
            score += 1

    final_score = int(round(score * 5 / 10))
    if final_score == 0:
        raise AssertionError("Not enough correct answers to score points.")

    print(f"{score} / 10 correct answers. Your score is {final_score}.")
    
    return final_score
