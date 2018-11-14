from sphinx_markdown_builder.markdown_writer import MarkdownTranslator, MarkdownWriter
from munch import munchify
import yaml

class JekyllTranslator(MarkdownTranslator):
    def visit_document(self, node):
        variables = munchify({
            'current_docname': getattr(self.builder, 'current_docname'),
            'images': getattr(self.builder, 'images'),
            'versioning_method': getattr(self.builder, 'versioning_method')
        })
        variables_yaml = yaml.safe_dump(variables)
        frontmatter = '---\n' + variables_yaml + '---\n'
        self.add(frontmatter, section='head')
        super().visit_document(node)

    def depart_document(self, node):
        super().depart_document(node)

class JekyllWriter(MarkdownWriter):
    translator_class = JekyllTranslator
