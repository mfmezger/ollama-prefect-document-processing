from prefect import task
from pathlib import Path


@task
def read_data(directory: str = "data", amount: int = 5) -> list:
    files = sorted(Path(directory).glob("*.pdf"))

    return files[:amount]


@task
def load_data():
    pass


@task
def extract_data():
    pass


@task
def save_results():
    pass


@task
def cleanup():
    pass


def main_flow(directory: str = "data"):
    file_names = read_data(directory=directory)
    print(file_names)


if __name__ == "__main__":
    main_flow()

    # main_flow.serve()
