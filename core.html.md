# GhApi details


<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

You can set an environment variable named `GH_HOST` to override the
default of `https://api.github.com` incase you are running [GitHub
Enterprise](https://github.com/enterprise)(GHE). However, this library
has not been tested on GHE, so proceed at your own risk.

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L100"
target="_blank" style="float:right; font-size:smaller">source</a>

### print_summary

>      print_summary (req:urllib.request.Request)

*Print `Request.summary` with the token (if any) removed*

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L105"
target="_blank" style="float:right; font-size:smaller">source</a>

### GhApi

>      GhApi (owner=None, repo=None, token=None, jwt_token=None, debug=None,
>             limit_cb=None, gh_host=None, authenticate=True, **kwargs)

*Initialize self. See help(type(self)) for accurate signature.*

### Access by path

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L123"
target="_blank" style="float:right; font-size:smaller">source</a>

### GhApi.\_\_call\_\_

>      GhApi.__call__ (path:str, verb:str=None, headers:dict=None,
>                      route:dict=None, query:dict=None, data=None,
>                      timeout=None, decode=True)

*Call a fully specified `path` using HTTP `verb`, passing arguments to
`fastcore.core.urlsend`*

``` python
api = GhApi()
```

You can call a [`GhApi`](https://ghapi.fast.ai/core.html#ghapi) object
as a function, passing in the path to the endpoint, the HTTP verb, and
any route, query parameter, or post data parameters as required.

``` python
api('/repos/{owner}/{repo}/git/ref/{ref}', 'GET', route=dict(
    owner='fastai', repo='ghapi-test', ref='heads/master'))
```

``` json
{ 'node_id': 'MDM6UmVmMzE1NzEyNTg4OnJlZnMvaGVhZHMvbWFzdGVy',
  'object': { 'sha': '17efbb7eb346f0f9161c227af9c8db93597321e2',
              'type': 'commit',
              'url': 'https://api.github.com/repos/fastai/ghapi-test/git/commits/17efbb7eb346f0f9161c227af9c8db93597321e2'},
  'ref': 'refs/heads/master',
  'url': 'https://api.github.com/repos/fastai/ghapi-test/git/refs/heads/master'}
```

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L147"
target="_blank" style="float:right; font-size:smaller">source</a>

### GhApi.\_\_getitem\_\_

>      GhApi.__getitem__ (k)

*Lookup and call an endpoint by path and verb (which defaults to ‘GET’)*

You can access endpoints by indexing into the object. When using the API
this way, you do not need to specify what type of parameter (route,
query, or post data) is being used. This is, therefore, the same call as
above:

``` python
api['/repos/{owner}/{repo}/git/ref/{ref}'](owner='fastai', repo='ghapi-test', ref='heads/master')
```

``` json
{ 'node_id': 'MDM6UmVmMzE1NzEyNTg4OnJlZnMvaGVhZHMvbWFzdGVy',
  'object': { 'sha': '17efbb7eb346f0f9161c227af9c8db93597321e2',
              'type': 'commit',
              'url': 'https://api.github.com/repos/fastai/ghapi-test/git/commits/17efbb7eb346f0f9161c227af9c8db93597321e2'},
  'ref': 'refs/heads/master',
  'url': 'https://api.github.com/repos/fastai/ghapi-test/git/refs/heads/master'}
```

### Media types

For some endpoints GitHub lets you specify a [media
type](https://docs.github.com/en/rest/overview/media-types) the for
response data, using the `Accept` header. If you choose a media type
that is not JSON formatted (for instance
`application/vnd.github.v3.sha`) then the call to the
[`GhApi`](https://ghapi.fast.ai/core.html#ghapi) object will return a
string instead of an object.

``` python
api('/repos/{owner}/{repo}/commits/{ref}', 'GET', route=dict(
    owner='fastai', repo='ghapi-test', ref='refs/heads/master'),
    headers={'Accept': 'application/vnd.github.VERSION.sha'})
```

    '17efbb7eb346f0f9161c227af9c8db93597321e2'

### Rate limits

GitHub has various [rate
limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#rate-limiting)
for their API. After each call, the response includes information about
how many requests are remaining in the hourly quota. If you’d like to
add alerts, or indications showing current quota usage, you can register
a callback with [`GhApi`](https://ghapi.fast.ai/core.html#ghapi) by
passing a callable to the `limit_cb` parameter. This callback will be
called whenever the amount of quota used changes. It will be called with
two arguments: the new quota remaining, and the total hourly quota.

``` python
def _f(rem,quota): print(f"Quota remaining: {rem} of {quota}")

api = GhApi(limit_cb=_f)
api['/repos/{owner}/{repo}/git/ref/{ref}'](owner='fastai', repo='ghapi-test', ref='heads/master').ref
```

    Quota remaining: 4897 of 5000

    'refs/heads/master'

You can always get the remaining quota from the `limit_rem` attribute:

``` python
api.limit_rem
```

    '4897'

## Operations

Instead of passing a path to
[`GhApi`](https://ghapi.fast.ai/core.html#ghapi), you will more often
use the operation methods provided in the API’s operation groups, which
include documentation, signatures, and auto-complete.

If you provide `owner` and/or `repo` to the constructor, they will be
automatically inserted into any calls which use them (except when
calling [`GhApi`](https://ghapi.fast.ai/core.html#ghapi) as a function).
You can also pass any other arbitrary keyword arguments you like to have
them used as defaults for any relevant calls.

You must include a GitHub API token if you need to access any
authenticated endpoints. If don’t pass the `token` param, then your
`GITHUB_TOKEN` environment variable will be used, if available.

``` python
api = GhApi(owner='fastai', repo='ghapi-test', token=token)
```

### Operation groups

The following groups of endpoints are provided, which you can list at
any time along with a link to documentation for all endpoints in that
group, by displaying the
[`GhApi`](https://ghapi.fast.ai/core.html#ghapi) object:

``` python
api
```

- [actions](https://docs.github.com/rest/reference/actions)
- [activity](https://docs.github.com/rest/reference/activity)
- [apps](https://docs.github.com/rest/reference/apps)
- [billing](https://docs.github.com/rest/reference/billing)
- [checks](https://docs.github.com/rest/reference/checks)
- [classroom](https://docs.github.com/rest/reference/classroom)
- [code_scanning](https://docs.github.com/rest/reference/code-scanning)
- [code_security](https://docs.github.com/rest/reference/code-security)
- [codes_of_conduct](https://docs.github.com/rest/reference/codes-of-conduct)
- [codespaces](https://docs.github.com/rest/reference/codespaces)
- [copilot](https://docs.github.com/rest/reference/copilot)
- [dependabot](https://docs.github.com/rest/reference/dependabot)
- [dependency_graph](https://docs.github.com/rest/reference/dependency-graph)
- [emojis](https://docs.github.com/rest/reference/emojis)
- [gists](https://docs.github.com/rest/reference/gists)
- [git](https://docs.github.com/rest/reference/git)
- [gitignore](https://docs.github.com/rest/reference/gitignore)
- [interactions](https://docs.github.com/rest/reference/interactions)
- [issues](https://docs.github.com/rest/reference/issues)
- [licenses](https://docs.github.com/rest/reference/licenses)
- [markdown](https://docs.github.com/rest/reference/markdown)
- [meta](https://docs.github.com/rest/reference/meta)
- [migrations](https://docs.github.com/rest/reference/migrations)
- [oidc](https://docs.github.com/rest/reference/oidc)
- [orgs](https://docs.github.com/rest/reference/orgs)
- [packages](https://docs.github.com/rest/reference/packages)
- [projects](https://docs.github.com/rest/reference/projects)
- [pulls](https://docs.github.com/rest/reference/pulls)
- [rate_limit](https://docs.github.com/rest/reference/rate-limit)
- [reactions](https://docs.github.com/rest/reference/reactions)
- [repos](https://docs.github.com/rest/reference/repos)
- [search](https://docs.github.com/rest/reference/search)
- [secret_scanning](https://docs.github.com/rest/reference/secret-scanning)
- [security_advisories](https://docs.github.com/rest/reference/security-advisories)
- [teams](https://docs.github.com/rest/reference/teams)
- [users](https://docs.github.com/rest/reference/users)

``` python
api.codes_of_conduct
```

- [codes-of-conduct.get_all_codes_of_conduct](https://docs.github.com/rest/codes-of-conduct/codes-of-conduct#get-all-codes-of-conduct)():
  *Get all codes of conduct*
- [codes-of-conduct.get_conduct_code](https://docs.github.com/rest/codes-of-conduct/codes-of-conduct#get-a-code-of-conduct)(key):
  *Get a code of conduct*

### Calling endpoints

The GitHub API’s endpoint names generally start with a verb like “get”,
“list”, “delete”, “create”, etc, followed `_`, then by a noun such as
“ref”, “webhook”, “issue”, etc.

Each endpoint has a different signature, which you can see by using
<kbd>Shift</kbd>-<kbd>Tab</kbd> in Jupyter, or by just printing the
endpoint object (which also shows a link to the GitHub docs):

``` python
print(api.repos.create_webhook)
```

    repos.create_webhook(name: str = None, config: dict = None, events: list = ['push'], active: bool = True)
    https://docs.github.com/rest/repos/webhooks#create-a-repository-webhook

Displaying an endpoint object in Jupyter also provides a formatted
summary and link to the official GitHub documentation:

``` python
api.repos.create_webhook
```

[repos.create_webhook](https://docs.github.com/rest/repos/webhooks#create-a-repository-webhook)(name,
config, events, active): *Create a repository webhook*

Endpoint objects are called using standard Python method syntax:

``` python
ref = api.git.get_ref('heads/master')
test_eq(ref.object.type, 'commit')
```

Information about the endpoint are available as attributes:

``` python
api.git.get_ref.path,api.git.get_ref.verb
```

    ('/repos/fastai/ghapi-test/git/ref/{ref}', 'get')

You can get a list of all endpoints available in a group, along with a
link to documentation for each, by viewing the group:

``` python
api.git
```

- [git.create_blob](https://docs.github.com/rest/git/blobs#create-a-blob)(content,
  encoding): *Create a blob*
- [git.get_blob](https://docs.github.com/rest/git/blobs#get-a-blob)(file_sha):
  *Get a blob*
- [git.create_commit](https://docs.github.com/rest/git/commits#create-a-commit)(message,
  tree, parents, author, committer, signature): *Create a commit*
- [git.get_commit](https://docs.github.com/rest/git/commits#get-a-commit-object)(commit_sha):
  *Get a commit object*
- [git.list_matching_refs](https://docs.github.com/rest/git/refs#list-matching-references)(ref):
  *List matching references*
- [git.get_ref](https://docs.github.com/rest/git/refs#get-a-reference)(ref):
  *Get a reference*
- [git.create_ref](https://docs.github.com/rest/git/refs#create-a-reference)(ref,
  sha): *Create a reference*
- [git.update_ref](https://docs.github.com/rest/git/refs#update-a-reference)(ref,
  sha, force): *Update a reference*
- [git.delete_ref](https://docs.github.com/rest/git/refs#delete-a-reference)(ref):
  *Delete a reference*
- [git.create_tag](https://docs.github.com/rest/git/tags#create-a-tag-object)(tag,
  message, object, type, tagger): *Create a tag object*
- [git.get_tag](https://docs.github.com/rest/git/tags#get-a-tag)(tag_sha):
  *Get a tag*
- [git.create_tree](https://docs.github.com/rest/git/trees#create-a-tree)(tree,
  base_tree): *Create a tree*
- [git.get_tree](https://docs.github.com/rest/git/trees#get-a-tree)(tree_sha,
  recursive): *Get a tree*

For “list” endpoints, the noun will be a plural form, e.g.:

``` python
hooks = api.repos.list_webhooks()
test_eq(len(hooks), 0)
```

You can pass dicts, lists, etc. directly, where they are required for
GitHub API endpoints:

``` python
url = 'https://example.com'
cfg = dict(url=url, content_type='json', secret='XXX')
hook = api.repos.create_webhook(config=cfg, events=['ping'])
test_eq(hook.config.url, url)
```

Let’s confirm that our new webhook has been created:

``` python
hooks = api.repos.list_webhooks()
test_eq(len(hooks), 1)
test_eq(hooks[0].events, ['ping'])
```

Finally, we can delete our new webhook:

``` python
api.repos.delete_webhook(hooks[0].id)
```

``` json
{}
```

### Convenience functions

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L156"
target="_blank" style="float:right; font-size:smaller">source</a>

### date2gh

>      date2gh (dt:datetime.datetime)

*Convert `dt` (which is assumed to be in UTC time zone) to a format
suitable for GitHub API operations*

The GitHub API assumes that dates will be in a specific string format.
[`date2gh`](https://ghapi.fast.ai/core.html#date2gh) converts Python
standard `datetime` objects to that format. For instance, to find issues
opened in the ‘fastcore’ repo in the last 4 weeks:

``` python
dt = date2gh(datetime.utcnow() - timedelta(weeks=4))
issues = GhApi('fastai').issues.list_for_repo(repo='fastcore', since=dt)
len(issues)
```

    3

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L161"
target="_blank" style="float:right; font-size:smaller">source</a>

### gh2date

>      gh2date (dtstr:str)

*Convert date string `dtstr` received from a GitHub API operation to a
UTC `datetime`*

``` python
created = issues[0].created_at
print(created, '->', gh2date(created))
```

    2024-08-27T06:49:29Z -> 2024-08-27 06:49:29

You can set the `debug` attribute to any callable to intercept all
requests, for instance to print `Request.summary`.
[`print_summary`](https://ghapi.fast.ai/core.html#print_summary) is
provided for this purpose. Using this, we can see the preview header
that is added for preview functionality, e.g.

``` python
api.debug=print_summary
api.codes_of_conduct.get_all_codes_of_conduct()[0]
api.debug=None
```

    {'data': None,
     'full_url': 'https://api.github.com/codes_of_conduct',
     'headers': {'Accept': 'application/vnd.github.v3+json'},
     'method': 'GET'}

### Preview endpoints

GitHub’s preview API functionality requires a special header to be
passed to enable it. This is added automatically for you.

## Convenience methods

Some methods in the GitHub API are a bit clunky or unintuitive. In these
situations we add convenience methods to
[`GhApi`](https://ghapi.fast.ai/core.html#ghapi) to make things simpler.
There are also some multi-step processes in the GitHub API that
[`GhApi`](https://ghapi.fast.ai/core.html#ghapi) provide convenient
wrappers for. The methods currently available are shown below; do not
hesitate to [create an
issue](https://github.com/fastai/ghapi-test/issues) or pull request if
there are other processes that you’d like to see supported better.

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L167"
target="_blank" style="float:right; font-size:smaller">source</a>

### GhApi.create_gist

>      GhApi.create_gist (description, content, filename='gist.txt',
>                         public=False)

*Create a gist containing a single file*

``` python
gist = api.create_gist("some description", "some content")
gist.html_url, gist.files['gist.txt'].content
```

    ('https://gist.github.com/jph00/d11f49a2c4515491f09d520e402ede75',
     'some content')

``` python
api.gists.delete(gist.id)
```

``` json
{}
```

Note that if you want to create a gist with multiple files, call the
GitHub API directly, e.g.:

``` python
api.gists.create("some description", files={"f1.txt": {"content": "my content"}, ...})
```

### Releases

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L173"
target="_blank" style="float:right; font-size:smaller">source</a>

### GhApi.delete_release

>      GhApi.delete_release (release)

*Delete a release and its associated tag*

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L180"
target="_blank" style="float:right; font-size:smaller">source</a>

### GhApi.upload_file

>      GhApi.upload_file (rel, fn)

*Upload `fn` to endpoint for release `rel`*

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L189"
target="_blank" style="float:right; font-size:smaller">source</a>

### GhApi.create_release

>      GhApi.create_release (tag_name, branch='master', name=None, body='',
>                            draft=False, prerelease=False, files=None)

*Wrapper for `GhApi.repos.create_release` which also uploads `files`*

Creating a release and attaching files to it is normally a multi-stage
process, so `create_release` wraps this up for you. It takes the same
arguments as
[`repos.create_release`](https://docs.github.com/rest/reference/repos#create-a-release),
along with `files`, which can contain a single file name, or a list of
file names to upload to your release:

``` python
rel = api.create_release('0.0.1', files=['README.md'])
test_eq(rel.name, 'v0.0.1')
```

``` python
sleep(0.2)
rels = api.repos.list_releases()
test_eq(len(rels), 1)
```

We can check that our file has been uploaded; GitHub refers to them as
“assets”:

``` python
assets = api.repos.list_release_assets(rels[0].id)
test_eq(assets[0].name, 'README.md')
```

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L173"
target="_blank" style="float:right; font-size:smaller">source</a>

### GhApi.delete_release

>      GhApi.delete_release (release)

*Delete a release and its associated tag*

### Branches and tags

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L200"
target="_blank" style="float:right; font-size:smaller">source</a>

### GhApi.list_tags

>      GhApi.list_tags (prefix:str='')

*List all tags, optionally filtered to those starting with `prefix`*

With no `prefix`, all tags are listed.

``` python
test_eq(len(api.list_tags()), 1)
```

Using the full tag name will return just that tag.

``` python
test_eq(len(api.list_tags(rel.tag_name)), 1)
```

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L206"
target="_blank" style="float:right; font-size:smaller">source</a>

### GhApi.list_branches

>      GhApi.list_branches (prefix:str='')

*List all branches, optionally filtered to those starting with `prefix`*

Branches can be listed in the exactly the same way as tags.

``` python
test_eq(len(api.list_branches('master')), 1)
```

We can delete our release and confirm that it is removed:

``` python
api.delete_release(rels[0])
test_eq(len(api.repos.list_releases()), 0)
```

``` python
# #|hide
# #not working
# #|export
# @patch
# def create_branch_empty(self:GhApi, branch):
#     c = self.git.create_commit(f'create {branch}', EMPTY_TREE_SHA)
#     return self.git.create_ref(f'refs/heads/{branch}', c.sha)
```

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L216"
target="_blank" style="float:right; font-size:smaller">source</a>

### GhApi.create_branch_empty

>      GhApi.create_branch_empty (branch)

``` python
ref = api.create_branch_empty("testme")
test_eq(len(api.list_branches('testme')), 1)
```

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L224"
target="_blank" style="float:right; font-size:smaller">source</a>

### GhApi.delete_tag

>      GhApi.delete_tag (tag:str)

*Delete a tag*

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L230"
target="_blank" style="float:right; font-size:smaller">source</a>

### GhApi.delete_branch

>      GhApi.delete_branch (branch:str)

*Delete a branch*

``` python
api.delete_branch('testme')
test_eq(len(api.list_branches('testme')), 0)
```

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L236"
target="_blank" style="float:right; font-size:smaller">source</a>

### GhApi.get_branch

>      GhApi.get_branch (branch=None)

### Content (git files)

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L242"
target="_blank" style="float:right; font-size:smaller">source</a>

### GhApi.list_files

>      GhApi.list_files (branch=None)

``` python
files = api.list_files()
files['README.md']
```

``` json
{ 'mode': '100644',
  'path': 'README.md',
  'sha': 'eaea0f2698e76c75602058bf4e2e9fd7940ac4e3',
  'size': 72,
  'type': 'blob',
  'url': 'https://api.github.com/repos/fastai/ghapi-test/git/blobs/eaea0f2698e76c75602058bf4e2e9fd7940ac4e3'}
```

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L249"
target="_blank" style="float:right; font-size:smaller">source</a>

### GhApi.get_content

>      GhApi.get_content (path)

``` python
readme = api.get_content('README.md').decode()
assert 'ghapi' in readme
```

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L255"
target="_blank" style="float:right; font-size:smaller">source</a>

### GhApi.create_or_update_file

>      GhApi.create_or_update_file (path, message, committer, author,
>                                   content=None, sha=None, branch='')

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L265"
target="_blank" style="float:right; font-size:smaller">source</a>

### GhApi.create_file

>      GhApi.create_file (path, message, committer, author, content=None,
>                         branch=None)

``` python
person = dict(name="Monalisa Octocat", email="octocat@github.com")
res = api.create_file(
    path='foo',
    message="Create foo",
    content="foobar",
    committer=person, author=person
)
test_eq('foobar', api.get_content('foo').decode())
```

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L271"
target="_blank" style="float:right; font-size:smaller">source</a>

### GhApi.delete_file

>      GhApi.delete_file (path, message, committer, author, sha=None,
>                         branch=None)

``` python
api.delete_file('foo', 'delete foo', committer=person, author=person)
assert 'foo' not in api.list_files()
```

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L279"
target="_blank" style="float:right; font-size:smaller">source</a>

### GhApi.update_contents

>      GhApi.update_contents (path, message, committer, author, content,
>                             sha=None, branch=None)

``` python
res = api.update_contents(
    path='README.md',
    message="Update README",
    committer=person, author=person,
    content=readme+"foobar"
)
res.content.size
```

    78

``` python
readme = api.get_content('README.md').decode()
assert 'foobar' in readme
api.update_contents('README.md', "Revert README", committer=person, author=person, content=readme[:-6]);
```

### GitHub Pages

------------------------------------------------------------------------

<a href="https://github.com/fastai/ghapi/blob/master/ghapi/core.py#L286"
target="_blank" style="float:right; font-size:smaller">source</a>

### GhApi.enable_pages

>      GhApi.enable_pages (branch=None, path='/')

*Enable or update pages for a repo to point to a `branch` and `path`.*

`branch` is set to the default branch if `None`. `path` must be `/docs`
or `/`.

``` python
res = api.enable_pages(branch='new-branch', path='/')

test_eq(res.source.branch, 'new-branch')
test_eq(res.source.path, '/')

api.repos.delete_pages_site()
api.delete_branch('new-branch')
```