from import_export import resources
from .models import *

class DownloadtableResource(resources.ModelResource):
    class Meta:
        model = Downloadtable