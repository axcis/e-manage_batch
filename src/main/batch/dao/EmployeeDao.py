# coding: UTF-8
'''
社員マスタテーブル定義ファイル

@author: takanori_gozu
'''
from src.main.batch.base.BaseDao import BaseDao

class EmployeeDao(BaseDao):

    TABLE_NAME = 'employee'

    COL_ID = 'id'
    COL_NAME = 'name'
    COL_HIRAGANA = 'hiragana'
    COL_HIRE_DATE = 'hire_date'
    COL_HALF_HIRE_DATE = 'half_hire_date'
    COL_ONE_YEAR_HIRE_DATE = 'one_year_hire_date'
    COL_RETIREMENT = 'retirement'
    COL_RETIREMENT_DATE = 'retirement_date'

    '''
    コンストラクタ
    '''
    def __init__(self, db):
        super(EmployeeDao, self).__init__(db, self.TABLE_NAME)
