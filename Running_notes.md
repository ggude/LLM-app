```Java script 
1.Embeddings :
https://medium.com/misc-posts/an-experiment-with-similarity-search-and-a-vector-database-part-2-7e82dbdbb7cd
text embedding models:

1. all-MiniLM-L6-v2 (“MiniLM”)
2. text-embedding-ada-002 (“Ada”)
3. text-similarity-davinci-001 (Davinci”)

Ada embeddings performed better than MiniLM. This may be attributable to its higher dimension (1536 vs 384),
and also ChatGPT, which also likely uses Ada or its close variant, was used to generate target result sentences.

Github link : https://github.com/neelp-git/embeddings-similarity/blob/main/similarity2.ipynb

2. BM25 -  "Best Matching 25," is a ranking algorithm used in information retrieval and search engines.
It addresses some of the limitations of TF-IDF(Term Frequency-Inverse Document Frequency) weighting.
"ranking" refers to the process of ordering or prioritizing documents in a search engine's search results
based on their relevance to a user's query.It calculates a score.
key components of the BM25 algorithm:
Term Frequency (TF), Inverse Document Frequency (IDF), Document Length,k1 and b are tuning parameters that control the saturation effects.
```
