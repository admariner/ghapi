# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['GH_HOST', 'GhApi']

# Cell
from fastcore.utils import *
from fastcore.foundation import *
from fastcore.meta import *

import pprint,inspect,json,copy,urllib,mimetypes
from inspect import signature,Parameter,Signature
from urllib.parse import urlencode
from .metadata import funcs
from urllib.request import Request,urlretrieve

# Cell
GH_HOST = "https://api.github.com"
_DOC_URL = 'https://docs.github.com/'

# Cell
def _mk_param(nm, **kwargs): return Parameter(nm, kind=Parameter.POSITIONAL_OR_KEYWORD, **kwargs)

def _mk_sig(req_args, def_args):
    "Create a signature object with required and default arguments"
    params =  [_mk_param(k) for k in req_args]
    params += [_mk_param(k, default=v) for k,v in def_args.items()]
    return Signature(params)

# Cell
class _GhVerb:
    __slots__ = 'path,verb,tag,name,summary,url,route_ps,params,data,hdrs,__doc__'.split(',')
    def __init__(self, path, verb, oper, summary, url, params, data, hdrs, kwargs):
        tag,name = oper.split('/')
        name = name.replace('-','_')
        path,route_ps,_ = partial_format(path, **kwargs)
        __doc__ = summary
        store_attr()

    def __call__(self, *args, headers=None, **kwargs):
        headers = {**headers,**self.hdrs} if headers else self.hdrs
        flds = [o for o in self.route_ps+self.params+self.data if o not in kwargs]
        for a,b in zip(args,flds): kwargs[b]=a
        route_p,query_p,data_p = [{p:kwargs[p] for p in o if p in kwargs}
                                 for o in (self.route_ps,self.params,self.data)]
        return dict2obj(urlsend(GH_HOST+self.path, self.verb, headers=headers,
                              route=route_p, query=query_p, data=data_p))

    @property
    def __signature__(self): return _mk_sig(self.route_ps, dict.fromkeys(self.params+self.data))
    __call__.__signature__ = __signature__

    def _repr_markdown_(self):
        params = ', '.join(self.route_ps+self.params+self.data)
        return f"[{self.tag}/{self.name}]({_DOC_URL}{self.url})({params}): *{self.summary}*"
    __repr__ = _repr_markdown_

class _GhVerbGroup:
    def __init__(self, verbs):
        self.verbs = verbs
        for o in verbs: setattr(self, o.name, o)
    def _repr_markdown_(self): return "\n".join(f'- [{v.name}]({_DOC_URL}{v.url})' for v in self.verbs)

# Cell
_docroot = 'https://docs.github.com/en/free-pro-team@latest/rest/reference/'

# Cell
class GhApi:
    def __init__(self, owner=None, repo=None, token=None, **kwargs):
        self.headers = { 'Accept': 'application/vnd.github.v3+json' }
        if token: self.headers['Authorization'] = 'token ' + token
        if owner: kwargs['owner'] = owner
        if repo:  kwargs['repo' ] = repo
        funcs_ = L(funcs).starmap(_GhVerb, hdrs=self.headers, kwargs=kwargs)
        self._fs = {k:_GhVerbGroup(v) for k,v in groupby(funcs_, 'tag').items()}

    def __dir__(self): return super().__dir__() + list(self._fs)
    def _repr_markdown_(self): return "\n".join(f'- [{o}]({_docroot+o})' for o in self._fs)
    def __getattr__(self,k): return self._fs[k] if k in self._fs else stop(AttributeError(k))

# Cell
@patch
def _upload_file(self:GhApi, url:str, fn:str):
    "Upload `fn` to endpoint `url`"
    mime = mimetypes.guess_type(fn, False)[0] or 'application/octet-stream'
    headers = {**self.headers, 'Content-Type':mime}
    data = Path(fn).read_bytes()
    return urlsend(url, 'POST', headers=headers, query = {'name':fn}, data=data)

# Cell
@patch
def create_release(self:GhApi, tag_name, branch='master', name=None, body='',
                   draft=False, prerelease=False, files=None):
    "Wrapper for `GhApi.repos.create_release` which also uploads `files`"
    if name is None: name = 'v'+tag_name
    rel = self.repos.create_release(tag_name, target_commitish=branch, name=name, body=body,
                                   draft=draft, prerelease=prerelease)
    url = rel.upload_url.replace('{?name,label}','')
    for file in listify(files): self._upload_file(url, file)
    return rel

# Cell
@patch
def list_tags(self:GhApi, prefix:str=''):
    "List all tags, optionally filtered to those starting with `prefix`"
    return self.git.list_matching_refs(f'tags/{prefix}')

# Cell
@patch
def list_branches(self:GhApi, prefix:str=''):
    "List all branches, optionally filtered to those starting with `prefix`"
    return self.git.list_matching_refs(f'heads/{prefix}')

# Cell
@patch
def delete_release(self:GhApi, release):
    "Delete a release and its associated tag"
    self.repos.delete_release(rel.id)
    self.git.delete_ref(ref)