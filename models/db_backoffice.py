# -*- coding: utf-8 -*-

# To understand this schema, please know that every table automatically has an
# autoincrement field called 'id' and when a table references another table, it does via
# this id field.

db.define_table('affiliate',
                Field('user_id', 'reference auth_user'),
                Field('referrer',  'reference auth_user')
                )

# An asset is something of value that one holds.
# Examples: bitcoin, burstcoin, etc.
db.define_table('asset',
                Field('name', unique=True, requires=IS_NOT_EMPTY()),
                Field('url'),
                Field('description', 'text'),
                format='%(name)s'
)

# A wallet is where an asset is held.
# E.g: BitTrex, mycelium wallet, Horizon Platform, Burst Platform.
db.define_table('wallet',
                Field('name', unique=True, requires=IS_NOT_EMPTY()),
                Field('url'),
                Field('description', type='text'),
                format='%(name)s'
)

# A wallet can hold many assets and an asset can be held in many wallets.
# E.g: ADSactly is an asset that can be held in a Horizon Wallet or a Burst Wallet and maybe one day a BitTrex wallet.
db.define_table('purchase',
                Field('user_id', 'reference auth_user'),
                Field('wallet_id', 'reference wallet'),
                Field('asset_id', 'reference asset'),
                Field('amount', type='double'),
                Field('purchase_price', type='double'),
                format=lambda r: '%f of %s is held in %s by %s %s' % (amount, r.asset_id.name, r.wallet_id.name, r.user_id.first_name, r.user_id.last_name)
)
