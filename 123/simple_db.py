import sys,shelve
def store_persion(db):
    """让用户输入数据存储到shelf对象中"""
    pid = input("Enter unique ID number:")
    persion = {}
    persion['name'] = input("Enter name:")
    persion['age'] = input("Enter age:")
    persion['phone'] = input("Enter phone:")
    db[pid] = persion

def lookup_persion(db):
    """让用户输入ID，以及所需要的字段，并从shelf对象中获取数据"""
    pid = input("Enter ID number:")
    field = input("Would you like to know? (name,age,phone)")
    field = field.strip().lower()
    print(field.capitalize() + ":",db[pid][field])

def enter_command():
    cmd = input("Enter command:")
    cmd = cmd.strip().lower()
    return cmd

def mian():
    database = shelve.open(r'E:\AutoTest-4\database.dat')
    try:
        while True:
            cmd = enter_command()
            if cmd == "store":
                store_persion(database)
            elif cmd == "look":
                lookup_persion(database)
            elif cmd == "quit":
                return

    finally:
        database.close()

if __name__ == '__main__':
    mian()

