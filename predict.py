import pycrfsuite
tagger = pycrfsuite.Tagger()

def predict_label(txt):
  tagger.open('./model/crf.model')
  return [tagger.tag(xseq) for xseq in txt]