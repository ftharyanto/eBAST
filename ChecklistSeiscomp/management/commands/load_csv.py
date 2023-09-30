from csv import DictReader
from django.core.management import BaseCommand

# Import the model 
from ChecklistSeiscomp.models import StationListModel


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from csv file"

    def handle(self, *args, **options):
    
        # Show this if the data already exist in the database
        if StationListModel.objects.exists():
            print('csv data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
            
        # Show this before loading the data into the database
        print("Loading csv data")


        #Code to load the data into database
        for row in DictReader(open('./station_list.csv')):
            data=StationListModel(kode=row['kode'],
                                  lokasi=row['stasiun'],
                                  tipe=row['tipe'])  
            data.save()