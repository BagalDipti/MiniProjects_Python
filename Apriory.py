#---------Apriory Algorithm--------------------------------------------------------------------------------------

dataset=[['Milk','Onion','Nutmeg','Kidney Beans','Eggs','Yogurt'],
         ['Dill','Onion','Nutmeg','Kidney Beans','Eggs','Yogurt'],
         ['Milk','Apple','Kidney Beans','Eggs'],
         ['Milk','unicorn','corn','Kideny Beans','Yogurt'],
         ['corn','onoin','onion','kideny Beans','Ice cream','Eggs']]
from tkinter import *

window = Tk()

window.title("Apriory Algorithm")

lbl1 = Label(window, text="Support count", font=("Arial Bold",40))

lbl1.grid(column=0, row=0)

et1=Entry(window,text="")

et1.grid(column=2,row=0)

lbl2 = Label(window, text="Confidance", font=("Arial Bold",40))

lbl2.grid(column=0, row=2)

et2=Entry(window,text="")

et2.grid(column=2,row=2)


import pandas as pd

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori,association_rules

def abc():

    te=TransactionEncoder()
    te_ary=te.fit(dataset).transform(dataset)
    df=pd.DataFrame(te_ary,columns=te.columns_)
    print(df)


    print(apriori(df,min_support=0.6))

    print(apriori(df,min_support=0.6,use_colnames=True))


    frequent_itemset=apriori(df,min_support=0.6,use_colnames=True)
    def retrieve_input():
        inputValue=et1.get("1.0",END)
        print(inputValue)
    frequent_itemset['length']=frequent_itemset['itemsets'].apply(lambda x: len(x))
    print(frequent_itemset)

    print(frequent_itemset[(frequent_itemset['length']==2)&(frequent_itemset['support']>=0.8)])

    rules=association_rules(frequent_itemset,metric='confidence',min_threshold=0.7)

    print(rules)


btn1=Button(window,text="Show frequent item set",command=abc)

btn1.grid(column=1,row=6)

btn2=Button(window,text="Strong rule",command=abc)

btn2.grid(column=1,row=7)


window.mainloop()