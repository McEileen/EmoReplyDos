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
    sims = trained_model.docvecs.most_similar([inferred_vector],
                                              topn=len(trained_model.docvecs))

    # Compare & print the most/median/least similar docs from the train corpus
    print('Test Doc ({}): «{}»\n'.format(doc_id, ' '.join(test_corpus[doc_id].words))) # noqa
    print(u'SIMILAR/DISSIMILAR DOCS PER MODEL %s:\n' % trained_model)
    for label, idx in [('MOST', 0), ('MEDIAN', len(sims)//2), ('LEAST', len(sims) - 1)]: # noqa
        print(u'%s %s: «%s»\n' % (label, sims[idx], ' '.join(train_corpus[sims[idx][0]].words))) # noqa


if __name__ == '__main__':
    test_model()
