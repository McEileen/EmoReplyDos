import gensim
import smart_open


def read_corpus(source_text, tokens_only=False):
    with smart_open.open(source_text, encoding="iso-8859-1") as f:
        for i, line in enumerate(f):
            if tokens_only:
                yield gensim.utils.simple_preprocess(line)
            else:
                yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(line), [i])


def build_model(source_text):
    corpus = list(read_corpus(source_text))
    model = gensim.models.doc2vec.Doc2Vec(vector_size=50, min_count=2, epochs=40)
    model.build_vocab(corpus)
    return model


def train_model(model, train_corpus):
    model.train(train_corpus, total_examples=model.corpus_count, epochs=model.epochs)
    return model


def find_perks_response(model, input, train_corpus):
    tokenized_input = gensim.utils.simple_preprocess(input)
    inferred_vector = model.infer_vector(tokenized_input)
    most_sim_vector = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))[0]
    response_idx = most_sim_vector[0]
    response = train_corpus[response_idx]
    reply = ' '.join(response.words).capitalize()
    return reply
