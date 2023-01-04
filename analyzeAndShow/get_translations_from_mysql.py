from multiprocessing import Pool

import pandas as pd
from sqlalchemy import create_engine
from functools import reduce
from unidecode import unidecode
import re

from analyzeAndShow.constants_mysql import tb_names, languages, db_names


def get_df_from_db(db_name):
    db_connection = create_engine(f'mariadb+mariadbconnector://newuser:newpassword@127.0.0.1:3306/{db_name}')
    tb_list = []
    for tb in tb_names:
        res = pd.read_sql_table(f"{tb}", con=db_connection)
        tb_list.append(res)
    tb_df = reduce(lambda left, right: pd.merge(left, right, on=['id', ], how='inner', suffixes=("", "_1")), tb_list)
    tb_df = (tb_df.T.drop_duplicates()).T
    only_translations = tb_df[languages].applymap(unidecode).applymap(str.lower).applymap(lambda x: re.sub(r'[^a-zA-Z ]', "", x))
    return (" ".join(db_name.split("_")[1:-1]), only_translations)

with Pool(24) as pool:
    table_list = pool.map(get_df_from_db, db_names)

translations_df = pd.concat(dict(table_list), axis=0).reset_index(level=1, drop=True)
translations_df.index.rename("Topic", inplace=True)