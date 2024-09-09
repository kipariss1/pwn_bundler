export interface WalletDetailsInterface {
    id: number,
    address: string,
    AssetsETH: number,
    AssetsERC20: WalletERC20Assets
    AssetsNFT: WalletNFTAssets 
}

export interface WalletERC20Assets {

}

export interface WalletNFTAssets {

}