import sys
import os
from PySide6.QtWidgets import QApplication, QDialog, QWidget
from PySide6.QtGui import QIcon
from gui.mp3_player_ui import Ui_Form
from gui.downloadDialog import DownloadDialog   # 직접 만들 파일
from gui.constants import icon

class MP3Player(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 초기 상태: 반복 모드 꺼짐 (loop)
        self.loop_mode = False

        # 타이틀 바 텍스트 및 아이콘 설정
        self.setWindowTitle("YouTube MP3 Player")
        self.setWindowIcon(QIcon(icon("mp3_icon.png")))

        # 버튼 클릭 시 슬롯 연결
        self.ui.PlaybackBtn.clicked.connect(self.toggle_loop_mode)

        # Download 버튼에 연결 추가
        self.ui.downloadBtn.clicked.connect(self.open_download_ui)

        # 아이콘 초기 설정
        self.update_loop_icon()

    def toggle_loop_mode(self):
        self.loop_mode = not self.loop_mode
        self.update_loop_icon()

    def update_loop_icon(self):
        if self.loop_mode:
            icon_path = "single_vector_icon.svg"
        else:
            icon_path = "loop_icon.svg"
        self.ui.PlaybackBtn.setIcon(QIcon(icon(icon_path)))

    def open_download_ui(self):
        dialog = DownloadDialog(self)  # QDialog 상속한 클래스
        dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MP3Player()
    window.show()
    sys.exit(app.exec())