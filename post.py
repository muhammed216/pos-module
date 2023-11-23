import requests
from PIL import Image
from io import BytesIO


grafik_URL =  'https://image-charts.com/chart'

payload = {
    'chco': '3092de',
    'chd': 't:81,65,50,67,59,81',
    'ch1': 'hiz|sut|pas|top_surus|defans|fizik',
    'chd1': 'Falcao',
    'chd1p': 'b',
    'chs': '480x480',
    'cht': 'r'
    'chtt''Futbolcu Özellikleri'
}




response = requests.post(grafik_URL, data=payload)

image = Image.open(BytesIO(response.content))
image.show()


print(response.status_code)
print(response.content)
print(type(response.content))


image = Image.open(BytesIO(response.content))
image.show()

class Futbolcu():
    def __init__(self, isim, hiz, sut , pas, top_surus, defans, fizik):
        self.isim = isim
        self.hiz = hiz
        self.sut = sut
        self.pas = pas
        self.top_surus = top_surus
        self.defans = defans
        self.fizik = fizik
    def yetenek_hazirla(self):
        return ','.join([
            str(self.hiz),
            str(self.sut),
            str(self.pas),
            str(self.top_surus),
            str(self.defans),
            str(self.fizik)
        ])

    def yetenek_gorsellestir(self):
        grafik_URL = 'https://image-charts.com/chart'

        payload = {
            'chco' '3092de',
            'chd' 't:' + self.yetenek_hazirla(),
            'chd1' 'self.isim',
            'chd1p' 'b',
            'chs' '480x480',
            'cht' 'r',
            'chtt' 'Futbolcu Özellikleri',
            'ch1' 'hiz|sut|pas|top_surus|defans|fizik',
            'chx1' '0: 0|20|40|60|80|100',
            'chxt' 'x',
            'chxr' '0,0.0,0.100,0'
            'chm' 'B,AAAAAABB,0,0,0'
        }
        response = requests.post(grafik_URL, data=payload)

        image = Image.open(BytesIO(response.content))
        image.show()

    def yetenek_kiyaslama_goster(self, hedef_futbolcu):
        grafik_URL = 'https://image-charts.com/chart'

        payload = {
            'chco' '3092de',
            'chd' 't:' + self.yetenek_hazirla() + '|' + hedef_futbolcu.yetenek_hazirla(),
            'chd1' 'self.isim' + '|' + hedef_futbolcu.isim,
            'chd1p' 'b',
            'chs' '480x480',
            'cht' 'r',
            'chtt' 'Futbolcu Özellikleri',
            'ch1' 'hiz|sut|pas|top_surus|defans|fizik',
            'chx1' '0: 0|20|40|60|80|100',
            'chxt' 'x',
            'chxr' '0,0.0,0.100,0'
            'chm' 'B,AAAAAABB,0,0,0|B,0073CFBB,1,0,0'
        }
        response = requests.post(grafik_URL, data=payload)

        image = Image.open(BytesIO(response.content))
        image.show()




messi = Futbolcu('Messi', 85, 92, 91, 95, 38, 65)
ronaldo = Futbolcu('Ronaldo', 89, 93, 81, 89, 35, 77)

print(messi.yetenek_gorsellestir())









