data = {'neg':0, 'pos':0}
with open('PA_temp.tsv') as f:
    for l in f.readlines():
        if l != '\n':
            if l.split('\t')[1] == 'neg':
                data['neg']+=1
            else:
                data['pos']+=1
print(data)