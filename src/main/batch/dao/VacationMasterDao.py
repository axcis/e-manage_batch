# coding: UTF-8
'''
有休付与マスタテーブル定義ファイル

@author: takanori_gozu
'''
from src.main.batch.base.BaseDao import BaseDao

class VacationMasterDao(BaseDao):

    TABLE_NAME = 'vacation_master'

    COL_COUNT_KEY = 'count_key'
    COL_GIVE_COUNT = 'give_count'

    '''
    コンストラクタ
    '''
    def __init__(self, db):
        super(VacationMasterDao, self).__init__(db, self.TABLE_NAME)
