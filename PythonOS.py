import os
import datetime
import random
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
    import html2text
    WEB_SUPPORT = True
except ImportError:
    WEB_SUPPORT = False
    print("⚠️  For browser install libraries:")
    print("   pip install requests beautifulsoup4 html2text")
    print("   Browser will work in demo mode\n")

class PythonOS:
    def __init__(self):
        self.running = True
        self.current_user = "user"
        self.current_directory = Path("/home/user")
        self.filesystem = {
            "/": {
                "home": {
                    "user": {
                        "documents": {},
                        "downloads": {},
                        "desktop": {},
                        "readme.txt": "Welcome to PythonOS!\nДобро пожаловать в PythonOS!\n",
                        "notes.txt": "My notes\nМои заметки\n"
                    }
                },
                "system": {
                    "config.ini": "[system]\nversion=1.0\n"
                }
            }
        }
        self.processes = []
        self.version = "1.0"
        self.os_name = "PythonOS"
        self.language = "en"
    
    def _(self, en_text, ru_text):
        return ru_text if self.language == "ru" else en_text
    
    def cmd_lang(self, args):
        if not args:
            print(self._(
                "Current language: " + ("English" if self.language == "en" else "Russian"),
                "Текущий язык: " + ("Русский" if self.language == "ru" else "Английский")
            ))
            print(self._(
                "Usage: lang [en/ru]",
                "Использование: lang [en/ru]"
            ))
            return
        
        if args[0].lower() in ["en", "eng", "english", "английский"]:
            self.language = "en"
            print(self._("Language set to English", "Язык изменён на английский"))
        elif args[0].lower() in ["ru", "rus", "russian", "русский"]:
            self.language = "ru"
            print(self._("Language set to Russian", "Язык изменён на русский"))
        else:
            print(self._(
                "Unknown language. Use: lang en / lang ru",
                "Неизвестный язык. Используй: lang en / lang ru"
            ))
    
    def run(self):
        """Main loop / Главный цикл"""
        self.clear_screen([])
        self.show_boot_screen()
        
        while self.running:
            try:
                self.show_prompt()
                command = input().strip()
                if command:
                    self.execute_command(command)
            except KeyboardInterrupt:
                print("\n^C")
            except Exception as e:
                print(f"{self._('Error', 'Ошибка')}: {e}")
    
    def show_boot_screen(self):
        """Boot screen / Загрузочный экран"""
        print("=" * 50)
        print(f"   {self.os_name} v{self.version}")
        print(self._(
            "   Simple operating system running on Python",
            "   Небольшая ОС работающая на Пайтоне"
        ))
        if WEB_SUPPORT:
            print(self._("   🌐 Browser: ACTIVE", "   🌐 Браузер: АКТИВИРОВАН"))
        else:
            print(self._("   🌐 Browser: DEMO MODE", "   🌐 Браузер: ДЕМО-РЕЖИМ"))
        print(self._("   📔 Notebook: READY", "   📔 Блокнот: ГОТОВ"))
        print(self._("   🎸 Rock Generator: READY", "   🎸 Рок-генератор: ГОТОВ"))
        print(self._("   🎮 Nick Generator: READY", "   🎮 Генератор ников: ГОТОВ"))
        print("=" * 50)
        print(f"{self._('Boot time', 'Время загрузки')}: {datetime.datetime.now().strftime('%H:%M:%S')}")
        print(f"{self._('User', 'Пользователь')}: {self.current_user}")
        print(self._(
            "Type 'help' for commands list",
            "Введите 'help' для списка команд"
        ))
        print(self._(
            "Language: English (use 'lang ru' for Russian)",
            "Язык: Русский (используй 'lang en' для английского)"
        ))
        print()
    
    def show_prompt(self):
        """Show prompt / Показать приглашение"""
        path = str(self.current_directory).replace("/home/user", "~")
        print(f"\n{self.os_name}:{path}$ ", end="")
    
    def clear_screen(self, args):
        """Clear screen / Очистить экран"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{self.os_name} v{self.version} - {self._('Cleared', 'Очищено')}")
    
    def cmd_help(self, args):
        """Show help / Показать справку"""
        if self.language == "ru":
            print("\nДоступные команды:")
            print("-" * 70)
            commands_info = [
                ("help", "Показать эту справку"),
                ("clear", "Очистить экран"),
                ("ls/dir", "Показать содержимое папки"),
                ("cd [папка]", "Сменить папку"),
                ("pwd", "Показать текущую папку"),
                ("mkdir [имя]", "Создать папку"),
                ("mkdir_mass [кол-во] [префикс]", "Создать много папок"),
                ("touch [файл]", "Создать файл"),
                ("cat [файл]", "Показать содержимое файла"),
                ("rm [имя]", "Удалить файл/папку"),
                ("echo [текст]", "Вывести текст"),
                ("date", "Показать дату"),
                ("time", "Показать время"),
                ("sysinfo", "Информация о системе"),
                ("calc", "Простой калькулятор"),
                ("random", "Случайное число"),
                ("edit [файл]", "Редактировать файл"),
                ("browser [url]", "🌐 Открыть сайт в текстовом браузере"),
                ("browser_save [url] [файл]", "💾 Сохранить сайт в файл"),
                ("browser_demo [сайт]", "🔄 Демо-браузер (без интернета)"),
                ("search [запрос]", "🔍 Поиск в Google"),
                ("search_demo [запрос]", "🔍 Демо-поиск"),
                ("note", "📔 Блокнот (управление заметками)"),
                ("rock", "🎸 Случайная рок-композиция"),
                ("rock fact", "📖 Случайный факт о роке"),
                ("rock list", "📋 Список исполнителей"),
                ("nick", "🎮 Случайный никнейм"),
                ("nick [тип]", "🎮 Никнейм определённого стиля"),
                ("nick list", "📋 Список стилей"),
                ("lang [en/ru]", "🌐 Сменить язык"),
                ("exit/shutdown", "Выйти из системы"),
                
            ]
            for cmd, desc in commands_info:
                print(f"  {cmd:<35} - {desc}")
        else:
            print("\nAvailable commands:")
            print("-" * 70)
            commands_info = [
                ("help", "Show this help"),
                ("clear", "Clear screen"),
                ("ls/dir", "List directory contents"),
                ("cd [folder]", "Change directory"),
                ("pwd", "Print working directory"),
                ("mkdir [name]", "Create directory"),
                ("mkdir_mass [count] [prefix]", "Create many folders"),
                ("touch [file]", "Create file"),
                ("cat [file]", "Show file contents"),
                ("rm [name]", "Delete file/folder"),
                ("echo [text]", "Print text"),
                ("date", "Show date"),
                ("time", "Show time"),
                ("sysinfo", "System information"),
                ("calc", "Simple calculator"),
                ("random", "Random number"),
                ("edit [file]", "Edit file"),
                ("browser [url]", "🌐 Open website in text browser"),
                ("browser_save [url] [file]", "💾 Save website to file"),
                ("browser_demo [site]", "🔄 Demo browser (no internet)"),
                ("search [query]", "🔍 Google search"),
                ("search_demo [query]", "🔍 Demo search"),
                ("note", "📔 Notebook (manage notes)"),
                ("rock", "🎸 Random rock song"),
                ("rock fact", "📖 Random rock fact"),
                ("rock list", "📋 Artists list"),
                ("nick", "🎮 Random nickname"),
                ("nick [style]", "🎮 Nickname in specific style"),
                ("nick list", "📋 Styles list"),
                ("lang [en/ru]", "🌐 Change language"),
                ("exit/shutdown", "Exit system"),
                
            ]
            for cmd, desc in commands_info:
                print(f"  {cmd:<35} - {desc}")
    
    def cmd_mkdir_mass(self, args):
        """Create many folders at once"""
        if not args:
            print(self._(
                "Usage: mkdir_mass [count] [prefix]\nExample: mkdir_mass 1000 test",
                "Использование: mkdir_mass [количество] [префикс]\nПример: mkdir_mass 1000 test"
            ))
            return
        
        try:
            count = int(args[0])
            prefix = args[1] if len(args) > 1 else "folder"
            
            items = self.navigate_to_path(self.current_directory)
            created = 0
            
            for i in range(count):
                folder_name = f"{prefix}_{i}"
                if folder_name not in items:
                    items[folder_name] = {}
                    created += 1
                
                if count > 100:
                    if i % (count // 10) == 0 and i > 0:
                        print(self._(
                            f"🔄 Progress: {i/count*100:.0f}% ({i}/{count})",
                            f"🔄 Прогресс: {i/count*100:.0f}% ({i}/{count})"
                        ))
                elif i % 100 == 0 and i > 0:
                    print(self._(
                        f"🔄 Created {i} folders...",
                        f"🔄 Создано {i} папок..."
                    ))
            
            print(self._(
                f"✅ Done! Created {created} folders with prefix '{prefix}'",
                f"✅ Готово! Создано {created} папок с префиксом '{prefix}'"
            ))
            
        except ValueError:
            print(self._(
                "❌ Error: count must be a number",
                "❌ Ошибка: количество должно быть числом"
            ))
        except MemoryError:
            print(self._(
                "💥 CRITICAL ERROR: Out of memory!",
                "💥 КРИТИЧЕСКАЯ ОШИБКА: Закончилась память!"
            ))
    
    def cmd_browser(self, args):
        """🌐 Text web browser"""
        if not WEB_SUPPORT:
            print(self._(
                "❌ Libraries not installed. Run:\n   pip install requests beautifulsoup4 html2text\n\nUse demo mode: browser_demo [site]",
                "❌ Библиотеки не установлены. Запусти:\n   pip install requests beautifulsoup4 html2text\n\nИспользуй демо-режим: browser_demo [сайт]"
            ))
            return
        
        if not args:
            print(self._(
                "🌐 Usage: browser [url]\n   Example: browser https://example.com\n   Example: browser google.com (https:// will be added)",
                "🌐 Использование: browser [url]\n   Пример: browser https://example.com\n   Пример: browser google.com (добавится https://)"
            ))
            return
        
        url = args[0]
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        try:
            print(self._(
                f"🌐 Loading {url}...",
                f"🌐 Загрузка {url}..."
            ))
            
            headers = {
                'User-Agent': 'PythonOS Browser/1.0'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            h = html2text.HTML2Text()
            h.ignore_links = False
            h.ignore_images = True
            h.ignore_emphasis = True
            h.body_width = 0
            
            text = h.handle(response.text)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string.strip() if soup.title else self._("No title", "Без названия")
            
            print("\n" + "=" * 60)
            print(f"📄 {title}")
            print(f"🔗 {url}")
            print("=" * 60)
            
            lines = text.split('\n')
            for i, line in enumerate(lines[:50]):
                if line.strip():
                    print(line)
            
            if len(lines) > 50:
                print(self._(
                    f"\n... and {len(lines) - 50} more lines",
                    f"\n... и ещё {len(lines) - 50} строк"
                ))
                
            print("=" * 60)
            print(self._(
                "💡 To save: browser_save [url] [filename]",
                "💡 Чтобы сохранить: browser_save [url] [имя_файла]"
            ))
            
        except requests.exceptions.ConnectionError:
            print(self._(
                "❌ Connection error. Check URL or internet",
                "❌ Ошибка подключения. Проверь URL или интернет"
            ))
        except requests.exceptions.Timeout:
            print(self._(
                "❌ Timeout. Site is too slow",
                "❌ Таймаут. Сайт слишком долго отвечает"
            ))
        except Exception as e:
            print(self._(
                f"❌ Error: {e}",
                f"❌ Ошибка: {e}"
            ))
    
    def cmd_browser_save(self, args):
        """💾 Save webpage to file"""
        if not WEB_SUPPORT:
            print(self._(
                "❌ Libraries not installed. Run:\n   pip install requests beautifulsoup4 html2text",
                "❌ Библиотеки не установлены. Запусти:\n   pip install requests beautifulsoup4 html2text"
            ))
            return
        
        if len(args) < 2:
            print(self._(
                "💾 Usage: browser_save [url] [filename]",
                "💾 Использование: browser_save [url] [имя_файла]"
            ))
            return
        
        url = args[0]
        filename = args[1]
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        try:
            print(self._(
                f"💾 Downloading {url}...",
                f"💾 Загрузка {url}..."
            ))
            
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            items = self.navigate_to_path(self.current_directory)
            
            h = html2text.HTML2Text()
            h.ignore_links = False
            text = h.handle(response.text)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string.strip() if soup.title else self._("No title", "Без названия")
            
            content = f"URL: {url}\n{self._('Title', 'Заголовок')}: {title}\n\n{text}"
            items[filename] = content
            
            print(self._(
                f"✅ Page saved as '{filename}' ({len(content)} bytes)",
                f"✅ Страница сохранена как '{filename}' ({len(content)} байт)"
            ))
            
        except Exception as e:
            print(self._(
                f"❌ Error: {e}",
                f"❌ Ошибка: {e}"
            ))
    
    def cmd_browser_demo(self, args):
        """🔄 Demo browser (no internet)"""
        sites = {
            "google": self._(
                "Google - search engine\n\nEnter query: _\n\nNews:\n• Python 3.12 released\n• AI learned to write OS\n• Cats took over the internet",
                "Google - поисковая система\n\nВведите запрос: _\n\nНовости:\n• Python 3.12 вышел\n• ИИ научился писать ОС\n• Котики захватили интернет"
            ),
            "youtube": self._(
                "YouTube - video hosting\n\nTrending now:\n• 🎬 Python Guide for Beginners (10M views)\n• 🎬 How to make your own OS (5M views)\n• 🎬 10 hours of cats (infinite)",
                "YouTube - видео хостинг\n\nСейчас в тренде:\n• 🎬 Гайд по Python для начинающих (10M просмотров)\n• 🎬 Как сделать свою ОС (5M просмотров)\n• 🎬 10 часов котиков (бесконечно)"
            ),
            "github": self._(
                "GitHub - code platform\n\nPopular repositories:\n• ⭐ python-os: Python OS on Python\n• ⭐ python-browser: Console browser\n• ⭐ 30-seconds-of-code",
                "GitHub - платформа для кода\n\nПопулярные репозитории:\n• ⭐ python-os: ОС на Python\n• ⭐ python-browser: Браузер в консоли\n• ⭐ 30-seconds-of-code"
            ),
            "reddit": self._(
                "Reddit - forum\n\nr/python:\n• 🔥 How to make a browser in 5 minutes\n• 🔥 My first OS\n• 🔥 Code optimization tip",
                "Reddit - форум\n\nr/python:\n• 🔥 Как сделать браузер за 5 минут\n• 🔥 Моя первая ОС\n• 🔥 Совет по оптимизации кода"
            ),
            "wiki": self._(
                "Wikipedia\n\nOperating system — a set of programs that...\n\nThe first Python OS was created in 2026 by an enthusiast.",
                "Википедия\n\nОперационная система — комплекс программ, обеспечивающий...\n\nПервая ОС на Python была создана в 2026 году энтузиастом."
            ),
            "habr": self._(
                "Habr - IT news\n\n• 🚀 Python 3.13 released\n• 🚀 10 libraries for hackers\n• 🚀 Programmer career in 2026",
                "Habr - IT новости\n\n• 🚀 Вышла Python 3.13\n• 🚀 10 библиотек для хакера\n• 🚀 Карьера программиста в 2026"
            ),
        }
        
        if not args:
            print(self._(
                "🌐 Available sites in demo mode:",
                "🌐 Доступные сайты в демо-режиме:"
            ))
            for site in sites.keys():
                print(f"   • {site}")
            print(self._(
                "\nUsage: browser_demo [site_name]\nExample: browser_demo google",
                "\nИспользование: browser_demo [имя_сайта]\nПример: browser_demo google"
            ))
            return
        
        site = args[0].lower()
        if site in sites:
            print("\n" + "=" * 60)
            print(f"🌐 {site}.com ({self._('DEMO MODE', 'ДЕМО-РЕЖИМ')})")
            print("=" * 60)
            print(sites[site])
            print("\n" + "=" * 60)
            if not WEB_SUPPORT:
                print(self._(
                    "💡 Install libraries for real browser:",
                    "💡 Установи библиотеки для реального браузера:"
                ))
                print("   pip install requests beautifulsoup4 html2text")
        else:
            print(self._(
                f"❌ Site '{site}' not found in demo mode",
                f"❌ Сайт '{site}' не найден в демо-режиме"
            ))
            print(self._(
                "Available sites:", 
                "Доступные сайты:"
            ), ", ".join(sites.keys()))
    
    def cmd_search(self, args):
        """🔍 Google search"""
        if not WEB_SUPPORT:
            print(self._(
                "❌ Libraries needed for search. Install:\n   pip install requests beautifulsoup4 html2text\n\nUse demo search: search_demo [query]",
                "❌ Для поиска нужны библиотеки. Установи:\n   pip install requests beautifulsoup4 html2text\n\nИспользуй демо-поиск: search_demo [запрос]"
            ))
            return
        
        if not args:
            print(self._(
                "🔍 Usage: search [query]\n   Example: search python os\n   Example: search how to make browser",
                "🔍 Использование: search [запрос]\n   Пример: search python os\n   Пример: search как сделать браузер"
            ))
            return
        
        query = "+".join(args)
        url = f"https://www.google.com/search?q={query}"
        print(self._(
            f"🔍 Searching: {' '.join(args)}",
            f"🔍 Поиск: {' '.join(args)}"
        ))
        self.cmd_browser([url])
    
    def cmd_search_demo(self, args):
        """🔍 Demo search (no internet)"""
        if not args:
            print(self._(
                "🔍 Usage: search_demo [query]\n   Example: search_demo python\n   Example: search_demo how to make os",
                "🔍 Использование: search_demo [запрос]\n   Пример: search_demo python\n   Пример: search_demo как сделать ос"
            ))
            return
        
        query = " ".join(args).lower()
        
        results = {
            "python": self._(
                "🐍 Python — language PythonOS is written in. Learn it!",
                "🐍 Python — язык, на котором написана PythonOS. Изучай!"
            ),
            "os": self._(
                "🖥️ Operating System — program that manages computer",
                "🖥️ Операционная система — программа для управления компьютером"
            ),
            "operating system": self._(
                "🖥️ Same as OS — program that manages computer.",
                "🖥️ То же самое что ОС — программа для управления компьютером."
            ),
            "browser": self._(
                "🌐 Browser — available in PythonOS! Use browser_demo or browser",
                "🌐 Браузер — есть в PythonOS! Используй browser_demo или browser"
            ),
            "internet": self._(
                "🌍 Demo mode works without internet. Install libraries for real access.",
                "🌍 Без интернета работает демо-режим. Установи библиотеки для реального доступа."
            ),
            "file": self._(
                "📄 Files are stored in virtual FS. Use ls, cat, touch",
                "📄 Файлы хранятся в виртуальной ФС. Используй ls, cat, touch"
            ),
            "folder": self._(
                "📁 Folders created with mkdir or mkdir_mass",
                "📁 Папки создаются командой mkdir или mkdir_mass"
            ),
            "code": self._(
                "💻 OS code is in python_os.py. You can improve it!",
                "💻 Код ОС лежит в python_os.py. Можешь его улучшать!"
            ),
            "cat": self._(
                "🐱 Cats — always the answer. Here's a cat: =^._.^=",
                "🐱 Котики — всегда ответ. Вот тебе кот: =^._.^="
            ),
            "google": self._(
                "🔍 Google: browser google.com or search query",
                "🔍 Google: browser google.com или search запрос"
            ),
            "yandex": self._(
                "🇷🇺 Yandex: browser yandex.ru",
                "🇷🇺 Яндекс: browser yandex.ru"
            ),
            "youtube": self._(
                "🎬 YouTube: browser youtube.com (demo has trends!)",
                "🎬 YouTube: browser youtube.com (в демо есть тренды!)"
            ),
            "github": self._(
                "🐙 GitHub: browser github.com",
                "🐙 GitHub: browser github.com"
            ),
            "pythonos": self._(
                "✨ Your OS! Version 1.0.",
                "✨ Твоя ОС! Версия 1.0."
            ),
            "help": self._(
                "📖 Help command shows all available commands.",
                "📖 Команда help показывает все доступные команды."
            ),
            "command": self._(
                "📋 Commands list: help, ls, cd, mkdir, browser, search, nick...",
                "📋 Список команд: help, ls, cd, mkdir, browser, search, nick..."
            ),
            "error": self._(
                "🐞 Errors are normal. Read what it says and google it!",
                "🐞 Ошибки — это нормально. Главное — читать, что написано, и гуглить!"
            ),
            "thanks": self._(
                "🙏 You're welcome! Glad to help with OS. What else to add?",
                "🙏 Пожалуйста! Рад помочь с ОС. Что ещё сделать?"
            ),
            "nick": self._(
                "🎮 Nick generator: nick or nick [style]. Styles: game, fantasy, cyber, funny, japan, rock",
                "🎮 Генератор ников: nick или nick [стиль]. Стили: game, fantasy, cyber, funny, japan, rock"
            ),
            "nickname": self._(
                "🎮 Same thing! Just type nick",
                "🎮 То же самое! Просто напиши nick"
            ),
        }
        
        print("\n" + "=" * 60)
        print(self._(
            f"🔍 DEMO SEARCH: {' '.join(args)}",
            f"🔍 ДЕМО-ПОИСК: {' '.join(args)}"
        ))
        print("=" * 60)
        
        found = False
        for key, answer in results.items():
            if key in query:
                print(f"📌 {answer}")
                found = True
                break
        
        if not found:
            words = query.split()
            for word in words:
                if len(word) > 3:
                    for key, answer in results.items():
                        if word in key or key in word:
                            print(f"📌 {self._('By word', 'По слову')} '{word}': {answer}")
                            found = True
                            break
                if found:
                    break
        
        if not found:
            print(self._(
                f"❌ Nothing found for query: '{query}'",
                f"❌ Ничего не найдено по запросу: '{query}'"
            ))
            print(self._(
                "💡 Try: python, os, browser, file, folder, code, cat, nick",
                "💡 Попробуй: python, ос, браузер, файл, папка, код, котики, ник"
            ))
        
        print("=" * 60)
    
    def cmd_note(self, args):
        """📔 Notebook - manage notes"""
        if not args:
            print(self._(
                "📔 PythonOS NOTEBOOK\n" + "=" * 50 + "\nCommands:\n"
                "  note new [name]     - create new note\n"
                "  note list           - show all notes\n"
                "  note view [name]    - read note\n"
                "  note edit [name]    - edit note\n"
                "  note delete [name]  - delete note\n"
                "  note search [text]  - search notes",
                "📔 БЛОКНОТ PythonOS\n" + "=" * 50 + "\nКоманды:\n"
                "  note new [название]    - создать новую заметку\n"
                "  note list              - показать все заметки\n"
                "  note view [название]   - прочитать заметку\n"
                "  note edit [название]   - редактировать заметку\n"
                "  note delete [название] - удалить заметку\n"
                "  note search [текст]    - поиск по заметкам"
            ))
            return
        
        subcmd = args[0].lower()
        
        notes_path = self.current_directory / "notes"
        notes_dir = self.navigate_to_path(notes_path)
        
        if notes_dir is None:
            parent_items = self.navigate_to_path(self.current_directory)
            parent_items["notes"] = {}
            notes_dir = parent_items["notes"]
        
        if subcmd == "new":
            if len(args) < 2:
                print(self._(
                    "❌ Specify note name: note new [name]",
                    "❌ Укажи название заметки: note new [название]"
                ))
                return
            
            note_name = args[1] + ".txt"
            if note_name in notes_dir:
                print(self._(
                    f"❌ Note '{note_name}' already exists",
                    f"❌ Заметка '{note_name}' уже существует"
                ))
                return
            
            print(self._(
                f"📝 Creating note: {note_name}\nEnter note text (empty line to finish):",
                f"📝 Создание заметки: {note_name}\nВведи текст заметки (пустая строка - завершить):"
            ))
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            
            notes_dir[note_name] = "\n".join(lines)
            print(self._(
                f"✅ Note '{note_name}' saved!",
                f"✅ Заметка '{note_name}' сохранена!"
            ))
        
        elif subcmd == "list":
            if not notes_dir:
                print(self._(
                    "📔 You don't have any notes yet. Create first: note new [name]",
                    "📔 У тебя пока нет заметок. Создай первую: note new [название]"
                ))
                return
            
            print(self._(
                "\n📔 YOUR NOTES:",
                "\n📔 ТВОИ ЗАМЕТКИ:"
            ))
            print("=" * 50)
            for note in sorted(notes_dir.keys()):
                if isinstance(notes_dir[note], str):
                    preview = notes_dir[note][:50].replace("\n", " ")
                    if len(notes_dir[note]) > 50:
                        preview += "..."
                    print(f"📄 {note} - {preview}")
            print("=" * 50)
            print(self._(
                f"📊 Total notes: {len([n for n in notes_dir if isinstance(notes_dir[n], str)])}",
                f"📊 Всего заметок: {len([n for n in notes_dir if isinstance(notes_dir[n], str)])}"
            ))
        
        elif subcmd == "view":
            if len(args) < 2:
                print(self._(
                    "❌ Specify note name: note view [name]",
                    "❌ Укажи название заметки: note view [название]"
                ))
                return
            
            note_name = args[1] + ".txt" if not args[1].endswith('.txt') else args[1]
            if note_name not in notes_dir:
                print(self._(
                    f"❌ Note '{note_name}' not found",
                    f"❌ Заметка '{note_name}' не найдена"
                ))
                return
            
            print(f"\n📄 {note_name}")
            print("=" * 50)
            print(notes_dir[note_name])
            print("=" * 50)
        
        elif subcmd == "edit":
            if len(args) < 2:
                print(self._(
                    "❌ Specify note name: note edit [name]",
                    "❌ Укажи название заметки: note edit [название]"
                ))
                return
            
            note_name = args[1] + ".txt" if not args[1].endswith('.txt') else args[1]
            if note_name not in notes_dir:
                print(self._(
                    f"❌ Note '{note_name}' not found",
                    f"❌ Заметка '{note_name}' не найдена"
                ))
                return
            
            print(self._(
                f"📝 Editing {note_name}",
                f"📝 Редактирование {note_name}"
            ))
            print(self._(
                "Current text:",
                "Текущий текст:"
            ))
            print("-" * 40)
            print(notes_dir[note_name])
            print("-" * 40)
            print(self._(
                "Enter new text (empty line to finish):",
                "Введи новый текст (пустая строка - завершить):"
            ))
            
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            
            if lines:
                notes_dir[note_name] = "\n".join(lines)
                print(self._(
                    f"✅ Note '{note_name}' updated!",
                    f"✅ Заметка '{note_name}' обновлена!"
                ))
            else:
                print(self._(
                    "⚠️ Text not changed",
                    "⚠️ Текст не изменён"
                ))
        
        elif subcmd == "delete":
            if len(args) < 2:
                print(self._(
                    "❌ Specify note name: note delete [name]",
                    "❌ Укажи название заметки: note delete [название]"
                ))
                return
            
            note_name = args[1] + ".txt" if not args[1].endswith('.txt') else args[1]
            if note_name not in notes_dir:
                print(self._(
                    f"❌ Note '{note_name}' not found",
                    f"❌ Заметка '{note_name}' не найдена"
                ))
                return
            
            confirm = input(self._(
                f"Delete note '{note_name}'? (y/n): ",
                f"Удалить заметку '{note_name}'? (y/n): "
            ))
            if confirm.lower() == 'y':
                del notes_dir[note_name]
                print(self._(
                    f"✅ Note '{note_name}' deleted!",
                    f"✅ Заметка '{note_name}' удалена!"
                ))
        
        elif subcmd == "search":
            if len(args) < 2:
                print(self._(
                    "❌ Specify search text: note search [text]",
                    "❌ Укажи текст для поиска: note search [текст]"
                ))
                return
            
            search_text = " ".join(args[1:]).lower()
            found = []
            
            for note_name, content in notes_dir.items():
                if isinstance(content, str) and search_text in content.lower():
                    found.append((note_name, content))
            
            if found:
                print(self._(
                    f"\n🔍 Found in {len(found)} notes:",
                    f"\n🔍 Найдено в {len(found)} заметках:"
                ))
                print("=" * 50)
                for note_name, content in found:
                    preview = content[:70].replace("\n", " ")
                    if len(content) > 70:
                        preview += "..."
                    print(f"📄 {note_name}: {preview}")
            else:
                print(self._(
                    f"❌ Nothing found for query: '{search_text}'",
                    f"❌ Ничего не найдено по запросу: '{search_text}'"
                ))
        
        else:
            print(self._(
                f"❌ Unknown command: {subcmd}\nUse 'note' without arguments for help",
                f"❌ Неизвестная команда: {subcmd}\nИспользуй 'note' без аргументов для справки"
            ))
    
    def cmd_rock(self, args):
        """🎸 Random rock song"""
        rock_songs = [
            ("Led Zeppelin", "Stairway to Heaven"),
            ("Queen", "Bohemian Rhapsody"),
            ("Pink Floyd", "Comfortably Numb"),
            ("The Beatles", "While My Guitar Gently Weeps"),
            ("The Rolling Stones", "(I Can't Get No) Satisfaction"),
            ("Deep Purple", "Smoke on the Water"),
            ("Lynyrd Skynyrd", "Free Bird"),
            ("The Who", "Baba O'Riley"),
            ("The Doors", "Riders on the Storm"),
            ("Creedence Clearwater Revival", "Fortunate Son"),
            ("AC/DC", "Thunderstruck"),
            ("AC/DC", "Back in Black"),
            ("Guns N' Roses", "Sweet Child o' Mine"),
            ("Guns N' Roses", "November Rain"),
            ("Metallica", "Nothing Else Matters"),
            ("Metallica", "Enter Sandman"),
            ("Ozzy Osbourne", "No More Tears"),
            ("Ozzy Osbourne", "Crazy Train"),
            ("Black Sabbath", "Paranoid"),
            ("Iron Maiden", "The Number of the Beast"),
            ("Judas Priest", "Breaking the Law"),
            ("Nirvana", "Smells Like Teen Spirit"),
            ("Pearl Jam", "Alive"),
            ("Soundgarden", "Black Hole Sun"),
            ("Alice in Chains", "Would?"),
            ("Foo Fighters", "Everlong"),
            ("Red Hot Chili Peppers", "Californication"),
            ("Kino", "Blood Type"),
            ("Kino", "Changes"),
            ("Aria", "Careless Angel"),
            ("Aria", "Lost Paradise"),
            ("Sektor Gaza", "Lyrics"),
            ("Splin", "No Way Out"),
            ("DDT", "What is Autumn"),
            ("Nautilus Pompilius", "I Want to Be With You"),
            ("Alisa", "Highway E-95"),
            ("Agata Kristi", "Like at War"),
            ("Korol i Shut", "Forester"),
            ("Korol i Shut", "Witch's Doll"),
            ("Imagine Dragons", "Believer"),
            ("Twenty One Pilots", "Stressed Out"),
            ("Linkin Park", "In the End"),
            ("System of a Down", "Chop Suey!"),
            ("Rammstein", "Du Hast"),
            ("Slipknot", "Duality"),
            ("Muse", "Uprising"),
            ("Arctic Monkeys", "Do I Wanna Know?"),
        ]
        
        rock_facts = [
            self._(
                "🤘 Fact: Ozzy Osbourne bit the head off a bat on stage in 1982!",
                "🤘 Факт: Ozzy Osbourne откусил голову летучей мыши на концерте в 1982!"
            ),
            self._(
                "🎸 Fact: Smoke on the Water is the most recognizable riff in rock history",
                "🎸 Факт: Smoke on the Water — самый узнаваемый рифф в истории рока"
            ),
            self._(
                "⚡ Fact: Freddie Mercury wrote Bohemian Rhapsody on piano in his apartment",
                "⚡ Факт: Freddie Mercury написал Bohemian Rhapsody на пианино в своей квартире"
            ),
            self._(
                "🔥 Fact: Led Zeppelin sold over 300 million albums",
                "🔥 Факт: Led Zeppelin продали более 300 миллионов альбомов"
            ),
            self._(
                "🌊 Fact: Viktor Tsoi died in a car accident in 1990",
                "🌊 Факт: Виктор Цой погиб в автокатастрофе в 1990 году"
            ),
            self._(
                "💀 Fact: Metallica played in Antarctica — the only band to perform on all continents",
                "💀 Факт: Metallica играла в Антарктиде — это единственная группа, выступавшая на всех континентах"
            ),
            self._(
                "🎤 Fact: Ozzy Osbourne had dyslexia and read syllable by syllable until the end of his life",
                "🎤 Факт: У Оззи Осборна была дислексия, он читал по слогам до конца жизни"
            ),
            self._(
                "🎸 Fact: Slash (Guns N' Roses) always wears a top hat because he's too lazy to comb his hair",
                "🎸 Факт: Гитарист Slash (Guns N' Roses) всегда носит цилиндр, потому что ему лень причесываться"
            ),
            self._(
                "📀 Fact: The loudest concert in history — Deep Purple in 1972, 117 dB",
                "📀 Факт: Самый громкий концерт в истории — Deep Purple в 1972, 117 дБ"
            ),
            self._(
                "🎼 Fact: The battle for best guitar solo — Stairway to Heaven vs Bohemian Rhapsody",
                "🎼 Факт: Битва за гитарное соло — Stairway to Heaven vs Bohemian Rhapsody"
            ),
            self._(
                "🦇 Fact: Ozzy Osbourne passed away in 2025, but his music lives forever",
                "🦇 Факт: Оззи Осборн ушёл из жизни в 2025, но его музыка живёт вечно"
            ),
        ]
        
        if args and args[0] == "fact":
            print(f"📖 {random.choice(rock_facts)}")
        elif args and args[0] == "list":
            artists = sorted(set(song[0] for song in rock_songs))
            print(self._(
                "🎸 ARTISTS IN DATABASE:",
                "🎸 ИСПОЛНИТЕЛИ В БАЗЕ:"
            ))
            print("=" * 50)
            for artist in artists:
                count = sum(1 for song in rock_songs if song[0] == artist)
                print(f"  • {artist} — {count} {self._('songs', 'песен')}")
            print("=" * 50)
            print(self._(
                f"📊 Total: {len(artists)} artists, {len(rock_songs)} songs",
                f"📊 Всего: {len(artists)} исполнителей, {len(rock_songs)} песен"
            ))
        else:
            artist, song = random.choice(rock_songs)
            show_fact = random.choice([True, False])
            
            print("\n" + "=" * 60)
            print(self._(
                "🎸🤘 RANDOM ROCK SONG 🤘🎸",
                "🎸🤘 СЛУЧАЙНАЯ РОК-КОМПОЗИЦИЯ 🤘🎸"
            ))
            print("=" * 60)
            print(f"\n   {artist} — {song}")
            print("\n" + "=" * 60)
            
            if show_fact:
                print(f"\n📖 {random.choice(rock_facts)}")
                print("=" * 60)
            
            print(self._(
                "\n💡 Other commands:\n   rock fact  - random rock fact\n   rock list  - artists list",
                "\n💡 Другие команды:\n   rock fact  - случайный факт о роке\n   rock list  - список исполнителей в базе"
            ))
    
    def cmd_nick(self, args):
        """🎮 Random nickname generator"""
        
        
        prefixes = [
            "xX", "Xx", "Mr", "Mrs", "Dr", "Sir", "Lord", "Lady", "King", "Queen",
            "Pro", "Ultra", "Super", "Mega", "Hyper", "Dark", "Shadow", "Night",
            "Fire", "Ice", "Thunder", "Storm", "Wolf", "Dragon", "Phoenix", "Ghost",
            "Cyber", "Neo", "Proto", "Infra", "Ultra", "Alpha", "Beta", "Omega",
            "Lil", "Big", "Little", "Old", "Young", "Crazy", "Mad", "Sly", "Sneaky",
            "Agent", "Captain", "Commander", "General", "Sarge", "Chief",
            "The", "Not", "Just", "Real", "Official", "Original", "Fake"
        ]
        
        roots = [
            "Py", "Pyth", "Python", "Code", "Dev", "Prog", "Script", "Byte", "Bit",
            "Pixel", "Data", "Logic", "Kernel", "Shell", "Terminal", "Console",
            "Wolf", "Fox", "Hawk", "Eagle", "Raven", "Crow", "Owl", "Tiger", "Lion",
            "Panther", "Leopard", "Viper", "Cobra", "Shark", "Whale", "Bear",
            "Dragon", "Wyvern", "Griffin", "Pegasus", "Phoenix", "Kraken",
            "Wizard", "Mage", "Sorcerer", "Knight", "Paladin", "Rogue", "Assassin",
            "Hunter", "Ranger", "Archer", "Warrior", "Berserker", "Titan",
            "Gamer", "Player", "Noob", "Pro", "Legend", "Hero", "Champion",
            "Storm", "Wind", "Thunder", "Lightning", "Blizzard", "Tornado",
            "Shadow", "Shade", "Phantom", "Spectre", "Wraith", "Reaper",
            "Neon", "Cyber", "Techno", "Digital", "Virtual", "Quantum", "Neural",
            "Ozzy", "Sabbath", "Metallica", "Hendrix", "Joplin", "Morrison",
            "Sakura", "Kumo", "Yami", "Hikari", "Kage", "Tora", "Ryuu"
        ]
        
        suffixes = [
            "xX", "Xx", "YT", "TV", "HD", "4K", "Pro", "Elite", "Prime",
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
            "11", "22", "33", "44", "55", "66", "77", "88", "99", "00",
            "123", "321", "666", "777", "999", "1337", "42",
            "_", "-", "~", "™", "®", "©", "🔥", "⚡", "💀", "👑",
            "RU", "US", "EU", "UA", "KZ", "BY",
            "Ops", "Inc", "Corp", "Labs", "Studio", "Team", "Crew"
        ]
        
        
        style_prefixes = {
            "game": ["xX", "Xx", "Pro", "Ultra", "Mega", "Hyper", "Shadow", "Night", "Dark", "Ghost"],
            "fantasy": ["Lord", "Lady", "King", "Queen", "Sir", "Dragon", "Phoenix", "Shadow", "Night", "Dark"],
            "cyber": ["Cyber", "Neo", "Proto", "Digital", "Virtual", "Quantum", "Neural", "Techno", "Byte", "Pixel"],
            "funny": ["Not", "Just", "Real", "Fake", "Lil", "Big", "Little", "Old", "Crazy", "Mad", "Sly", "Sneaky"],
            "japan": ["Sakura", "Kumo", "Yami", "Hikari", "Kage", "Tora", "Ryuu", "Kenji", "Yuki", "Haru"],
            "rock": ["Ozzy", "Slash", "Jimmy", "Freddie", "Kurt", "James", "Ronnie", "Bruce", "Viktor", "Mike"],
        }
        
        style_roots = {
            "game": ["Gamer", "Player", "Noob", "Pro", "Legend", "Hero", "Hunter", "Killer", "Sniper", "Fragger"],
            "fantasy": ["Wizard", "Mage", "Sorcerer", "Knight", "Paladin", "Rogue", "Assassin", "Hunter", "Ranger", "Druid"],
            "cyber": ["Hacker", "Coder", "Dev", "Runner", "Knight", "Ghost", "Phantom", "System", "Core", "Link"],
            "funny": ["Potato", "Pizza", "Cat", "Dog", "Nyan", "Derp", "Fail", "Noob", "Cake", "Memes"],
            "japan": ["Samurai", "Ninja", "Shogun", "Ronin", "Geisha", "Zen", "Dojo", "Sensei", "Katana", "Shuriken"],
            "rock": ["Osbourne", "Rose", "Page", "Mercury", "Cobain", "Hetfield", "Dio", "Dickinson", "Tsoi", "Kashin"],
        }
        
        style_suffixes = {
            "game": ["xX", "Xx", "YT", "TV", "1337", "666", "777", "_", "-"],
            "fantasy": ["™", "®", "👑", "🔥", "⚡", "💀", "_", "-"],
            "cyber": ["42", "1337", "0", "1", "2077", "3000", "_", "-", "™"],
            "funny": ["_", "-", "~", "lol", "rofl", "xd", "42", "1337"],
            "japan": ["_", "-", "~", "san", "kun", "chan", "sama", "desu"],
            "rock": ["666", "777", "1980", "1991", "2025", "_", "-", "🎸", "🤘"],
        }
        
        
        if args and args[0] == "list":
            print(self._(
                "🎮 AVAILABLE NICKNAME STYLES:",
                "🎮 ДОСТУПНЫЕ СТИЛИ НИКНЕЙМОВ:"
            ))
            print("=" * 50)
            styles = {
                "game": self._("Gamer style (xX_ProGamer_Xx)", "Геймерский стиль (xX_ProGamer_Xx)"),
                "fantasy": self._("Fantasy style (LordWizard👑)", "Фэнтези стиль (LordWizard👑)"),
                "cyber": self._("Cyber style (NeoHacker2077)", "Киберпанк стиль (NeoHacker2077)"),
                "funny": self._("Funny style (NotAPotato)", "Смешной стиль (NotAPotato)"),
                "japan": self._("Japanese style (SakuraNinja)", "Японский стиль (SakuraNinja)"),
                "rock": self._("Rock style (OzzyOsbourne🎸)", "Рокерский стиль (OzzyOsbourne🎸)"),
            }
            for style, desc in styles.items():
                print(f"  • {style}: {desc}")
            print("=" * 50)
            print(self._(
                "Usage: nick          - random style\n       nick [style]   - specific style\n       nick list      - this list",
                "Использование: nick          - случайный стиль\n       nick [стиль]   - определённый стиль\n       nick list      - этот список"
            ))
            return
        
        if args and args[0] in style_prefixes:
            style = args[0]
            prefix = random.choice(style_prefixes[style])
            root = random.choice(style_roots[style])
            suffix = random.choice(style_suffixes[style])
        else:
            prefix = random.choice(prefixes)
            root = random.choice(roots)
            suffix = random.choice(suffixes)
        
        variants = [
            f"{prefix}{root}",
            f"{root}{suffix}",
            f"{prefix}{root}{suffix}",
            f"{prefix}_{root}",
            f"{root}_{suffix}",
            f"{prefix}_{root}_{suffix}",
            f"{prefix}{random.choice(['', '_', '-'])}{root}{random.choice(['', '_', '-'])}{suffix}",
        ]
        
        nickname = random.choice(variants)
        
        if random.choice([True, False]):
            year = random.choice(["06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"])
            nickname += year
        
        print("\n" + "=" * 60)
        print(self._(
            "🎮✨ RANDOM NICKNAME GENERATOR ✨🎮",
            "🎮✨ ГЕНЕРАТОР СЛУЧАЙНЫХ НИКНЕЙМОВ ✨🎮"
        ))
        print("=" * 60)
        print(f"\n   {nickname}")
        print("\n" + "=" * 60)
        
        if args and args[0] in style_prefixes:
            style_names = {
                "game": self._("Gamer", "Геймерский"),
                "fantasy": self._("Fantasy", "Фэнтези"),
                "cyber": self._("Cyber", "Киберпанк"),
                "funny": self._("Funny", "Смешной"),
                "japan": self._("Japanese", "Японский"),
                "rock": self._("Rock", "Рокерский"),
            }
            print(self._(
                f"\n💡 Style: {style_names.get(style, style)}",
                f"\n💡 Стиль: {style_names.get(style, style)}"
            ))
        
        print(self._(
            "\n💡 Try: nick game, nick fantasy, nick cyber, nick funny, nick japan, nick rock",
            "\n💡 Попробуй: nick game, nick fantasy, nick cyber, nick funny, nick japan, nick rock"
        ))
        print("=" * 60)
    
    def cmd_ls(self, args):
        """List directory contents"""
        try:
            items = self.navigate_to_path(self.current_directory)
            if items is not None:
                for item in sorted(items.keys()):
                    if isinstance(items[item], dict):
                        print(f"📁 {item}/")
                    else:
                        size = len(items[item]) if isinstance(items[item], str) else 0
                        print(f"📄 {item} ({size} {self._('bytes', 'байт')})")
        except Exception as e:
            print(f"{self._('Error', 'Ошибка')}: {e}")
    
    def cmd_cd(self, args):
        """Change directory"""
        if not args:
            self.current_directory = Path("/home/user")
            return
        
        target = args[0]
        
        if target == "..":
            if self.current_directory != Path("/home/user"):
                self.current_directory = self.current_directory.parent
            return
        elif target == "/":
            self.current_directory = Path("/")
            return
        
        new_path = self.current_directory / target
        items = self.navigate_to_path(self.current_directory)
        
        if target in items and isinstance(items[target], dict):
            self.current_directory = new_path
        else:
            print(self._(
                f"Folder '{target}' not found",
                f"Папка '{target}' не найдена"
            ))
    
    def cmd_pwd(self, args):
        """Print working directory"""
        print(self.current_directory)
    
    def cmd_mkdir(self, args):
        """Create directory"""
        if not args:
            print(self._(
                "Specify folder name",
                "Укажите имя папки"
            ))
            return
        
        dir_name = args[0]
        items = self.navigate_to_path(self.current_directory)
        
        if dir_name not in items:
            items[dir_name] = {}
            print(self._(
                f"Folder '{dir_name}' created",
                f"Папка '{dir_name}' создана"
            ))
        else:
            print(self._(
                f"Folder '{dir_name}' already exists",
                f"Папка '{dir_name}' уже существует"
            ))
    
    def cmd_touch(self, args):
        """Create file"""
        if not args:
            print(self._(
                "Specify file name",
                "Укажите имя файла"
            ))
            return
        
        file_name = args[0]
        items = self.navigate_to_path(self.current_directory)
        
        if file_name not in items:
            items[file_name] = ""
            print(self._(
                f"File '{file_name}' created",
                f"Файл '{file_name}' создан"
            ))
        else:
            print(self._(
                f"File '{file_name}' already exists",
                f"Файл '{file_name}' уже существует"
            ))
    
    def cmd_cat(self, args):
        """Show file contents"""
        if not args:
            print(self._(
                "Specify file name",
                "Укажите имя файла"
            ))
            return
        
        file_name = args[0]
        items = self.navigate_to_path(self.current_directory)
        
        if file_name in items:
            if isinstance(items[file_name], str):
                print(items[file_name])
            else:
                print(self._(
                    f"'{file_name}' is a folder",
                    f"'{file_name}' это папка"
                ))
        else:
            print(self._(
                f"File '{file_name}' not found",
                f"Файл '{file_name}' не найден"
            ))
    
    def cmd_rm(self, args):
        """Delete file or folder"""
        if not args:
            print(self._(
                "Specify name to delete",
                "Укажите имя для удаления"
            ))
            return
        
        name = args[0]
        items = self.navigate_to_path(self.current_directory)
        
        if name in items:
            confirm = input(self._(
                f"Delete '{name}'? (y/n): ",
                f"Удалить '{name}'? (y/n): "
            ))
            if confirm.lower() == 'y':
                del items[name]
                print(self._(
                    f"'{name}' deleted",
                    f"'{name}' удален"
                ))
        else:
            print(self._(
                f"'{name}' not found",
                f"'{name}' не найден"
            ))
    
    def cmd_echo(self, args):
        """Print text"""
        print(" ".join(args))
    
    def cmd_date(self, args):
        """Show date"""
        print(datetime.datetime.now().strftime("%d.%m.%Y"))
    
    def cmd_time(self, args):
        """Show time"""
        print(datetime.datetime.now().strftime("%H:%M:%S"))
    
    def cmd_sysinfo(self, args):
        """System information"""
        print(f"\n{'='*40}")
        print(f"{self._('System', 'Система')}: {self.os_name}")
        print(f"{self._('Version', 'Версия')}: {self.version}")
        print(f"{self._('User', 'Пользователь')}: {self.current_user}")
        print(f"{self._('Date', 'Дата')}: {datetime.datetime.now().strftime('%d.%m.%Y')}")
        print(f"{self._('Time', 'Время')}: {datetime.datetime.now().strftime('%H:%M:%S')}")
        print(f"{self._('Current folder', 'Текущая папка')}: {self.current_directory}")
        print(f"{self._('Browser', 'Браузер')}: {'✅ ACTIVE' if WEB_SUPPORT else '⚠️ DEMO MODE'}")
        print(f"{self._('Language', 'Язык')}: {'English' if self.language == 'en' else 'Русский'}")
        print(f"{'='*40}")
    
    def cmd_calc(self, args):
        """Simple calculator"""
        try:
            if args:
                expression = " ".join(args)
                result = eval(expression)
                print(f"{expression} = {result}")
            else:
                print(self._(
                    "Calculator. Enter expression (e.g. 2 + 2):",
                    "Калькулятор. Введите выражение (например: 2 + 2):"
                ))
                expr = input("> ")
                result = eval(expr)
                print(f"= {result}")
        except:
            print(self._(
                "Error in expression",
                "Ошибка в выражении"
            ))
    
    def cmd_random(self, args):
        """Random number"""
        if len(args) >= 2:
            try:
                min_val = int(args[0])
                max_val = int(args[1])
                print(random.randint(min_val, max_val))
            except:
                print(random.randint(1, 100))
        else:
            print(random.randint(1, 100))
    
    def cmd_edit(self, args):
        """Edit file"""
        if not args:
            print(self._(
                "Specify file name",
                "Укажите имя файла"
            ))
            return
        
        file_name = args[0]
        items = self.navigate_to_path(self.current_directory)
        
        if file_name in items and isinstance(items[file_name], str):
            print(self._(
                f"Editing {file_name}. Enter text (empty line to finish):",
                f"Редактирование {file_name}. Введите текст (пустая строка для завершения):"
            ))
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            
            items[file_name] = "\n".join(lines)
            print(self._(
                f"File {file_name} saved",
                f"Файл {file_name} сохранен"
            ))
        else:
            print(self._(
                f"File '{file_name}' not found",
                f"Файл '{file_name}' не найден"
            ))
    
    def cmd_exit(self, args):
        """Exit system"""
        print(self._(
            "Shutting down...",
            "Завершение работы..."
        ))
        self.running = False
    
    def execute_command(self, command):
        """Execute command"""
        parts = command.split()
        cmd = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        
        commands = {
            "help": self.cmd_help,
            "clear": self.clear_screen,
            "ls": self.cmd_ls,
            "dir": self.cmd_ls,
            "cd": self.cmd_cd,
            "pwd": self.cmd_pwd,
            "mkdir": self.cmd_mkdir,
            "mkdir_mass": self.cmd_mkdir_mass,
            "touch": self.cmd_touch,
            "cat": self.cmd_cat,
            "rm": self.cmd_rm,
            "echo": self.cmd_echo,
            "date": self.cmd_date,
            "time": self.cmd_time,
            "sysinfo": self.cmd_sysinfo,
            "calc": self.cmd_calc,
            "random": self.cmd_random,
            "edit": self.cmd_edit,
            "browser": self.cmd_browser,
            "browser_save": self.cmd_browser_save,
            "browser_demo": self.cmd_browser_demo,
            "search": self.cmd_search,
            "search_demo": self.cmd_search_demo,
            "note": self.cmd_note,
            "rock": self.cmd_rock,
            "nick": self.cmd_nick,
            "lang": self.cmd_lang,
            "exit": self.cmd_exit,
            "shutdown": self.cmd_exit,
            
        }
        
        if cmd in commands:
            try:
                commands[cmd](args)
            except Exception as e:
                print(f"{self._('Error executing command', 'Ошибка выполнения команды')}: {e}")
        else:
            print(self._(
                f"Command '{cmd}' not found. Type 'help' for commands list",
                f"Команда '{cmd}' не найдена. Введите 'help' для списка команд"
            ))
    
    def navigate_to_path(self, path):
        """Navigate virtual filesystem"""
        current = self.filesystem["/"]
        parts = str(path).split("/")[1:]
        
        for part in parts:
            if part in current:
                current = current[part]
            else:
                return None
        
        return current

if __name__ == "__main__":
    os_system = PythonOS()
    os_system.run()