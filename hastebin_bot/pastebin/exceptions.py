class PastebinError(Exception):
    def __init__(self, service=None, txt=None):
        self.txt = f'error with {service}'
        if txt:
            self.txt = f'{self.txt}: {txt}'
