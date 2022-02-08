# GCP Python API - Create bucket, upload to bucket, download from bucket

### Steps:

+ Enable API
  + API and Services 
  + Select Cloud Storage API and enable 
+ Enable credentials
  + Give the  credentials a name
  + Cloud storage - Owner Role 
  + Click on the service account you just created and download the JSON key file
+ Python:
  + pip install --upgrade google-cloud-storage
+ GCP
  + Create a new bucket 





## Quick Command Reference:
```
pip install --upgrade google-cloud-storage

```

# Errors Encountered:

+ Note bucket.location is depricated

Assignment to 'Bucket.location' is deprecated, as it is only valid before the bucket is created. Instead, pass the location to `Bucket.create

https://stackoverflow.com/questions/54992263/creating-bucket-in-google-cloud-storage-in-custom-location

+ Note use unique google storage bucket name
google.api_core.exceptions.Conflict: 409 POST https://storage.googleapis.com/storage/v1/b?project=tranquil-lore-340713&prettyPrint=false: You already own this bucket. Please select another name.