import { defineStore } from "pinia";
import _axios from "@/../axios";
import {
  WALLET_DETAILS_REQUEST,
  WALLET_DETAILS_SUCCESS,
  WALLET_DETAILS_FAIL,
} from "@/../constants/wallet_constants";
import type { WalletDetailsInterface } from "@/interfaces/wallet_details_interface";

export const useWalletDetailsStore = defineStore("wallet-details-store", {
  state: () => ({
    wallet_details: {} as WalletDetailsInterface,
    type: WALLET_DETAILS_REQUEST,
    error: "",
  }),
  getters: {
    // TODO: make all this getters, make interfaces for wallet details
    getWalletID: (state) => state.wallet_details.id,
    getWalletEthAssets: (state) => state.wallet_details.AssetsETH,
    getWalletERC20Assets: (state) => state.wallet_details.AssetsERC20,
    getWalletNFTAssets: (state) => state.wallet_details.AssetsNFT,
  },
  actions: {
    async getWalletDetailsAction(id: number) {
      this.wallet_details = {} as WalletDetailsInterface;
      this.error = "";
      const promiseEth = _axios.get(`/api/wallet/get_balance/${id}/`);
      const promiseERC20 = _axios.get(`/api/wallet/get_erc20_assets/${id}/`);
      const promiseNFT = _axios.get(`/api/wallet/get_nft_assets/${id}/`);
      Promise.all([promiseEth, promiseERC20, promiseNFT])
        .then((values) => {
          this.type = WALLET_DETAILS_SUCCESS;
          this.wallet_details.AssetsETH = values[0].data;
          this.wallet_details.AssetsERC20 = values[1].data;
          this.wallet_details.AssetsNFT = values[2].data.result;
          console.log(values);
        })
        .catch((error) => {
          this.type = WALLET_DETAILS_FAIL;
          this.error = String(error);
        });
    },
  },
});
