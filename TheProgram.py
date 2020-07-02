import psycopg2
import argparse

if __name__ == '__main__':
    # Initialize the parser
    parser = argparse.ArgumentParser()

    # Add the parameters positional/optional
    parser.add_argument('Command', help="Command to display list or insert into list")
    parser.add_argument('ThePartID', help="The part id to insert", nargs='?', default='null')
    parser.add_argument('ThePartName', help="The part name to insert", nargs='?', default='null')
    parser.add_argument('ThePartBrand', help="The part brand to insert", nargs='?', default='null')
    parser.add_argument('ThePartPrice', help="The part price to insert", nargs='?', default='null')

    # Parse the arguments
    args = parser.parse_args()

    # connect to the db
    con = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="4321"
    )

    cur = con.cursor()

    if args.Command == 'list':
        cur.execute("select part_id, part_name, brand, price from pc_parts")
        rows = cur.fetchall()

        for r in rows:
            print(f"Part_ID: {r[0]} Part_Name: {r[1]} Brand: {r[2]} Price: {r[3]}")

    if args.Command == 'add':
        the_part_id = int(args.ThePartID)
        the_part_name = args.ThePartName
        the_part_brand = args.ThePartBrand
        the_part_price = float(args.ThePartPrice)
        cur.execute("insert into pc_parts (part_id, part_name, brand, price) values (%s, %s, "
                    "%s, %s)", (the_part_id, the_part_name, the_part_brand, the_part_price))
        con.commit()

    cur.close()

    # close the connection
    con.close()
