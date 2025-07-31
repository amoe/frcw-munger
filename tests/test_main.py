import lxml.etree
import pdb

INPUT = """<?xml version="1.0"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Some Title</title>
</head>

<body xml:lang="EN-US">
<div class="Section1">
<p class="MsoNormal">The quick brown fox</p>
</div>
</body>
</html>"""


def get_content(tree) -> str:
    xhtml_ns = tree.nsmap.get(None)
    namespaces = {'x': xhtml_ns}
    p = tree.find('.//x:p', namespaces=namespaces)
    return ''.join(p.itertext())

    
def test_sanity():
    parser = lxml.etree.XMLParser()
    tree = lxml.etree.fromstring(INPUT, parser=parser)
    assert get_content(tree) == 'The quick brown fox'
