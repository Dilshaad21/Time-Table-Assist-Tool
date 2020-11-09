def slot_allot(a,b):
    import pandas as pd
    course=pd.read_csv(a,sep=",")
    dictn=dict()
    error=dict()
    # print(course)
    for i,j in zip(course["Faculty_code"],course["Slot"]):
        try:
            a=dictn[j]
            if i in a:
                try:
                    error[j].append(i)
                except KeyError:
                    error[j]=[i]
            else:
                dictn[j].append(i)
        except KeyError:
            dictn[j]=[i]
    if len(error)!=0:
        print("Error Found")
        for i in error:
            s="Teacher "
            for j in error[i]:
                s+=j+", "
            s+="are allotted multiple courses in slot "+str(i)
        print(s)

    else:
        d=[[0 for i in range(8)] for j in range (5)]
        ind=0
        slot=list(set(course["Slot"]))
        for i in range(5):
            for j in range(len(slot)):
                d[i][(ind+j)%8]=slot[j]
            ind+=1
        for i in d:
            print(i)
        Class=pd.read_csv(b,sep=",")
        return d