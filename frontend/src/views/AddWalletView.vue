<template>
    <div class="row py-3 justify-content-center">
        <div class="col-4">
            <form>
                <div class="form-group">
                    <label for="formGroupExampleInput">Name</label>
                    <input type="text" class="form-control" id="formGroupExampleInput" placeholder="New wallet's name">
                </div>
                <div class="form-group">
                    <label for="formGroupExampleInput2">Address</label>
                    <input type="text" class="form-control" id="formGroupExampleInput2" placeholder="New wallet's address">
                </div>
                <button type="submit" class="btn btn-primary" @click="submitNewWallet">Add</button>
            </form>
        </div>
    </div>
</template>

<script setup lang="ts">

    async function submitNewWallet(event: Event) {
        event.preventDefault();
        console.log("Sending new wallet to backend ....");
    }

</script>

<style scoped>

</style>