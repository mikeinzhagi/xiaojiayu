from tempfile import  TemporaryFile
with TemporaryFile('w+t') as fp:
    fp.write('Hello universe!')
    fp.seek(0)
    fp.read()
# 临时文件现在已经被关闭和删除