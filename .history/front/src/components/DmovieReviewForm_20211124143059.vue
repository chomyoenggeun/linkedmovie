<template>
  <div>
    <h1>영화 리뷰 작성 폼</h1>
    <div>
      <v-autocomplete @click="getMovieData"
      filled
      rounded
      solo
      ></v-autocomplete>

    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>