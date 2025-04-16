from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from clickhouse import ClickHouseClient
from flatfile import FlatFileHandler
from ingestion import ingest_clickhouse_to_flatfile, ingest_flatfile_to_clickhouse

app = FastAPI()

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ClickHouseConnectRequest(BaseModel):
    host: str
    port: int
    database: str
    user: str
    jwt_token: str

class FlatFileSchemaRequest(BaseModel):
    file_path: str
    delimiter: str = ","

class IngestionRequest(BaseModel):
    source: str
    target: str
    table: Optional[str]
    columns: List[str]
    file_path: Optional[str]
    delimiter: Optional[str]
    clickhouse_config: Optional[ClickHouseConnectRequest]

@app.post("/connect/clickhouse")
def connect_clickhouse(config: ClickHouseConnectRequest):
    try:
        client = ClickHouseClient(**config.dict())
        tables = client.get_tables()
        return {"status": "connected", "tables": tables}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/schema/clickhouse")
def get_clickhouse_columns(config: ClickHouseConnectRequest, table: str):
    try:
        client = ClickHouseClient(**config.dict())
        columns = client.get_columns(table)
        return {"columns": columns}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/schema/flatfile")
def get_flatfile_schema(data: FlatFileSchemaRequest):
    try:
        handler = FlatFileHandler(data.file_path, data.delimiter)
        columns = handler.get_columns()
        return {"columns": columns}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/ingest")
def ingest_data(req: IngestionRequest):
    try:
        if req.source == "ClickHouse" and req.target == "FlatFile":
            record_count = ingest_clickhouse_to_flatfile(req)
        elif req.source == "FlatFile" and req.target == "ClickHouse":
            record_count = ingest_flatfile_to_clickhouse(req)
        else:
            raise HTTPException(status_code=400, detail="Invalid ingestion direction.")
        return {"status": "success", "records_processed": record_count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
