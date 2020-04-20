"""
getbucket and getobject are two tiny getter functions for getting s3 bucket and file names

>> getbucket(event['Records'][0])
'lambda-artifacts-deafc19498e3f2df'

>> [*map(getobject, event['Records'])]
.. ['b21b84d653bb07b05b1e6b33684dc11b',
..  'b21b84d653bb07b05b1e6b33684dc11a',
..  'b21b84d653bb07b05b1e6b33684dc11c']

"""
import operator
from functools import reduce, partial

getbucket = partial(reduce, operator.getitem, ["s3", "bucket", "name"])
getobject = partial(reduce, operator.getitem, ["s3", "object", "key"])
