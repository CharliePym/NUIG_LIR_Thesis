from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Judgments
from .forms import UserInputForm
from .query_judgments import get_user_embeddings, query_pinecone, get_judgments

# app homepage
def homepage(request):

    template = loader.get_template('home.html')

    return HttpResponse(template.render())

# app about page
def about_page(request):

    template = loader.get_template('about.html')

    return HttpResponse(template.render())

# app search page
def search_page(request):

    query_form = UserInputForm(request.POST)
    
    # check that form is valid
    if query_form.is_valid():
        query_dict = query_form.cleaned_data  # return dict of valid user input
        user_query = query_dict.get('search_query')  # get user query
        num_judgments = int(query_dict.get('num_judgments')) # get num_judgments in INT format      

        query_embeddings = get_user_embeddings(user_query)  # get query embeddings

        # retrieve judgment ids from pinecone based on query embeddings
        top_judgments_ids = query_pinecone(query_embeddings, num_judgments)

        # get judgements from DB based on Pinecone ids
        retrieved_judgments = get_judgments(top_judgments_ids)
        print(retrieved_judgments)

        # return retrieved judgments on results page
        return render(request, 'results.html', {'top_judgments': retrieved_judgments})

    return render(request, "search.html", {'form': query_form})

# app results page
def results_page(request):

    top_judgments = {'top_judgments': None}

    template = loader.get_template('results.html')

    return HttpResponse(template.render(request, top_judgments))

# app judgment page 
def judgment_page(request, judgment_id):

    judgment = get_object_or_404(Judgments, judgment_id=judgment_id)
    
    return render(request, 'judgment.html', {'judgment': judgment})



