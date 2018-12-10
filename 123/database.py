import sqlite3

conn = sqlite3.connect("food.db")
curs = conn.cursor()

#创建数据库
def create():
    # def convert(value):
    #     if value.startswith('~'):
    #         return value.strip('~')
    #     if not value:
    #         value = '0'
    #     return float(value)

    curs.execute('''
    CREATE TABLE food (
    id TEXT PRIMARY KEY,
    name TEXT,
    age FLOAT
    )
    ''')


    query1 = 'INSERT INTO food VALUES (1,"ysl1",11)'
    query2 = 'INSERT INTO food VALUES (2,"ysl2",12)'
    query3 = 'INSERT INTO food VALUES (3,"ysl3",13)'
    curs.execute(query1)
    curs.execute(query2)
    curs.execute(query3)
    conn.commit()
    # field_count = 3
    # for line in open('test.txt'):
    #     fields = line.split("^")
    #     vals = [convert(f) for f in fields[:field_count]]
    #     curs.execute(query,vals)
    #     print(vals)


    # conn.close()

#查询数据库
def select():
    #查询语句
    condition = input("请输入查询条件：")
    query = 'SELECT * FROM food %s'%condition
    # print(query)
    curs.execute(query)
    # print(curs.description)
    #names---表的字段列表
    names = [f[0] for f in curs.description]
    print(curs.fetchall())
    #rows---符合查询条件的内容列表
    for row in curs.fetchall():
        for pair in zip(names, row):
            print('{}: {}'.format(*pair))
        print()

if __name__ == '__main__':
    # create()
    select()