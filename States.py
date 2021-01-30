def distinct(*args):
    return len(set(args)) == len(args)

for h in range (1,10):
    for a in range (0,10):
        for w in range (0,10):
            for i in range (0,10):
                for d in range (0,10):
                    for o in range (0,10):
                        for s in range (1,10):
                            for t in range (0,10):
                                for e in range (0,10):
                                    if distinct(h, a, w, i, d, o, s, t, e):
                                        hawaii = int("{}{}{}{}{}{}".format(h, a, w, a, i, i))
                                        idaho = int("{}{}{}{}{}".format(i, d, a, h, o))
                                        iowa = int("{}{}{}{}".format(i, o, w, a))
                                        ohio = int("{}{}{}{}".format(o, h, i, o))
                                        states = int("{}{}{}{}{}{}".format(s, t, a, t, e, s))
                                        if hawaii + idaho + iowa + ohio == states:
                                            print("This is correct: {}+{}+{}+{}={}".format(hawaii, idaho, iowa, ohio, states))
