import os, shutil

src = r'C:\Users\USER\Substack2Markdown\substack_html_pages\damnang2'
dst = r'C:\Users\USER\da-substack'

for filename in os.listdir(src):
    if filename.endswith('.html'):
        filepath_src = os.path.join(src, filename)
        filepath_dst = os.path.join(dst, filename)
        with open(filepath_src, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace('../../assets/css/essay-styles.css', 'assets/css/essay-styles.css')
        with open(filepath_dst, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Fixed: ' + filename)

print('All done')