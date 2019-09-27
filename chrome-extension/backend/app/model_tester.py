import os
import random

from emoreply_generator import read_corpus, build_model, train_model

def test_model():
    print("Reading in the training and text corpuses...")
    train_txt = os.getcwd() + "/Perks.txt"
    test_txt = os.getcwd() + "/Perks_Half.txt"
    train_corpus = list(read_corpus(train_txt))
    test_corpus = list(read_corpus(test_txt))
    
    print("Building and training the model....")
    untrained_model = build_model(train_txt)
    trained_model = train_model(untrained_model, train_corpus)    
    
    print("The model is ready!")
    doc_id = random.randint(0, len(test_corpus) - 1)
    inferred_vector = trained_model.infer_vector(test_corpus[doc_id].words)
    sims = trained_model.docvecs.most_similar([inferred_vector], topn=len(trained_model.docvecs))

    # Compare and print the most/median/least similar documents from the train corpus
    print('Test Document ({}): «{}»\n'.format(doc_id, ' '.join(test_corpus[doc_id].words)))
    print(u'SIMILAR/DISSIMILAR DOCS PER MODEL %s:\n' % trained_model)
    for label, index in [('MOST', 0), ('MEDIAN', len(sims)//2), ('LEAST', len(sims) - 1)]:
        print(u'%s %s: «%s»\n' % (label, sims[index], ' '.join(train_corpus[sims[index][0]].words)))
    return 0

if __name__ == '__main__':
    test_model()