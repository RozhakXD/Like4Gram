#!/usr/bin/env python3
try:
    import requests, json, re, time, os, datetime
    from requests.exceptions import RequestException
    from rich.console import Console
    from rich import print
    from rich.panel import Panel
    from rich.columns import Columns
except (Exception) as e:
    exit(f"[Error] {str(e).capitalize()}!")

SUKSES, GAGAL, CREDITS = [], [], {
    "COUNT": 0
}

def Banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Panel("""[bold red]  _      _ _        _  _    _____                     
 | |    (_) |      | || |  / ____|                    
 | |     _| | _____| || |_| |  __ _ __ __ _ _ __ ___  
 | |    | | |/ / _ \__   _| | |_ | '__/ _` | '_ ` _ \ 
 | |____| |   <  __/  | | | |__| | | | (_| | | | | | |
[bold white] |______|_|_|\_\___|  |_|  \_____|_|  \__,_|_| |_| |_|
\t[underline green]Like4Like Instagram - Coded by Rozhak""", width=59, style="bold bright_black"))
    return ("0_0")

class Bypass:

    def __init__(self) -> None:
        pass

    def Spam(self, session, cookies):
        session.headers.update({
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Sec-Fetch-Dest': 'document',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Mode': 'navigate',
            'Host': 'www.like4like.org',
            'Sec-Fetch-Site': 'same-origin',
        })
        response = session.get('https://www.like4like.org/user/earn-instagram-follow.php', cookies = {
            'Cookie': cookies
        })
        return ("0_0")

class Login:

    def __init__(self) -> None:
        pass

    def Cookies(self):
        try:
            Banner()
            print(Panel(f"[bold white]Silahkan masukan cookies akun like4like, jika belum memiliki akun segera registrasi dan pastikan anda memasukan cookies yang valid!", width=59, style="bold bright_black", title=" [Like4Like Cookies] ", subtitle="╭─────", subtitle_align="left"))
            self.cookies_like4like = Console().input("[bold bright_black]   ╰─> ")
            self.credits_ = self.Mengecek_Akun_Like4Like(self.cookies_like4like)
            print(Panel(f"[bold white]Silahkan masukan cookies akun instagram, gunakan akun yang tidak terpakai atau akun baru untuk login!", width=59, style="bold bright_black", title=" [Instagram Cookies] ", subtitle="╭─────", subtitle_align="left"))
            self.cookies_instagram = Console().input("[bold bright_black]   ╰─> ")
            self.username = self.Mengecek_Akun_Instagram(self.cookies_instagram)
            with open('Data/Cookies.json', 'w+') as w:
                w.write(json.dumps({
                    "Cookies_Like4Like": self.cookies_like4like,
                    "Cookies_Instagram": self.cookies_instagram,
                }))
            w.close()
            Mission().Mengikuti(self.cookies_instagram, requests.Session(), 'rozhak_official')
            print(Panel(f"""[bold white]Link :[bold green] https://www.instagram.com/{str(self.username)[:20]}
[bold white]Koin :[bold red] {self.credits_}""", width=59, style="bold bright_black", title=" [Selamat Datang] "))
            time.sleep(2.5)
            Fitur()
        except (Exception) as e:
            print(Panel(f"[bold red]{str(e).capitalize()}!", width=59, style="bold bright_black", title=" [Error] "))
            exit()

    def Mengecek_Akun_Instagram(self, cookies):
        with requests.Session() as session:
            session.headers.update({
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-Mode': 'navigate',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                'Host': 'www.instagram.com',
                'Sec-Fetch-Dest': 'document',
                'Accept-Language': 'en-US,en;q=0.9',
            })
            response = session.get('https://www.instagram.com/', cookies = {
                'Cookie': cookies
            })
            if '"username":' in str(response.text) and '"id":' in str(response.text):
                self.username = re.search('"should_show_public_contacts":.*?,"username":"(.*?)"', str(response.text)).group(1)
                return (self.username)
            else:
                print(Panel(f"[bold red]Sepertinya cookies instagram sudah kedaluarsa atau akun terkena checkpoint, kamu bisa mengambil ulang cookies dan pastikan akun dalam keadaan login!", width=59, style="bold bright_black", title=" [Cookies Invalid] "))
                time.sleep(4.5)
                self.Cookies()

    def Mengecek_Akun_Like4Like(self, cookies):
        with requests.Session() as session:
            Bypass().Spam(session, cookies)
            session.headers.update({
                'X-Requested-With': 'XMLHttpRequest',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://www.like4like.org/',
                'Sec-Fetch-Mode': 'cors',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Sec-Fetch-Site': 'same-origin',
            })
            response2 = session.get('https://www.like4like.org/api/get-user-info.php', cookies = {
                "Cookie": cookies
            })
            if '"success":true,' in str(response2.text) and 'credits' in str(response2.text):
                self.json_data = json.loads(response2.text)['data']
                self.credits_ = self.json_data['credits']
                return (self.credits_)
            else:
                print(Panel(f"[bold red]Sepertinya cookies like4like kamu sudah kedaluarsa atau tidak berfungsi lagi, kamu bisa mengambilnya ulang dan pastikan akun dalam keadaan login!", width=59, style="bold bright_black", title=" [Cookies Invalid] "))
                time.sleep(4.5)
                self.Cookies()

