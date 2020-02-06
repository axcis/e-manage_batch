# coding: UTF-8
'''
雇用情報管理システム自動更新バッチ

@author: takanori_gozu
'''
import sys
from src.main.batch.base.BaseBatch import BaseBatch
from src.main.batch.logic.EmanageAutoUpdateLogic import EmanageAutoUpdateLogic

class EmanageAutoUpdate(BaseBatch):

    appId = 'EmanageAutoUpdate'
    appName = '雇用情報管理システム自動更新バッチ'

    '''
    ロジック
    '''
    def getLogic(self, db, logger, form):
        logic = EmanageAutoUpdateLogic(db, logger, form)
        return logic

    '''
    アプリID
    '''
    def getAppId(self):
        return self.appId

    '''
    アプリ名
    '''
    def getAppName(self):
        return self.appName

if __name__ == '__main__':
    batch = EmanageAutoUpdate()
    batch.mainProc(sys.argv)