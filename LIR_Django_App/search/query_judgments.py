import pinecone
import psycopg2
from transformers import AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer, util
from .models import Judgments
from .apps import SearchConfig

# instantiate  Sentence Bert model from Huggingface
print("Loading SBert model...")
model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
print("SBert model loaded!")


# method to get SBert embeddings from user query
def get_user_embeddings(user_query):    
   
    # create user query embeddings
    query_embeddings = model.encode([user_query]).tolist()
        
    print(query_embeddings) # prints out embeddings to console

    return query_embeddings


# method to query Pinecone index with query embeddings
def query_pinecone(query_embeddings, num_judgments):

    # connect to Pinecone index
    pinecone_index = pinecone.Index("case-embeddings")
    print(pinecone_index.describe_index_stats()) #logs pinecone index to console
    
    # call the pinecone query function to return the top x judgments
    top_judgment_ids = pinecone_index.query(query_embeddings, top_k=num_judgments, include_metadata=False)

    return top_judgment_ids


# method to retrieve judgments docs from PostgreSQL DB based on returned ids from Pinecone
def get_judgments(top_judgment_ids):        

    judgments_dict = {} # store judgment object and similarity score in dictionary 

    # loop over returned judgment ids from Pinecone
    for judgment in top_judgment_ids["matches"]:

        judgment_id = judgment.id
        similarity_score = judgment.score
        similarity_score = '{:.2%}'.format(similarity_score) # return score as percentage

        # retrieve top judgments from judgments_DB using corresponding IDs
        judgment = Judgments.objects.get(pk = judgment_id)

        # assign to dict object
        judgment_similarity = {'similarity' : similarity_score}

        # assign similarity to judgment object key in dict
        judgments_dict[judgment]=judgment_similarity
    
    return judgments_dict