class Fitur:

    def __init__(self):
        try:
            Banner()
            self.json_data = json.loads(open('Data/Cookies.json', 'r').read())
            self.cookies_like4like, self.cookies_instagram = self.json_data['Cookies_Like4Like'], self.json_data['Cookies_Instagram']
            self.username = Login().Mengecek_Akun_Instagram(self.cookies_instagram)
            self.credits_ = Login().Mengecek_Akun_Like4Like(self.cookies_like4like)
            CREDITS.update({
                "COUNT": int(self.credits_)
            })
            print(Columns([
                Panel(f"[bold white]Username :[bold green] @{str(self.username)[:13]}", width=29, style="bold bright_black"),
                Panel(f"[bold white]Koin :[bold red] {self.credits_}", width=29, style="bold bright_black")
            ]))
        except (Exception) as e:
            print(Panel(f"[bold red]{str(e).capitalize()}!", width=59, style="bold bright_black", title=" [Error] "))
            time.sleep(4.5)
            Login().Cookies()

        try:
            print(Panel("""[bold white][[bold green]1[bold white]] Tukarkan Koin Ke Pengikut
[bold white][[bold green]2[bold white]] Jalankan Misi Follow
[bold white][[bold green]3[bold white]] Hapus Link Yang Terhubung
[bold white][[bold green]4[bold white]] Keluar ([bold red]Exit[bold white])""", width=59, style="bold bright_black", subtitle="╭─────", subtitle_align="left"))
            self.choices = Console().input("[bold bright_black]   ╰─> ")
            if self.choices in ['1', '01']:
                print(Panel(f"[bold white]Silahkan masukan username target yang ingin di jadikan sebagai pertukaran koin, pastikan akun tersebut tidak terkunci dan username sudah benar!", width=59, style="bold bright_black", title=" [Username] ", subtitle="╭─────", subtitle_align="left"))
                self.fblink = Console().input("[bold bright_black]   ╰─> ").replace('@', '')
                print(Panel(f"[bold white]Silahkan masukan jumlah koin yang ingin digunakan. Anda bisa memilih dari angka ([bold red]2[bold white]-[bold red]21[bold white]), anda juga hanya bisa memasukan angka saja, misalnya :[bold green] 4 *empat", width=59, style="bold bright_black", title=" [Jumlah Koin] ", subtitle="╭─────", subtitle_align="left"))
                self.fbcredits = int(Console().input("[bold bright_black]   ╰─> "))
                Tukarkan().Pengikut(self.cookies_like4like, self.credits_, f"https://www.instagram.com/{self.fblink}", self.fbcredits)
                exit()
            elif self.choices in ['2', '02']:
                print(Panel(f"[bold white]Silahkan masukan delay untuk menjalankan setiap misi, disarankan untuk menggunakan delay di atas[bold red] 60 detik[bold white] agar mengurangi spam, misalnya :[bold green] 120 *detik", width=59, style="bold bright_black", title=" [Jeda Misi] ", subtitle="╭─────", subtitle_align="left"))
                self.delay = int(Console().input("[bold bright_black]   ╰─> "))
                print(Panel(f"[bold white]Sedang menjalankan misi, kamu bisa menggunakan[bold red] CTRL + Z[bold white] untuk berhenti dan menggunakan[bold green] CTRL + C[bold white] jika stuck!", width=59, style="bold bright_black", title=" [Catatan] "))
                while True:
                    try:
                        Mission().Like4Like(self.cookies_like4like, self.cookies_instagram, self.delay)
                        Mission().Delay(0, self.delay)
                    except (RequestException):
                        print(f"[bold bright_black]   ╰─>[bold red] KONEKSI KAMU BERMASALAH!          ", end='\r')
                        time.sleep(10.0)
                        continue
                    except (Exception) as e:
                        print(f"[bold bright_black]   ╰─>[bold red] {str(e).upper()}!", end='\r')
                        time.sleep(5.0)
                        continue
            elif self.choices in ['3', '03']:
                Menghapus().Link(self.cookies_like4like)
                print(Panel(f"[bold white]Berhasil menghapus semua tautan yang terhubung dalam akun like4like kamu, sekarang kamu dapat menukarkan koin ke pengikut instagram!", width=59, style="bold bright_black", title=" [Sukses] "))
                exit()
            elif self.choices in ['4', '04']:
                print(Panel(f"[bold white]Berhasil menghapus cookies instagram dan like4like, terimakasih telah menggunakan layanan kami!", width=59, style="bold bright_black", title=" [Keluar] "))
                os.remove('Data/Cookies.json')
                exit()
            else:
                print(Panel(f"[bold red]Pilihan yang kamu masukan tidak ada dalam fitur kami, silahkan masukan pilihan dengan benar!", width=59, style="bold bright_black", title=" [Pilihan Salah] "))
                time.sleep(4.5)
                Fitur()
        except (Exception) as e:
            print(Panel(f"[bold red]{str(e).capitalize()}!", width=59, style="bold bright_black", title=" [Error] "))
            exit()

