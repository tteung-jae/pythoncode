import pymysql

def create_conn():
    conn = pymysql.connect(host='localhost',
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8')
    return conn
# 테이블 생성
def create_table():
    conn = create_conn()
    c = conn.cursor()
    sql = '''
            create table if not exists books(
                book_id integer
                    NOT NULL AUTO_INCREMENT PRIMARY KEY,
                title text,
                published_date text,
                publisher text,
                pages integer,
                recommend integer)DEFAULT CHARSET=utf8;
            )'''
    c.execute(sql)
    conn.commit()
    c.close()
def insert_book(item):
    conn = create_conn()
    c = conn.cursor()
    sql = 'insert into books(title,published_date,publisher,pages,recommend) values(%s,%s,%s,%s,%s)'
    c.execute(sql, item)
    conn.commit()
    c.close()
    conn.close()
def insert_books(items):
    conn = create_conn()
    c = conn.cursor()
    sql = 'insert into books(title,published_date,publisher,pages,recommend) values(%s,%s,%s,%s,%s)'
    c.executemany(sql, items)
    conn.commit()
    c.close()
    conn.close()
def all_books():
    conn = create_conn()
    c = conn.cursor()
    sql = 'select * from books'
    c.execute(sql)
    books = c.fetchall()
    print(books)
    return books
def one_book(title):
    conn = create_conn()
    c = conn.cursor()
    sql = "select * from books where title=%s"
    c.execute(sql, title)
    book = c.fetchone()
    return book
def one_book_id(id):
    conn = create_conn()
    c = conn.cursor()
    sql = "select * from books where rowid=%s"
    c.execute(sql, id)
    book = c.fetchone()
    return book
def select_book(title):
    conn = create_conn()
    c = conn.cursor()
    sql = "select * from books where title like %s"
    title = "%"+title+"%"
    c.execute(sql, (title,))
    book = c.fetchone()
    return book
def update_title(data):
    conn = create_conn()
    c = conn.cursor()
    sql = '''update books
            set title = %s where book_id=%s'''
    c.execute(sql, data)
    conn.commit()
    conn.close()
def delete_book(id):
    conn = create_conn()
    c = conn.cursor()
    sql = 'delete from books where book_id=%s'
    c.execute(sql, id)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    dbo = mariadb_book()
    dbo.create_table()
    item = ('2020-07-13', 'SELL', 'RHAT', 100.0, 85.00)
    dbo.insert_book(item)
    items = [
        ('2020-07-09', 'BUY', 'IBM', 1000, 45.00),
        ('2020-07-10', 'SELL', 'MSFT', 500, 72.00),
        ('2020-07-11', 'BUY', 'IBM', 800, 53.00),
        ('2020-07-12', 'SELL', 'RHAT', 100.0, 90.00)
    ]
    dbo.insert_books(items)

    dbo.all_books()
    book = dbo.one_book(('RHAT',))
    print(book)

    book = dbo.one_book_id((2,))
    print(book)

    book = dbo.select_book('I')
    print(book)
