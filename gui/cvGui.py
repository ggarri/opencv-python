# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cvGui.ui'
#
# Created: Wed Mar 23 04:17:53 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
   _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
   _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
   def setupUi(self, MainWindow):
      MainWindow.setObjectName(_fromUtf8("MainWindow"))
      MainWindow.setEnabled(True)
      MainWindow.resize(401, 685)
      sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
      sizePolicy.setHorizontalStretch(0)
      sizePolicy.setVerticalStretch(0)
      sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
      MainWindow.setSizePolicy(sizePolicy)
      MainWindow.setMinimumSize(QtCore.QSize(401, 685))
      MainWindow.setMaximumSize(QtCore.QSize(401, 685))
      self.centralwidget = QtGui.QWidget(MainWindow)
      self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
      self.selectPath_groupBox = QtGui.QGroupBox(self.centralwidget)
      self.selectPath_groupBox.setGeometry(QtCore.QRect(10, 70, 381, 91))
      self.selectPath_groupBox.setObjectName(_fromUtf8("selectPath_groupBox"))
      self.selectPath_widget = QtGui.QWidget(self.selectPath_groupBox)
      self.selectPath_widget.setGeometry(QtCore.QRect(170, 30, 205, 51))
      self.selectPath_widget.setObjectName(_fromUtf8("selectPath_widget"))
      self.horizontalLayout = QtGui.QHBoxLayout(self.selectPath_widget)
      self.horizontalLayout.setMargin(0)
      self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
      self.videoPath_lineEdit = QtGui.QLineEdit(self.selectPath_widget)
      self.videoPath_lineEdit.setObjectName(_fromUtf8("videoPath_lineEdit"))
      self.horizontalLayout.addWidget(self.videoPath_lineEdit)
      self.selectPath_toolButton = QtGui.QToolButton(self.selectPath_widget)
      self.selectPath_toolButton.setObjectName(_fromUtf8("selectPath_toolButton"))
      self.horizontalLayout.addWidget(self.selectPath_toolButton)
      self.videoImageCamSelector_frame = QtGui.QWidget(self.selectPath_groupBox)
      self.videoImageCamSelector_frame.setGeometry(QtCore.QRect(15, 30, 153, 51))
      self.videoImageCamSelector_frame.setObjectName(_fromUtf8("videoImageCamSelector_frame"))
      self.formLayout = QtGui.QFormLayout(self.videoImageCamSelector_frame)
      self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
      self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
      self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
      self.formLayout.setMargin(0)
      self.formLayout.setObjectName(_fromUtf8("formLayout"))
      self.selectCamSource_radioButton = QtGui.QRadioButton(self.videoImageCamSelector_frame)
      self.selectCamSource_radioButton.setChecked(True)
      self.selectCamSource_radioButton.setObjectName(_fromUtf8("selectCamSource_radioButton"))
      self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.selectCamSource_radioButton)
      self.selectVideoSource_radioButton = QtGui.QRadioButton(self.videoImageCamSelector_frame)
      self.selectVideoSource_radioButton.setChecked(False)
      self.selectVideoSource_radioButton.setObjectName(_fromUtf8("selectVideoSource_radioButton"))
      self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.selectVideoSource_radioButton)
      self.vision_groupBox = QtGui.QGroupBox(self.centralwidget)
      self.vision_groupBox.setGeometry(QtCore.QRect(10, 160, 381, 331))
      self.vision_groupBox.setObjectName(_fromUtf8("vision_groupBox"))
      self.vision_tabWidget = QtGui.QTabWidget(self.vision_groupBox)
      self.vision_tabWidget.setGeometry(QtCore.QRect(10, 30, 361, 291))
      self.vision_tabWidget.setUsesScrollButtons(False)
      self.vision_tabWidget.setObjectName(_fromUtf8("vision_tabWidget"))
      self.background_tab = QtGui.QWidget()
      self.background_tab.setObjectName(_fromUtf8("background_tab"))
      self.background_frame = QtGui.QFrame(self.background_tab)
      self.background_frame.setEnabled(True)
      self.background_frame.setGeometry(QtCore.QRect(10, 10, 341, 241))
      self.background_frame.setFrameShape(QtGui.QFrame.StyledPanel)
      self.background_frame.setFrameShadow(QtGui.QFrame.Raised)
      self.background_frame.setObjectName(_fromUtf8("background_frame"))
      self.separationWidget = QtGui.QWidget(self.background_frame)
      self.separationWidget.setGeometry(QtCore.QRect(0, 30, 311, 31))
      self.separationWidget.setObjectName(_fromUtf8("separationWidget"))
      self.horizontalLayout_4 = QtGui.QHBoxLayout(self.separationWidget)
      self.horizontalLayout_4.setContentsMargins(10, 5, 5, 5)
      self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
      self.selectBackgroundReplacementPath_lineEdit = QtGui.QLineEdit(self.separationWidget)
      self.selectBackgroundReplacementPath_lineEdit.setObjectName(_fromUtf8("selectBackgroundReplacementPath_lineEdit"))
      self.horizontalLayout_4.addWidget(self.selectBackgroundReplacementPath_lineEdit)
      self.selectBackgroundPath_toolButton = QtGui.QToolButton(self.separationWidget)
      self.selectBackgroundPath_toolButton.setObjectName(_fromUtf8("selectBackgroundPath_toolButton"))
      self.horizontalLayout_4.addWidget(self.selectBackgroundPath_toolButton)
      self.backgroundPathSelect_label = QtGui.QLabel(self.background_frame)
      self.backgroundPathSelect_label.setGeometry(QtCore.QRect(20, 10, 181, 16))
      self.backgroundPathSelect_label.setObjectName(_fromUtf8("backgroundPathSelect_label"))
      self.backgroundOptions_frame = QtGui.QFrame(self.background_frame)
      self.backgroundOptions_frame.setGeometry(QtCore.QRect(10, 70, 321, 161))
      self.backgroundOptions_frame.setFrameShape(QtGui.QFrame.StyledPanel)
      self.backgroundOptions_frame.setFrameShadow(QtGui.QFrame.Raised)
      self.backgroundOptions_frame.setObjectName(_fromUtf8("backgroundOptions_frame"))
      self.backgroundAlgorithm_comboBox = QtGui.QComboBox(self.backgroundOptions_frame)
      self.backgroundAlgorithm_comboBox.setGeometry(QtCore.QRect(20, 20, 191, 26))
      self.backgroundAlgorithm_comboBox.setObjectName(_fromUtf8("backgroundAlgorithm_comboBox"))
      self.backgroundAlgorithm_comboBox.addItem(_fromUtf8(""))
      self.backgroundAlgorithm_comboBox.addItem(_fromUtf8(""))
      self.backgroundAlgorithm_comboBox.addItem(_fromUtf8(""))
      self.backgroundAlgorithm_comboBox.addItem(_fromUtf8(""))
      self.backgroundAlgorithm_label = QtGui.QLabel(self.backgroundOptions_frame)
      self.backgroundAlgorithm_label.setGeometry(QtCore.QRect(220, 20, 62, 31))
      self.backgroundAlgorithm_label.setObjectName(_fromUtf8("backgroundAlgorithm_label"))
      self.backgoundThreshold_label = QtGui.QLabel(self.backgroundOptions_frame)
      self.backgoundThreshold_label.setGeometry(QtCore.QRect(70, 60, 71, 16))
      self.backgoundThreshold_label.setObjectName(_fromUtf8("backgoundThreshold_label"))
      self.backgroundThreshold_slider = QtGui.QSlider(self.backgroundOptions_frame)
      self.backgroundThreshold_slider.setGeometry(QtCore.QRect(20, 80, 171, 21))
      self.backgroundThreshold_slider.setMaximum(255)
      self.backgroundThreshold_slider.setOrientation(QtCore.Qt.Horizontal)
      self.backgroundThreshold_slider.setObjectName(_fromUtf8("backgroundThreshold_slider"))
      self.backgroundColor_label = QtGui.QLabel(self.backgroundOptions_frame)
      self.backgroundColor_label.setGeometry(QtCore.QRect(60, 120, 111, 21))
      self.backgroundColor_label.setObjectName(_fromUtf8("backgroundColor_label"))
      self.backgroundColor_pushButton = QtGui.QPushButton(self.backgroundOptions_frame)
      self.backgroundColor_pushButton.setGeometry(QtCore.QRect(30, 120, 21, 21))
      self.backgroundColor_pushButton.setAutoFillBackground(False)
      self.backgroundColor_pushButton.setStyleSheet(_fromUtf8("background-color: rgb(0,255,0)"))
      self.backgroundColor_pushButton.setText(_fromUtf8(""))
      self.backgroundColor_pushButton.setAutoRepeatDelay(300)
      self.backgroundColor_pushButton.setFlat(False)
      self.backgroundColor_pushButton.setObjectName(_fromUtf8("backgroundColor_pushButton"))
      self.backgroundThreshold_spinBox = QtGui.QSpinBox(self.backgroundOptions_frame)
      self.backgroundThreshold_spinBox.setGeometry(QtCore.QRect(200, 80, 51, 25))
      self.backgroundThreshold_spinBox.setMaximum(255)
      self.backgroundThreshold_spinBox.setObjectName(_fromUtf8("backgroundThreshold_spinBox"))
      self.vision_tabWidget.addTab(self.background_tab, _fromUtf8(""))
      self.tracking_tab = QtGui.QWidget()
      self.tracking_tab.setObjectName(_fromUtf8("tracking_tab"))
      self.trackingOptions_frame = QtGui.QFrame(self.tracking_tab)
      self.trackingOptions_frame.setEnabled(True)
      self.trackingOptions_frame.setGeometry(QtCore.QRect(10, 10, 341, 241))
      self.trackingOptions_frame.setFrameShape(QtGui.QFrame.StyledPanel)
      self.trackingOptions_frame.setFrameShadow(QtGui.QFrame.Raised)
      self.trackingOptions_frame.setObjectName(_fromUtf8("trackingOptions_frame"))
      self.trackingMethod_comboBox = QtGui.QComboBox(self.trackingOptions_frame)
      self.trackingMethod_comboBox.setGeometry(QtCore.QRect(20, 40, 191, 26))
      self.trackingMethod_comboBox.setObjectName(_fromUtf8("trackingMethod_comboBox"))
      self.trackingMethod_comboBox.addItem(_fromUtf8(""))
      self.trackingMethod_comboBox.addItem(_fromUtf8(""))
      self.trackingAlgorithm_label = QtGui.QLabel(self.trackingOptions_frame)
      self.trackingAlgorithm_label.setGeometry(QtCore.QRect(220, 40, 62, 31))
      self.trackingAlgorithm_label.setObjectName(_fromUtf8("trackingAlgorithm_label"))
      self.trackingThreshold_label = QtGui.QLabel(self.trackingOptions_frame)
      self.trackingThreshold_label.setGeometry(QtCore.QRect(70, 80, 71, 16))
      self.trackingThreshold_label.setObjectName(_fromUtf8("trackingThreshold_label"))
      self.trackingThreshold_horizontalSlider = QtGui.QSlider(self.trackingOptions_frame)
      self.trackingThreshold_horizontalSlider.setGeometry(QtCore.QRect(20, 90, 191, 21))
      self.trackingThreshold_horizontalSlider.setMaximum(255)
      self.trackingThreshold_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
      self.trackingThreshold_horizontalSlider.setObjectName(_fromUtf8("trackingThreshold_horizontalSlider"))
      self.trackingBrushColor_label = QtGui.QLabel(self.trackingOptions_frame)
      self.trackingBrushColor_label.setGeometry(QtCore.QRect(50, 200, 96, 21))
      self.trackingBrushColor_label.setObjectName(_fromUtf8("trackingBrushColor_label"))
      self.trackingBrushColor_pushButton = QtGui.QPushButton(self.trackingOptions_frame)
      self.trackingBrushColor_pushButton.setGeometry(QtCore.QRect(20, 200, 21, 21))
      self.trackingBrushColor_pushButton.setAutoFillBackground(False)
      self.trackingBrushColor_pushButton.setStyleSheet(_fromUtf8("background-color: rgb(0,255,0)"))
      self.trackingBrushColor_pushButton.setText(_fromUtf8(""))
      self.trackingBrushColor_pushButton.setAutoRepeatDelay(300)
      self.trackingBrushColor_pushButton.setFlat(False)
      self.trackingBrushColor_pushButton.setObjectName(_fromUtf8("trackingBrushColor_pushButton"))
      self.tracking_label = QtGui.QLabel(self.trackingOptions_frame)
      self.tracking_label.setGeometry(QtCore.QRect(20, 20, 181, 16))
      self.tracking_label.setObjectName(_fromUtf8("tracking_label"))
      self.trackingBrushThick_horizontalSlider = QtGui.QSlider(self.trackingOptions_frame)
      self.trackingBrushThick_horizontalSlider.setGeometry(QtCore.QRect(20, 130, 191, 21))
      self.trackingBrushThick_horizontalSlider.setMaximum(255)
      self.trackingBrushThick_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
      self.trackingBrushThick_horizontalSlider.setObjectName(_fromUtf8("trackingBrushThick_horizontalSlider"))
      self.trackingBrushThick_label = QtGui.QLabel(self.trackingOptions_frame)
      self.trackingBrushThick_label.setGeometry(QtCore.QRect(50, 120, 121, 21))
      self.trackingBrushThick_label.setWordWrap(True)
      self.trackingBrushThick_label.setObjectName(_fromUtf8("trackingBrushThick_label"))
      self.trackingThreshold_spinBox = QtGui.QSpinBox(self.trackingOptions_frame)
      self.trackingThreshold_spinBox.setGeometry(QtCore.QRect(220, 90, 57, 25))
      self.trackingThreshold_spinBox.setMaximum(255)
      self.trackingThreshold_spinBox.setObjectName(_fromUtf8("trackingThreshold_spinBox"))
      self.trackingBrushThick_spinBox = QtGui.QSpinBox(self.trackingOptions_frame)
      self.trackingBrushThick_spinBox.setGeometry(QtCore.QRect(220, 130, 57, 25))
      self.trackingBrushThick_spinBox.setMaximum(255)
      self.trackingBrushThick_spinBox.setObjectName(_fromUtf8("trackingBrushThick_spinBox"))
      self.trackingObjectColor_label = QtGui.QLabel(self.trackingOptions_frame)
      self.trackingObjectColor_label.setGeometry(QtCore.QRect(50, 170, 111, 21))
      self.trackingObjectColor_label.setObjectName(_fromUtf8("trackingObjectColor_label"))
      self.trackingObjectColor_pushButton = QtGui.QPushButton(self.trackingOptions_frame)
      self.trackingObjectColor_pushButton.setGeometry(QtCore.QRect(20, 170, 21, 21))
      self.trackingObjectColor_pushButton.setAutoFillBackground(False)
      self.trackingObjectColor_pushButton.setStyleSheet(_fromUtf8("background-color: rgb(0,255,0)"))
      self.trackingObjectColor_pushButton.setText(_fromUtf8(""))
      self.trackingObjectColor_pushButton.setAutoRepeatDelay(300)
      self.trackingObjectColor_pushButton.setFlat(False)
      self.trackingObjectColor_pushButton.setObjectName(_fromUtf8("trackingObjectColor_pushButton"))
      self.vision_tabWidget.addTab(self.tracking_tab, _fromUtf8(""))
      self.tab = QtGui.QWidget()
      self.tab.setObjectName(_fromUtf8("tab"))
      self.BgTrackOptions_frame = QtGui.QFrame(self.tab)
      self.BgTrackOptions_frame.setEnabled(True)
      self.BgTrackOptions_frame.setGeometry(QtCore.QRect(10, 10, 341, 241))
      self.BgTrackOptions_frame.setFrameShape(QtGui.QFrame.StyledPanel)
      self.BgTrackOptions_frame.setFrameShadow(QtGui.QFrame.Raised)
      self.BgTrackOptions_frame.setObjectName(_fromUtf8("BgTrackOptions_frame"))
      self.BgTrackMethod_comboBox = QtGui.QComboBox(self.BgTrackOptions_frame)
      self.BgTrackMethod_comboBox.setGeometry(QtCore.QRect(20, 90, 191, 26))
      self.BgTrackMethod_comboBox.setObjectName(_fromUtf8("BgTrackMethod_comboBox"))
      self.BgTrackMethod_comboBox.addItem(_fromUtf8(""))
      self.BgTrackMethod_comboBox.addItem(_fromUtf8(""))
      self.BgTrackAlgorithm_label = QtGui.QLabel(self.BgTrackOptions_frame)
      self.BgTrackAlgorithm_label.setGeometry(QtCore.QRect(220, 90, 62, 31))
      self.BgTrackAlgorithm_label.setObjectName(_fromUtf8("BgTrackAlgorithm_label"))
      self.BgTrackThreshold_label = QtGui.QLabel(self.BgTrackOptions_frame)
      self.BgTrackThreshold_label.setGeometry(QtCore.QRect(70, 120, 71, 16))
      self.BgTrackThreshold_label.setObjectName(_fromUtf8("BgTrackThreshold_label"))
      self.BgTrackThreshold_horizontalSlider = QtGui.QSlider(self.BgTrackOptions_frame)
      self.BgTrackThreshold_horizontalSlider.setGeometry(QtCore.QRect(20, 140, 191, 21))
      self.BgTrackThreshold_horizontalSlider.setMaximum(255)
      self.BgTrackThreshold_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
      self.BgTrackThreshold_horizontalSlider.setObjectName(_fromUtf8("BgTrackThreshold_horizontalSlider"))
      self.BgTrack_label = QtGui.QLabel(self.BgTrackOptions_frame)
      self.BgTrack_label.setGeometry(QtCore.QRect(20, 70, 181, 16))
      self.BgTrack_label.setObjectName(_fromUtf8("BgTrack_label"))
      self.BgTrackBrushThick_horizontalSlider = QtGui.QSlider(self.BgTrackOptions_frame)
      self.BgTrackBrushThick_horizontalSlider.setGeometry(QtCore.QRect(20, 180, 191, 21))
      self.BgTrackBrushThick_horizontalSlider.setMaximum(255)
      self.BgTrackBrushThick_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
      self.BgTrackBrushThick_horizontalSlider.setObjectName(_fromUtf8("BgTrackBrushThick_horizontalSlider"))
      self.BgTrackBrushThick_label = QtGui.QLabel(self.BgTrackOptions_frame)
      self.BgTrackBrushThick_label.setGeometry(QtCore.QRect(50, 160, 121, 21))
      self.BgTrackBrushThick_label.setWordWrap(True)
      self.BgTrackBrushThick_label.setObjectName(_fromUtf8("BgTrackBrushThick_label"))
      self.BgTrackThreshold_spinBox = QtGui.QSpinBox(self.BgTrackOptions_frame)
      self.BgTrackThreshold_spinBox.setGeometry(QtCore.QRect(220, 140, 57, 25))
      self.BgTrackThreshold_spinBox.setMaximum(255)
      self.BgTrackThreshold_spinBox.setObjectName(_fromUtf8("BgTrackThreshold_spinBox"))
      self.BgTrackBrushThick_spinBox = QtGui.QSpinBox(self.BgTrackOptions_frame)
      self.BgTrackBrushThick_spinBox.setGeometry(QtCore.QRect(220, 180, 57, 25))
      self.BgTrackBrushThick_spinBox.setMaximum(255)
      self.BgTrackBrushThick_spinBox.setObjectName(_fromUtf8("BgTrackBrushThick_spinBox"))
      self.BgTrackObjectColor_label = QtGui.QLabel(self.BgTrackOptions_frame)
      self.BgTrackObjectColor_label.setGeometry(QtCore.QRect(50, 210, 96, 21))
      self.BgTrackObjectColor_label.setObjectName(_fromUtf8("BgTrackObjectColor_label"))
      self.BgTrackObjectColor_pushButton = QtGui.QPushButton(self.BgTrackOptions_frame)
      self.BgTrackObjectColor_pushButton.setGeometry(QtCore.QRect(20, 210, 21, 21))
      self.BgTrackObjectColor_pushButton.setAutoFillBackground(False)
      self.BgTrackObjectColor_pushButton.setStyleSheet(_fromUtf8("background-color: rgb(0,255,0)"))
      self.BgTrackObjectColor_pushButton.setText(_fromUtf8(""))
      self.BgTrackObjectColor_pushButton.setAutoRepeatDelay(300)
      self.BgTrackObjectColor_pushButton.setFlat(False)
      self.BgTrackObjectColor_pushButton.setObjectName(_fromUtf8("BgTrackObjectColor_pushButton"))
      self.separationWidget_2 = QtGui.QWidget(self.BgTrackOptions_frame)
      self.separationWidget_2.setGeometry(QtCore.QRect(0, 30, 311, 31))
      self.separationWidget_2.setObjectName(_fromUtf8("separationWidget_2"))
      self.horizontalLayout_5 = QtGui.QHBoxLayout(self.separationWidget_2)
      self.horizontalLayout_5.setContentsMargins(10, 5, 5, 5)
      self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
      self.BgTrackselectBackgroundPath_lineEdit = QtGui.QLineEdit(self.separationWidget_2)
      self.BgTrackselectBackgroundPath_lineEdit.setObjectName(_fromUtf8("BgTrackselectBackgroundPath_lineEdit"))
      self.horizontalLayout_5.addWidget(self.BgTrackselectBackgroundPath_lineEdit)
      self.BgTrackselectBackgroundPath_toolButton = QtGui.QToolButton(self.separationWidget_2)
      self.BgTrackselectBackgroundPath_toolButton.setObjectName(_fromUtf8("BgTrackselectBackgroundPath_toolButton"))
      self.horizontalLayout_5.addWidget(self.BgTrackselectBackgroundPath_toolButton)
      self.BgTrackPathSelect_label = QtGui.QLabel(self.BgTrackOptions_frame)
      self.BgTrackPathSelect_label.setGeometry(QtCore.QRect(20, 10, 181, 16))
      self.BgTrackPathSelect_label.setObjectName(_fromUtf8("BgTrackPathSelect_label"))
      self.vision_tabWidget.addTab(self.tab, _fromUtf8(""))
      self.fun_tab = QtGui.QWidget()
      self.fun_tab.setObjectName(_fromUtf8("fun_tab"))
      self.frame = QtGui.QFrame(self.fun_tab)
      self.frame.setGeometry(QtCore.QRect(10, 10, 331, 241))
      self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
      self.frame.setFrameShadow(QtGui.QFrame.Raised)
      self.frame.setObjectName(_fromUtf8("frame"))
      self.funBrushSize_horizontalSlider = QtGui.QSlider(self.frame)
      self.funBrushSize_horizontalSlider.setGeometry(QtCore.QRect(30, 120, 191, 21))
      self.funBrushSize_horizontalSlider.setMaximum(255)
      self.funBrushSize_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
      self.funBrushSize_horizontalSlider.setObjectName(_fromUtf8("funBrushSize_horizontalSlider"))
      self.funBrushThreshold_label = QtGui.QLabel(self.frame)
      self.funBrushThreshold_label.setGeometry(QtCore.QRect(80, 140, 71, 16))
      self.funBrushThreshold_label.setObjectName(_fromUtf8("funBrushThreshold_label"))
      self.frame_2 = QtGui.QFrame(self.frame)
      self.frame_2.setGeometry(QtCore.QRect(30, 20, 151, 71))
      self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
      self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
      self.frame_2.setObjectName(_fromUtf8("frame_2"))
      self.formLayout_2 = QtGui.QFormLayout(self.frame_2)
      self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
      self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
      self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
      self.clean_radioButton = QtGui.QRadioButton(self.frame_2)
      self.clean_radioButton.setObjectName(_fromUtf8("clean_radioButton"))
      self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.clean_radioButton)
      self.lamp_radioButton = QtGui.QRadioButton(self.frame_2)
      self.lamp_radioButton.setChecked(True)
      self.lamp_radioButton.setObjectName(_fromUtf8("lamp_radioButton"))
      self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.lamp_radioButton)
      self.funBrushThreshold_spinBox = QtGui.QSpinBox(self.frame)
      self.funBrushThreshold_spinBox.setGeometry(QtCore.QRect(230, 160, 57, 25))
      self.funBrushThreshold_spinBox.setMaximum(255)
      self.funBrushThreshold_spinBox.setObjectName(_fromUtf8("funBrushThreshold_spinBox"))
      self.funObjectColor_pushButton = QtGui.QPushButton(self.frame)
      self.funObjectColor_pushButton.setGeometry(QtCore.QRect(40, 200, 21, 21))
      self.funObjectColor_pushButton.setAutoFillBackground(False)
      self.funObjectColor_pushButton.setStyleSheet(_fromUtf8("background-color: rgb(0,255,0)"))
      self.funObjectColor_pushButton.setText(_fromUtf8(""))
      self.funObjectColor_pushButton.setAutoRepeatDelay(300)
      self.funObjectColor_pushButton.setFlat(False)
      self.funObjectColor_pushButton.setObjectName(_fromUtf8("funObjectColor_pushButton"))
      self.funBrushThreshold_horizontalSlider = QtGui.QSlider(self.frame)
      self.funBrushThreshold_horizontalSlider.setGeometry(QtCore.QRect(30, 160, 191, 21))
      self.funBrushThreshold_horizontalSlider.setMaximum(255)
      self.funBrushThreshold_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
      self.funBrushThreshold_horizontalSlider.setObjectName(_fromUtf8("funBrushThreshold_horizontalSlider"))
      self.funBrushSize_spinBox = QtGui.QSpinBox(self.frame)
      self.funBrushSize_spinBox.setGeometry(QtCore.QRect(230, 120, 57, 25))
      self.funBrushSize_spinBox.setMaximum(255)
      self.funBrushSize_spinBox.setObjectName(_fromUtf8("funBrushSize_spinBox"))
      self.Brush_label_2 = QtGui.QLabel(self.frame)
      self.Brush_label_2.setGeometry(QtCore.QRect(70, 100, 121, 21))
      self.Brush_label_2.setWordWrap(True)
      self.Brush_label_2.setObjectName(_fromUtf8("Brush_label_2"))
      self.funObjectColor_label = QtGui.QLabel(self.frame)
      self.funObjectColor_label.setGeometry(QtCore.QRect(70, 200, 96, 21))
      self.funObjectColor_label.setObjectName(_fromUtf8("funObjectColor_label"))
      self.vision_tabWidget.addTab(self.fun_tab, _fromUtf8(""))
      self.filters_groupBox = QtGui.QGroupBox(self.centralwidget)
      self.filters_groupBox.setGeometry(QtCore.QRect(10, 490, 381, 141))
      self.filters_groupBox.setFlat(False)
      self.filters_groupBox.setCheckable(False)
      self.filters_groupBox.setObjectName(_fromUtf8("filters_groupBox"))
      self.filtersForm_frame = QtGui.QFrame(self.filters_groupBox)
      self.filtersForm_frame.setGeometry(QtCore.QRect(10, 30, 166, 101))
      self.filtersForm_frame.setFrameShape(QtGui.QFrame.StyledPanel)
      self.filtersForm_frame.setFrameShadow(QtGui.QFrame.Raised)
      self.filtersForm_frame.setObjectName(_fromUtf8("filtersForm_frame"))
      self.formLayout_3 = QtGui.QFormLayout(self.filtersForm_frame)
      self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
      self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
      self.canny_radioButton = QtGui.QRadioButton(self.filtersForm_frame)
      self.canny_radioButton.setObjectName(_fromUtf8("canny_radioButton"))
      self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.canny_radioButton)
      self.gaussian_radioButton = QtGui.QRadioButton(self.filtersForm_frame)
      self.gaussian_radioButton.setObjectName(_fromUtf8("gaussian_radioButton"))
      self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.gaussian_radioButton)
      self.median_radioButton = QtGui.QRadioButton(self.filtersForm_frame)
      self.median_radioButton.setObjectName(_fromUtf8("median_radioButton"))
      self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.median_radioButton)
      self.noFilter_radioButton = QtGui.QRadioButton(self.filtersForm_frame)
      self.noFilter_radioButton.setChecked(True)
      self.noFilter_radioButton.setObjectName(_fromUtf8("noFilter_radioButton"))
      self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.noFilter_radioButton)
      self.play_pushButton = QtGui.QPushButton(self.filters_groupBox)
      self.play_pushButton.setEnabled(True)
      self.play_pushButton.setGeometry(QtCore.QRect(240, 30, 61, 61))
      self.play_pushButton.setStyleSheet(_fromUtf8("background-color: transparent"))
      self.play_pushButton.setText(_fromUtf8(""))
      self.play_pushButton.setIconSize(QtCore.QSize(48, 48))
      self.play_pushButton.setFlat(False)
      self.play_pushButton.setObjectName(_fromUtf8("play_pushButton"))
      self.pause_pushButton = QtGui.QPushButton(self.filters_groupBox)
      self.pause_pushButton.setGeometry(QtCore.QRect(290, 30, 71, 61))
      self.pause_pushButton.setStyleSheet(_fromUtf8("background-color: transparent"))
      self.pause_pushButton.setText(_fromUtf8(""))
      self.pause_pushButton.setIconSize(QtCore.QSize(48, 48))
      self.pause_pushButton.setObjectName(_fromUtf8("pause_pushButton"))
      self.clearScreen_pushButton = QtGui.QPushButton(self.filters_groupBox)
      self.clearScreen_pushButton.setEnabled(False)
      self.clearScreen_pushButton.setGeometry(QtCore.QRect(240, 100, 121, 32))
      self.clearScreen_pushButton.setObjectName(_fromUtf8("clearScreen_pushButton"))
      self.activeWindows_groupBox = QtGui.QGroupBox(self.centralwidget)
      self.activeWindows_groupBox.setGeometry(QtCore.QRect(10, 0, 381, 69))
      self.activeWindows_groupBox.setObjectName(_fromUtf8("activeWindows_groupBox"))
      self.activeWindows_comboBox = QtGui.QComboBox(self.activeWindows_groupBox)
      self.activeWindows_comboBox.setGeometry(QtCore.QRect(12, 31, 241, 26))
      self.activeWindows_comboBox.setObjectName(_fromUtf8("activeWindows_comboBox"))
      self.activeWindowsClose_pushButton = QtGui.QPushButton(self.activeWindows_groupBox)
      self.activeWindowsClose_pushButton.setGeometry(QtCore.QRect(273, 30, 91, 32))
      self.activeWindowsClose_pushButton.setObjectName(_fromUtf8("activeWindowsClose_pushButton"))
      MainWindow.setCentralWidget(self.centralwidget)
      self.statusbar = QtGui.QStatusBar(MainWindow)
      self.statusbar.setObjectName(_fromUtf8("statusbar"))
      MainWindow.setStatusBar(self.statusbar)
      self.toolBar = QtGui.QToolBar(MainWindow)
      self.toolBar.setObjectName(_fromUtf8("toolBar"))
      MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
      self.actionClose = QtGui.QAction(MainWindow)
      self.actionClose.setObjectName(_fromUtf8("actionClose"))
      self.actionLoad = QtGui.QAction(MainWindow)
      self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
      self.actionOpen = QtGui.QAction(MainWindow)
      self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
      self.actionExit = QtGui.QAction(MainWindow)
      self.actionExit.setObjectName(_fromUtf8("actionExit"))
      self.actionAbout = QtGui.QAction(MainWindow)
      self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
      self.actionNew_Window = QtGui.QAction(MainWindow)
      self.actionNew_Window.setObjectName(_fromUtf8("actionNew_Window"))
      self.toolBar.addAction(self.actionExit)
      self.toolBar.addSeparator()
      self.toolBar.addAction(self.actionNew_Window)
      self.toolBar.addAction(self.actionAbout)

      self.retranslateUi(MainWindow)
      self.vision_tabWidget.setCurrentIndex(0)
      QtCore.QObject.connect(self.backgroundThreshold_slider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.backgroundThreshold_spinBox.setValue)
      QtCore.QObject.connect(self.backgroundThreshold_spinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.backgroundThreshold_slider.setValue)
      QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
      QtCore.QObject.connect(self.trackingThreshold_horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.trackingThreshold_spinBox.setValue)
      QtCore.QObject.connect(self.trackingBrushThick_spinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.trackingBrushThick_horizontalSlider.setValue)
      QtCore.QObject.connect(self.trackingThreshold_spinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.trackingThreshold_horizontalSlider.setValue)
      QtCore.QObject.connect(self.trackingBrushThick_horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.trackingBrushThick_spinBox.setValue)
      QtCore.QObject.connect(self.selectCamSource_radioButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.selectPath_widget.setDisabled)
      QtCore.QObject.connect(self.BgTrackThreshold_horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.BgTrackThreshold_spinBox.setValue)
      QtCore.QObject.connect(self.BgTrackThreshold_spinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.BgTrackThreshold_horizontalSlider.setValue)
      QtCore.QObject.connect(self.BgTrackBrushThick_horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.BgTrackBrushThick_spinBox.setValue)
      QtCore.QObject.connect(self.BgTrackBrushThick_spinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.BgTrackBrushThick_horizontalSlider.setValue)
      QtCore.QObject.connect(self.funBrushThreshold_horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.funBrushThreshold_spinBox.setValue)
      QtCore.QObject.connect(self.funBrushSize_spinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.funBrushSize_horizontalSlider.setValue)
      QtCore.QObject.connect(self.funBrushThreshold_spinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.funBrushThreshold_horizontalSlider.setValue)
      QtCore.QObject.connect(self.funBrushSize_horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.funBrushSize_spinBox.setValue)
      QtCore.QObject.connect(self.selectVideoSource_radioButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.selectPath_widget.setEnabled)
      QtCore.QMetaObject.connectSlotsByName(MainWindow)

   def retranslateUi(self, MainWindow):
      MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
      self.selectPath_groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Video / Image Selection", None, QtGui.QApplication.UnicodeUTF8))
      self.selectPath_toolButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
      self.selectCamSource_radioButton.setText(QtGui.QApplication.translate("MainWindow", "Webcam", None, QtGui.QApplication.UnicodeUTF8))
      self.selectVideoSource_radioButton.setText(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
      self.vision_groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Computer Vision Technics", None, QtGui.QApplication.UnicodeUTF8))
      self.selectBackgroundPath_toolButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
      self.backgroundPathSelect_label.setText(QtGui.QApplication.translate("MainWindow", "Select Replacement Media", None, QtGui.QApplication.UnicodeUTF8))
      self.backgroundAlgorithm_comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Matrix Operations", None, QtGui.QApplication.UnicodeUTF8))
      self.backgroundAlgorithm_comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Matrix Operations 2", None, QtGui.QApplication.UnicodeUTF8))
      self.backgroundAlgorithm_comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "Movement detection", None, QtGui.QApplication.UnicodeUTF8))
      self.backgroundAlgorithm_comboBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "Brute Force", None, QtGui.QApplication.UnicodeUTF8))
      self.backgroundAlgorithm_label.setText(QtGui.QApplication.translate("MainWindow", "Algorithm", None, QtGui.QApplication.UnicodeUTF8))
      self.backgoundThreshold_label.setText(QtGui.QApplication.translate("MainWindow", "Threshold", None, QtGui.QApplication.UnicodeUTF8))
      self.backgroundColor_label.setText(QtGui.QApplication.translate("MainWindow", "Color to Replace", None, QtGui.QApplication.UnicodeUTF8))
      self.vision_tabWidget.setTabText(self.vision_tabWidget.indexOf(self.background_tab), QtGui.QApplication.translate("MainWindow", "Background Replace", None, QtGui.QApplication.UnicodeUTF8))
      self.trackingMethod_comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Matrix Operations", None, QtGui.QApplication.UnicodeUTF8))
      self.trackingMethod_comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Color Ranges", None, QtGui.QApplication.UnicodeUTF8))
      self.trackingAlgorithm_label.setText(QtGui.QApplication.translate("MainWindow", "Algorithm", None, QtGui.QApplication.UnicodeUTF8))
      self.trackingThreshold_label.setText(QtGui.QApplication.translate("MainWindow", "Threshold", None, QtGui.QApplication.UnicodeUTF8))
      self.trackingBrushColor_label.setText(QtGui.QApplication.translate("MainWindow", "Brush Color", None, QtGui.QApplication.UnicodeUTF8))
      self.tracking_label.setText(QtGui.QApplication.translate("MainWindow", "Select Tracking Method", None, QtGui.QApplication.UnicodeUTF8))
      self.trackingBrushThick_label.setText(QtGui.QApplication.translate("MainWindow", "Brush Thickness", None, QtGui.QApplication.UnicodeUTF8))
      self.trackingObjectColor_label.setText(QtGui.QApplication.translate("MainWindow", "Tracking Color", None, QtGui.QApplication.UnicodeUTF8))
      self.vision_tabWidget.setTabText(self.vision_tabWidget.indexOf(self.tracking_tab), QtGui.QApplication.translate("MainWindow", "Tracking", None, QtGui.QApplication.UnicodeUTF8))
      self.BgTrackMethod_comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Matrix Operations", None, QtGui.QApplication.UnicodeUTF8))
      self.BgTrackMethod_comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Color Range", None, QtGui.QApplication.UnicodeUTF8))
      self.BgTrackAlgorithm_label.setText(QtGui.QApplication.translate("MainWindow", "Algorithm", None, QtGui.QApplication.UnicodeUTF8))
      self.BgTrackThreshold_label.setText(QtGui.QApplication.translate("MainWindow", "Threshold", None, QtGui.QApplication.UnicodeUTF8))
      self.BgTrack_label.setText(QtGui.QApplication.translate("MainWindow", "Select Tracking Method", None, QtGui.QApplication.UnicodeUTF8))
      self.BgTrackBrushThick_label.setText(QtGui.QApplication.translate("MainWindow", "Brush Thickness", None, QtGui.QApplication.UnicodeUTF8))
      self.BgTrackObjectColor_label.setText(QtGui.QApplication.translate("MainWindow", "Tracking color", None, QtGui.QApplication.UnicodeUTF8))
      self.BgTrackselectBackgroundPath_toolButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
      self.BgTrackPathSelect_label.setText(QtGui.QApplication.translate("MainWindow", "Select Replacement Media", None, QtGui.QApplication.UnicodeUTF8))
      self.vision_tabWidget.setTabText(self.vision_tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Both", None, QtGui.QApplication.UnicodeUTF8))
      self.funBrushThreshold_label.setText(QtGui.QApplication.translate("MainWindow", "Threshold", None, QtGui.QApplication.UnicodeUTF8))
      self.clean_radioButton.setText(QtGui.QApplication.translate("MainWindow", "Cleaner Mode", None, QtGui.QApplication.UnicodeUTF8))
      self.lamp_radioButton.setText(QtGui.QApplication.translate("MainWindow", "Lamp mode", None, QtGui.QApplication.UnicodeUTF8))
      self.Brush_label_2.setText(QtGui.QApplication.translate("MainWindow", "Brush Thickness", None, QtGui.QApplication.UnicodeUTF8))
      self.funObjectColor_label.setText(QtGui.QApplication.translate("MainWindow", "Tracking Color", None, QtGui.QApplication.UnicodeUTF8))
      self.vision_tabWidget.setTabText(self.vision_tabWidget.indexOf(self.fun_tab), QtGui.QApplication.translate("MainWindow", "Extra", None, QtGui.QApplication.UnicodeUTF8))
      self.filters_groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Set filters", None, QtGui.QApplication.UnicodeUTF8))
      self.canny_radioButton.setText(QtGui.QApplication.translate("MainWindow", "Canny", None, QtGui.QApplication.UnicodeUTF8))
      self.gaussian_radioButton.setText(QtGui.QApplication.translate("MainWindow", "Gaussian Smooth", None, QtGui.QApplication.UnicodeUTF8))
      self.median_radioButton.setText(QtGui.QApplication.translate("MainWindow", "Median Smooth", None, QtGui.QApplication.UnicodeUTF8))
      self.noFilter_radioButton.setText(QtGui.QApplication.translate("MainWindow", "No filter", None, QtGui.QApplication.UnicodeUTF8))
      self.clearScreen_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Clear screen", None, QtGui.QApplication.UnicodeUTF8))
      self.activeWindows_groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Active windows", None, QtGui.QApplication.UnicodeUTF8))
      self.activeWindowsClose_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
      self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
      self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
      self.actionLoad.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
      self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
      self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
      self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
      self.actionNew_Window.setText(QtGui.QApplication.translate("MainWindow", "New Window", None, QtGui.QApplication.UnicodeUTF8))
      self.actionNew_Window.setToolTip(QtGui.QApplication.translate("MainWindow", "Create new window", None, QtGui.QApplication.UnicodeUTF8))

