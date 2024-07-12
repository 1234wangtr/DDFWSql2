import os
import openpyxl
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DDFWSql2.settings')
application = get_wsgi_application()

from CoreApp.models import HumanisticCategory, HumanisticHeritage, HumanisticTopic

def import_humanistic_data_from_excel(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active

    for row in sheet.iter_rows(min_row=1, values_only=True):
        category_name = row[0].strip()
        parent_name = row[1].strip()
        child_name = row[2].strip()

        # Determine model class based on category_name
        if category_name == '文化类型':
            ModelClass = HumanisticCategory
        elif category_name == '文化遗产':
            ModelClass = HumanisticHeritage
        elif category_name == '文化专题':
            ModelClass = HumanisticTopic
        else:
            print(f"Unknown category: {category_name}")
            continue

        # Check if parent exists, create if not
        parent_obj, created = ModelClass.objects.get_or_create(name=parent_name, parent=None)
        if created:
            print(f"Created {parent_obj}")

        # Create child with parent relationship
        child_obj, created = ModelClass.objects.get_or_create(name=child_name, parent=parent_obj)
        if created:
            print(f"Created {child_obj} under {parent_obj}")

    print("Import completed.")

if __name__ == "__main__":
    file_path = "E:\WangTR2\College2\C2-3\DDFW\数据结构表0711\人文.xlsx"  # Update with your actual file path
    import_humanistic_data_from_excel(file_path)
