# main.py
import sys
from PySide6.QtWidgets import QApplication
from gui.mainWindow import MP3Player  # 여기서 가져오면 됩니다

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MP3Player()
    window.show()
    sys.exit(app.exec())
