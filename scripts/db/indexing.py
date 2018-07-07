from pymongo import MongoClient

indexDict = {
    'kavita': [("content", "text")],
    'kahani': [("kahaniText", "text")],
    'dohe': [("doha", "text")],
    'muhavare': [("muhavara", "text")],
    'dictionary': [("key", "text")]
}

# Function to create index according to scheme define in indexDict dictionary.
def create_indexes():
    for k, vl in indexDict.items():
        create_index(collectionDict[k], vl)
        print('After creating...')
        get_indexes(collectionDict[k])
        drop_index(collectionDict[k], vl)
        print('After dropping...')
        get_indexes(collectionDict[k])


# Function to index a collection on the keys.
def create_index(collection, keys):
    collection.create_index(keys)


# Function to output all the indexes of a collection.
def get_indexes(collection):
    indexes = collection.list_indexes()
    for index in indexes:
        print('Index: ', index)
    print("Total number of indexes: ", len(indexes))


# Function to drop an index from a collection..
def drop_index(collection, index):
    collection.drop_index(index)