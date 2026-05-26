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

    
def test_project_details_():
    parent_dir = Path(__file__).resolve().parent.parent
    config_path = str(parent_dir / "pyproject.toml").replace("\\", "/")
    with open(config_path, "rb") as f:
        data = tomllib.load(f)
    tab_name_ = data["clickhouse-db"]["table_name_"]
    assert tab_name_ == "Incubyte_Assignment_Employee_Table_"


