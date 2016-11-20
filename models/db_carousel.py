# -*- coding: utf-8 -*-

from os import path

db.define_table('carousel',
    Field('is_enabled', 'boolean', readable=True, writable=True, default=True, label=T('Is Enabled')),
#   Field('page', 'reference page', label=T('Page')),
    Field('name', 'string',length=256, notnull=True, label=T('Name')),
    Field('url', 'string', length=256,label=T('Url')),
    Field('image_file', 'upload', uploadfolder=path.join(
        request.folder,'static','images','carousel'
        ), autodelete=True, label=T('Image File')),
    Field('created_on','datetime',default=request.now,
            writable=False,readable=False, label=T('Created on')),
    format='%(name)s'
)
