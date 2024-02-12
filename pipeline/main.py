from prefect import task, flow
from pathlib import Path
import pypdfium2 as pdfium

@task
def read_data(directory: str = "data", amount: int = 5) -> list[Path]:
    """Find out how many files are in the directory and return the first `amount` of them."""
    files = sorted(Path(directory).glob("*.pdf"))
    return files[:amount]


def load_and_clean(pdf_path: Path):
    try:

        pdf_reader = pypdfium2.PdfDocument(pdf_path, autoclose=True)
        try:
            for page_number, page in enumerate(pdf_reader):
                text_page = page.get_textpage()
                content = text_page.get_text_range()
                text_page.close()
                content += "\n" + self._extract_images_from_page(page)
                page.close()
                metadata = {"page": page_number}
                yield Document(page_content=content, metadata=metadata)
        finally:
            pdf_reader.close()
    

@flow
def load_data(documents: list):
    load_and_clean.submit(documents)


@task
def extract_data():
    pass


@task
def save_results():
    pass


@task
def cleanup():
    pass

@flow
def main_flow(directory: str = "data"):
    file_names = read_data(directory=directory)

    data = load_data(file_names)
    



if __name__ == "__main__":
    main_flow()

    # main_flow.serve()
