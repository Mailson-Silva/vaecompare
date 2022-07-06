#----------------------------------------------------------------------
# Copyright 2018 Marco Inacio <pythonpackages@marcoinacio.com>
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, version 3 of the License.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program. If not, see <http://www.gnu.org/licenses/>.
#----------------------------------------------------------------------

import numpy as np
import pickle

def unpickle(f):
    with open(f, 'rb') as fo:

        obj = pickle.load(fo, encoding='bytes')

    return obj

def get_category(category):
    datasets = []
    for i in range(1, 2):
        #obj = unpickle('datasets/data_batch_' + str(i))
        obj = unpickle('./data' + str(1))
        #https://www.cs.toronto.edu/~kriz/cifar.html  --> CIFAR dataset instructions and files
        #idx = np.array(obj[b'labels']) == category
        #obj = obj[b'data'][idx]
        idx = np.array(obj[b'labels']) == category
        obj = np.array(obj[b'data'])[idx]
        datasets.append(obj)
    x = np.array(np.vstack(datasets), dtype=np.float32)
    x = x / 255

    print(np.shape(x))
    return x

def get_categories(category1, category2):
    if category1 != category2:
        print('c1: ', category1)
        print('c2: ', category2)
        db1 = get_category(category1)
        db2 = get_category(category2)
        l_db1 = len(db1)
        print(l_db1)
        l_db2 = len(db2)
        print(l_db2)

        db1 = db1[np.random.choice(range(l_db1), int(l_db1/2), False)]
        db2 = db2[np.random.choice(range(l_db2), int(l_db2/2), False)]
        db1 = db1[np.random.choice(range(len(db1)), 10, False)]
        db2 = db2[np.random.choice(range(len(db2)), 10, False)]
    else:
        db = get_category(category1)
        l_db = len(db)
        idx1 = np.random.choice(range(l_db), int(l_db/2), False)
        idx2 = list(set(range(l_db)).difference(idx1))
        idx1 = np.random.choice(range(20), 10, False)
        idx2 = list(set(range(20)).difference(idx1))
        db1 = np.ascontiguousarray(db[idx1])
        db2 = np.ascontiguousarray(db[idx2])

    return db1, db2
'''


def get_categories(category1, category2):
    if category1 != category2:
        db1 = get_category(category1)
        db2 = get_category(category2)
        db1 = db1[np.random.choice(range(5000), 2500, False)]
        db2 = db2[np.random.choice(range(5000), 2500, False)]
        db1 = db1[np.random.choice(range(100), 50, False)]
        db2 = db2[np.random.choice(range(100), 50, False)]
    else:
        db = get_category(category1)
        idx1 = np.random.choice(range(5000), 2500, False)
        idx2 = list(set(range(5000)).difference(idx1))
        idx1 = np.random.choice(range(100), 50, False)
        idx2 = list(set(range(100)).difference(idx1))
        db1 = np.ascontiguousarray(db[idx1])
        db2 = np.ascontiguousarray(db[idx2])

    return db1, db2
'''

