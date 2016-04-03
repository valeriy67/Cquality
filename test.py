from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTableView, QMessageBox
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlQueryModel, QSqlQuery


def createConnection():
    db = QSqlDatabase.addDatabase('QODBC')
    db.setDatabaseName('farmadb_mdb')
    if not db.open():
        QMessageBox.critical(None, "Cannot open database",
                "Unable to establish a database connection.",
                QMessageBox.Cancel)
        return False
    return True

def initializeModel(model):
    # model.setTable('PData')

    model.setQuery("SELECT Id, PrepData, ReadyData FROM PData")

    # model.setEditStrategy(QSqlTableModel.OnManualSubmit)
    # model.select()

    model.setHeaderData(0, Qt.Horizontal, "Серія")
    model.setHeaderData(1, Qt.Horizontal, "Проміжна")
    model.setHeaderData(2, Qt.Horizontal, "Готова")


def createView(title, model):
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)

    # model = QSqlTableModel()
    model = QSqlQueryModel()

    model.setQuery("SELECT Id, PrepData, ReadyData FROM PData")

    initializeModel(model)

    view1 = createView("Table Model (View 1)", model)
    view1.show()
    sys.exit(app.exec_())