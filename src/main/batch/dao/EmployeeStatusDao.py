# coding: UTF-8
'''
雇用形態情報テーブル定義ファイル

@author: takanori_gozu
'''
from src.main.batch.base.BaseDao import BaseDao

class EmployeeStatusDao(BaseDao):

    TABLE_NAME = 'employee_status'

    COL_EMPLOYEE_ID = 'employee_id'
    COL_CONTRACT_DATE = 'contract_date'
    COL_REGULAR_DATE = 'regular_date'

    '''
    コンストラクタ
    '''
    def __init__(self, db):
        super(EmployeeStatusDao, self).__init__(db, self.TABLE_NAME)
