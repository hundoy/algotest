#!/usr/bin/python2
# -*- coding: utf-8 -*-

# min icon problem
def less_coin(candis, val):
    min_coin_rs = [0]
    min_coin_plan = [[]]
    for i in range(1, val+1):
        plan = {}
        for c in candis:
            # candi val is more than target val, skip
            if c>i: continue
            plan[c] = min_coin_rs[i-c] + 1

        min_v = min(plan.values())
        min_k = filter(lambda k: plan[k]==min_v, plan.keys())[0]
        min_coin_rs.append(min_v)
        min_coin_plan.append(min_coin_plan[i-min_k] + [str(min_k)])

    plan_str = ",".join(min_coin_plan[len(min_coin_plan)-1])
    print("for val %d, at least need coins: %d, plan is: %s" % (val, min_coin_rs[len(min_coin_rs)-1], plan_str))


for i in range(1,12):
    less_coin([1,3,5], i)






