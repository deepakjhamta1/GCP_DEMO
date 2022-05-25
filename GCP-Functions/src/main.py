from google.cloud import storage
from google.cloud import bigquery


def file_trigger(event , context):
    
    storageClient = storage.Client()
    bigqueryClient = bigquery.Client()
    
    
    file = event
    
    uriFilePath = "gs://{}/{}".format(file["bucket"], file["name"])
    