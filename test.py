import preprocess

tkn_txt = preprocess.tokenize_text('My name is Saikat')
while("" in tkn_txt) : 
    tkn_txt.remove("") 
print(preprocess.pos_tagger([tkn_txt]))
X = [preprocess.extract_features(preprocess.pos_tagger([tkn_txt])[0])]

print(preprocess.predict_label(X))