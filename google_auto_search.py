import sys
import time
import os
import random
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QComboBox, QTextEdit,
    QFrame, QTabWidget, QFormLayout, QCheckBox, QSpinBox, QSlider,
    QProgressBar, QMessageBox
)
from PyQt6.QtCore import (
    Qt, QThread, pyqtSignal, QPropertyAnimation, QEasingCurve, QRect
)
from PyQt6.QtGui import (
    QFont, QColor, QCursor, QIcon
)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ================================
# LANGUAGES
# ================================
LANGUAGES = {
    "English": {
        "code": "en", "dir": "ltr",
        "title": "Google Auto Search with Selenium",
        "search_label": "Search Query:", "search_placeholder": "Enter your search term...",
        "delay_label": "Human-like Delay (ms):", "click_first_label": "Click First Result",
        "headless_label": "Headless Mode", "start_button": "Start Search",
        "stop_button": "Stop", "log_title": "Execution Log",
        "status_ready": "Ready", "status_running": "Running...", "status_error": "Error!",
        "status_done": "Done!", "tab_general": "General", "tab_log": "Log",
        "tab_about": "About", "about_text": "<h3>Google Auto Search</h3><p>Simulates human search using Selenium.</p>",
        "theme_system": "System", "theme_light": "Light", "theme_dark": "Dark",
        "theme_red": "Red", "theme_blue": "Blue"
    },
    "فارسی": {
        "code": "fa", "dir": "rtl",
        "title": "جستجوی خودکار گوگل با سلنیوم",
        "search_label": "عبارت جستجو:", "search_placeholder": "عبارت جستجو را وارد کنید...",
        "delay_label": "تاخیر انسانی (میلی‌ثانیه):", "click_first_label": "کلیک روی اولین نتیجه",
        "headless_label": "حالت بدون رابط", "start_button": "شروع جستجو",
        "stop_button": "توقف", "log_title": "گزارش اجرا",
        "status_ready": "آماده", "status_running": "در حال اجرا...", "status_error": "خطا!",
        "status_done": "انجام شد!", "tab_general": "عمومی", "tab_log": "گزارش",
        "tab_about": "درباره", "about_text": "<h3>جستجوی خودکار گوگل</h3><p>شبیه‌سازی رفتار انسانی با سلنیوم.</p>",
        "theme_system": "سیستم", "theme_light": "روشن", "theme_dark": "تیره",
        "theme_red": "قرمز", "theme_blue": "آبی"
    },
    "中文": {
        "code": "zh", "dir": "ltr",
        "title": "使用 Selenium 自动谷歌搜索",
        "search_label": "搜索词:", "search_placeholder": "输入搜索内容...",
        "delay_label": "人类延迟 (毫秒):", "click_first_label": "点击第一个结果",
        "headless_label": "无头模式", "start_button": "开始搜索",
        "stop_button": "停止", "log_title": "执行日志",
        "status_ready": "就绪", "status_running": "运行中...", "status_error": "错误!",
        "status_done": "完成!", "tab_general": "常规", "tab_log": "日志",
        "tab_about": "关于", "about_text": "<h3>谷歌自动搜索</h3><p>使用 Selenium 模拟人类行为。</p>",
        "theme_system": "系统", "theme_light": "亮色", "theme_dark": "暗色",
        "theme_red": "红色", "theme_blue": "蓝色"
    },
    "Русский": {
        "code": "ru", "dir": "ltr",
        "title": "Автоматический поиск Google с Selenium",
        "search_label": "Запрос:", "search_placeholder": "Введите запрос...",
        "delay_label": "Задержка (мс):", "click_first_label": "Клик по первому результату",
        "headless_label": "Без GUI", "start_button": "Начать",
        "stop_button": "Стоп", "log_title": "Журнал",
        "status_ready": "Готов", "status_running": "Выполняется...", "status_error": "Ошибка!",
        "status_done": "Готово!", "tab_general": "Общие", "tab_log": "Лог",
        "tab_about": "О программе", "about_text": "<h3>Автоматический поиск Google</h3><p>Имитация поведения с Selenium.</p>",
        "theme_system": "Система", "theme_light": "Светлая", "theme_dark": "Тёмная",
        "theme_red": "Красная", "theme_blue": "Синяя"
    }
}

