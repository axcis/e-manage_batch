# coding: UTF-8
'''
有休付与情報テーブル定義ファイル

@author: takanori_gozu
'''
from src.main.batch.base.BaseDao import BaseDao

class VacationDateDao(BaseDao):

    TABLE_NAME = 'vacation_date'

    COL_EMPLOYEE_ID = 'employee_id'
    COL_GIVE_DATE = 'give_date'
    COL_WORK_YEAR = 'work_year'

    '''
    コンストラクタ
    '''
    def __init__(self, db):
        super(VacationDateDao, self).__init__(db, self.TABLE_NAME)
