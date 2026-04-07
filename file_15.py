class Parser:
    def parse_int(self, value):
        try:
            return int(value)
        except:
            return None
