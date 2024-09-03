from django.urls import path
from token_bundler.views import wallet_views as wallet_views

urlpatterns = [
    path('wallets/', view=wallet_views.Wallets.as_view(), name='wallet'),
    path('wallet_detail/<pk>/', view=wallet_views.WalletDetail.as_view(), name='wallet-detail'),
    path('wallet_create/', wallet_views.WalletCreate.as_view(), name='wallet-create'),
    path('get_balance/<int:wid>/', wallet_views.get_wallet_ballance, name='get-wallet-balance'),
    path('get_erc20_assets/<int:wid>/', wallet_views.get_wallet_erc20_assets, name='erc20-assets'),
    path('get_nft_assets/<int:wid>/', wallet_views.get_wallet_nft_assets, name='nft-assets'),
    path('get_nft_col_assets/<int:wid>/', wallet_views.get_wallet_nft_collections_assets, name='nft-col-assets'),
]