# ================================
# THEMES
# ================================
THEMES = {
    "System": {"bg": "#F5F5F5", "fg": "#000000", "accent": "#0078D4", "card": "#FFFFFF", "border": "#CCCCCC"},
    "Light":  {"bg": "#FAFAFA", "fg": "#000000", "accent": "#0078D4", "card": "#FFFFFF", "border": "#E0E0E0"},
    "Dark":   {"bg": "#1E1E1E", "fg": "#FFFFFF", "accent": "#0A84FF", "card": "#2D2D2D", "border": "#404040"},
    "Red":    {"bg": "#2B1A1A", "fg": "#FFFFFF", "accent": "#D32F2F", "card": "#3D2A2A", "border": "#5D3A3A"},
    "Blue":   {"bg": "#1A2B3C", "fg": "#FFFFFF", "accent": "#1B9CFC", "card": "#2A3B4C", "border": "#3A5B7C"}
}

# ================================
# WORKER THREAD
# ================================
class SearchWorker(QThread):
    log_signal = pyqtSignal(str)
    status_signal = pyqtSignal(str)
    finished_signal = pyqtSignal()
    error_signal = pyqtSignal(str)

    def __init__(self, query, delay, click_first, headless):
        super().__init__()
        self.query = query
        self.delay = delay / 1000.0
        self.click_first = click_first
        self.headless = headless
        self._stop = False

    def human_type(self, element, text):
        for char in text:
            if self._stop: return
            element.send_keys(char)
            time.sleep(random.uniform(0.05, 0.15))

    def run(self):
        driver = None
        try:
            self.log_signal.emit("Initializing Chrome driver...")
            opts = Options()
            if self.headless:
                opts.add_argument("--headless=new")  # Updated headless mode
            opts.add_argument("--no-sandbox")
            opts.add_argument("--disable-dev-shm-usage")
            opts.add_argument("--disable-blink-features=AutomationControlled")
            opts.add_experimental_option("excludeSwitches", ["enable-automation"])
            opts.add_experimental_option("useAutomationExtension", False)

            # Set user agent to avoid detection
            opts.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")

            driver = webdriver.Chrome(options=opts)
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
            self.log_signal.emit("Driver initialized successfully.")

            self.log_signal.emit("Opening Google...")
            driver.get("https://www.google.com")
            time.sleep(2 + random.random())
            self.log_signal.emit("Google page loaded.")

            # Wait for search box
            self.log_signal.emit("Waiting for search box...")
            box = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
            box.click()
            time.sleep(0.5)
            self.log_signal.emit(f"Typing query: '{self.query}'")
            self.human_type(box, self.query)
            time.sleep(self.delay)
            box.send_keys(Keys.RETURN)
            self.log_signal.emit("Search submitted.")

            # Wait for results
            self.log_signal.emit("Waiting for search results...")
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div#search"))
            )
            time.sleep(3 + random.random() * 2)

            if self.click_first:
                self.log_signal.emit("Looking for first result...")
                first_result = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
                )
                parent_link = first_result.find_element(By.XPATH, "./ancestor::a")
                href = parent_link.get_attribute("href")
                self.log_signal.emit(f"Found first result: {href}")
                parent_link.click()
                self.log_signal.emit("Clicked on first result.")
                time.sleep(3)

            self.status_signal.emit("done")
            self.log_signal.emit("Search completed successfully!")
        except Exception as e:
            error_msg = f"Selenium Error: {str(e)}"
            self.error_signal.emit(error_msg)
            self.status_signal.emit("error")
            self.log_signal.emit(error_msg)
        finally:
            if driver:
                try:
                    driver.quit()
                    self.log_signal.emit("Browser closed.")
                except:
                    pass
            if not self._stop:
                self.finished_signal.emit()

    def stop(self):
        self._stop = True


