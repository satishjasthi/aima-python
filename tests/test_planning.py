from planning import *
from utils import expr
from logic import FolKB

def test_action():
    precond = [[expr("P(x)"), expr("Q(y, z)")]
               ,[expr("Q(x)")]]
    effect = [[expr("Q(x)")]
              , [expr("P(x)")]]
    a=Action(expr("A(x,y,z)"),precond, effect)
    args = [expr("A"), expr("B"), expr("C")]
    assert a.substitute(expr("P(x, z, y)"), args) == expr("P(A, C, B)")
    test_kb = FolKB([expr("P(A)"), expr("Q(B, C)"), expr("R(D)")])
    assert a.check_precond(test_kb, args)
    a.act(test_kb, args)
    assert test_kb.ask(expr("P(A)")) is False
    assert test_kb.ask(expr("Q(A)")) is not False
    assert test_kb.ask(expr("Q(B, C)")) is not False
    assert not a.check_precond(test_kb, args)

def test_air_cargo():
    p = air_cargo()
    assert p.goal_test() is False
    solution =[expr("Load(C1 , P1, SFO)"),
               expr("Fly(P1, SFO, JFK)"),
               expr("Unload(C1, P1, JFK)"),
               expr("Load(C2, P2, JFK)"),
               expr("Fly(P2, JFK, SFO)"),
               expr("Unload (C2, P2, SFO)")]

    for action in solution:
        p.act(action)

    assert p.goal_test()
