import psycopg2

# connect to the db
con = psycopg2.connect(
            host = "localhost",
            database = "postgres",
            user = "postgres",
            password = "4321"
)


cur = con.cursor()
#uncomment below to insert a part into the db
#cur.execute("insert into pc_parts (part_id, part_name, brand, price) values (112, 'Storage', 'Dell, 49.99)")
cur.execute("select part_id, part_name, brand, price from pc_parts")

rows = cur.fetchall()

for r in rows:
    print (f"Part_ID: {r[0]} Part_Name: {r[1]} Brand: {r[2]} Price: {r[3]}")

#uncomment below to commit the change
#con.commit()

cur.close()

#close the connection
con.close()