# ================================
# ANIMATED BUTTON
# ================================
class AnimatedButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(150)
        self.anim.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.orig = self.geometry()

    def enterEvent(self, e):
        r = self.geometry()
        nr = QRect(r.x()-3, r.y()-3, r.width()+6, r.height()+6)
        self.anim.setStartValue(r)
        self.anim.setEndValue(nr)
        self.anim.start()
        super().enterEvent(e)

    def leaveEvent(self, e):
        self.anim.setStartValue(self.geometry())
        self.anim.setEndValue(self.orig)
        self.anim.start()
        super().leaveEvent(e)


# ================================
# CARD WIDGET
# ================================
class ModernCard(QFrame):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.setObjectName("card")
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setStyleSheet("border-radius: 12px;")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(8)

        t = QLabel(title)
        t.setObjectName("cardTitle")
        t.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        layout.addWidget(t)

        self.content = QWidget()
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.content)

    def add_widget(self, widget):
        self.content_layout.addWidget(widget)


# ================================
# MAIN WINDOW
# ================================
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lang = "فارسی"
        self.theme = "System"
        self.worker = None
        self.init_ui()
        self.apply_lang()
        self.apply_theme()

    def init_ui(self):
        self.setWindowTitle("Google Auto Search")
        self.setMinimumSize(960, 640)

        central = QWidget()
        self.setCentralWidget(central)
        main = QVBoxLayout(central)
        main.setContentsMargins(20, 20, 20, 20)
        main.setSpacing(16)

        # Header
        header = QHBoxLayout()
        title = QLabel("Google Auto Search")
        title.setObjectName("title")
        title.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        header.addWidget(title)
        header.addStretch()

        self.lang_combo = QComboBox()
        self.lang_combo.addItems(LANGUAGES.keys())
        self.lang_combo.setCurrentText(self.lang)
        self.lang_combo.currentTextChanged.connect(self.change_lang)
        header.addWidget(QLabel("Language:"))
        header.addWidget(self.lang_combo)

        self.theme_combo = QComboBox()
        self.theme_combo.addItems(THEMES.keys())
        self.theme_combo.setCurrentText(self.theme)
        self.theme_combo.currentTextChanged.connect(self.change_theme)
        header.addWidget(QLabel("Theme:"))
        header.addWidget(self.theme_combo)

        main.addLayout(header)

        # Tabs
        self.tabs = QTabWidget()
        main.addWidget(self.tabs)

        # Tab 1: General
        tab1 = QWidget()
        t1 = QVBoxLayout(tab1)

        card = ModernCard("Search Settings")
        form_widget = QWidget()
        form = QFormLayout(form_widget)
        form.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        form.setHorizontalSpacing(12)
        form.setVerticalSpacing(10)

        self.query_input = QLineEdit()
        self.query_input.setPlaceholderText("...")
        self.query_input.setMinimumHeight(36)
        form.addRow("Search Query:", self.query_input)

        delay_lay = QHBoxLayout()
        self.delay_spin = QSpinBox()
        self.delay_spin.setRange(100, 5000)
        self.delay_spin.setValue(800)
        self.delay_spin.setSuffix(" ms")
        self.delay_slider = QSlider(Qt.Orientation.Horizontal)
        self.delay_slider.setRange(100, 5000)
        self.delay_slider.setValue(800)
        self.delay_slider.valueChanged.connect(self.delay_spin.setValue)
        self.delay_spin.valueChanged.connect(self.delay_slider.setValue)
        delay_lay.addWidget(self.delay_spin)
        delay_lay.addWidget(self.delay_slider)
        form.addRow("Delay:", delay_lay)

        self.click_cb = QCheckBox()
        self.click_cb.setChecked(True)
        form.addRow(self.click_cb)

        self.headless_cb = QCheckBox()
        form.addRow(self.headless_cb)

        card.add_widget(form_widget)
        t1.addWidget(card)

        # Buttons
        btn_lay = QHBoxLayout()
        btn_lay.addStretch()
        self.start_btn = AnimatedButton("Start")
        self.start_btn.setMinimumSize(160, 44)
        self.start_btn.clicked.connect(self.start_search)
        self.stop_btn = AnimatedButton("Stop")
        self.stop_btn.setMinimumSize(120, 44)
        self.stop_btn.setEnabled(False)
        self.stop_btn.clicked.connect(self.stop_search)
        btn_lay.addWidget(self.start_btn)
        btn_lay.addWidget(self.stop_btn)
        t1.addLayout(btn_lay)

        self.status = QLabel("Ready")
        self.status.setObjectName("status")
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status.setMinimumHeight(36)
        t1.addWidget(self.status)

        self.progress = QProgressBar()
        self.progress.setRange(0, 0)
        self.progress.setTextVisible(False)
        self.progress.setVisible(False)
        t1.addWidget(self.progress)

        self.tabs.addTab(tab1, "General")

        # Tab 2: Log
        tab2 = QWidget()
        t2 = QVBoxLayout(tab2)
        log_card = ModernCard("Log")
        self.log_edit = QTextEdit()
        self.log_edit.setReadOnly(True)
        self.log_edit.setMinimumHeight(260)
        self.log_edit.setFont(QFont("Consolas", 9))
        log_card.add_widget(self.log_edit)
        t2.addWidget(log_card)
        clear = AnimatedButton("Clear")
        clear.clicked.connect(self.log_edit.clear)
        t2.addWidget(clear, alignment=Qt.AlignmentFlag.AlignRight)
        self.tabs.addTab(tab2, "Log")

        # Tab 3: About
        tab3 = QWidget()
        t3 = QVBoxLayout(tab3)
        self.about_label = QLabel()
        self.about_label.setWordWrap(True)
        self.about_label.setOpenExternalLinks(True)
        t3.addWidget(self.about_label)
        t3.addStretch()
        self.tabs.addTab(tab3, "About")

    def change_lang(self, l):
        self.lang = l
        self.apply_lang()

    def change_theme(self, t):
        self.theme = t
        self.apply_theme()

    def apply_lang(self):
        tr = LANGUAGES[self.lang]
        self.setLayoutDirection(Qt.LayoutDirection.LeftToRight if tr["dir"] == "ltr" else Qt.LayoutDirection.RightToLeft)
        self.setWindowTitle(tr["title"])

        self.tabs.setTabText(0, tr["tab_general"])
        self.tabs.setTabText(1, tr["tab_log"])
        self.tabs.setTabText(2, tr["tab_about"])

        self.query_input.setPlaceholderText(tr["search_placeholder"])
        self.click_cb.setText(tr["click_first_label"])
        self.headless_cb.setText(tr["headless_label"])
        self.start_btn.setText(tr["start_button"])
        self.stop_btn.setText(tr["stop_button"])

        # Card titles
        search_card_title = self.tabs.widget(0).layout().itemAt(0).widget().layout().itemAt(0).widget()
        search_card_title.setText(tr.get("search_label", "Search Settings") if self.lang != "English" else "Search Settings")
        log_card_title = self.tabs.widget(1).layout().itemAt(0).widget().layout().itemAt(0).widget()
        log_card_title.setText(tr["log_title"])

        # About
        self.about_label.setText(tr["about_text"])

    def apply_theme(self):
        th = THEMES[self.theme]
        accent = th["accent"]
        css = f"""
        QMainWindow {{ background: {th["bg"]}; color: {th["fg"]}; }}
        #title {{ color: {accent}; }}
        #card {{ background: {th["card"]}; border: 1px solid {th["border"]}; border-radius: 12px; }}
        #cardTitle {{ color: {accent}; }}
        QLineEdit, QTextEdit, QSpinBox {{
            background: {th["card"]}; border: 1px solid {th["border"]}; border-radius: 8px;
            padding: 6px; color: {th["fg"]};
        }}
        QLineEdit:focus {{ border: 2px solid {accent}; }}
        QPushButton {{
            background: {accent}; color: white; border: none; border-radius: 10px;
            padding: 10px 20px; font-weight: bold;
        }}
        QPushButton:hover {{ background: {self.darken(accent, 15)}; }}
        QPushButton:pressed {{ background: {self.darken(accent, 30)}; }}
        QPushButton:disabled {{ background: #888; }}
        QComboBox {{
            background: {th["card"]}; border: 1px solid {th["border"]}; border-radius: 8px;
            padding: 6px; color: {th["fg"]};
        }}
        QTabWidget::pane {{ border: 1px solid {th["border"]}; background: {th["bg"]}; border-radius: 12px; }}
        QTabBar::tab {{
            background: {th["card"]}; border: 1px solid {th["border"]}; padding: 8px 16px;
            border-top-left-radius: 10px; border-top-right-radius: 10px;
        }}
        QTabBar::tab:selected {{ background: {accent}; color: white; }}
        #status {{ background: {th["card"]}; border: 1px solid {th["border"]}; border-radius: 8px; padding: 8px; font-weight: bold; }}
        QProgressBar {{ border: 1px solid {th["border"]}; border-radius: 8px; }}
        QProgressBar::chunk {{ background: {accent}; }}
        QCheckBox {{ color: {th["fg"]}; }}
        QCheckBox::indicator {{ width: 16px; height: 16px; border-radius: 4px; border: 2px solid {th["border"]}; }}
        QCheckBox::indicator:checked {{ background: {accent}; border: 2px solid {accent}; }}
        """
        self.setStyleSheet(css)

    def darken(self, color, amount):
        c = QColor(color)
        return QColor(max(0, c.red() - amount), max(0, c.green() - amount), max(0, c.blue() - amount)).name()

    def log_message(self, msg):
        t = time.strftime("%H:%M:%S")
        self.log_edit.append(f"[{t}] {msg}")
        self.log_edit.ensureCursorVisible()

    def start_search(self):
        q = self.query_input.text().strip()
        if not q:
            QMessageBox.warning(self, "Warning", "Please enter a search query!")
            return

        # Reset log
        self.log_edit.clear()
        self.log_message("Starting search process...")

        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.progress.setVisible(True)
        self.status.setText(LANGUAGES[self.lang]["status_running"])

        self.worker = SearchWorker(
            query=q,
            delay=self.delay_spin.value(),
            click_first=self.click_cb.isChecked(),
            headless=self.headless_cb.isChecked()
        )
        self.worker.log_signal.connect(self.log_message)
        self.worker.status_signal.connect(self.set_status)
        self.worker.finished_signal.connect(self.search_done)
        self.worker.error_signal.connect(self.search_error)
        self.worker.start()

    def stop_search(self):
        if self.worker and self.worker.isRunning():
            self.worker.stop()
            self.worker.terminate()
            self.log_message("Search stopped by user.")
            self.search_done()

    def set_status(self, s):
        tr = LANGUAGES[self.lang]
        self.status.setText(tr["status_done"] if s == "done" else tr["status_error"])

    def search_done(self):
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.progress.setVisible(False)
        self.status.setText(LANGUAGES[self.lang]["status_ready"])

    def search_error(self, e):
        self.log_message(f"Error: {e}")
        QMessageBox.critical(self, "Error", f"An error occurred:\n{e}")
        self.search_done()


# ================================
# RUN
# ================================
def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # Check if ChromeDriver is available
    try:
        webdriver.Chrome()
    except Exception as e:
        QMessageBox.critical(None, "Error", f"ChromeDriver not found or incompatible:\n{e}\n\nPlease install ChromeDriver and add it to PATH.")
        return

    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()