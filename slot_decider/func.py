def slot_allot(a,b):
    import pandas as pd                     # pandas for reading csv file
    course=pd.read_csv(a,sep=",")           #readed csv data
    dictn=dict()                            #required dictionary for algorithm
    error=dict()                            #required dictionary for algorithm
    # print(course)
    #algorithm follows
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
    # if error found- more than 1 course of a particular in 1 slot
    if len(error)!=0:
        print("Error Found")
        for i in error:
            s="Teacher "
            for j in error[i]:
                s+=j+", "
            s+="are allotted multiple courses in slot "+str(i)
        print(s)  # printing the error

    else:
        d=[[0 for i in range(8)] for j in range (5)]  # time table 2d array
        ind=0
        slot=list(set(course["Slot"]))
        for i in range(5):
            for j in range(len(slot)):
                d[i][(ind+j)%8]=slot[j]
            ind+=1
        for i in d: # printing time table
            print(i)
        Class=pd.read_csv(b,sep=",")
        return d