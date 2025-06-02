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

def count_nodes(l):
    n_nodes = 0
    p = l.base
    while p.next_node is not None:
        p = p.next_node
        n_nodes += 1
    return n_nodes

# No picking
def exercise_7(answers):
    solution = {"question_1": '4fc82b26aecb47d2868c4efbe3581732a3e7cbcc6c2efb32062c08170a05eeb8',
                "question_2": '785f3ec7eb32f30b90cd0fcf3657d388b5ff4297f2f9716ff66e9b69c05ddd09',
                "question_3":'86e50149658661312a9e0b35558d84f6c6d3da797f552a9657fe0558ca40cdef',
                "question_4":'73475cb40a568e8da8a045ced110137e159f890ac4da883b6b17dc651b3a8049',
                "question_5":'2fca346db656187102ce806ac732e06a62df0dbb2829e511a770556d398e1a6e'}
    common_pairs = dict()
    for key in answers:
        if (key in solution and hashlib.sha256(str(answers[key]+10*int(key.split('_')[1])).encode()).hexdigest() == solution[key]):
            common_pairs[key] = answers[key]

    assert len(common_pairs)==5, "You have "+ str(5- len(common_pairs))+" incorrect answer."

    print("Answer is correct. Good Job.")


