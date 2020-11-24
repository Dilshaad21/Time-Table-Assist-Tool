def recur(arr,ind,s_ind,p,n,sem_list,co_list,cse_list,ee_list,me_list,ce_list,course_fac,fac_slot,z):
    if(ind>=n):
        return 1
    arr1=[[list() for i in range(4)] for j in range(8)]
    if(sem_list[ind]==p):
        for i in range(8):
            for j in range(4):
                arr1[i][j]=arr[i][j].copy()
        arr1[0][0].append(1)
    else:
        p=sem_list[ind]
    flag=0
    for i in range(s_ind,s_ind+8):
        i%=8
        if cse_list[ind] not in arr1[i][0] and ee_list[ind] not in arr1[i][1] and me_list[ind] not in arr1[i][2] and ce_list[ind] not in arr1[i][3]:
            if i not in fac_slot[course_fac[co_list[ind]]]:
                fac_slot[course_fac[co_list[ind]]].append(i)
                arr1[i][0].append(cse_list[ind])
                arr1[i][1].append(ee_list[ind])
                arr1[i][2].append(me_list[ind])
                arr1[i][3].append(ce_list[ind])
                re=recur(arr1,ind+1,i+1,p,n,sem_list,co_list,cse_list,ee_list,me_list,ce_list,course_fac,fac_slot,z)
                if(re==1):
                    #fac_slot[course_fac[co_list[ind]]].append(i)
                    z[i].append(co_list[ind])
                    
                    flag=1
                    return 1
                else:
                    fac_slot[course_fac[co_list[ind]]].pop()
                    arr1[i][0].pop()
                    arr1[i][1].pop()
                    arr1[i][2].pop()
                    arr1[i][3].pop()
        if(flag):
            return 1
    return 0
                    
def slot_allot(f1,f2,f3):
    import pandas as pd                     
    df=f2
    df1=f3
    course_fac=dict()
    cou_stre=dict()
    fac_slot=dict()  #
    n=len(df)
    sem_list=list(df['Semester'])
    co_list=list(df['Course No.'])
    cse_list=list(df['For CSE'])
    ee_list=list(df['For EE'])
    me_list=list(df['For ME'])
    ce_list=list(df['For CE'])
    for i,j in zip(df1['Course No.'],df1['Instructor']):
        course_fac[i]=j
        fac_slot[j]=[]
    for i,j in zip(df1['Course No.'],df1['Strength']):
        cou_stre[i]=j
    
        
    slot_tmp=[[list() for i in range(4)] for j in range(8)]
    z=[[] for j in range(8)]
    recur(slot_tmp,0,0,1,n,sem_list,co_list,cse_list,ee_list,me_list,ce_list,course_fac,fac_slot,z)
    
    d=[[0 for i in range(8)] for j in range (5)]  # time table 2d array
    ind=0
    slot=[i for i in range(0,8)]
    for i in range(5):
        for j in range(len(slot)):
            d[i][(ind+j)%8]=slot[j]
        ind+=1
    for i in d: # printing time table
        print(i)
    df=f1
    final_df = df.sort_values(by=['Capacity'], ascending=False)
    final_df=list(final_df['Class'])
    ditn=dict()
    for i in z:
        li=[]
        for j in i:
            li.append([cou_stre[j],j])
        li.sort(reverse=True)
        co=0
        for j in li:
            ditn[j[1]]=final_df[co]
            co+=1
            
        
    return [d,z,ditn]