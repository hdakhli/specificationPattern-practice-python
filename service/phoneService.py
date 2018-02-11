class PhoneService:

    def __init__(self):
        self._phones = []

    @staticmethod
    def fetch_phones_from_api():
        #fetch phones from repository
        return []

    def fetch_all_phones(self):
        self._phones = PhoneService.fetch_phones_from_api()

    @property
    def phones(self):
        return self._phones

    @phones.setter
    def phones(self, phones):
        self._phones = phones

    '''
     Premium (cost >= 400)
     return All premium phones
    '''
    def get_all_premium_phones(self):
        return list(filter(lambda phone: phone['cost'] >= 400, self._phones))

    '''
     return Only brand Samsung
    '''
    def get_samsung_phones(self):
        return list(filter(lambda phone: phone['brand'] == 'SAMSUNG', self._phones))

    '''
     return Only premium brand Samsung
    '''
    def get_premium_samsung_phones(self):
        return list(filter(lambda phone: phone['brand'] == 'SAMSUNG' and phone['cost'] >= 400, self._phones))

    '''
     return Either brand Samsung or HTC
    '''
    def get_samsung_and_htc_phones(self):
        return list(filter(lambda phone: phone['brand'] == 'SAMSUNG' or phone['brand'] == 'HTC', self._phones))

    '''
     return All premium and brand Samsung or HTC
    '''
    def get_premium_samsung_and_htc_phones(self):
        return list(filter(lambda phone: phone['cost'] >= 400 and (phone['brand'] == 'SAMSUNG' or phone['brand'] == 'HTC'), self._phones))

    '''
     return All but brand Samsung
    '''
    def get_all_except_samsung_phones(self):
        return list(filter(lambda phone: phone['brand'] != 'SAMSUNG', self._phones))

    '''
     return All premium but brand Samsung and htc
    '''
    def get_all_premium_except_samsung_and_htc_phones(self):
        return list(filter(lambda phone: phone['cost'] >= 400 and (phone['brand'] != 'SAMSUNG' and phone['brand'] != 'HTC'), self._phones))
