# %env PYTHONHASHSEED=0
from copyreg import pickle
from django.shortcuts import render,redirect
import joblib
import nltk
from nltk.stem import WordNetLemmatizer
# from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from nltk.corpus import stopwords
import re
import joblib
# import pickle
from tensorflow.keras.preprocessing.text import hashing_trick

# nltk.download('omw-1.4')

def wordEmbedding(sample_tweet):
    w=WordNetLemmatizer()
    samp_out=re.sub('[^a-zA-Z]', ' ', sample_tweet)
    samp_out=samp_out.lower()
    samp_out=samp_out.split()
    samp_out=[w.lemmatize(word) for word in samp_out if not word in set(stopwords.words("english"))]
    samp_out=" ".join(samp_out)
    print(samp_out)

    # if 

    voc_size=20000
    oh_rep=hashing_trick(samp_out,voc_size,hash_function='md5' )
    print(oh_rep)

    sent_length=30
    emb_docs=pad_sequences([oh_rep],padding='pre',maxlen=sent_length)
    print(emb_docs)
    return emb_docs

# Create your views here.
def answer(request,context):
    return render(request,"classifyTweets/result.html",context)

def takeInput(request):

    if request.method == 'POST':
        # model = pickle.load('rnn_model.pkl')
        # model = pickle.load(open('rnn_model.pkl', 'rb'))

        model = load_model('tweet_ananlyse.h5')

        input_data = request.POST['inputbox']
        processed_input = wordEmbedding(input_data) 
        # print(processed_input)

        probVal = model.predict(processed_input)
        print(probVal)
        
        if probVal>0.5:
            ans = 1
        else:
            ans = 0

        # ans=1

        context={
            "tweet":input_data,
            "ans":ans
        }
            
        return answer(request, context)



    return render(request,"classifyTweets/inputTweet.html")
