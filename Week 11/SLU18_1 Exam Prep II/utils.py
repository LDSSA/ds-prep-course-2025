import math
import sys
import hashlib

#ipython = get_ipython()


#def hide_traceback(exc_tuple=None, filename=None, tb_offset=None,
#                   exception_only=False, running_compiled_code=False):
#    etype, value, tb = sys.exc_info()
#    return ipython._showtraceback(etype, value, ipython.InteractiveTB.get_exception_only(etype, value))


# Uncomment after tests
#ipython.showtraceback = hide_traceback


# No picking
    
def exercise_6(answers):

    solution = {"question_1": '8527a891e224136950ff32ca212b45bc93f69fbb801c3b1ebedac52775f99e61', 
                "question_2": '535fa30d7e25dd8a49f1536779734ec8286108d115da5045d77f3b4185d8f790',
                "question_3":'e29c9c180c6279b0b02abd6a1801c7c04082cf486ec027aa13515e4f3884bb6b',
                "question_4":'44cb730c420480a0477b505ae68af508fb90f96cf0ec54c6ad16949dd427f13a',
                "question_5":'41cfc0d1f2d127b04555b7246d84019b4d27710a3f3aff6e7764375b1e06e05d'}
    
    
    common_pairs = dict()
    for key in answers:
        if (key in solution and hashlib.sha256(str(answers[key]+10*int(key.split('_')[1])).encode()).hexdigest() == solution[key]):
            common_pairs[key] = answers[key]

#    assert len(common_pairs)==5, "You have "+ str(5- len(common_pairs))+" incorrect answer. The answers you were correct are: \n"+str((common_pairs))
    assert len(common_pairs)==5, "You have "+ str(5- len(common_pairs))+" incorrect answer(s)."

    print("Answer is correct. Good Job.")


