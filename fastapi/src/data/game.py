from data.init_db import curs
import random
import string
import re

def random_english(length: int) -> str:
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def get_word() -> str:
    qry = "select name from creature order by random() limit 1"
    curs.execute(qry)
    row = curs.fetchone()
    if row:
        name = row[0]
        if not re.fullmatch(r'[a-zA-Z]+', name):
            name = random_english(len(name))
    else:
        name = "bigfoot"
    return name.lower()