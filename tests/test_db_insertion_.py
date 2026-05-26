import sys
import os
import pandas as pd
### ------ ADDING THE PROJECT DIRECTORIES TO THE PATH
from pathlib import Path
import tomllib
parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))
for root, dirs, files in os.walk(parent_dir):
    for d in dirs:
        sys.path.append(os.path.join(root, d))

def test_insertion_command_():
    parent_dir = Path(__file__).resolve().parent.parent
    config_path = str(parent_dir / "pyproject.toml").replace("\\", "/")
    with open(config_path, "rb") as f:
        data = tomllib.load(f)
    tab_name_ = data["clickhouse-db"]["table_name_"]
    table_cols_ = data["clickhouse-db"]["table_columns_"]   # Nested entries (tables)
    from db_utils_.import_data_from_clickhouse_ import fetch_all_rows_ as fetch_rows_
    from db_utils_ import db_commands_ as db_commands_
    from db_utils_ .import_data_from_clickhouse_ import clickhouse_client_ as clickhouse_client_
    a_client_ = clickhouse_client_()
    temp_df_ = pd.DataFrame({
        "first_names": "Sarah",
        "last_names": "Miller",
        "gross_sal": 85000,
        "emp_locs": "New York",
        "emp_timezone": "UTC + 2"
    }, index=[0])
    a_client_.insert_df(table=tab_name_, df=temp_df_, column_names=table_cols_)
    fetch_data_query_ = db_commands_.fetch_all_entries_from_table(table_name_=tab_name_)
    tab_result = a_client_.query_df(fetch_data_query_)
    the_first_name_ = tab_result.iat[0,0]
    the_last_name_ = tab_result.iat[0,1]
    assert the_first_name_ == "Sarah"
    assert the_last_name_ == "Miller"
    

if __name__ == "__main__":
    test_insertion_command_()