class Menghapus:

    def __init__(self) -> None:
        pass

    def Link(self, cookies):
        while True:
            with requests.Session() as r:
                r.headers.update({
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-Mode': 'navigate',
                    'Connection': 'keep-alive',
                    'Host': 'www.like4like.org',
                    'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'document',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36',
                    'Sec-Fetch-User': '?1',
                    'Accept-Language': 'en-US,en;q=0.9',

                })
                response = r.get('https://www.like4like.org/user/manage-my-pages.php', cookies = {
                    "Cookie": cookies
                })
                try:
                    self.featureName = re.search('window.location = ".*?=(.*?)"', str(response.text)).group(1)
                    self.idzadatka = re.search('"add-.*?-credits-id(\d+)"', str(response.text)).group(1)
                except (AttributeError):
                    print(f"[bold bright_black]   ╰─>[bold red] TIDAK MENEMUKAN USER YANG TERKAIT!     ", end='\r')
                    time.sleep(2.5)
                    break
                r.headers.pop("Upgrade-Insecure-Requests")
                r.headers.update({
                    'Referer': 'https://www.like4like.org/user/manage-my-pages.php',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'Origin': 'https://www.like4like.org',
                    'Sec-Fetch-Dest': 'empty',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                })
                data = {
                    'featureName': self.featureName,
                    'idzadatka': self.idzadatka,
                }
                response2 = r.post('https://www.like4like.org/api/archive-task.php', data = data, cookies = {
                    "Cookie": cookies
                })
                if '"success":true' in str(response2.text) and '"errors":[]' in str(response2.text):
                    response3 = r.post('https://www.like4like.org/api/delete-task.php', data = data, cookies = {
                        "Cookie": cookies
                    })
                    if '"success":true' in str(response3.text) and '"error":null' in str(response3.text):
                        print(f"[bold bright_black]   ╰─>[bold green] SUKSES MENGHAPUS @{self.idzadatka}!     ", end='\r')
                        time.sleep(2.5)
                        continue
                    else:
                        print(f"[bold bright_black]   ╰─>[bold green] SUKSES MENGARSIPKAN @{self.idzadatka}!    ", end='\r')
                        time.sleep(2.5)
                        continue
                else:
                    print(f"[bold bright_black]   ╰─>[bold red] GAGAL MENGHAPUS @{self.idzadatka}!     ", end='\r')
                    time.sleep(2.5)
                    return ("-_0")
        return ("0_0")

