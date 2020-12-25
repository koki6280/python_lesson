import zipfile

with zipfile.ZipFile('test.zip', 'w') as z:
    z.write('add_dir')
    z.write('add_dir/add.txt')