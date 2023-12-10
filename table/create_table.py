from view import text_collection
from .additional_stuff import diagramm_create, analysis_create
from docxtpl import DocxTemplate
from additional_stuff import word_create


def create_doc(word_document, option: int):
    doc = DocxTemplate(word_document)  # открываем шаблон

    context = word_create.full_context(option)

    doc.render(context)
    doc.save(f"спидозные козявки.docx")


def get_analysis(option: int, operand):
    if operand == text_collection.yes:
        print(analysis_create.analysis(option))
    elif operand == text_collection.no:
        print(text_collection.analysis_not_print)
    else:
        print(text_collection.only_yes_and_no)


def get_diagrams(option: int, operand):
    if operand == text_collection.yes:
        diagramm_create.get_diagrams(option)
    elif operand == text_collection.no:
        print(text_collection.diagrams_not_print)
    else:
        print(text_collection.only_yes_and_no)
