# Internal - OpenAPI Parser


<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

This library leverages the [OpenAPI
Specification](https://github.com/OAI/OpenAPI-Specification) to create a
python client for the GitHub API. The OpenAPI specification contains
metadata on all of the endpoints and how to access them properly. Using
this metadata, we can construct a python client dynamically that updates
automatically along with the OpenAPI Spec.

------------------------------------------------------------------------

<a
href="https://github.com/fastai/ghapi/blob/master/ghapi/build_lib.py#L38"
target="_blank" style="float:right; font-size:smaller">source</a>

### build_funcs

>      build_funcs (nm='ghapi/metadata.py', url='https://github.com/github/rest-
>                   api-description/raw/main/descriptions/api.github.com/api.git
>                   hub.com.json?raw=true', docurl='https://docs.github.com/')

*Build module metadata.py from an Open API spec and optionally filter by
a path `pre`*

This module created by
[`build_funcs`](https://ghapi.fast.ai/build_lib.html#build_funcs)
contains a list of metadata for each endpoint, containing the path,
verb, operation id, summary, documentation relative URL, and list of
parameters (if any), e.g:

``` python
from ghapi.metadata import funcs
```

``` python
GhMeta(*funcs[3])
```

    GhMeta(path='/app/hook/config', verb='get', oper_id='apps/get-webhook-config-for-app', summary='Get a webhook configuration for an app', doc_url='rest/reference/apps#get-a-webhook-configuration-for-an-app', params=[], data=[], preview='')