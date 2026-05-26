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


def test_db_available():
    parent_dir = Path(__file__).resolve().parent.parent
    config_path = str(parent_dir / "pyproject.toml").replace("\\", "/")
    with open(config_path, "rb") as f:
        data = tomllib.load(f)
    tab_name_ = data["clickhouse-db"]["table_name_"]
    from db_utils_ import db_commands_ as db_commands_
    from db_utils_ .import_data_from_clickhouse_ import clickhouse_client_ as clickhouse_client_
    a_client_ = clickhouse_client_()
    check_table_ = a_client_.command(db_commands_.check_table(table_name_=tab_name_))
    assert check_table_ == 1

if __name__ == "__main__":
    test_db_available()