import { defineStore } from 'pinia'
import _axios from '../axios'
import { 
    WALLET_LIST_FAIL,
    WALLET_LIST_REQUEST,
    WALLET_LIST_SUCCESS, 
  } from '@/../constants/wallet_constants'
  

export const useWalletsStore = defineStore('wallets-store', {
    state: () => ({
        wallets: [],
        type: WALLET_LIST_REQUEST,
        error: null
    }),
    getters: {
        getWallets: (state) => state.wallets
    },
    actions: {
        async getWalletsAction() {
            this.type = WALLET_LIST_REQUEST
            try {
                this.wallets = await _axios.get("/api/wallet/wallets/")
                this.type = WALLET_LIST_SUCCESS
            } catch(error) {
                this.type = WALLET_LIST_FAIL
                this.error = String(error)
            }
        }
    }
})
