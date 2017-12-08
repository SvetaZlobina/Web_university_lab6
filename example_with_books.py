import MySQLdb

db = MySQLdb.connect(
    host='localhost',
    user='FlowerLight_admin',
    passwd='admin',
    db='FlowerLight_db',
    charset='utf8'
)

c = db.cursor()

# c.execute('INSERT INTO main_app_product(name, price, description, image, type) VALUES (%s, %s, %s, %s, %s);',
#           ('Лилии', 100.00, 'Цветы белой лилии свежесрезанные для букета', 'img/default_flower_image.png', 1))
# db.commit()

c.execute('SELECT * FROM main_app_product;')
rows = c.fetchall()

for r in rows:
    print(r)

c.close()
db.close()
