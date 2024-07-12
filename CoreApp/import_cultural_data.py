import os
import openpyxl
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DDFWSql2.settings')
application = get_wsgi_application()

from CoreApp.models import CulturalAgriProduct, CulturalDelicacies, CulturalProcessedProduct


def import_data_from_excel(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        category_name = row[0].strip()
        parent_name = row[1].strip()
        child_name = row[2].strip()
        print(category_name,parent_name,child_name)

        # Determine model class based on category_name
        if category_name == '初级农产品':
            ModelClass = CulturalAgriProduct
        elif category_name == '美食':
            ModelClass = CulturalDelicacies
        elif category_name == '加工食品':
            ModelClass = CulturalProcessedProduct
        else:
            print(f"Unknown category: {category_name}")
            continue

        # Check if parent exists, create if not
        parent_obj, created = ModelClass.objects.get_or_create(name=parent_name, parent=None)

        # Create child with parent relationship
        child_obj, created = ModelClass.objects.get_or_create(name=child_name, parent=parent_obj)

        if created:
            print(f"Created {child_obj}")

    print("Import completed.")


if __name__ == "__main__":
    file_path = "E:\WangTR2\College2\C2-3\DDFW\数据结构表0711\美食.xlsx"  # Update with your actual file path
    import_data_from_excel(file_path)
