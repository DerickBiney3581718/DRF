from algoliasearch_django import algolia_engine

def get_client():
    return algolia_engine.client
# Get the client


def get_index(index_name='dev_cfe_Product'):
    """
    Gets the client from the algolia engine and 
    returns the index to be used.
    Args:
        index_name (str, optional): _description_. Defaults to 'dev_cfe_Products'.
    Returns:
        _type_: _description_
    """
    client = get_client()
    index = client.init_index(index_name)
    return index

def perform_search(query, **kwargs):
    index = get_index()
    params = {}
    tags = ""
    if 'tags' in kwargs:
        tags = kwargs.pop('tags') or []
        if len(tags) != 0:
            params['tagFilters'] = tags
    index_filters = [f"{k}:{v}" for k,v in kwargs.items() if v]
    if len(index_filters):
        params['facetFilters'] = index_filters
    results = index.search(query, params)
    return results