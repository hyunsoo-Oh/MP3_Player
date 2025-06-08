from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon, QKeyEvent
from PySide6.QtCore import Qt
from gui.download_ui import Ui_Dialog
from gui.constants import icon
from download.youtube_search import YoutubeSearchModel, YoutubeCardDelegate, search_youtube

class DownloadDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Download Dialog")
        self.setWindowIcon(QIcon(icon("download_icon.png")))

        # 검색 버튼 연결 및 엔터 연결
        self.ui.searchBtn.setIcon(QIcon(icon("search_icon.svg")))
        self.ui.searchBtn.clicked.connect(self.on_search)

        self.model = YoutubeSearchModel()
        self.delegate = YoutubeCardDelegate()

        self.ui.listView.setModel(self.model)
        self.ui.listView.setItemDelegate(self.delegate)
        self.ui.listView.doubleClicked.connect(self.on_item_selected)

        # 포커스별 엔터 키 처리
        self.ui.searchEdit.returnPressed.connect(self.on_search)
        # 리스트 뷰에서 엔터 키 직접 처리
        self.ui.listView.installEventFilter(self)

    def handle_enter(self):
        focus_widget = self.focusWidget()

        if focus_widget == self.ui.searchEdit:
            # 🔍 검색 입력창에 포커스 있을 때 → 검색
            self.on_search()

        elif focus_widget == self.ui.listView:
            # 🎵 리스트에서 엔터 → 항목 선택
            current_index = self.ui.listView.currentIndex()
            if current_index.isValid():
                self.on_item_selected(current_index)
                self.accept()  # 다이얼로그 닫기

    def on_search(self):
        keyword = self.ui.searchEdit.text().strip()
        results = search_youtube(keyword)
        self.model.update(results)

    def on_item_selected(self, index):
        data = self.model.data(index, Qt.DisplayRole)
        video_id = data['video_id']
        print(f"🎯 선택된 영상 ID: {video_id}")
        # download_audio(video_id) 호출로 MP3 다운로드 연동

    def eventFilter(self, source, event):
        # listView에서 Enter 키 누르면 on_item_selected 실행
        if source == self.ui.listView and isinstance(event, QKeyEvent):
            if event.type() == QKeyEvent.KeyPress and event.key() == Qt.Key_Return:
                index = self.ui.listView.currentIndex()
                if index.isValid():
                    self.on_item_selected(index)
                    return True  # 이벤트 처리 완료 (다른 동작 방지)
        return super().eventFilter(source, event)