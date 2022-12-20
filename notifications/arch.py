import gzip
import shutil
with gzip.open('UTM5.users.sql.gz', 'rb') as f_in:
    with open('UTM5.users.sql', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

