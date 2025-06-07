import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon
from mp3_player_ui import Ui_Form  # 방금 생성된 .py 파일

class MP3Player(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 초기 상태: 반복 모드 꺼짐 (loop)
        self.loop_mode = False

        # 버튼 클릭 시 슬롯 연결
        self.ui.PlaybackBtn.clicked.connect(self.toggle_loop_mode)

        # 아이콘 초기 설정
        self.update_loop_icon()

    def toggle_loop_mode(self):
        self.loop_mode = not self.loop_mode
        self.update_loop_icon()

    def update_loop_icon(self):
        if self.loop_mode:
            icon = QIcon("../resources/single_loop_icon.svg")
        else:
            icon = QIcon("../resources/loop_icon.svg")
        self.ui.PlaybackBtn.setIcon(icon)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MP3Player()
    window.show()
    sys.exit(app.exec())