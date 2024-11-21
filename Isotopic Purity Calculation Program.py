import pandas as pd
def calculate_m(a, b, c, d, e, f, m):
    cm = []
    for i in range(a,-1,-1):
        for j in range(c,-1,-1):
            for k in range(e,-1,-1):
                cm.append((i,j,k))
    mm = []
    mc = m
    for i_list in cm:
        aa,cc,ee = i_list
        m = mc - ((a-aa)*1.003354835+(c-cc)*1.006276746+(e-ee)*0.997034895)
        mm.append(m)
    mmq = [0]*len(mm)
    data = pd.DataFrame({"m/z":mm,"Intensity":mmq})
    data.to_excel('standard.xlsx', index=False)
    return cm
def repaanddel(path):
    df = pd.read_excel(path)
    stan_df = pd.read_excel("standard.xlsx")
    for i in range(len(df['m/z'])):
        for j in range(len(stan_df['m/z'])):
            error = abs(df['m/z'][i] - stan_df["m/z"][j]) / stan_df["m/z"][j]
            if error <= 5 * 10 ** -6:
                stan_df.loc[j, "m/z"] = df['m/z'][i]
                stan_df.loc[j, "Intensity"] = df['Intensity'][i]
    stan_df.to_excel('output.xlsx', index=False)
def tongji(cm,a,c,e):
    ai = []
    ci = []
    ei = []
    for l in range(a, -1, -1):
        for k, ii in enumerate(cm):
            if ii[0] == a - l:
                ai.append({"a{}".format(a - l): k}) 

    for l in range(c, -1, -1):
        for k, ii in enumerate(cm):
            if ii[1] == c - l:
                ci.append({"c{}".format(c - l): k})

    for l in range(e, -1, -1):
        for k, ii in enumerate(cm):
            if ii[2] == e - l:
                ei.append({"e{}".format(e - l): k})

    return  tongji_d(ai),tongji_d(ci),tongji_d(ei)
def tongji_d(ai):
    merged_data_key = []
    merged_data_values = []
    for d in ai:
        for key, value in d.items():
            if key not in merged_data_key:
                merged_data_key.append(key)
    for dvi in merged_data_key:
        merged_data_value = []
        for dv in ai:
            for key1, value1 in dv.items():
                if dvi == key1:
                    merged_data_value.append(value1)
        merged_data_values.append(merged_data_value)
    return merged_data_key,merged_data_values

def add_Intensity(ai):
    df = pd.read_excel("output.xlsx")
    key ,value_index_lists = ai
    In = []
    for value_index_list in value_index_lists:
        m = 0
        for value_index in value_index_list:

                m += df['Intensity'][value_index]
        In.append(m)

    return In

def kna(b, g):
    n = [i for i in range(1,b+1)]
    sn = [(b - i + 1) / i for i in n]
    tn = 1
    tn_list = []
    for i in range(len(n)):
        tn *= sn[i]
        tn_list.append(tn)
    Kn = [tn_list[i-1] * ((((100 - g) / 100) ** (b - i) )* (g / 100)** i)/(((100 - g) / 100) ** (b) ) for i in n]
    return Kn

def overaxb(In,Kn):
    a = len(In)-1
    for j in range(a):
        I_i_j = [In[j]*Kn[i] for i in range(a-j)]
        Inpart = []
        for jj in range(j+1,a+1):
            try:
                v = In[jj] - I_i_j[jj - j - 1]
                if v < 0:
                    Inpart.append(0)
                else:
                    Inpart.append(In[jj] - I_i_j[jj - j - 1])
            except IndexError as e:
                v = In[jj] - I_i_j[0]
                if v < 0:
                    Inpart.append(0)
                else:
                    Inpart.append(In[jj] - I_i_j[0])
        In = In[0:j + 1] +Inpart
    return In

def overadb(In,Kn,b):
    a = len(In)-1
    Inc=In
    for j in range(a):
        if (b+j)<a:
            I_i_j = [In[j] * Kn[i] for i in range(b)]
            Inpart = []
            for jj in range(j + 1, b+j + 1):
                try:
                    v = In[jj] - I_i_j[jj - 1]
                    if v < 0:
                        Inpart.append(0)
                    else:
                        Inpart.append(In[jj] - I_i_j[jj - 1])
                except IndexError as e:
                    v = In[jj] - I_i_j[0]
                    if v < 0:
                        Inpart.append(0)
                    else:
                        Inpart.append(In[jj] - I_i_j[0])
            In = In[0:j + 1] + Inpart
            if len(In)< len(Inc):
                In = In + Inc[len(In):]
        elif (b+j)==a:
            I_i_j = [In[j] * Kn[i] for i in range(a - j)]
            Inpart = []
            for jj in range(j + 1, a + 1):
                try:
                    v = In[jj] - I_i_j[jj - 1]
                    if v < 0:
                        Inpart.append(0)
                    else:
                        Inpart.append(In[jj] - I_i_j[jj - 1])
                except IndexError as e:
                    v = In[jj] - I_i_j[0]
                    if v < 0:
                        Inpart.append(0)
                    else:
                        Inpart.append(In[jj] - I_i_j[0])
            In = In[0:j + 1] + Inpart

        else:
            I_i_j = [In[j] * Kn[i] for i in range(a - j)]
            Inpart = []
            for jj in range(j + 1, a + 1):
                try:
                    v = In[jj] - I_i_j[jj - 1]
                    if v < 0:
                        Inpart.append(0)
                    else:
                        Inpart.append(In[jj] - I_i_j[jj - 1])
                except IndexError as e:
                    v = In[jj] - I_i_j[0]
                    if v < 0:
                        Inpart.append(0)
                    else:
                        Inpart.append(In[jj] - I_i_j[0])
            In = In[0:j + 1] + Inpart

    return In
def fengdu(In,a):
    if a==0:
        print("Not calculate")
        return
    m = 0
    n = 0
    for i in  range(len(In)):
        m+=In[i]*i
        n+=In[i]
    try:
        print(100*m/n/a)
    except ZeroDivisionError as e:
        print("In_a only has one value I0,and it is not possible to calculate the abundance using the formula！")

def fengzhuang(ai,a,b,g):
    In_a = add_Intensity(ai)
    Kn_a = kna(b, g)
    if a <= b:
        In_a = overaxb(In_a, Kn_a)
    else:
        In_a = overadb(In_a, Kn_a, b)
    fengdu(In_a, a)

def run():
    path = "data.xlsx"
    a, b, c, d, e, f, m = 6, 6, 0, 0, 0, 0, 480.9430
    cm = calculate_m(a, b, c, d, e, f, m)
    ai, ci, ei = tongji(cm, a, c, e)

    repaanddel(path)

    fengzhuang(ai,a,b,1.07)

    fengzhuang(ci,c,d,0.0115)

    fengzhuang(ei,e,f,0.368)


if __name__ == '__main__':
    run()