from prefect import task


@task
def read_data():
    pass


@task
def clean_data():
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


def main_flow():
    pass


if __name__ == "__main__":
    main_flow()

    # main_flow.serve()
