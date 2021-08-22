try:
    try:
        # curs.execute(sql)
        # NB : you won't get an IntegrityError when reading
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)
        # return None

    try:
        # user = curs.fetchone()[0]
        # return user
    except TypeError as e:
        print(e)
        # return None

finally:
    # conn.close()