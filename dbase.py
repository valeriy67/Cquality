# -*- coding: utf-8 -*-
__author__ = 'Valeriy'

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTableView, QMessageBox
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlQueryModel, QSqlQuery

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

import sys

class DbData():
    def __init__(self):
        self.createConnection()
        self.query = QSqlQuery()
        return None

    def createConnection(self):
        self.con = QSqlDatabase.addDatabase('QODBC')
        # self.con.setConnectOptions('CharSet="cp1251"')
        self.con.setDatabaseName('farmadb_mdb')
        if not self.con.open():
            QMessageBox.critical(None, "Cannot open database", "Cannot open database.", QMessageBox.Cancel)
            return False
        return True

    def queryTypeProd(self):
        # self.query = QSqlQuery()
        self.query.exec("SELECT TypeData FROM PType")
        strType = []
        while self.query.next():
            strType = strType + [self.query.value(0)]
        return strType

    def queryNamePrep(self, sqlstr):
        # self.query = QSqlQuery()
        strsql = "SELECT Id FROM PType WHERE TypeData="+"'"+sqlstr+"'"
        self.query.exec(strsql)
        self.query.next()
        idT = self.query.value(0)

        sqlstr1 = "SELECT PName FROM Preparation WHERE TypeId="+str(idT)
        self.query.exec(sqlstr1)
        strName = ['']
        while self.query.next():
            strName = strName + [self.query.value(0)]
        return strName

    def queryNameSign(self, sqlstr):
        # self.query = QSqlQuery()
        self.query.clear()
        strsql = "SELECT Id FROM Preparation WHERE PName="+"'"+sqlstr+"'"
        self.query.exec(strsql)
        self.query.next()
        idP = self.query.value(0)
        # print(self.query.lastError().text().encode('utf-8').decode('cp1251'))
        sqlstr1 = "SELECT SigName FROM Significat WHERE PNameId="+str(idP)
        self.query.exec(sqlstr1)
        strName = ['']
        while self.query.next():
            strName = strName + [self.query.value(0)]
        return strName

    def queryIdPrepSing(self, strName, strSign):
        # Отримуємо ID препарата
        self.query.clear()
        sqlPrep = "SELECT Id FROM Preparation WHERE PName='"+strName+"'"
        self.query.exec(sqlPrep)
        self.query.next()
        idPrep = self.query.value(0)
        # Отримуємо ID показника
        self.query.clear()
        sqlSign = "SELECT Id FROM Significat WHERE (PNameId=" + str(idPrep) +" AND SigName='" + strSign+"')"
        # print(sqlSign.encode('utf-8').decode('cp1251'))
        self.query.exec(sqlSign)
        self.query.next()
        idSign = self.query.value(0)
        resultData = (idPrep, idSign)
        return resultData

    def queryGetYear(self):
        self.query.clear()
        self.query.exec("SELECT YData FROM Yeartable ORDER BY YData DESC")
        strYear = []
        while self.query.next():
            strYear = strYear + [self.query.value(0)]
        return strYear

    def queryGetCountRec(self):
        pass

    def queryGetDataPrep(self, nameId, signId, yearId, typeProg):
        self.query.clear()
        if typeProg:
            sqlstr = "SELECT ReadyData FROM Pdata WHERE ((PNameId="+str(nameId)+")"+" AND (SNameId="+str(signId)+") AND (YearId='"+str(yearId)+"'))"
        else:
            sqlstr = "SELECT PrepData FROM Pdata WHERE ((PNameId="+str(nameId)+")"+" AND (SNameId="+str(signId)+") AND (YearId='"+str(yearId)+"'))"

        self.query.exec(sqlstr)
        # self.query.next()
        getData = []
        while self.query.next():
            tmpData = self.query.value(0)
            if tmpData != '':
                  getData = getData + [float(tmpData)]
        self.query.clear()
        sqlcount = "SELECT COUNT(*) FROM Pdata WHERE ((PNameId="+str(nameId)+")" \
                 " AND (SNameId="+str(signId)+") AND (YearId='"+str(yearId)+"'))"
        self.query.exec(sqlcount)
        self.query.next()
        countData = int(self.query.value(0))
        return (countData, getData)


    def queryGetDataSign(self, nameId, signId):

        '''
        :param nameId: індекс препарата
        :param signId: назва показника
        :return SMax, SMin, OnlyReady, верхня межа, нижня межа, тип готова, проміжна:
        '''
        self.query.clear()
        sqlstr = "SELECT SMax, SMin, OnlyReady FROM Significat WHERE ((PNameId={0}) AND (Id={1}))".format(nameId, str(signId))
        self.query.exec(sqlstr)
        self.query.next()
        getData = (float(self.query.value(0)), float(self.query.value(1)), bool(self.query.value(2)))
        self.query.clear()
        return getData

    def __del__(self):
        self.con.close()
        return None

app = QApplication(sys.argv)
dBase = DbData()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = DbData()
    str = db.queryGetDataSign(2, 14)
    print(str)
    # st = db.queryGetDataPrep(2, 14, 2016)
    # print('Main ', st)
#      print('______________')
#      s = db.queryNamePrep('Препарат')
#      print(s)

# print(strName.encode('utf-8').decode('cp1251'))
# print(self.query.lastError().text().encode('utf-8').decode('cp1251'))

