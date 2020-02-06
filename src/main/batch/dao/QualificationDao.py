# coding: UTF-8
'''
資格マスタテーブル定義ファイル

@author: takanori_gozu
'''
from src.main.batch.base.BaseDao import BaseDao

class QualificationDao(BaseDao):

    TABLE_NAME = 'qualification'

    COL_CLASS_ID = 'class_id'
    COL_RANK = 'rank'
    COL_NAME = 'name'
    COL_ALLOWANCE_PRICE = 'allowance_price'

    '''
    コンストラクタ
    '''
    def __init__(self, db):
        super(QualificationDao, self).__init__(db, self.TABLE_NAME)
