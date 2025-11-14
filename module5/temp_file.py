import tempfile

with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
    tmpfile.write(b"Some temporary content")
    print(tmpfile.name)