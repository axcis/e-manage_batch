# coding: UTF-8
'''
雇用情報管理システム自動更新バッチ処理ロジック

@author: takanori_gozu
'''

from datetime import datetime
from dateutil.relativedelta import relativedelta
from src.main.batch.base.BaseLogic import BaseLogic
from src.main.batch.dao.EmployeeDao import EmployeeDao
from src.main.batch.lib.string.StringOperation import StringOperation
from src.main.batch.dao.QualificationAllowanceDao import QualificationAllowanceDao
from src.main.batch.dao.VacationDateDao import VacationDateDao
from src.main.batch.dao.EmployeeStatusDao import EmployeeStatusDao

class EmanageAutoUpdateLogic(BaseLogic):

    '''
    コンストラクタ
    '''
    def __init__(self, db, logger, form):
        super(EmanageAutoUpdateLogic, self).__init__(db, logger, form)

    '''
    run
    '''
    def run(self):
        date = self.getForm('-date')

        if date == '':
            self.writeLog('parameter:-date is not set')
            return

        #基準日を取得
        stdDate = self.getStandardDate(date)

        self.writeLog('削除基準日：' + stdDate)

        #社員のIDを取得
        ids = self.getDeleteTargetIds(stdDate)

        if len(ids) == 0:
            self.writeLog('退職者データなし')
        else:
            #各種データを削除
            self.deleteData(ids)
            self.writeLog('データ削除完了')

        #次回有休付与データの追加登録
        self.insertVacationDate(date)

        return


    '''
    削除基準日を取得する(半年前)
    '''
    def getStandardDate(self, dt):
        date = dt + ' 00:00:00'
        bdt = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

        #文字列で返す
        return StringOperation.toString((bdt - relativedelta(months=6)).date())

    '''
    削除対象の社員IDを取得
    '''
    def getDeleteTargetIds(self, dt):
        dao = EmployeeDao(self.db)

        dao.addWhereStr(EmployeeDao.COL_RETIREMENT, '1')
        dao.addWhereStr(EmployeeDao.COL_RETIREMENT_DATE, dt, EmployeeDao.COMP_LESS)

        return dao.doSelectCol(EmployeeDao.COL_ID)

    '''
    各種データを削除する
    '''
    def deleteData(self, ids):
        #資格手当情報
        dao = QualificationAllowanceDao(self.db)

        dao.addWhereIn(QualificationAllowanceDao.COL_EMPLOYEE_ID, ids)

        count = dao.doCount()

        self.writeLog('資格手当情報削除対象件数：' + StringOperation.toString(count) + '件')
        dao.doDelete()

        #有休付与情報
        dao = VacationDateDao(self.db)

        dao.addWhereIn(VacationDateDao.COL_EMPLOYEE_ID, ids)

        count = dao.doCount()

        self.writeLog('有休付与情報削除対象件数：' + StringOperation.toString(count) + '件')
        dao.doDelete()

        #雇用形態情報
        dao = EmployeeStatusDao(self.db)

        dao.addWhereIn(EmployeeStatusDao.COL_EMPLOYEE_ID, ids)

        count = dao.doCount()

        self.writeLog('雇用形態情報削除対象件数：' + StringOperation.toString(count) + '件')
        dao.doDelete()

        #社員情報
        dao = EmployeeDao(self.db)

        dao.addWhereIn(EmployeeDao.COL_ID, ids)

        count = dao.doCount()

        self.writeLog('社員情報削除対象件数：' + StringOperation.toString(count) + '件')
        dao.doDelete()

        return

    '''
    前月に有休付与された人の次回有休付与情報を登録
    '''
    def insertVacationDate(self, date):

        dt = StringOperation.toString((datetime.strptime(date + ' 00:00:00', '%Y-%m-%d %H:%M:%S') - relativedelta(months=1)).date())

        dao = VacationDateDao(self.db)

        dao.addWhereStr(VacationDateDao.COL_GIVE_DATE, dt, dao.COMP_GREATER_EQUAL)
        dao.addWhereStr(VacationDateDao.COL_GIVE_DATE, date, dao.COMP_LESS)

        select = dao.doSelect()
        count = 0

        for i in range(len(select)):
            employeeId = select[i][VacationDateDao.COL_EMPLOYEE_ID]
            giveDate = StringOperation.toString((datetime.strptime(str(select[i][VacationDateDao.COL_GIVE_DATE]) + ' 00:00:00', '%Y-%m-%d %H:%M:%S') + relativedelta(years=1)).date())
            workYear = select[i][VacationDateDao.COL_WORK_YEAR]
            if workYear < 7:
                workYear += 1
            dao = VacationDateDao(self.db)
            dao.addColVal(VacationDateDao.COL_EMPLOYEE_ID, employeeId)
            dao.addColValStr(VacationDateDao.COL_GIVE_DATE, giveDate)
            dao.addColVal(VacationDateDao.COL_WORK_YEAR, workYear)
            dao.doInsert()
            count+=1

        self.writeLog('有休付与情報追加件数：' + StringOperation.toString(count) + '件')

        return