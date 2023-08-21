from django.apps import AppConfig
from aws_secrets_utils import get_LIR_secrets

class SearchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'search'

    # initialise Pinecone DB connection
    def ready(self):

        import pinecone
        
        # define Pinecone api key
        pinecone_api_key = get_LIR_secrets()['pinecone_api_key']
        
        # initalise pinecone 
        pinecone.init(api_key=pinecone_api_key, environment="us-west4-gcp")

        return 
    
                


    


