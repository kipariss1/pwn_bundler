import { defineStore } from "pinia";
import _axios from "@/../axios";
import {
  WALLET_DETAILS_REQUEST,
  WALLET_DETAILS_SUCCESS,
  WALLET_DETAILS_FAIL,
} from "@/../constants/wallet_constants";
import type { WalletDetailsInterface } from "@/interfaces/wallet_details_interface"

export const useWalletDetailsStore = defineStore("wallet-details-store", {
  state: () => ({
    wallet_details: {} as WalletDetailsInterface,
    type: WALLET_DETAILS_REQUEST,
    error: "",
  }),
  getters: {
    // TODO: make all this getters, make interfaces for wallet details
    getWalletID: (state) => state.wallet_details.id,
    getWalletEthAssets: (state) => null,
    getWalletERC20Assets: (state) => null,
    getWalletNFTAssets: (state) => null,
    getWalletNFTCollectionsAssets: (state) => null,
  },
  actions: {
    async getWalletDetailsAction(id: number) {
      this.wallet_details = {} as WalletDetailsInterface;
      this.error = ""
      const promiseEth = _axios.get(`/api/wallet/get_balance/${id}/`);
      const promiseERC20 = _axios.get(`/api/wallet/get_erc20_assets/${id}/`);
      const promiseNFT = _axios.get(`/api/wallet/get_nft_assets/${id}/`);
      Promise.all(
        [promiseEth, promiseERC20, promiseNFT]
    ).then(
        (values) => {
            this.type = WALLET_DETAILS_SUCCESS
            console.log(values);
        }
    ).catch(error => {
        this.type = WALLET_DETAILS_FAIL
        this.error = String(error)
    })
    },
  },
});
