import pymysql.cursors

c = pymysql.connect(

    host='localhost', 

    port=3307, 

    user='root', 

    password='123456', 

    db='library', 

    cursorclass=pymysql.cursors.DictCursor
    )
with c.cursor() as mycursor:

   while True:
        name = input("Book name")
        genre = input("Genre")
        price = input("Type price of book")
        publisher = input ("Publisher")
        pages = input("Pages")


        mycursor.execute("INSERT INTO books1 (name, genre, price, publisher, pages) values(%s, %s, %s, %s, %s)", [name, genre, price, publisher, pages])

        

        c.commit()

