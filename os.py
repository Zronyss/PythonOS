import os, datetime, random, time
from pathlib import Path

()
try:
    import requests
    from bs4 import BeautifulSoup
    import html2text

    WEB = True
except:
    WEB = False
    print("⚠️ Browser: pip install requests beautifulsoup4 html2text\n")


class PythonOS:
    def __init__(self):
        self.running = True
        self.path = Path("/home/user")
        self.user = "user"
        self.lang = "en"
        self.vfs = {
            "/": {"home": {"user": {"documents": {}, "downloads": {}, "desktop": {},
                                    "readme.txt": "Welcome to PythonOS!\nДобро пожаловать в PythonOS!\n",
                                    "notes.txt": "My notes\nМои заметки\n"}},
                  "system": {"config.ini": "[system]\nversion=1.0\n"}}}

        self.rock_songs = [
            ("Led Zeppelin", "Stairway to Heaven"), ("Queen", "Bohemian Rhapsody"),
            ("Pink Floyd", "Comfortably Numb"), ("AC/DC", "Thunderstruck"),
            ("Metallica", "Nothing Else Matters"), ("Ozzy Osbourne", "No More Tears"),
            ("Guns N' Roses", "Sweet Child o' Mine"), ("Nirvana", "Smells Like Teen Spirit"),
            ("Кино", "Группа крови"), ("Король и Шут", "Лесник"),
            ("Rammstein", "Du Hast"), ("System of a Down", "Chop Suey!"),
        ]

        self.rock_facts = [
            ("🦇 Ozzy bit a bat head in 1982!", "🦇 Оззи откусил голову летучей мыши в 1982!"),
            ("🎸 Ozzy had dyslexia, read syllable by syllable until 2025", "🎸 Оззи читал по слогам до 2025"),
            ("💀 Ozzy Osbourne passed away in 2025", "💀 Оззи Осборн ушёл из жизни в 2025"),
        ]

        self.nick_db = {
            "pre": ["xX", "Mr", "Lord", "Cyber", "Not", "Ozzy", "Dark", "Pro"],
            "root": ["Python", "Gamer", "Wizard", "Hacker", "Potato", "Osbourne", "Shadow", "Wolf"],
            "suf": ["Xx", "YT", "1337", "666", "™", "🔥", "_", "-"],
            "styles": {
                "game": ("xX", "Gamer", "Xx"), "fantasy": ("Lord", "Wizard", "👑"),
                "cyber": ("Cyber", "Hacker", "2077"), "funny": ("Not", "Potato", "lol"),
                "japan": ("Sakura", "Ninja", "san"), "rock": ("Ozzy", "Osbourne", "🎸")
            }
        }

        self.txt = {
            "en": {
                "welcome": "Simple OS on Python", "boot": "Boot time",
                "user": "User", "help": "Type 'help' for commands",
                "lang": "Language: English (use 'lang ru' for Russian)",
                "error": "Error", "cmd_not_found": "Command not found", "cleared": "Cleared",
                "usage": "Usage", "example": "Example", "done": "Done!", "created": "created",
                "not_found": "not found", "exists": "already exists", "deleted": "deleted",
            },
            "ru": {
                "welcome": "Простая ОС на Пайтоне", "boot": "Время загрузки",
                "user": "Пользователь", "help": "Введите 'help' для списка команд",
                "lang": "Язык: Русский (используй 'lang en' для английского)",
                "error": "Ошибка", "cmd_not_found": "Команда не найдена", "cleared": "Очищено",
                "usage": "Использование", "example": "Пример", "done": "Готово!", "created": "создано",
                "not_found": "не найдено", "exists": "уже существует", "deleted": "удалено",
            }
        }

        self.cmds = {
            "help": self.help, "clear": self.clear, "ls": self.ls, "dir": self.ls,
            "cd": self.cd, "pwd": self.pwd, "mkdir": self.mkdir, "touch": self.touch,
            "cat": self.cat, "rm": self.rm, "echo": self.echo, "date": self.date,
            "time": self.time, "sysinfo": self.sysinfo, "calc": self.calc,
            "random": self.rnd, "edit": self.edit, "note": self.note, "rock": self.rock,
            "nick": self.nick, "lang": self.lang_cmd, "exit": self.exit, "shutdown": self.exit,
            "browser": self.browser, "browser_demo": self.browser_demo, "search": self.search,
            "search_demo": self.search_demo,
            "mkdir_mass": self.mkdir_mass,
        }

    def _(self, en, ru):
        return ru if self.lang == "ru" else en

    def t(self, key):
        return self.txt[self.lang].get(key, self.txt["en"][key])

    def run(self):
        self.clear(None)
        print("=" * 50 + f"\n   PythonOS v1.0\n   {self.t('welcome')}\n" + "=" * 50 +
              f"\n{self.t('boot')}: {datetime.datetime.now():%H:%M:%S}\n{self.t('user')}: {self.user}\n{self.t('help')}\n{self.t('lang')}\n")
        while self.running:
            try:
                p = str(self.path).replace("/home/user", "~")
                cmd = input(f"\nPythonOS:{p}$ ").strip().split()
                if cmd: self.cmds.get(cmd[0].lower(),
                                      lambda x: print(f"{self.t('error')}: {cmd[0]} {self.t('cmd_not_found')}"))(
                    cmd[1:])
            except KeyboardInterrupt:
                print("\n^C")
            except Exception as e:
                print(f"{self.t('error')}: {e}")

    def nav(self, p=None):
        c = self.vfs["/"]
        for part in str(p or self.path).split("/")[1:]:
            if part in c:
                c = c[part]
            else:
                return None
        return c

    def ls(self, a):
        i = self.nav()
        if i:
            for n, v in sorted(i.items()):
                print(f"{'📁' if isinstance(v, dict) else '📄'} {n}/" if isinstance(v,
                                                                                  dict) else f"📄 {n} ({len(v) if isinstance(v, str) else 0} B)")

    def cd(self, a):
        if not a:
            self.path = Path("/home/user")
        elif a[0] == "..":
            if self.path != Path("/home/user"): self.path = self.path.parent
        elif a[0] == "/":
            self.path = Path("/")
        else:
            i = self.nav()
            if a[0] in i and isinstance(i[a[0]], dict):
                self.path /= a[0]
            else:
                print(f"❌ {self.t('not_found')}")

    def pwd(self, a):
        print(self.path)

    def mkdir(self, a):
        if not a:
            print(f"❌ {self.t('usage')}: mkdir [name]")
        else:
            i = self.nav()
            if a[0] not in i:
                i[a[0]] = {}; print(f"✅ {a[0]} {self.t('created')}")
            else:
                print(f"❌ {self.t('exists')}")

    def mkdir_mass(self, a):
        if not a:
            print(f"📁 Usage: mkdir_mass [count] [prefix]")
        else:
            i, c = self.nav(), int(a[0])
            p = a[1] if len(a) > 1 else "folder"
            for n in range(c): i[f"{p}_{n}"] = {}
            print(f"✅ {c} {self.t('created')}")

    def touch(self, a):
        if not a:
            print(f"❌ {self.t('usage')}: touch [file]")
        else:
            i = self.nav()
            if a[0] not in i:
                i[a[0]] = ""; print(f"✅ {a[0]} {self.t('created')}")
            else:
                print(f"❌ {self.t('exists')}")

    def cat(self, a):
        if not a:
            print(f"❌ {self.t('usage')}: cat [file]")
        else:
            i = self.nav()
            if a[0] in i:
                if isinstance(i[a[0]], str):
                    print(i[a[0]])
                else:
                    print(f"❌ {a[0]} is folder")
            else:
                print(f"❌ {self.t('not_found')}")

    def rm(self, a):
        if not a:
            print(f"❌ {self.t('usage')}: rm [name]")
        else:
            i = self.nav()
            if a[0] in i:
                if input(f"Delete {a[0]}? (y/n): ").lower() == 'y':
                    del i[a[0]];
                    print(f"✅ {a[0]} {self.t('deleted')}")
            else:
                print(f"❌ {self.t('not_found')}")

    def edit(self, a):
        if not a:
            print(f"❌ {self.t('usage')}: edit [file]")
        else:
            i = self.nav()
            if a[0] in i and isinstance(i[a[0]], str):
                print(f"📝 Editing {a[0]} (empty line to finish):")
                l = []
                while True:
                    line = input()
                    if line == "": break
                    l.append(line)
                if l: i[a[0]] = "\n".join(l); print(f"✅ Saved")
            else:
                print(f"❌ {self.t('not_found')}")

    def note(self, a):
        npath = self.path / "notes"
        ndir = self.nav(npath)
        if ndir is None:
            self.nav()["notes"] = {}
            ndir = self.nav(npath)

        if not a:
            print(
                "📔 NOTE:\n note new [name] - create\n note list - all\n note view [name] - read\n note edit [name] - edit\n note del [name] - delete")
        elif a[0] == "new" and len(a) > 1:
            name = a[1] + ".txt"
            if name not in ndir:
                print(f"📝 {name}:")
                l = []
                while True:
                    line = input()
                    if line == "": break
                    l.append(line)
                ndir[name] = "\n".join(l)
                print(f"✅ Saved")
            else:
                print(f"❌ {self.t('exists')}")
        elif a[0] == "list":
            print("\n📔 NOTES:")
            for n in sorted(ndir.keys()):
                if isinstance(ndir[n], str):
                    prev = ndir[n][:50].replace("\n", " ")
                    print(f"📄 {n} - {prev}{'...' if len(ndir[n]) > 50 else ''}")
        elif a[0] == "view" and len(a) > 1:
            name = a[1] + ".txt"
            if name in ndir:
                print(f"\n📄 {name}\n" + "=" * 40 + f"\n{ndir[name]}\n" + "=" * 40)
            else:
                print(f"❌ {self.t('not_found')}")
        elif a[0] == "edit" and len(a) > 1:
            name = a[1] + ".txt"
            if name in ndir:
                print(f"📝 {name}\nCurrent:\n{ndir[name]}\nNew text:")
                l = []
                while True:
                    line = input()
                    if line == "": break
                    l.append(line)
                if l: ndir[name] = "\n".join(l); print(f"✅ Updated")
            else:
                print(f"❌ {self.t('not_found')}")
        elif a[0] in ["del", "delete"] and len(a) > 1:
            name = a[1] + ".txt"
            if name in ndir and input(f"Delete {name}? (y/n): ").lower() == 'y':
                del ndir[name];
                print(f"✅ Deleted")

    def rock(self, a):
        if a and a[0] == "fact":
            f = random.choice(self.rock_facts)
            print(f"📖 {f[0] if self.lang == 'en' else f[1]}")
        elif a and a[0] == "list":
            arts = sorted(set(s[0] for s in self.rock_songs))
            print("🎸 ARTISTS:\n" + "=" * 40)
            for art in arts: print(f"  • {art}")
        else:
            art, song = random.choice(self.rock_songs)
            print("\n" + "=" * 60 + "\n🎸🤘 RANDOM ROCK 🤘🎸\n" + "=" * 60 + f"\n   {art} — {song}\n" + "=" * 60)
            if random.choice([0, 1]):
                f = random.choice(self.rock_facts)
                print(f"📖 {f[0] if self.lang == 'en' else f[1]}\n" + "=" * 60)

    def nick(self, a):
        db = self.nick_db
        if a and a[0] == "list":
            print("🎮 STYLES:\n" + "=" * 40)
            for s in db["styles"]: print(f"  • {s}")
        elif a and a[0] in db["styles"]:
            p, r, s = db["styles"][a[0]]
            nick = f"{p}{random.choice(db['root'])}{r}"[:1].upper() + f"{p}{random.choice(db['root'])}{r}"[1:]
            print("\n" + "=" * 60 + f"\n   {nick}\n" + "=" * 60 + f"\n💡 Style: {a[0]}")
        else:
            p, r, s = random.choice(db["pre"]), random.choice(db["root"]), random.choice(db["suf"])
            nick = random.choice([f"{p}{r}", f"{r}{s}", f"{p}_{r}", f"{r}_{s}"])
            print("\n" + "=" * 60 + f"\n   {nick}\n" + "=" * 60)

    def browser(self, a):
        if not WEB:
            print("❌ Install: pip install requests beautifulsoup4 html2text")
        elif not a:
            print(f"🌐 {self.t('usage')}: browser [url]")
        else:
            url = a[0]
            if not url.startswith(('http://', 'https://')): url = 'https://' + url
            try:
                print(f"🌐 Loading...")
                r = requests.get(url, headers={'User-Agent': 'PythonOS/1.0'}, timeout=5)
                soup = BeautifulSoup(r.text, 'html.parser')
                print("\n" + "=" * 60 + f"\n📄 {soup.title.string if soup.title else 'No title'}\n🔗 {url}\n" + "=" * 60)
                print(html2text.HTML2Text().handle(r.text)[:1000] + "...")
            except:
                print("❌ Connection error")

    def browser_demo(self, a):
        sites = {
            "google": ("Google - search", "Google - поиск"),
            "youtube": ("YouTube - videos", "YouTube - видео"),
            "github": ("GitHub - code", "GitHub - код"),
        }
        if not a:
            print("🌐 Demo sites:", ", ".join(sites.keys()))
        elif a[0] in sites:
            print(
                "\n" + "=" * 60 + f"\n🌐 {a[0]}.com (DEMO)\n" + "=" * 60 + f"\n{sites[a[0]][0 if self.lang == 'en' else 1]}\n" + "=" * 60)

    def search(self, a):
        if not WEB:
            print("❌ Install libraries")
        elif not a:
            print(f"🔍 {self.t('usage')}: search [query]")
        else:
            self.browser([f"https://www.google.com/search?q={'+'.join(a)}"])

    def search_demo(self, a):
        if not a:
            print(f"🔍 {self.t('usage')}: search_demo [query]")
        else:
            print(f"🔍 Demo search: {' '.join(a)}\n📌 Try 'browser_demo' for sites")

    def help(self, a):
        print(f"\n{'📋 COMMANDS' if self.lang == 'en' else '📋 КОМАНДЫ'}:")
        for cmd in sorted(self.cmds.keys())[:28]: print(f"  {cmd:<12}", end="")
        print("\n\n © PythonOS, 2026")

    def clear(self, a):
        os.system('cls' if os.name == 'nt' else 'clear')

    def echo(self, a):
        print(" ".join(a))

    def date(self, a):
        print(datetime.datetime.now().strftime("%d.%m.%Y"))

    def time(self, a):
        print(datetime.datetime.now().strftime("%H:%M:%S"))

    def rnd(self, a):
        if len(a) >= 2:
            print(random.randint(int(a[0]), int(a[1])))
        else:
            print(random.randint(1, 100))

    def calc(self, a):
        try:
            if a:
                print(f"{' '.join(a)} = {eval(' '.join(a))}")
            else:
                print(f"= {eval(input('> '))}")
        except:
            print("❌ Error")

    def sysinfo(self, a):
        print(
            f"\n{'=' * 40}\nSystem: PythonOS v1.0\nUser: {self.user}\nLang: {'EN' if self.lang == 'en' else 'RU'}\nPath: {self.path}\n{'=' * 40}")

    def lang_cmd(self, a):
        if not a:
            print(f"Current: {'EN' if self.lang == 'en' else 'RU'}\nUse: lang en/ru")
        elif a[0].lower() in ['en', 'ru']:
            self.lang = a[0].lower(); print(f"Lang: {self.lang}")

    def exit(self, a):
        print("👋 Bye!"); self.running = False


if __name__ == "__main__":
    PythonOS().run()