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
    ping_val_ = the_clickhouse_client_.ping()
    assert tab_name_ == "Incubyte_Assignment_Employee_Table_"
    assert ping_val_ == True

if __name__ == "__main__":
    test_db_connection_()

