import mysql.connector as MySQL
dbcon = MySQL.connect(
    host="mysql", 
    user="root", 
    password="password", 
    db = "excel_db"
    )
cursor = dbcon.cursor()
if(dbcon):
    # sql = ""
    pass
    print("connected")
import pandas as pd
real = pd.read_excel("apos.xlsx", index_col=0)
dfs = pd.DataFrame(real)
for df in range(len(dfs)):
    rowses = dfs.iloc[df]
    pdtname = rowses[0]
    price = rowses[1]
    pdcost = rowses[2]
    pid = df + 1
    rowtuple = tuple(rowses.to_list())
    print(pid)
    sql = f"""insert into `sheet_tab` values (%s, %s, %s, %s)"""
    cursor.execute(sql, (pid, pdtname, price, pdcost,))
    # cursor.execute(sql, rowtuple)
    dbcon.commit()
    # if(dbcon.commit()):
    #     print("data inserted")
    # print(pdtname)
    # print(price)
    # print(pdcost)
    # for rowse in range(len(rowses)):
    #     print(type(rowses.iloc[rowse]))
    # print(dfs.iloc[df])
# print(len(dfs))
# print(dfs.iloc)
# sql = pd.DataFrame.to_sql(name=real, con=cursor)
# cursor.commit()
# print(real)
# print(df)
# print(sql)