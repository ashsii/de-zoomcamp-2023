from pathlib import Path
from prefect.filesystems import GitHub
import os
import shutil
from prefect.deployments import Deployment

script_path = os.path.realpath(os.path.dirname(__file__))
github_path = "week_2/question4"
python_flow = "etl_web_to_gcs.py"
github_block = GitHub.load("zoom-github")

if __name__ == "__main__":
    # Get data
    github_block.get_directory(from_path=Path('week_2/question4'),local_path=Path(script_path))

    # Move data to directory
    try:
        Path(f"{script_path}/{github_path}/{python_flow}").rename(f"{script_path}/{python_flow}")
    except:
        os.remove(f"{script_path}/{python_flow}")
        Path(f"{script_path}/{github_path}/{python_flow}").rename(f"{script_path}/{python_flow}")

    # Delete reduntant folder
    shutil.rmtree(f"{script_path}/week_2")

    # Import from py
    from etl_web_to_gcs import etl_web_to_gcs

    # Deploy
    deployment = Deployment.build_from_flow(
        flow=etl_web_to_gcs,
        name="github-etl-to-gcs",
        storage=github_block,
        entrypoint="week_2/question4/etl_web_to_gcs.py:etl_web_to_gcs")

    deployment.apply()
