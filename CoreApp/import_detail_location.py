import os
import openpyxl
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DDFWSql2.settings')
application = get_wsgi_application()

from CoreApp.models import PlaceLocation, PlaceNatural, PlaceHumanistic


path = "E:\WangTR2\College2\C2-3\DDFW\省市县\提炼.xlsx"


# 不统计改名省直辖
def import_place_data_from_excel(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active

    tmp_province = None
    tmp_city = None
    tmp_country = None

    i = 0

    for row in sheet.iter_rows(min_row=2, values_only=True):
        i += 1
        # if i>=500:
        #     break
        try:
            province = row[0].strip()
        except:
            province = None

        try:
            city = row[1].strip()
        except:
            city = None

        try:
            country = row[2].strip()
        except:
            country = None

        if province and province != '':
            tmp_province = province
            tmp_province,dum = PlaceLocation.objects.get_or_create(name=province, parent=None)

        elif city and city != '':
            tmp_city = city
            if city == '不统计':
                city = '省直辖'
            tmp_city = PlaceLocation.objects.create(name=city,parent=tmp_province)
            print(f"City {city} in Province {tmp_province}")

        elif country and country != '':
            tmp_country = country
            tmp_country,dum = PlaceLocation.objects.get_or_create(name=country,parent=tmp_city)
            print(f"Country {country} in City {tmp_city}")

def clear_all():
    PlaceLocation.objects.all().delete()

def clear_butongji():
    res = PlaceLocation.objects.filter(name='不统计').delete()
    print(res)

if __name__ == '__main__':
    clear_butongji()
    #clear_all()
    #import_place_data_from_excel(path)