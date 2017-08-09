import difflib

class sentimenTypo:
    def match(self):
       a = difflib.get_close_matches('blm', ['belum', 'bukan', 'tak', 'tanpa', 'tidak', 'pantang', 'jangan', 'bukanlah', 'sok', 'tidak pernah'])
       print a


sentimenTypo().match()