import bs4

INPUT = """
<?xml version="1.0"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Some Title</title>
</head>

<body xml:lang="EN-US">
<p class="MsoNormal">The quick brown fox</p>
</div>
</body>
</html>
"""

def test_sanity():
    assert 2 + 2 == 4
