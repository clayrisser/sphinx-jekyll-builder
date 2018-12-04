from sphinx_markdown_builder.markdown_writer import MarkdownTranslator, MarkdownWriter
from munch import munchify
import yaml

class JekyllTranslator(MarkdownTranslator):
    visited_title = False
    title = None

    def visit_document(self, node):
        self.title = getattr(self.builder, 'current_docname')
        super(JekyllTranslator, self).visit_document(node)

    def depart_document(self, node):
        variables = munchify({
            'current_docname': getattr(self.builder, 'current_docname'),
            'images': getattr(self.builder, 'images'),
            'title': self.title,
            'versioning_method': getattr(self.builder, 'versioning_method')
        })
        variables_yaml = yaml.safe_dump(variables)
        frontmatter = '---\n' + variables_yaml + '---\n'
        self.add(frontmatter, section='head')
        super(JekyllTranslator, self).depart_document(node)

    def visit_title(self, node):
        if not self.visited_title:
            self.title = node.astext()
        self.visited_title = True
        super(JekyllTranslator, self).visit_title(node)

    def depart_title(self, node):
        super(JekyllTranslator, self).depart_title(node)

class JekyllWriter(MarkdownWriter):
    translator_class = JekyllTranslator
