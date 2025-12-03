from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QTabWidget, QTextEdit, QListWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap, QColor, QPalette

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("제임스돈 아이디 관리 통합 프로그램")
        self.setGeometry(100, 100, 1200, 800)
        self.setup_ui()
        self.apply_cute_style()
    
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        header = QLabel("제임스돈 아이디 관리 통합 프로그램")
        header.setAlignment(Qt.AlignCenter)
        header_font = QFont("맑은 고딕", 24, QFont.Bold)
        header.setFont(header_font)
        main_layout.addWidget(header)
        
        tabs = QTabWidget()
        tabs.addTab(self.create_account_tab(), "계정 관리")
        tabs.addTab(self.create_streamer_tab(), "스트리머 관리")
        tabs.addTab(self.create_prism_tab(), "프리즘 관리")
        tabs.addTab(self.create_settings_tab(), "설정")
        
        main_layout.addWidget(tabs)
    
    def create_account_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        
        title = QLabel("구글 계정 관리 (최대 1000개)")
        title_font = QFont("맑은 고딕", 14, QFont.Bold)
        title.setFont(title_font)
        layout.addWidget(title)
        
        input_label = QLabel("계정 정보 입력 (구글아이디 비번 2FA인증키 형식으로 한 줄씩):")
        layout.addWidget(input_label)
        
        self.account_input = QTextEdit()
        self.account_input.setPlaceholderText("예시:\naccount1@gmail.com password123 2FAKEY123\naccount2@gmail.com password456 2FAKEY456")
        layout.addWidget(self.account_input)
        
        button_layout = QHBoxLayout()
        save_btn = QPushButton("저장하기")
        save_btn.clicked.connect(self.save_accounts)
        button_layout.addWidget(save_btn)
        
        check_btn = QPushButton("계정 상태 확인")
        check_btn.clicked.connect(self.check_accounts)
        button_layout.addWidget(check_btn)
        
        layout.addLayout(button_layout)
        
        self.account_list = QListWidget()
        layout.addWidget(self.account_list)
        
        return widget
    
    def create_streamer_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        
        title = QLabel("스트리머 관리 (최대 10명)")
        title_font = QFont("맑은 고딕", 14, QFont.Bold)
        title.setFont(title_font)
        layout.addWidget(title)
        
        self.streamer_list = QListWidget()
        self.streamer_list.addItems(["제임스", "마포짱", "몽콕", "판다실장", "존피디", "떙치리", "존피디"])
        layout.addWidget(self.streamer_list)
        
        button_layout = QHBoxLayout()
        add_btn = QPushButton("스트리머 추가")
        add_btn.clicked.connect(self.add_streamer)
        button_layout.addWidget(add_btn)
        
        edit_btn = QPushButton("스트리머 설정")
        edit_btn.clicked.connect(self.edit_streamer)
        button_layout.addWidget(edit_btn)
        
        layout.addLayout(button_layout)
        
        return widget
    
    def create_prism_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        
        title = QLabel("프리즘 인스턴스 관리 (최대 6개)")
        title_font = QFont("맑은 고딕", 14, QFont.Bold)
        title.setFont(title_font)
        layout.addWidget(title)
        
        status_label = QLabel("프리즘 상태:")
        layout.addWidget(status_label)
        
        self.prism_list = QListWidget()
        for i in range(1, 7):
            self.prism_list.addItem(f"프리즘 {i}: 대기 중")
        layout.addWidget(self.prism_list)
        
        button_layout = QHBoxLayout()
        start_btn = QPushButton("프리즘 시작")
        start_btn.clicked.connect(self.start_prism)
        button_layout.addWidget(start_btn)
        
        stop_btn = QPushButton("프리즘 중지")
        stop_btn.clicked.connect(self.stop_prism)
        button_layout.addWidget(stop_btn)
        
        layout.addLayout(button_layout)
        
        return widget
    
    def create_settings_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        
        title = QLabel("설정")
        title_font = QFont("맑은 고딕", 14, QFont.Bold)
        title.setFont(title_font)
        layout.addWidget(title)
        
        info_label = QLabel("프리즘 경로, 데이터베이스 설정 등을 여기서 관리합니다.")
        layout.addWidget(info_label)
        
        return widget
    
    def apply_cute_style(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(255, 240, 245))
        palette.setColor(QPalette.WindowText, QColor(75, 0, 130))
        palette.setColor(QPalette.Base, QColor(255, 250, 250))
        palette.setColor(QPalette.AlternateBase, QColor(255, 230, 240))
        palette.setColor(QPalette.Button, QColor(255, 182, 193))
        palette.setColor(QPalette.ButtonText, QColor(139, 0, 139))
        palette.setColor(QPalette.Highlight, QColor(255, 105, 180))
        palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
        self.setPalette(palette)
        
        self.setStyleSheet("""
            QPushButton {
                background-color: #FFB6C1;
                border: 2px solid #FF69B4;
                border-radius: 10px;
                padding: 8px;
                font-weight: bold;
                color: #8B008B;
            }
            QPushButton:hover {
                background-color: #FF69B4;
                color: white;
            }
            QPushButton:pressed {
                background-color: #FF1493;
            }
            QTabWidget::pane {
                border: 2px solid #FFB6C1;
                border-radius: 5px;
                background-color: #FFF0F5;
            }
            QTabBar::tab {
                background-color: #FFE4E1;
                border: 1px solid #FFB6C1;
                padding: 8px 20px;
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
            }
            QTabBar::tab:selected {
                background-color: #FFB6C1;
                color: #8B008B;
                font-weight: bold;
            }
            QListWidget {
                border: 2px solid #FFB6C1;
                border-radius: 5px;
                background-color: white;
            }
            QTextEdit {
                border: 2px solid #FFB6C1;
                border-radius: 5px;
                background-color: white;
            }
        """)
    
    def save_accounts(self):
        text = self.account_input.toPlainText()
        lines = text.strip().split('\n')
        count = 0
        for line in lines:
            if line.strip():
                parts = line.strip().split()
                if len(parts) >= 2:
                    count += 1
        self.account_list.addItem(f"저장된 계정: {count}개")
    
    def check_accounts(self):
        self.account_list.addItem("계정 상태 확인 중...")
    
    def add_streamer(self):
        self.streamer_list.addItem("새 스트리머")
    
    def edit_streamer(self):
        current_item = self.streamer_list.currentItem()
        if current_item:
            self.streamer_list.addItem(f"{current_item.text()} 설정 열기")
    
    def start_prism(self):
        current_item = self.prism_list.currentItem()
        if current_item:
            current_item.setText(current_item.text().replace("대기 중", "실행 중"))
    
    def stop_prism(self):
        current_item = self.prism_list.currentItem()
        if current_item:
            current_item.setText(current_item.text().replace("실행 중", "대기 중"))

