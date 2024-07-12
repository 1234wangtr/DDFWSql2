import os
import openpyxl
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DDFWSql2.settings')
application = get_wsgi_application()

from CoreApp.models import PlaceLocation, PlaceNatural, PlaceHumanistic

def import_place_data_from_excel(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        category_name = row[0].strip()
        parent_name = row[1].strip()
        try:
            child_name = row[2].strip()
        except:
            child_name = ''
        try:
            subchild_name = row[3].strip()
        except:
            subchild_name = ''

        # Determine model class based on category_name
        if category_name == '行政区划':
            ModelClass = PlaceLocation
        elif category_name == '自然景观':
            ModelClass = PlaceNatural
        elif category_name == '人文景观':
            ModelClass = PlaceHumanistic
        else:
            print(f"Unknown category: {category_name}")
            continue

        # Check if parent exists, create if not
        parent_obj, created = ModelClass.objects.get_or_create(name=parent_name, parent=None)
        if created:
            print(f"Created {parent_obj}")

        if not child_name or child_name=='':
            continue
        child_obj, created = ModelClass.objects.get_or_create(name=child_name, parent=parent_obj)
        if created:
            print(f"Created {child_obj} under {parent_obj}")

        if not subchild_name or subchild_name=='':
            continue
        subchild_obj, created = ModelClass.objects.get_or_create(name=subchild_name, parent=child_obj)
        if created:
            print(f"Created {subchild_obj} under {child_obj}")




    print("Import completed.")

if __name__ == "__main__":
    file_path = "E:\WangTR2\College2\C2-3\DDFW\数据结构表0711\在地.xlsx"  # Update with your actual file path
    import_place_data_from_excel(file_path)
