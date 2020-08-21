class PhoneNumber:
    def __init__(self, number):

        self.number = self.clean_number(number)
        self.area_code = self.number[:3]
    
    def clean_number(self, dirty_number):
        clean_number = []

        for char in dirty_number:
            if char.isdigit():
                clean_number.append(char)
        
        if 10 > len(clean_number) or 11 < len(clean_number):
            raise ValueError('Number is invalid length')

        if len(clean_number) == 11:
            if clean_number[0] != '1':
                raise ValueError('Invalid country code!')
            else:
                clean_number = clean_number[1:]

        if int(clean_number[0]) < 2 or int(clean_number[3]) < 2:
            raise ValueError('Invalid N numbers')
        else:
            return ''.join(clean_number)

    def pretty(self):
        return f'({self.area_code}) {self.number[3:6]}-{self.number[6:]}'
