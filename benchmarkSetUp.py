import time
import psycopg2
import redis
import random


def setup_postgres():
    conn = psycopg2.connect(
        dbname='testdb',
        user='james',
        host='localhost',
        port=5432
    )

    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS test_table;")
    cur.execute(
        "CREATE TABLE test_table (id SERIAL PRIMARY KEY, value INTEGER);")

    print("Inserting 1'000'000 rows into PostgreSQL...")
    start_time = time.time()
    for _ in range(1000000):

        if _ % 100000 == 0:
            print(f"Inserted {_} rows")

        cur.execute("INSERT INTO test_table (value) VALUES (%s);",
                    (random.randint(1, 1000000),))
    conn.commit()
    print(f"PostgreSQL insert completed in {
          time.time() - start_time:.2f} seconds.")

    cur.close()
    conn.close()


def setup_redis():
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.flushdb()
    print("Inserting 1'000'000 elements into Redis...")
    start_time = time.time()
    for i in range(1, 1000000):

        if i % 100000 == 0:
            print(f"Inserted {i} rows")

        r.set(f"key:{i}", random.randint(1, 100000))
    print(f"Redis insert completed in {time.time() - start_time:.2f} seconds.")


if __name__ == "__main__":
    setup_postgres()
    setup_redis()
