def distinct(*args):
    return len(set(args)) == len(args)


#args = 1,3,5,6,7,8
#dupargs = 1,1,3,3,5,7

#set(args) = (1,3,5,6,7,8)
#set(dupargs) = (1,3,5,7)
# len(set(args) = 6
# len(set(dupargs)) = 4
# len(args) = 6
# len(dupargs) = 6

#if len(set(args)) (6) == len(args) (6) return true
# if len(set(dupargs)) (4) == len(dupargs) (6) return false


for s in range (0,10):
    for e in range (0,10):
        for n in range (0,10):
            for d in range (0,10):
                for m in range (1,10):
                    for o in range (0,10):
                        for r in range (0,10):
                            for y in range (0,10):
                                if distinct(s,e,n,d,m,o,r,y):
                                    send = int("{}{}{}{}".format(s,e,n,d))
                                    more = int("{}{}{}{}".format(m,o,r,e))
                                    money = int("{}{}{}{}{}".format(m,o,n,e,y))
                                    if send + more == money:
                                        print("This is correct:{}+{}={}".format(send,more,money))
