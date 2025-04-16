from clickhouse_connect import get_client

class ClickHouseClient:
    def __init__(self, host, port, database, user, jwt_token):
        self.client = get_client(
            host=host,
            port=port,
            username=user,
            password=jwt_token,
            database=database
        )

    def get_tables(self):
        return self.client.query("SHOW TABLES").result_rows

    def get_columns(self, table):
        query = f"DESCRIBE TABLE {table}"
        return [row[0] for row in self.client.query(query).result_rows]

    def read_table(self, table, columns):
        col_str = ", ".join(columns)
        query = f"SELECT {col_str} FROM {table}"
        return self.client.query(query).result_rows

    def create_table_from_schema(self, table, columns):
        column_def = ", ".join(f"{col} String" for col in columns)
        query = f"CREATE TABLE IF NOT EXISTS {table} ({column_def}) ENGINE = MergeTree() ORDER BY tuple()"
        self.client.command(query)

    def insert_data(self, table, columns, data):
        self.client.insert(table, data, column_names=columns)
