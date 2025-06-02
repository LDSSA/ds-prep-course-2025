import math
import sys
import hashlib

ipython = get_ipython()


def hide_traceback(exc_tuple=None, filename=None, tb_offset=None,
                   exception_only=False, running_compiled_code=False):
    etype, value, tb = sys.exc_info()
    return ipython._showtraceback(etype, value, ipython.InteractiveTB.get_exception_only(etype, value))


# Uncomment after tests
ipython.showtraceback = hide_traceback


# No picking
def exercise_1(answers):
    
    solution = {"question_1": '3fdba35f04dc8c462986c992bcf875546257113072a909c162f7e470e581e278',
                "question_2": '535fa30d7e25dd8a49f1536779734ec8286108d115da5045d77f3b4185d8f790',
                "question_3": 'e29c9c180c6279b0b02abd6a1801c7c04082cf486ec027aa13515e4f3884bb6b',
                "question_4": '71ee45a3c0db9a9865f7313dd3372cf60dca6479d46261f3542eb9346e4a04d6',
                "question_5": '031b4af5197ec30a926f48cf40e11a7dbc470048a21e4003b7a3c07c5dab1baa',
                "question_6": 'd029fa3a95e174a19934857f535eb9427d967218a36ea014b70ad704bc6c8d1c',
                "question_7": 'eb624dbe56eb6620ae62080c10a273cab73ae8eca98ab17b731446a31c79393a',
                "question_8": 'a46e37632fa6ca51a13fe39a567b3c23b28c2f47d8af6be9bd63e030e214ba38',
                "question_9": '8241649609f88ccd2a0a5b233a07a538ec313ff6adf695aa44a969dbca39f67d',
                "question_10": '16dc368a89b428b2485484313ba67a3912ca03f2b2b42429174a4f8b3dc84e44',
                "question_11": 'b1556dea32e9d0cdbfed038fd7787275775ea40939c146a64e205bcb349ad02f',
                "question_12": 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',
                "question_13": '5d389f5e2e34c6b0bad96581c22cee0be36dcf627cd73af4d4cccacd9ef40cc3',
                "question_14": '2c7d5490e6050836f8f2f0d496b1c8d6a38d4ffac2b898e6e77751bdcd20ebf5'}
    common_pairs = dict()
    for key in answers:
        if (key in solution and hashlib.sha256(str(answers[key]+10*int(key.split('_')[1])).encode()).hexdigest() == solution[key]):
            common_pairs[key] = answers[key]

    assert len(common_pairs)==14, "You have "+ str(14- len(common_pairs))+" incorrect answer(s)."

    print("Answer is correct. Good Job.")


