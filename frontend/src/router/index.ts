import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import WalletDetailsView from "@/views/WalletDetailsView.vue";
import AddWalletView from "@/views/AddWalletView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/wallet_details/:id",
      name: "wallet-details",
      component: WalletDetailsView,
      params: true,
    },
    {
      path: "/add_wallet",
      name: "add-wallet",
      component: AddWalletView,
    }
  ],
});

export default router;
