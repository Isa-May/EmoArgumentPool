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

#df.drop('Id', inplace=True, axis=1)
#df = df.iloc[: , 1:]
#df.to_csv('emotional_arguments.csv', index=False)
from django.db import transaction


##df = pandas.read_csv('emotional_arguments.csv')
#argument_ = df['argument']
#arg_strength_ = df['arg_strength']
#topic_ = df['topic']
#stance_ = df['stance']
#label_ = df['label']

#all_attributes = zip(argument_, arg_strength_, topic_,stance_, label_)
#with transaction.atomic():
 #   for obj_ in all_attributes:
  #      .save()

#print(list(all_attributes))
