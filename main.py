import json

    while chance<len(question)*3:
        answer=input("Enter the word :")
        f=list(answer.lower())
        sumb=0
        sumc=0
        if len(qlist) != len(f):
            print("Wrong")
            continue
        k = f
        for i in range(len(f)):
            if f[i] == qlist[i]:
                f[i] = 0
                sumb+=1

        for i in range(len(f)):
            for j in range(len(qlist)):
                if i!=j and f[i]==qlist[j]:
                    f[i] = 0
                    sumc+=1












