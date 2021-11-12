from django.core.management.base import BaseCommand
import pandas as pd
import json
from portal_user.serializers import StudentSerializer


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str,
                            help='Indicates the path to file')

    def file_to_records(self, file):
        array = []
        for item in json.loads(file.to_json(orient='records')):
            for key, value in item.items():
                array.append(dict(zip(key.split(','), value.split(","))))
        return array

    def handle(self, *args, **kwargs):
        file = pd.read_csv(kwargs['path'], sep=';')
        serializer = StudentSerializer(data=self.file_to_records(file),
                                       many=True)
        if not serializer.is_valid():
            print(serializer.errors)
        else:
            serializer.save()
            print("Student records added to database..")
