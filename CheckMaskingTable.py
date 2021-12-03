DB_USER = "postgres"
DB_PASS = "1234"
DB_NAME = "masking_test"
DB_HOST = "192.168.1.244"
DB_HOST_P = "192.168.10.108"
DB_PORT = "5436"
DB_PORT_P = "5433"

import psycopg2
def CheckMasking():
    try:
        con_base = psycopg2.connect(user=DB_USER,
                                    password=DB_PASS,
                                    host=DB_HOST,
                                    port=DB_PORT,
                                    database=DB_NAME)
        print("Database opened successfully")

        con_proxy = psycopg2.connect(user=DB_USER,
                                     password=DB_PASS,
                                     host=DB_HOST_P,
                                     port=DB_PORT_P,
                                     database=DB_NAME)
        print("Database opened with proxy successfully")


        cur_proxy = con_proxy.cursor()
        cur_base = con_base.cursor()

        cur_proxy.execute("SELECT * FROM public.mock_data;")
        cur_base.execute("SELECT * FROM public.mock_data;")

        rows_proxy = cur_proxy.fetchall()
        rows_base = cur_base.fetchall()
        result = 0
        for row in range(len(rows_base)):
            for col in range(len(rows_base[row])):
                if (rows_base[row][col] != rows_proxy[row][col] and (col == 1 or col == 2)):
                    if (rows_base[row][col][2::] == rows_proxy[row][col][2::] and rows_proxy[row][col][:2] == '**'):
                        result = 10


        return (result)

    except:
        return (-1)