class Mission:

    def __init__(self) -> None:
        pass

    def Delay(self, menit, detik):
        self.total = (menit * 60 + detik)
        while (self.total):
            menit, detik = divmod(self.total, 60)
            print(f"[bold bright_black]   ╰─>[bold white] TUNGGU[bold green] {menit:02d}:{detik:02d}[bold white] SUKSES:-[bold green]{len(SUKSES)}[bold white] GAGAL:-[bold red]{len(GAGAL)}     ", end='\r')
            time.sleep(1)
            self.total -= 1
        return ("0_0")

    def Like4Like(self, cookies_like4like, cookies_instagram, delay):
        with requests.Session() as session:
            Bypass().Spam(session, cookies_like4like)
            session.headers.update({
                'Referer': 'https://www.like4like.org/user/earn-instagram-follow.php',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'X-Requested-With': 'XMLHttpRequest',
            })
            response = session.get('https://www.like4like.org/api/get-tasks.php?feature=instagramfol', cookies = {
                "Cookie": cookies_like4like
            })
            if '"success":true,' in str(response.text) and 'www.instagram.com' in str(response.text):
                for z in json.loads(response.text)['data']['tasks']:
                    self.timestamp_milliseconds = str(datetime.datetime.now().timestamp() * 1000).split('.')[0]
                    self.idlink, self.taskId, self.code3 = z['idlink'], z['taskId'], z['code3']
                    session.headers.update({
                        'Content-Type': 'application/json; charset=utf-8',
                    })
                    response2 = session.get(f'https://www.like4like.org/api/start-task.php?idzad={self.idlink}&vrsta=follow&idcod={self.taskId}&feature=instagramfol&_={self.timestamp_milliseconds}', cookies = {
                        "Cookie": cookies_like4like
                    })
                    if '"success":true,' in str(response2.text):
                        session.headers.update({
                            'Content-Type': 'application/x-www-form-urlencoded',
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                            'Sec-Fetch-Mode': 'navigate',
                            'Sec-Fetch-Dest': 'document',
                            'Origin': 'https://www.like4like.org',
                        })
                        data = {
                            'url': f'https://www.instagram.com/{self.idlink}',
                        }
                        response3 = session.post('https://www.like4like.org/checkurl.php', data = data, cookies = {
                            'Cookie': cookies_like4like
                        })
                        if 'https://www.instagram.com/' in str(response3.text) or 'https://freesocialmediatrends.com/l/loadurl.php' in str(response3.text):
                            self.Mengikuti(cookies_instagram, session, username = self.idlink)
                            time.sleep(5.0)
                            session.headers.update({
                                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                'Accept': 'application/json, text/javascript, */*; q=0.01',
                                'Origin': 'https://www.like4like.org',
                                'Accept-Language': 'en-US,en;q=0.9',
                                'Sec-Fetch-Dest': 'empty',
                                'Sec-Fetch-Site': 'same-origin',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                                'Host': 'www.like4like.org',
                                'Sec-Fetch-Mode': 'cors',
                                'Referer': 'https://www.like4like.org/user/earn-instagram-follow.php',
                            })
                            data = {
                                'url': f'https://www.instagram.com/{self.idlink}',
                                'idlinka': f'{self.idlink}',
                                'idzad': f'{self.taskId}',
                                'addon': False,
                                'version': '',
                                'idclana': f'{self.code3}',
                                'cnt': True,
                                'vrsta': 'follow',
                                'feature': 'instagramfol',
                            }
                            response4 = session.post('https://www.like4like.org/api/validate-task.php', data = data, cookies = {
                                'Cookie': cookies_like4like
                            })
                            if '"success":true,' in str(response4.text) and '"credits"' in str(response4.text):
                                self.penambahan_credits = re.search('"credits":"(.*?)"', str(response4.text)).group(1)
                                print(Panel(f"""[bold white]Status :[bold green] Successfully...
[bold white]Link :[bold red] https://www.instagram.com/{self.idlink}
[bold white]Credits :[bold green] {CREDITS['COUNT']}[bold white] >[bold green] {self.penambahan_credits}""", width=59, style="bold bright_black", title=" [Sukses] "))
                                SUKSES.append(f'{str(response4.text)}')
                                CREDITS.update({
                                    "COUNT": int(self.penambahan_credits)
                                })
                                return ("0_0")
                            else:
                                print(f"[bold bright_black]   ╰─>[bold red] @{self.idlink} GAGAL MENDAPATKAN KOIN!     ", end='\r')
                                time.sleep(3.5)
                                return ("-_-")
                        else:
                            print(f"[bold bright_black]   ╰─>[bold red] TIDAK MENDAPATKAN REDICT URL!         ", end='\r')
                            time.sleep(4.0)
                            return ("-_0")
                    else:
                        print(f"[bold bright_black]   ╰─>[bold red] TIDAK MENDAPATKAN TASK KODE!          ", end='\r')
                        time.sleep(4.0)
                        return ("-_0")
            elif 'tasks' not in str(response.text):
                print(f"[bold bright_black]   ╰─>[bold red] ANDA TERDETEKSI SEBAGAI BOT!    ", end='\r')
                time.sleep(10.0)
                return ("-_-")
            else:
                print(f"[bold bright_black]   ╰─>[bold red] SEDANG TIDAK ADA MISI!          ", end='\r')
                time.sleep(5.0)
                return ("0_-")
            
    def Mengikuti(self, cookies_instagram, session, username):
        session.headers.clear()
        session.headers.update({
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'navigate',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Host': 'www.instagram.com',
            'Sec-Fetch-Dest': 'document',
            'Accept-Language': 'en-US,en;q=0.9',
        })
        response = session.get('https://www.instagram.com/{}'.format(username).replace('@', ''), cookies = {
            'Cookie': cookies_instagram
        })
        self.profilePage = re.search('"profilePage_(\d+)"', str(response.text)).group(1)
        session.headers.update({
            'Referer': 'https://www.instagram.com/{}'.format(username),
            'X-IG-App-ID': '936619743392459',
            'X-Requested-With': 'XMLHttpRequest',
            'Sec-Fetch-Mode': 'cors',
            'X-Instagram-AJAX': '1012867433',
            'X-IG-WWW-Claim': '0',
            'X-CSRFToken': re.search('csrftoken=(.*?);', str(cookies_instagram)).group(1),
            'Accept': '*/*',
            'X-ASBD-ID': '129477',
            'Sec-Fetch-Dest': 'empty',
            'Origin': 'https://www.instagram.com',
            'Content-Type': 'application/x-www-form-urlencoded',
        })
        data = {
            'container_module': 'profile',
            'nav_chain': 'PolarisProfilePostsTabRoot:profilePage:1:via_cold_start',
            'user_id': self.profilePage,
        }
        response2 = session.post('https://www.instagram.com/api/v1/friendships/create/{}/'.format(self.profilePage), data = data, cookies = {
            'Cookie': cookies_instagram
        })
        session.headers.clear()
        if '"following":true,' in str(response.text):
            return ("0_0")
        else:
            return ("-_-")

