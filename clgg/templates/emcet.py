import pandas as pd
df=pd.read_excel("AP2018.xlsx")

rank=int(input("Enter Rank:   "))
branch_code=input("Enter Barnch code:   ")
cat=input("Enter your Caste:   ")

df1=(df[(df[cat]<=rank)&(df["branch_ code"]==branch_code)])[["inst_name",cat]]
df1.sort_values([cat], ascending=[True], inplace=True)
print(df1)

['OC','BC_A','BC_B','BC_C','BC_D','BC_E',,'SC','ST']
