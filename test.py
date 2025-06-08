from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QListWidget, QListWidgetItem
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube 검색 테스트")
        self.resize(600, 400)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("검색어 입력")
        layout.addWidget(self.search_input)

        self.search_button = QPushButton("검색")
        layout.addWidget(self.search_button)

        self.result_list = QListWidget()
        layout.addWidget(self.result_list)

        self.search_button.clicked.connect(self.start_search)

    def start_search(self):
        query = self.search_input.text().strip()
        if not query:
            return

        self.result_list.clear()
        self.search_thread = YouTubeSearchThread(query)
        self.search_thread.search_completed.connect(self.display_results)
        self.search_thread.search_error.connect(self.display_error)
        self.search_thread.start()

    def display_results(self, results):
        for result in results:
            item = QListWidgetItem()
            widget = SearchResultWidget(result)
            item.setSizeHint(widget.sizeHint())
            self.result_list.addItem(item)
            self.result_list.setItemWidget(item, widget)

    def display_error(self, msg):
        error_item = QListWidgetItem(f"검색 오류: {msg}")
        self.result_list.addItem(error_item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())