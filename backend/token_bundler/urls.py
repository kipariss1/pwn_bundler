from django.urls import path
from token_bundler import views as views

urlpatterns = [
    path('wallets/', view=views.Wallets.as_view(), name='wallet'),
    path('wallet_detail/<pk>/', view=views.WalletDetail.as_view(), name='wallet-detail'),
    path('wallet_create/', views.WalletCreate.as_view(), name='wallet-create'),
    path('get_balance/<int:wid>/', views.get_wallet_ballance, name='get-wallet-balance'),
    path('get_erc20_assets/<int:wid>/', views.get_wallet_erc20_assets, name='erc20-assets'),
    path('get_nft_assets/<int:wid>/', views.get_wallet_nft_assets, name='nft-assets'),
    path('get_nft_col_assets/<int:wid>/', views.get_wallet_nft_collections_assets, name='nft-col-assets'),
]


