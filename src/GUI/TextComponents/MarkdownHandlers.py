import markdown
import re 
from markdown.inlinepatterns import InlineProcessor
from markdown.blockprocessors import BlockProcessor
from .Styles import TextSpace
import xml.etree.ElementTree as etree 

REGISTER_EXTENSIONS = [] # There has to be a better way of doing this (maybe not doing this at all?)

# Note Extension 
class NoteTagInlineProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        el = etree.Element("span")
        el.set("style", "color: orange; font-weight: bold;")
        el.text = f"{m.group(1)}"
        
        return el, m.start(0), m.end(0)


class NoteExtension(markdown.Extension): 
    def extendMarkdown(self, md):
        NOTE_RE = r'<(.*?)>'
        md.inlinePatterns.register(NoteTagInlineProcessor(NOTE_RE, md), "note", 175)

REGISTER_EXTENSIONS.append(NoteExtension())

# DefinitionExtension
class DefinitionBlockProcessor(BlockProcessor):
    RE = re.compile(r'^\$\s*(.*?)\s*:\s*(.*)$')

    def test(self, parent, block):
        return bool(self.RE.match(block))

    def run(self, parent, blocks):
        block = blocks.pop(0)
        match = self.RE.match(block)

        if match:
            title, content = match.groups() 

            # Create custom html structure 
            container = etree.SubElement(parent, "div")
            container.set("class", "custom-block")

            title_el = etree.SubElement(container, "span")
            title_el.set("style", TextSpace.DEF_TITLE)
            title_el.text = f"{title} : "

            content_el = etree.SubElement(container, "span")
            content_el.set("style", TextSpace.DEF_CONTENT)
            content_el.text = content
            
class DollarColonExtension(markdown.Extension):
    def extendMarkdown(self, md):
        md.parser.blockprocessors.register(DefinitionBlockProcessor(md.parser), "dollarcolon", 175)

REGISTER_EXTENSIONS.append(DollarColonExtension())