import cx_Oracle

def create_conn():
    conn = cx_Oracle.connect("hr/hr@localhost:1521/xe")
    return conn

# 테이블 생성 함수
def create_table():
    conn = create_conn()
    c = conn.cursor()

    # sql = "CREATE SEQUENCE book_seq START WITH 1 INCREMENT BY 1"
    # c.execute(sql)

    # sql = '''
    #         create table books(
    #             book_id number not null,
    #             title varchar2(50),
    #             published_date varchar2(50),
    #             publisher varchar2(50),
    #             pages number,
    #             recommend number,
    #             CONSTRAINT pk_book PRIMARY KEY(book_id)
    #         )
    #     '''
    # c.execute(sql)
    conn.commit()

    c.close()
    conn.close()

def insert_book(item):
    conn = create_conn()
    c = conn.cursor()
    sql = "insert into books values(book_seq.NEXTVAL, :1, :2, :3, :4, :5)"
    c.execute(sql, item)
    conn.commit()

    c.close()
    conn.close()

def insert_books(items):
    conn = create_conn()
    c = conn.cursor()
    sql = "insert into books values(book_seq.NEXTVAL, :1, :2, :3, :4, :5)"
    c.executemany(sql, items)
    conn.commit()

    c.close()
    conn.close()

# 전체 데이터 가져오기
def all_books():
    conn = create_conn()
    c = conn.cursor()
    sql = "select * from books"
    c.execute(sql)
    books = c.fetchall()
    print(books)
    return books

# 한 건의 데이터 가져오기
def one_book_id(id):
    conn = create_conn()
    c = conn.cursor()
    sql = "select * from books where book_id=:id"
    c.execute(sql, id=id)
    book = c.fetchone()
    print(book)
    return book

# 조건에 따라(제목으로) 데이터 가져오기
def search_books(title):
    conn = create_conn()
    c = conn.cursor()
    sql = "select * from books where title like :1"
    title = ("%"+title+"%", )
    c.execute(sql, title)
    books = c.fetchall()
    return books

# 데이터 수정하기(제목 수정)
def update_book(title, id):
    conn = create_conn()
    c = conn.cursor()
    sql = "update books set title=:title where book_id=:id"
    c.execute(sql, title=title, id=id)
    conn.commit()
    conn.close()

def delete_book(id):
    conn = create_conn()
    c = conn.cursor()
    sql = "delete from books where book_id=:id"
    c.execute(sql, id=id)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # create_table()
    # item = ('데이터분석실무', '2020-07-13', '위키북스', 300, 15)
    # insert_book(item)

    # items = [
    #     ('빅데이터', '2020-07-17', '이지퍼블리싱', 420, 15),
    #     ('인공지능', '2020-07-15', '위키북스', 500, 25),
    #     ('Spring', '2020-06-20', '삼성', 150, 38),
    #     ('안드로이드', '2020-08-06', '세림이네', 166, 115),
    #     ('Python', '2019-12-30', '민석이네', 600, 9)
    # ]
    # insert_books(items)

    # all_books()
    
    # book = one_book_id(2)
    # print(book)

    # book = search_books('데이터')
    # print(book)

    update_book('AI', 4)