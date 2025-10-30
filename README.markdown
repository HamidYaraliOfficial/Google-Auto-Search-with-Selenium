# Google Auto Search with Selenium

---

## English

### Overview
**Google Auto Search with Selenium** is a modern, elegant desktop application built with **Python** and **PyQt6** that **automates Google searches** using **Selenium WebDriver**. It simulates **human-like behavior** with random delays, realistic typing, and optional result clicking — perfect for web scraping, automation testing, or educational purposes.

Featuring a **multilingual interface**, **animated UI components**, **custom themes**, and **real-time execution logs**, this tool brings professional-grade browser automation to your desktop.

---

### Key Features
- **Human-like Search Simulation**:
  - Realistic character-by-character typing
  - Random delays between actions
  - Natural mouse and keyboard behavior
- **Selenium-Powered Automation**:
  - Full Chrome control
  - Headless or visible mode
  - Anti-detection techniques
- **Interactive UI**:
  - Modern **card-based design**
  - **Animated buttons** with hover effects
  - **Live execution log**
  - **Progress feedback**
- **Multilingual Support**:
  - English, Persian (فارسی), Chinese (中文), Russian (Русский)
  - Full **RTL layout** for Persian
- **5 Stunning Themes**:
  - System (auto-detect)
  - Light
  - Dark
  - Red
  - Blue
- **Configurable Options**:
  - Custom delay (100–5000 ms)
  - Click first result
  - Headless mode
- **Safe & Reliable**:
  - Threaded execution
  - Graceful stop
  - Error handling

---

### Requirements
- Python 3.8+
- PyQt6
- Selenium
- Google Chrome
- **ChromeDriver** (matching your Chrome version)

---

### Installation
1. Install dependencies:
   ```bash
   pip install PyQt6 selenium
   ```
