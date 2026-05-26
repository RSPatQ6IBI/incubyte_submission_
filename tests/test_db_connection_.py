import sys
import os
### ------ ADDING THE PROJECT DIRECTORIES TO THE PATH
from pathlib import Path
import tomllib
parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))
for root, dirs, files in os.walk(parent_dir):
    for d in dirs:
        sys.path.append(os.path.join(root, d))

    
def test_db_connection_():
    parent_dir = Path(__file__).resolve().parent.parent
    config_path = str(parent_dir / "pyproject.toml").replace("\\", "/")
    with open(config_path, "rb") as f:
        data = tomllib.load(f)
    tab_name_ = data["clickhouse-db"]["table_name_"]
    from db_utils_.import_data_from_clickhouse_ import get_clickhouse_client_ as get_client_ 
    the_clickhouse_client_ = get_client_()
    assert type(the_clickhouse_client_) == "<class 'clickhouse_connect.driver.httpclient.HttpClient'>"  
    


def test_db_communication_():
    parent_dir = Path(__file__).resolve().parent.parent
    config_path = str(parent_dir / "pyproject.toml").replace("\\", "/")
    with open(config_path, "rb") as f:
        data = tomllib.load(f)
    tab_name_ = data["clickhouse-db"]["table_name_"]
    from db_utils_.import_data_from_clickhouse_ import fetch_all_rows_ as fetch_rows_
    from db_utils_ import db_commands_ as db_commands_
    from db_utils_ .import_data_from_clickhouse_ import clickhouse_client_ as clickhouse_client_
    a_client_ = clickhouse_client_()
    fetch_data_query_ = db_commands_.fetch_all_entries_from_table(table_name_=tab_name_)
    tab_result = a_client_.query_df(fetch_data_query_)
    assert len(tab_result) == 10000
