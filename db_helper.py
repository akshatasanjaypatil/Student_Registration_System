
def create_table(db, table_name, **columns):
    cur = db.cursor()
    q_str = ''
    for c, t in columns.items():
        q_str += '{} {}, '.format(c, t)
    q_str = q_str[:-2]
    cur.execute('create table if not exists ' + table_name + '(' + q_str + ')')

def select(db, table_name, column , goal , *constraints):
    cur = db.cursor()
    cur.execute("SELECT "+column+" FROM "+table_name+" where "+goal+"=?", (tuple(constraints)))
    results = []
    while True:
        result = cur.fetchone()
        if not result:
            break
        results.append(result)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    return results

def select_pattern(db, table_name, goal , pattern):
    cur = db.cursor()
    cur.execute("SELECT * FROM "+table_name+" where "+goal+" like '" + pattern +"%'")
    results = []
    while True:
        result = cur.fetchone()
        if not result:
            break
        results.append(result)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    return results

def update(db, table_name, column , goal , *constraints):
    cur = db.cursor()
    cur.execute("UPDATE "+table_name+ " SET "+column+ "=? " +"where "+goal+"=?", (tuple(constraints)))

def select_all(db, table_name):
    cur = db.cursor()
    cur.execute("SELECT * FROM "+table_name)
    results = []
    while True:
        result = cur.fetchone()
        if not result:
            break
        results.append(result)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    return results

def insert(db, table_name,*constraints):
    cur = db.cursor()
    queMarkString = ""
    for _ in list(constraints):
        queMarkString += "?," 
    cur.execute("INSERT INTO "+table_name+" values (" + queMarkString[:-1] + ")", (tuple(constraints)))
    

def delete(db, table_name , goal , *constraint):
    cur = db.cursor()
    cur.execute("delete FROM "+table_name+" where "+goal+"=?", (tuple(constraint)))
    


  