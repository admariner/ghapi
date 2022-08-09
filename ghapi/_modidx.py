# Autogenerated by nbdev

d = { 'settings': { 'allowed_cell_metadata_keys': '',
                'allowed_metadata_keys': '',
                'audience': 'Developers',
                'author': 'Jeremy Howard',
                'author_email': 'info@fast.ai',
                'black_formatting': 'False',
                'branch': 'master',
                'clean_ids': 'True',
                'console_scripts': 'ghapi=ghapi.cli:ghapi\n'
                                   'ghpath=ghapi.cli:ghpath\n'
                                   'ghraw=ghapi.cli:ghraw\n'
                                   'completion-ghapi=ghapi.cli:completion_ghapi\n'
                                   'gh-create-workflow=ghapi.actions:gh_create_workflow',
                'copyright': 'fastai',
                'custom_sidebar': 'False',
                'description': 'A python client for the GitHub API',
                'dev_requirements': 'jsonref matplotlib',
                'doc_baseurl': '/',
                'doc_host': 'https://ghapi.fast.ai',
                'doc_path': '_docs',
                'git_url': 'https://github.com/fastai/ghapi/tree/master/',
                'host': 'github',
                'jupyter_hooks': 'True',
                'keywords': 'github api',
                'language': 'English',
                'lib_name': 'ghapi',
                'lib_path': 'ghapi',
                'license': 'apache2',
                'min_python': '3.7',
                'nbs_path': '.',
                'readme_nb': 'index.ipynb',
                'recursive': 'False',
                'requirements': 'fastcore>=1.5.4',
                'status': '5',
                'title': 'ghapi',
                'tst_flags': '',
                'user': 'fastai',
                'version': '1.0.0'},
  'syms': { 'ghapi.actions': { 'ghapi.actions.Event': 'https://ghapi.fast.ai/actions.html#event',
                               'ghapi.actions.actions_debug': 'https://ghapi.fast.ai/actions.html#actions_debug',
                               'ghapi.actions.actions_error': 'https://ghapi.fast.ai/actions.html#actions_error',
                               'ghapi.actions.actions_group': 'https://ghapi.fast.ai/actions.html#actions_group',
                               'ghapi.actions.actions_mask': 'https://ghapi.fast.ai/actions.html#actions_mask',
                               'ghapi.actions.actions_output': 'https://ghapi.fast.ai/actions.html#actions_output',
                               'ghapi.actions.actions_warn': 'https://ghapi.fast.ai/actions.html#actions_warn',
                               'ghapi.actions.context_env': 'https://ghapi.fast.ai/actions.html#context_env',
                               'ghapi.actions.context_github': 'https://ghapi.fast.ai/actions.html#context_github',
                               'ghapi.actions.context_job': 'https://ghapi.fast.ai/actions.html#context_job',
                               'ghapi.actions.context_matrix': 'https://ghapi.fast.ai/actions.html#context_matrix',
                               'ghapi.actions.context_needs': 'https://ghapi.fast.ai/actions.html#context_needs',
                               'ghapi.actions.context_runner': 'https://ghapi.fast.ai/actions.html#context_runner',
                               'ghapi.actions.context_secrets': 'https://ghapi.fast.ai/actions.html#context_secrets',
                               'ghapi.actions.context_steps': 'https://ghapi.fast.ai/actions.html#context_steps',
                               'ghapi.actions.context_strategy': 'https://ghapi.fast.ai/actions.html#context_strategy',
                               'ghapi.actions.contexts': 'https://ghapi.fast.ai/actions.html#contexts',
                               'ghapi.actions.create_workflow': 'https://ghapi.fast.ai/actions.html#create_workflow',
                               'ghapi.actions.create_workflow_files': 'https://ghapi.fast.ai/actions.html#create_workflow_files',
                               'ghapi.actions.def_pipinst': 'https://ghapi.fast.ai/actions.html#def_pipinst',
                               'ghapi.actions.env_contexts': 'https://ghapi.fast.ai/actions.html#env_contexts',
                               'ghapi.actions.env_github': 'https://ghapi.fast.ai/actions.html#env_github',
                               'ghapi.actions.example_payload': 'https://ghapi.fast.ai/actions.html#example_payload',
                               'ghapi.actions.fill_workflow_templates': 'https://ghapi.fast.ai/actions.html#fill_workflow_templates',
                               'ghapi.actions.gh_create_workflow': 'https://ghapi.fast.ai/actions.html#gh_create_workflow',
                               'ghapi.actions.github_token': 'https://ghapi.fast.ai/actions.html#github_token',
                               'ghapi.actions.set_git_user': 'https://ghapi.fast.ai/actions.html#set_git_user',
                               'ghapi.actions.user_repo': 'https://ghapi.fast.ai/actions.html#user_repo'},
            'ghapi.all': {},
            'ghapi.auth': { 'ghapi.auth.GhDeviceAuth': 'https://ghapi.fast.ai/auth.html#ghdeviceauth',
                            'ghapi.auth.GhDeviceAuth.auth': 'https://ghapi.fast.ai/auth.html#ghdeviceauth.auth',
                            'ghapi.auth.GhDeviceAuth.open_browser': 'https://ghapi.fast.ai/auth.html#ghdeviceauth.open_browser',
                            'ghapi.auth.GhDeviceAuth.url_docs': 'https://ghapi.fast.ai/auth.html#ghdeviceauth.url_docs',
                            'ghapi.auth.GhDeviceAuth.wait': 'https://ghapi.fast.ai/auth.html#ghdeviceauth.wait',
                            'ghapi.auth.Scope': 'https://ghapi.fast.ai/auth.html#scope',
                            'ghapi.auth.github_auth_device': 'https://ghapi.fast.ai/auth.html#github_auth_device',
                            'ghapi.auth.scope_str': 'https://ghapi.fast.ai/auth.html#scope_str'},
            'ghapi.build_lib': { 'ghapi.build_lib.GH_OPENAPI_URL': 'https://ghapi.fast.ai/build_lib.html#gh_openapi_url',
                                 'ghapi.build_lib.GhMeta': 'https://ghapi.fast.ai/build_lib.html#ghmeta',
                                 'ghapi.build_lib.build_funcs': 'https://ghapi.fast.ai/build_lib.html#build_funcs'},
            'ghapi.cli': { 'ghapi.cli.completion_ghapi': 'https://ghapi.fast.ai/cli.html#completion_ghapi',
                           'ghapi.cli.ghapi': 'https://ghapi.fast.ai/cli.html#ghapi',
                           'ghapi.cli.ghpath': 'https://ghapi.fast.ai/cli.html#ghpath',
                           'ghapi.cli.ghraw': 'https://ghapi.fast.ai/cli.html#ghraw'},
            'ghapi.core': { 'ghapi.core.EMPTY_TREE_SHA': 'https://ghapi.fast.ai/core.html#empty_tree_sha',
                            'ghapi.core.GH_HOST': 'https://ghapi.fast.ai/core.html#gh_host',
                            'ghapi.core.GhApi': 'https://ghapi.fast.ai/core.html#ghapi',
                            'ghapi.core.GhApi.create_branch_empty': 'https://ghapi.fast.ai/core.html#ghapi.create_branch_empty',
                            'ghapi.core.GhApi.create_file': 'https://ghapi.fast.ai/core.html#ghapi.create_file',
                            'ghapi.core.GhApi.create_gist': 'https://ghapi.fast.ai/core.html#ghapi.create_gist',
                            'ghapi.core.GhApi.create_or_update_file': 'https://ghapi.fast.ai/core.html#ghapi.create_or_update_file',
                            'ghapi.core.GhApi.create_release': 'https://ghapi.fast.ai/core.html#ghapi.create_release',
                            'ghapi.core.GhApi.delete_branch': 'https://ghapi.fast.ai/core.html#ghapi.delete_branch',
                            'ghapi.core.GhApi.delete_file': 'https://ghapi.fast.ai/core.html#ghapi.delete_file',
                            'ghapi.core.GhApi.delete_release': 'https://ghapi.fast.ai/core.html#ghapi.delete_release',
                            'ghapi.core.GhApi.delete_tag': 'https://ghapi.fast.ai/core.html#ghapi.delete_tag',
                            'ghapi.core.GhApi.enable_pages': 'https://ghapi.fast.ai/core.html#ghapi.enable_pages',
                            'ghapi.core.GhApi.full_docs': 'https://ghapi.fast.ai/core.html#ghapi.full_docs',
                            'ghapi.core.GhApi.get_branch': 'https://ghapi.fast.ai/core.html#ghapi.get_branch',
                            'ghapi.core.GhApi.get_content': 'https://ghapi.fast.ai/core.html#ghapi.get_content',
                            'ghapi.core.GhApi.list_branches': 'https://ghapi.fast.ai/core.html#ghapi.list_branches',
                            'ghapi.core.GhApi.list_files': 'https://ghapi.fast.ai/core.html#ghapi.list_files',
                            'ghapi.core.GhApi.list_tags': 'https://ghapi.fast.ai/core.html#ghapi.list_tags',
                            'ghapi.core.GhApi.update_contents': 'https://ghapi.fast.ai/core.html#ghapi.update_contents',
                            'ghapi.core.GhApi.upload_file': 'https://ghapi.fast.ai/core.html#ghapi.upload_file',
                            'ghapi.core.date2gh': 'https://ghapi.fast.ai/core.html#date2gh',
                            'ghapi.core.gh2date': 'https://ghapi.fast.ai/core.html#gh2date',
                            'ghapi.core.print_summary': 'https://ghapi.fast.ai/core.html#print_summary'},
            'ghapi.event': { 'ghapi.event.CheckRunEvent': 'https://ghapi.fast.ai/event.html#checkrunevent',
                             'ghapi.event.CheckSuiteEvent': 'https://ghapi.fast.ai/event.html#checksuiteevent',
                             'ghapi.event.CodeScanningAlertEvent': 'https://ghapi.fast.ai/event.html#codescanningalertevent',
                             'ghapi.event.CommitCommentEvent': 'https://ghapi.fast.ai/event.html#commitcommentevent',
                             'ghapi.event.ContentReferenceEvent': 'https://ghapi.fast.ai/event.html#contentreferenceevent',
                             'ghapi.event.ContextEvent': 'https://ghapi.fast.ai/event.html#contextevent',
                             'ghapi.event.CreateEvent': 'https://ghapi.fast.ai/event.html#createevent',
                             'ghapi.event.DeleteEvent': 'https://ghapi.fast.ai/event.html#deleteevent',
                             'ghapi.event.DeployKeyEvent': 'https://ghapi.fast.ai/event.html#deploykeyevent',
                             'ghapi.event.DeploymentEvent': 'https://ghapi.fast.ai/event.html#deploymentevent',
                             'ghapi.event.DeploymentStatusEvent': 'https://ghapi.fast.ai/event.html#deploymentstatusevent',
                             'ghapi.event.ForkEvent': 'https://ghapi.fast.ai/event.html#forkevent',
                             'ghapi.event.GhApi.fetch_events': 'https://ghapi.fast.ai/event.html#ghapi.fetch_events',
                             'ghapi.event.GhApi.list_events': 'https://ghapi.fast.ai/event.html#ghapi.list_events',
                             'ghapi.event.GhApi.list_events_parallel': 'https://ghapi.fast.ai/event.html#ghapi.list_events_parallel',
                             'ghapi.event.GhEvent': 'https://ghapi.fast.ai/event.html#ghevent',
                             'ghapi.event.GhEvent.description': 'https://ghapi.fast.ai/event.html#ghevent.description',
                             'ghapi.event.GhEvent.emoji': 'https://ghapi.fast.ai/event.html#ghevent.emoji',
                             'ghapi.event.GhEvent.full_type': 'https://ghapi.fast.ai/event.html#ghevent.full_type',
                             'ghapi.event.GhEvent.text': 'https://ghapi.fast.ai/event.html#ghevent.text',
                             'ghapi.event.GithubAppAuthorizationEvent': 'https://ghapi.fast.ai/event.html#githubappauthorizationevent',
                             'ghapi.event.GollumEvent': 'https://ghapi.fast.ai/event.html#gollumevent',
                             'ghapi.event.InstallationEvent': 'https://ghapi.fast.ai/event.html#installationevent',
                             'ghapi.event.InstallationRepositoriesEvent': 'https://ghapi.fast.ai/event.html#installationrepositoriesevent',
                             'ghapi.event.IssueCommentEvent': 'https://ghapi.fast.ai/event.html#issuecommentevent',
                             'ghapi.event.IssuesEvent': 'https://ghapi.fast.ai/event.html#issuesevent',
                             'ghapi.event.LabelEvent': 'https://ghapi.fast.ai/event.html#labelevent',
                             'ghapi.event.MarketplacePurchaseEvent': 'https://ghapi.fast.ai/event.html#marketplacepurchaseevent',
                             'ghapi.event.MemberEvent': 'https://ghapi.fast.ai/event.html#memberevent',
                             'ghapi.event.MembershipEvent': 'https://ghapi.fast.ai/event.html#membershipevent',
                             'ghapi.event.MetaEvent': 'https://ghapi.fast.ai/event.html#metaevent',
                             'ghapi.event.MilestoneEvent': 'https://ghapi.fast.ai/event.html#milestoneevent',
                             'ghapi.event.NeedsEvent': 'https://ghapi.fast.ai/event.html#needsevent',
                             'ghapi.event.OrgBlockEvent': 'https://ghapi.fast.ai/event.html#orgblockevent',
                             'ghapi.event.OrganizationEvent': 'https://ghapi.fast.ai/event.html#organizationevent',
                             'ghapi.event.PackageEvent': 'https://ghapi.fast.ai/event.html#packageevent',
                             'ghapi.event.PageBuildEvent': 'https://ghapi.fast.ai/event.html#pagebuildevent',
                             'ghapi.event.PingEvent': 'https://ghapi.fast.ai/event.html#pingevent',
                             'ghapi.event.ProjectCardEvent': 'https://ghapi.fast.ai/event.html#projectcardevent',
                             'ghapi.event.ProjectColumnEvent': 'https://ghapi.fast.ai/event.html#projectcolumnevent',
                             'ghapi.event.ProjectEvent': 'https://ghapi.fast.ai/event.html#projectevent',
                             'ghapi.event.PublicEvent': 'https://ghapi.fast.ai/event.html#publicevent',
                             'ghapi.event.PullRequestEvent': 'https://ghapi.fast.ai/event.html#pullrequestevent',
                             'ghapi.event.PullRequestReviewCommentEvent': 'https://ghapi.fast.ai/event.html#pullrequestreviewcommentevent',
                             'ghapi.event.PullRequestReviewEvent': 'https://ghapi.fast.ai/event.html#pullrequestreviewevent',
                             'ghapi.event.PushEvent': 'https://ghapi.fast.ai/event.html#pushevent',
                             'ghapi.event.ReleaseEvent': 'https://ghapi.fast.ai/event.html#releaseevent',
                             'ghapi.event.RepositoryDispatchEvent': 'https://ghapi.fast.ai/event.html#repositorydispatchevent',
                             'ghapi.event.RepositoryEvent': 'https://ghapi.fast.ai/event.html#repositoryevent',
                             'ghapi.event.RepositoryImportEvent': 'https://ghapi.fast.ai/event.html#repositoryimportevent',
                             'ghapi.event.RepositoryVulnerabilityAlertEvent': 'https://ghapi.fast.ai/event.html#repositoryvulnerabilityalertevent',
                             'ghapi.event.ScheduleEvent': 'https://ghapi.fast.ai/event.html#scheduleevent',
                             'ghapi.event.SecurityAdvisoryEvent': 'https://ghapi.fast.ai/event.html#securityadvisoryevent',
                             'ghapi.event.SponsorshipEvent': 'https://ghapi.fast.ai/event.html#sponsorshipevent',
                             'ghapi.event.StarEvent': 'https://ghapi.fast.ai/event.html#starevent',
                             'ghapi.event.StatusEvent': 'https://ghapi.fast.ai/event.html#statusevent',
                             'ghapi.event.TeamAddEvent': 'https://ghapi.fast.ai/event.html#teamaddevent',
                             'ghapi.event.TeamEvent': 'https://ghapi.fast.ai/event.html#teamevent',
                             'ghapi.event.WatchEvent': 'https://ghapi.fast.ai/event.html#watchevent',
                             'ghapi.event.WorkflowDispatchEvent': 'https://ghapi.fast.ai/event.html#workflowdispatchevent',
                             'ghapi.event.WorkflowRunEvent': 'https://ghapi.fast.ai/event.html#workflowrunevent',
                             'ghapi.event.described_evts': 'https://ghapi.fast.ai/event.html#described_evts',
                             'ghapi.event.evt_emojis': 'https://ghapi.fast.ai/event.html#evt_emojis',
                             'ghapi.event.load_sample_events': 'https://ghapi.fast.ai/event.html#load_sample_events',
                             'ghapi.event.save_sample_events': 'https://ghapi.fast.ai/event.html#save_sample_events'},
            'ghapi.metadata': {'ghapi.metadata.funcs': 'https://ghapi.fast.ai/metadata.html#funcs'},
            'ghapi.page': { 'ghapi.page.GhApi.last_page': 'https://ghapi.fast.ai/page.html#ghapi.last_page',
                            'ghapi.page.paged': 'https://ghapi.fast.ai/page.html#paged',
                            'ghapi.page.pages': 'https://ghapi.fast.ai/page.html#pages',
                            'ghapi.page.parse_link_hdr': 'https://ghapi.fast.ai/page.html#parse_link_hdr'},
            'ghapi.templates': { 'ghapi.templates.context_example': 'https://ghapi.fast.ai/templates.html#context_example',
                                 'ghapi.templates.needs_example': 'https://ghapi.fast.ai/templates.html#needs_example',
                                 'ghapi.templates.pre_tmpl': 'https://ghapi.fast.ai/templates.html#pre_tmpl',
                                 'ghapi.templates.wf_tmpl': 'https://ghapi.fast.ai/templates.html#wf_tmpl'}}}