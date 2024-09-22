import { defineStore } from "pinia";
import _axios from "@/../axios";
import {
    WALLET_ADD_FAIL,
    WALLET_ADD_REQUEST,
    WALLET_ADD_SUCCESS,
    WALLET_ADD_IDLE
} from "@/../constants/wallet_constants";

export const useAddWalletStore = defineStore('add-wallet-store', {
    state: () => ({
        type: WALLET_ADD_IDLE,
        error: "",
    }),
    actions: {
        async postNewWalletDetailsAction(name: string, address: string) {
            this.type = WALLET_ADD_REQUEST
            _axios.post(
                '/api/wallet/wallet_create/',
                {
                    name: name,
                    address: address
                },
                {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                }
            ).then(() => {
                this.type = WALLET_ADD_SUCCESS;
            }).catch((error) => {
                this.type = WALLET_ADD_FAIL;
                this.error = String(error.message);
            })
        }
    }
})