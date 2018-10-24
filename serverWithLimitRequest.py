# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math
import collections

def solution(A, Y):
    # write your code in Python 3.6
    # A: list of input ex.['java 0', 'python 15']
    # Y: limit of requests / min
    # t = 0 (mod 60)
    result = []
    tmpName = 'nullNameNoMeaning'
    request = 0     # count requests for each user
    nameDic = {}    # store users successful requests
    timeDiv = -1    # for distinguishing mins
    tmpTime = -1
    couPerMin = 0   # for excluding overwhelm request

    ifBlack = False # blacklist happen
    blackTime = 0   # timestamp when balcklist happen
    divReq = {}     # dict to store requests in each time division
    fiveSum = 0

    # i[0]: name, i[1]: timestamp
    for i in A:
        i = i.split()
        timeDiv = math.floor(int(i[1]) / 60)
        # if requests > 10 from one user in 5 mins -> backlist
        if fiveSum > 10:
            ifBlack == True

        # back to normal request mode
        if timeDiv > blackTime + 2:
            ifBlack == False

        # Blacklist
        if ifBlack:
            blackTime = i[1] / 60
            # stop all the clients for next 2 mins if backlist
            if timeDiv <= blackTime + 2:
                continue

        # normal request mode
        else:
            if timeDiv == tmpTime:
                couPerMin += 1
            else:
                couPerMin = 1
            tmpTime = timeDiv

            # requests from the same user
            if i[0] == tmpName:
                # ignore if request > limiation per min
                if couPerMin > Y:
                    continue
                request += 1
                nameDic[tmpName] += 1

                # record requests in each min
                divReq.setdefault(timeDiv, 0)
                divReq[timeDiv] += 1
                od = collections.OrderedDict(sorted(divReq.items(), reverse=True))

                if len(od) < 5:
                    for m, n in od.items():
                        fiveSum += n
                else:
                    for m, n in od[:5]:
                        fiveSum += n

            # requests from the new user
            else:
                request = 1
                nameDic[i[0]] = 1
                tmpName = i[0]

                # record requests in each min
                divReq.setdefault(timeDiv, 0)
                divReq[timeDiv] += 1
                od = collections.OrderedDict(sorted(divReq.items()))

    for k, v in nameDic.items():
        result.append('{0} {1}'.format(k,v))

    return result


    # pass

# test
# solution(['java 0', 'java 70', 'python 15'], 3)
