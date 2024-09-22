export interface WalletDetailsInterface {
    id: number,
    address: string,
    AssetsETH: number,
    AssetsERC20: WalletERC20Asset[],
    AssetsNFT: WalletNFTAsset[] 
}

export interface WalletERC20Asset {
    balance: string,
    decimals: number,
    logo: string,
    name: string,
    percentage_relative_to_total_supply: number,
    possible_spam: boolean,
    security_score: number,
    symbol: string,
    thumbnail: string,
    token_address: string,
    total_supply: string,
    total_supply_formatted: string,
    verified_contract: boolean, 
}

export interface WalletNFTAsset
{
    amount: string,
    token_id: string,
    token_address: string,
    contract_type: string,
    owner_of: string,
    last_metadata_sync: string,
    last_token_uri_sync: string,
    metadata: string | Object,
    block_number: string,
    block_number_minted: string,
    name: string,
    symbol: string,
    token_hash: string,
    token_uri: string,
    minter_address: string,
    rarity_rank: string,
    rarity_percentage: string,
    rarity_label: string,
    verified_collection: boolean,
    possible_spam: boolean,
    collection_logo: string,
    collection_banner_image: string,
    floor_price: string,
    floor_price_usd: string,
    floor_price_currency: string,
}