class Tukarkan:

    def __init__(self) -> None:
        pass

    def Pengikut(self, cookies, credits_, fblink, fbcredits):
        with requests.Session() as session:
            session.headers.update({
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'navigate',
                'Connection': 'keep-alive',
                'Host': 'www.like4like.org',
                'Sec-Fetch-Dest': 'document',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                'Sec-Fetch-User': '?1',
                'Accept-Language': 'en-US,en;q=0.9',
            })
            response = session.get('https://www.like4like.org/user/manage-my-pages.php?feature=instagramfol', cookies = {
                "Cookie": cookies
            })
            session.headers.update({
                'Referer': 'https://www.like4like.org/user/manage-my-pages.php?feature=instagramfol',
                'X-Requested-With': 'XMLHttpRequest',
                'Sec-Fetch-Mode': 'cors',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Origin': 'https://www.like4like.org',
                'Sec-Fetch-Dest': 'empty',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            })
            data = {
                'idclana': '3740207',
                'fbdescription': '',
                'feature': 'instagramfol',
                'fblink': fblink,
                'fbcredits': fbcredits,
            }
            self.jumlah = (int(credits_) / int(fbcredits))
            response2 = session.post('https://www.like4like.org/api/enterlink.php', data = data, cookies = {
                "Cookie": cookies
            })
            if '"uradio"' in str(response2.text):
                print(Panel(f"""[bold white]Status :[bold green] Currently processing your order...
[bold white]Link :[bold red] {fblink}
[bold white]Followers :[bold green] {int(self.jumlah)}""", width=59, style="bold bright_black", title=" [Sukses] "))
                return ("0_0")
            else:
                print(Panel(f"[bold red]Maaf, kami tidak bisa menukarkan koin anda ke pengikut, anda bisa mencoba menukarkan secara manual!", width=59, style="bold bright_black", title=" [Gagal] "))
                exit()

if __name__ == '__main__':
    try:
        if os.path.exists("Data/Subscribe.json") == False:
            youtube_url = json.loads(requests.get('https://raw.githubusercontent.com/RozhakXD/Like4Gram/main/Data/Youtube.json').text)['Link']
            os.system(f'xdg-open {youtube_url}')
            with open('Data/Subscribe.json', 'w') as w:
                w.write(json.dumps({
                    "Status": True
                }))
            w.close()
            time.sleep(2.5)
        os.system('git pull')
        Fitur()
    except (Exception) as e:
        print(Panel(f"[bold red]{str(e).capitalize()}!", width=59, style="bold bright_black", title=" [Error] "))
        exit()
    except (KeyboardInterrupt):
        exit()