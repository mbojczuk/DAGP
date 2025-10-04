import argparse
from trino.dbapi import connect
import json
import os

DEFAULT_HOST = os.environ.get("TRINO_HOST", "localhost")
DEFAULT_PORT = int(os.environ.get("TRINO_PORT", 8080))
DEFAULT_CATALOG = os.environ.get("TRINO_CATALOG", "memory")
DEFAULT_SCHEMA = os.environ.get("TRINO_SCHEMA", "default")

def query_one_row(sql: str, host=DEFAULT_HOST, port=DEFAULT_PORT,
                  catalog=DEFAULT_CATALOG, schema=DEFAULT_SCHEMA, user="tester"):
    conn = connect(host=host, port=port, catalog=catalog, schema=schema, user=user)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true", help="Run a smoke query")
    args = parser.parse_args()
    if args.smoke:
        # A safe lightweight query that works with Trino memory connector or most test setups
        sql = "SELECT 1 as one"
        rows = query_one_row(sql)
        print(json.dumps({"rows": rows}))
        return 0

if __name__ == "__main__":
    main()