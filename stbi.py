#import fungsi dari file tfidf
from tfidf import tf, idf

#variable
n_terms = 3
total_terms = 100
n_docs = 10000000
n_docs_with_term = 1000

#memanggil fungsi tf untuk menghitung term frequency
#variable tf_value akan menampung file dari hasil komputasi fungsi tf
tf_value = tf(n_terms, total_terms)
idf_value = idf(n_docs, n_docs_with_term)
#print tf_value
print("Term frequency: {0}".format(tf_value))
print("Inverse document frequency: {0}".format(idf_value))

tfidf_value = tf_value * idf_value

print("Tf * idf: {0}".format(tfidf_value))
