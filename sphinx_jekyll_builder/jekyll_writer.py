from .sphinx_markdown_builder.markdown_writer import MarkdownTranslator, MarkdownWriter

class JekyllTranslator(MarkdownTranslator):
    pass

class JekyllWriter(MarkdownWriter):
    translator_class = JekyllTranslator