2. Download **ChromeDriver** from [chromedriver.chromium.org](https://chromedriver.chromium.org/)
3. Place `chromedriver.exe` (Windows) or `chromedriver` (Linux/macOS) in your `PATH`
4. Save the script as `google_auto_search.py`
5. Run:
   ```bash
   python google_auto_search.py
   ```

---

### Usage
1. Enter your **search query**
2. Adjust **delay** using slider or spinbox
3. Enable **"Click First Result"** if needed
4. Toggle **Headless Mode** for background operation
5. Click **"Start Search"**
6. Monitor progress in the **Log** tab
7. Use **"Stop"** to cancel anytime

> Pro Tip: Use **headless + delay > 1500ms** for stealth automation.

---

### Project Structure
- `google_auto_search.py` – Complete standalone application
- No external assets required

---

### Contributing
Contributions are highly encouraged!  
You can:
- Add proxy support
- Support multiple search engines
- Export results
- Add scheduling
- Improve anti-bot bypass

Submit a **Pull Request** with clear descriptions.

---

### License
Released under the **MIT License**. Free for personal and commercial use.

---

## فارسی

### نمای کلی
**جستجوی خودکار گوگل با سلنیوم** یک برنامه دسکتاپ زیبا و حرفه‌ای است که با **پایتون** و **PyQt6** ساخته شده و با استفاده از **Selenium WebDriver** جستجو در گوگل را **به صورت خودکار و شبیه به رفتار انسانی** انجام می‌دهد. این ابزار با تأخیرهای تصادفی، تایپ واقعی و کلیک اختیاری روی نتایج، برای **وب اسکریپینگ**، **تست اتوماسیون** یا **آموزش** ایده‌آل است.

با رابط **چندزبانه**، **دکمه‌های انیمیشنی**، **تم‌های سفارشی** و **گزارش لحظه‌ای**، این ابزار اتوماسیون مرورگر را در سطح حرفه‌ای ارائه می‌دهد.

---

### ویژگی‌های کلیدی
- **شبیه‌سازی جستجوی انسانی**:
  - تایپ کاراکتر به کاراکتر
  - تأخیرهای تصادفی
  - رفتار طبیعی ماوس و کیبورد
- **اتوماسیون با سلنیوم**:
  - کنترل کامل کروم
  - حالت نمایان یا بدون رابط
  - تکنیک‌های ضد تشخیص
- **رابط کاربری تعاملی**:
  - طراحی **کارتی مدرن**
  - **دکمه‌های انیمیشنی**
  - **گزارش زنده اجرا**
  - **نمایش پیشرفت**
- **پشتیبانی چندزبانه**:
  - فارسی، انگلیسی، چینی، روسی
  - پشتیبانی کامل از **چیدمان راست‌به‌چپ**
- **۵ تم خیره‌کننده**:
  - سیستم (تشخیص خودکار)
  - روشن
  - تاریک
  - قرمز
  - آبی
- **گزینه‌های قابل تنظیم**:
  - تأخیر دلخواه (۱۰۰ تا ۵۰۰۰ میلی‌ثانیه)
  - کلیک روی اولین نتیجه
  - حالت بدون رابط
- **ایمن و پایدار**:
  - اجرای ترد جدا
  - توقف ایمن
  - مدیریت خطا

---

### پیش‌نیازها
- پایتون ۳.۸ یا بالاتر
- PyQt6
- Selenium
- گوگل کروم
- **ChromeDriver** (متناسب با نسخه کروم)

---

### نصب
1. نصب کتابخانه‌ها:
   ```bash
   pip install PyQt6 selenium
   ```
2. دانلود **ChromeDriver** از [chromedriver.chromium.org](https://chromedriver.chromium.org/)
3. قرار دادن `chromedriver.exe` (ویندوز) یا `chromedriver` (لینوکس/مک) در `PATH`
4. ذخیره اسکریپت با نام `google_auto_search.py`
5. اجرا:
   ```bash
   python google_auto_search.py
   ```

---

### نحوه استفاده
1. **عبارت جستجو** را وارد کنید
2. **تأخیر** را با اسلایدر یا عدد تنظیم کنید
3. در صورت نیاز **«کلیک روی اولین نتیجه»** را فعال کنید
4. برای اجرای پس‌زمینه، **«حالت بدون رابط»** را فعال کنید
5. روی **«شروع جستجو»** کلیک کنید
6. پیشرفت را در تب **«گزارش»** دنبال کنید
7. در هر زمان با **«توقف»** عملیات را متوقف کنید

> نکته حرفه‌ای: از **حالت بدون رابط + تأخیر بیش از ۱۵۰۰ میلی‌ثانیه** برای اتوماسیون مخفی استفاده کنید.

---

### ساختار پروژه
- `google_auto_search.py` – برنامه کامل و مستقل
- بدون نیاز به فایل خارجی

---

### مشارکت
مشارکت شما بسیار ارزشمند است!  
می‌توانید:
- پشتیبانی از پروکسی اضافه کنید
- موتورهای جستجوی دیگر را پشتیبانی کنید
- خروجی نتایج را ذخیره کنید
- زمان‌بندی اضافه کنید
- تکنیک‌های ضد ربات را بهبود دهید

درخواست کشش (Pull Request) با توضیحات واضح ارسال کنید.

---

### مجوز
تحت **مجوز MIT** منتشر شده است. آزاد برای استفاده شخصی و تجاری.

---

## 中文

### 项目概览
**使用 Selenium 自动谷歌搜索** 是一款优雅现代的桌面应用程序，使用 **Python** 和 **PyQt6** 构建，通过 **Selenium WebDriver** 实现 **自动化谷歌搜索**。它模拟**人类行为**，包括随机延迟、真实打字和可选的结果点击 — 适用于网页抓取、自动化测试或教育用途。

具备**多语言界面**、**动画组件**、**自定义主题**和**实时日志**，该工具将专业级浏览器自动化带到您的桌面。

---

### 核心功能
- **人性化搜索模拟**：
  - 逐字真实输入
  - 随机动作间隔
  - 自然鼠标键盘行为
- **Selenium 驱动自动化**：
  - 完全控制 Chrome
  - 有界面或无头模式
  - 反检测技术
- **交互式界面**：
  - 现代**卡片式设计**
  - **动画按钮**
  - **实时执行日志**
  - **进度反馈**
- **多语言支持**：
  - 中文、英语、波斯语、俄语
  - 完整支持**从右到左 (RTL)** 布局
- **5 种精美主题**：
  - 系统（自动检测）
  - 亮色
  - 暗色
  - 红色
  - 蓝色
- **可配置选项**：
  - 自定义延迟（100–5000 毫秒）
  - 点击首个结果
  - 无头模式
- **安全可靠**：
  - 线程化执行
  - 安全停止
  - 错误处理

---

### 系统要求
- Python 3.8+
- PyQt6
- Selenium
- Google Chrome
- **ChromeDriver**（与 Chrome 版本匹配）

---

### 安装步骤
1. 安装依赖：
   ```bash
   pip install PyQt6 selenium
   ```
2. 从 [chromedriver.chromium.org](https://chromedriver.chromium.org/) 下载 **ChromeDriver**
3. 将 `chromedriver.exe`（Windows）或 `chromedriver`（Linux/macOS）放入 `PATH`
4. 将脚本保存为 `google_auto_search.py`
5. 运行：
   ```bash
   python google_auto_search.py
   ```

---

### 使用指南
1. 输入**搜索词**
2. 使用滑块或数字调整**延迟**
3. 如需点击，启用**“点击第一个结果”**
4. 后台运行请启用**“无头模式”**
5. 点击**“开始搜索”**
6. 在 **“日志”** 标签页查看进度
7. 随时点击 **“停止”** 中止操作

> 专业提示：使用 **无头模式 + 延迟 > 1500ms** 实现隐形自动化。

---

### 项目结构
- `google_auto_search.py` – 完整独立应用程序
- 无需外部资源

---

### 贡献代码
我们非常欢迎贡献！您可以：
- 添加代理支持
- 支持其他搜索引擎
- 导出搜索结果
- 添加定时任务
- 增强反爬机制

请提交带有清晰说明的 **Pull Request**。

---

### 许可证
基于 **MIT 许可证** 发布。个人和商业用途完全免费。