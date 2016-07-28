def sort_Stack(st):
    temp=[]
    while st:
        cur=st.pop()
        if temp:
            if temp[-1]<=cur:
                temp.append(cur)
            else:
                while temp and cur>temp[-1]:
                    el=temp.pop()
                    st.append(el)
                temp.append(cur)

        else:
            temp.append(cur)