import pandas

df = pandas.read_csv('emotional_arguments.csv')

df = df.sample(frac=1)

df = df.sort_index(ascending=True)
df = df.iloc[:1000]

df.drop('confidence', inplace=True, axis=1)
df.drop('dataset', inplace=True, axis=1)

df['model']='simpleDataViewer.EmoArgument'
df = df.reindex(['model', 'id', 'argument', 'arg_strength', 'stance', 'topic', 'label'], axis=1)

df = df.to_json('emotional_arguments.json', orient = 'records')
