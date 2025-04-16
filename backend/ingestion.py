from clickhouse import ClickHouseClient
from flatfile import FlatFileHandler

def ingest_clickhouse_to_flatfile(req):
    client = ClickHouseClient(**req.clickhouse_config.dict())
    data = client.read_table(req.table, req.columns)
    handler = FlatFileHandler(req.file_path, req.delimiter)
    handler.write_data(req.columns, data)
    return len(data)

def ingest_flatfile_to_clickhouse(req):
    handler = FlatFileHandler(req.file_path, req.delimiter)
    data = handler.read_data(req.columns)
    table = req.table or "uploaded_data"
    client = ClickHouseClient(**req.clickhouse_config.dict())
    client.create_table_from_schema(table, req.columns)
    client.insert_data(table, req.columns, data)
    return len(data)
