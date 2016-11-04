import markdown
import codecs


def markdown_file_to_html(path):
    """Converting markdown file to HTML string.

     :param path:   string    Path to makrdown file.

    """

    input_file = codecs.open(path, mode="r", encoding="utf-8")
    text = input_file.read()
    return markdown.markdown(text)
