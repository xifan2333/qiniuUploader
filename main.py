# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Code\qiniuUploader\source\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from utils.config import Config
from utils.api import QiNiu
from components.add import dialog
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 414)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_choose_file = QtWidgets.QPushButton(self.tab)
        self.pushButton_choose_file.setObjectName("pushButton_choose_file")
        self.gridLayout_3.addWidget(self.pushButton_choose_file, 0, 0, 1, 1)
        self.pushButton_upload = QtWidgets.QPushButton(self.tab)
        self.pushButton_upload.setObjectName("pushButton_upload")
        self.gridLayout_3.addWidget(self.pushButton_upload, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 2, 1, 1)
        self.textEdit_path = QtWidgets.QTextEdit(self.tab)
        self.textEdit_path.setObjectName("textEdit_path")
        self.gridLayout_4.addWidget(self.textEdit_path, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setEnabled(True)
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_add_url = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_add_url.setObjectName("pushButton_add_url")
        self.gridLayout_2.addWidget(self.pushButton_add_url, 3, 2, 1, 1)
        self.lineEdit_ak = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_ak.setObjectName("lineEdit_ak")
        self.gridLayout_2.addWidget(self.lineEdit_ak, 0, 1, 1, 1)
        self.comboBox_buckets = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_buckets.setObjectName("comboBox_buckets")
        self.gridLayout_2.addWidget(self.comboBox_buckets, 2, 1, 1, 1)
        self.pushButton_reload_setting = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_reload_setting.setObjectName(
            "pushButton_reload_setting")
        self.gridLayout_2.addWidget(self.pushButton_reload_setting, 4, 0, 1, 1)
        self.pushButton_add_bucket = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_add_bucket.setObjectName("pushButton_add_bucket")
        self.gridLayout_2.addWidget(self.pushButton_add_bucket, 2, 2, 1, 1)
        self.comboBox_urls = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_urls.setObjectName("comboBox_urls")
        self.gridLayout_2.addWidget(self.comboBox_urls, 3, 1, 1, 1)
        self.pushButton_rm_url = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_rm_url.setObjectName("pushButton_rm_url")
        self.gridLayout_2.addWidget(self.pushButton_rm_url, 3, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.pushButton_rm_bucket = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_rm_bucket.setObjectName("pushButton_rm_bucket")
        self.gridLayout_2.addWidget(self.pushButton_rm_bucket, 2, 3, 1, 1)
        self.lineEdit_sk = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_sk.setObjectName("lineEdit_sk")
        self.gridLayout_2.addWidget(self.lineEdit_sk, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.textEdit_path.setAcceptDrops(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "七牛云上传工具"))
        self.pushButton_choose_file.setText(_translate("MainWindow", "选择文件"))
        self.pushButton_upload.setText(_translate("MainWindow", "上传"))
        self.label_5.setText(_translate("MainWindow", "上传文件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), _translate("MainWindow", "上传"))
        self.label.setText(_translate("MainWindow", "access key"))
        self.pushButton_add_url.setText(_translate("MainWindow", "增加"))
        self.pushButton_reload_setting.setText(
            _translate("MainWindow", "重载设置"))
        self.pushButton_add_bucket.setText(_translate("MainWindow", "增加"))
        self.pushButton_rm_url.setText(_translate("MainWindow", "删除"))
        self.label_4.setText(_translate("MainWindow", "存储空间名"))
        self.pushButton_rm_bucket.setText(_translate("MainWindow", "删除"))
        self.label_2.setText(_translate("MainWindow", "secret key"))
        self.label_3.setText(_translate("MainWindow", "自定义域名"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), _translate("MainWindow", "设置"))

    def readConfig(self):
        self.conf = Config.get_config()
        config = self.conf
        self.lineEdit_ak.setText(config['ak'])
        self.lineEdit_sk.setText(config['sk'])
        self.comboBox_buckets.setCurrentText(config['current_bucket'])
        self.comboBox_urls.setCurrentText(config['current_url'])
        if config['buckets']:
            self.comboBox_buckets.addItems(config['buckets'])
        if config['urls']:
            self.comboBox_urls.addItems(config['urls'])
        self.config = Config(ak=config['ak'], sk=config['sk'], buckets=config['buckets'], urls=config['urls'],
                             current_bucket=config['current_bucket'], current_url=config['current_url'])

    def removeBucket(self):
        bucket = self.comboBox_buckets.currentText()
        if self.config.buckets:
            self.config.rm_bucket(bucket)
            self.config.set_config()
            self.comboBox_buckets.removeItem(0)
        else:
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Warning, "警告", "已无选项可删除").exec()

    def removeBucketHandle(self):
        self.pushButton_rm_bucket.clicked.connect(self.removeBucket)

    def removeUrl(self):
        url = self.comboBox_urls.currentText()
        if self.config.urls:
            self.config.rm_url(url)
            self.config.set_config()
            self.comboBox_urls.removeItem(0)
        else:
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Warning, "警告", "已无选项可删除").exec()

    def removeUrlHandle(self):
        self.pushButton_rm_url.clicked.connect(self.removeUrl)

    def addBucket(self):
        addDialog = QtWidgets.QDialog()
        dig = dialog(addDialog)
        addDialog.exec()
        if addDialog.Accepted:
            self.config.add_buket(dig.lineEdit.text())
            self.config.set_config()
            self.comboBox_buckets.addItem(dig.lineEdit.text())

    def addBucketHandle(self):
        self.pushButton_add_bucket.clicked.connect(self.addBucket)

    def addUrl(self):
        addDialog = QtWidgets.QDialog()
        dig = dialog(addDialog)
        addDialog.exec()
        if addDialog.Accepted:
            self.config.add_url(dig.lineEdit.text())
            self.config.set_config()
            self.comboBox_urls.addItem(dig.lineEdit.text())

    def addUrlHandle(self):
        self.pushButton_add_url.clicked.connect(self.addUrl)

    def reloadSetting(self):
        ak = self.lineEdit_ak.text()
        sk = self.lineEdit_sk.text()
        bucket = self.comboBox_buckets.currentText()
        url = self.comboBox_urls.currentText()
        self.config.set_config(ak, sk, bucket, url)
        QtWidgets.QMessageBox(
            QtWidgets.QMessageBox.Information, "提示", "配置已重载！").exec()

    def reloadHandle(self):
        self.pushButton_reload_setting.clicked.connect(self.reloadSetting)

    def chooseFile(self):
      
        result = QtWidgets.QFileDialog.getOpenFileName()
        if result:
            self.textEdit_path.setPlainText(result[0])
      
    def chooseFileHandle(self):
        self.pushButton_choose_file.clicked.connect(self.chooseFile)
    
    def upload(self):
        ak = self.config.ak
        sk =self.config.sk
        bucket = self.config.current_bucket
        url = self.config.current_url
        path = self.textEdit_path.toPlainText()
        if os.path.isfile(path):
            path = path
        else:
            try:
                path = path.split('file:///')[1]
            except:
                QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Warning, "警告", "文件路径错误").exec()
        try:
            self.qiniu = QiNiu(ak,sk,bucket,url)
            self.qiniu.auth().set_path(path)
            self.qiniu.get_token()
            result = self.qiniu.upload()
            self.textEdit_path.setPlainText(result)
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Information, "提示", "上传成功！").exec()
        except:
                QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Warning, "警告", "上传失败，请检查路径或配置有无错误").exec()
    
    def uploadHandle(self):
        self.pushButton_upload.clicked.connect(self.upload)


    def setupEvents(self):
        self.readConfig()
        self.removeBucketHandle()
        self.removeUrlHandle()
        self.addBucketHandle()
        self.addUrlHandle()
        self.reloadHandle()
        self.chooseFileHandle()
        self.uploadHandle()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.setupEvents()
    MainWindow.show()
    sys.exit(app.exec_())
