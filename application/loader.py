__author__ = 'guillermo'

import sh

def load_data_set(host, api, graph_uri):
    sh.curl(host+api+graph_uri,
       digest=True, u="dba:root", verbose=True, X="POST", T="generated/../generated/dataset.ttl")


