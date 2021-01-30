def distinct (*args):
    return len(set(args)) == len(args)

for i in range (1,10):
    for l in range (1,10):
        for o in range (0,10):
            for v in range (0,10):
                for e in range (0,10):
                    for y in range (1,10):
                        for u in range (0,10):
                            for d in range (1,10):
                                for r in range (0,10):
                                    for a in range (0,10):
                                        if distinct(i, l, o, v, e, y, u, d, r, a):
                                            i = int("{}".format(i))
                                            love = int("{}{}{}{}".format(l, o, v, e))
                                            you = int("{}{}{}".format(y, o, u))
                                            dora = int("{}{}{}{}".format(d, o, r, a))
                                            if i + love + you == dora:
                                                print("This is correct: {}+{}+{}={}".format(i, love, you, dora))