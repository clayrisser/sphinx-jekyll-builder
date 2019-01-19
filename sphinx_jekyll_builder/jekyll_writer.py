from munch import munchify
from sphinx_markdown_builder.markdown_writer import MarkdownTranslator, MarkdownWriter
import pydash as _
import yaml

class JekyllTranslator(MarkdownTranslator):
    visited_title = False
    title = None

    def visit_document(self, node):
        self.title = getattr(self.builder, 'current_docname')
        MarkdownTranslator.visit_document(self, node)

    def depart_document(self, node):
        ctx = self.builder.ctx
        variables = munchify({
            'date': ctx.date,
            'docname': self.builder.current_docname,
            'images': self.builder.images,
            'path': self.get_path(self.builder.current_docname),
            'title': self.title
        })
        variables_yaml = yaml.safe_dump(variables)
        frontmatter = '---\n' + variables_yaml + '---\n'
        self.add(frontmatter, section='head')
        MarkdownTranslator.depart_document(self, node)

    def get_path(self, docname):
        path = '' if docname == 'index' else docname
        path = '/' + _.snake_case(path).replace('_', '-')
        return path

    def visit_title(self, node):
        if not self.visited_title:
            self.title = node.astext()
        self.visited_title = True
        MarkdownTranslator.visit_title(self, node)

    def depart_title(self, node):
        MarkdownTranslator.depart_title(self, node)

class JekyllWriter(MarkdownWriter):
    translator_class = JekyllTranslator
