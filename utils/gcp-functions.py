import requests, zipfile, io
from google.cloud import storage

GCP_PROJECT_ID = ''
STORAGE_BUCKET_NAME = ''
# You need to have a service account if this runs on a local machine
storage_client = storage.Client(project=GCP_PROJECT_ID)

def create_bucket(dataset_name):    
     """Creates a new bucket"""    
     print('function create_bucket called')    
     bucket = storage_client.create_bucket(dataset_name)
     print('Bucket {} created'.format(bucket.name))

def delete_bucket(bucket_name):
    """Deletes a bucket. The bucket must be empty."""
    # bucket_name = "your-bucket-name"
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    bucket.delete()
    print("Bucket {} deleted".format(bucket.name))  
    
def list_blobs(bucket_name):
    """Lists all the blobs in the bucket"""
    blobs = storage_client.list_blobs(bucket_name)
    for blob in blobs:
        print(blob.name)
        
def upload_blob(bucket_name, source_data, destination_blob_name):
    """Uploads a file to the bucket."""    
    print('function upload_blob called')     
    bucket = storage_client.get_bucket(bucket_name)    
    blob = bucket.blob(destination_blob_name)    
    blob.upload_from_string(source_data)    
    print('File {} uploaded to {}.'.format(destination_blob_name, bucket_name))

def upload_fao_data(request):
    zip_file_url = "https://fenixservices.fao.org/faostat/static/bulkdownloads/Food_Security_Data_E_All_Data_(Normalized).zip"
    r = requests.get(zip_file_url)
    z = zipfile.ZipFile(io.BytesIO(r.content))

    for filename in z.namelist():  
        print(filename)  
        with z.open(filename) as f:  
            data = f.read()  
            upload_blob(STORAGE_BUCKET_NAME,
                        data,
                        filename)
                        
    return list_blobs(STORAGE_BUCKET_NAME)