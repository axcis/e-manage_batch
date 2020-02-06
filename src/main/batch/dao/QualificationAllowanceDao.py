# coding: UTF-8
'''
資格手当情報テーブル定義ファイル

@author: takanori_gozu
'''
from src.main.batch.base.BaseDao import BaseDao

class QualificationAllowanceDao(BaseDao):

    TABLE_NAME = 'qualification_allowance'

    COL_EMPLOYEE_ID = 'employee_id'
    COL_CLASS_ID = 'class_id'
    COL_RANK = 'rank'
    COL_REQUEST_DATE = 'request_date'
    COL_START_YM = 'start_ym'

    '''
    コンストラクタ
    '''
    def __init__(self, db):
        super(QualificationAllowanceDao, self).__init__(db, self.TABLE_NAME)
