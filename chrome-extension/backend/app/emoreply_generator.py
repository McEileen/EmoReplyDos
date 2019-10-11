import gensim
import smart_open


def read_corpus(source_text, tokens_only=False):
    with smart_open.open(source_text, encoding="iso-8859-1") as f:
        for i, line in enumerate(f):
            if tokens_only:
                yield gensim.utils.simple_preprocess(line)
            else:
                yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(line), [i]) # noqa


def create_train_corpus(source_text):
    corpus = list(read_corpus(source_text))
    return corpus


def create_ref_corpus(source_text):
    ref_corpus = []
    with smart_open.open(source_text) as f:
        for i, line in enumerate(f):
            ref_corpus.append(line)
    return ref_corpus


def build_model(train_corpus):
    model = gensim.models.doc2vec.Doc2Vec(vector_size=50, min_count=2, epochs=40) # noqa
    model.build_vocab(train_corpus)
    return model


def train_model(model, train_corpus):
    model.train(train_corpus, total_examples=model.corpus_count, epochs=model.epochs) # noqa
    return model


def find_perks_response(model, input, train_corpus, ref_corpus):
    tokenized_input = gensim.utils.simple_preprocess(input)
    inferred_vector = model.infer_vector(tokenized_input)
    most_sim_vector = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))[0] # noqa
    response_idx = most_sim_vector[0]
    response = ref_corpus[response_idx].strip()
    return response
