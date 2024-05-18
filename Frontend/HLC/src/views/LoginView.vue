<template>
  <div class="d-flex justify-content-center align-items-center back">
    <div class="bg-body-secondary bg-opacity-75 text-white p-5 text-center border border-dark border-2">
      <h1>HLC</h1>
      <br>
      <form action="#">
        <p>아이디가 있으신가요?</p>
        <div class="m-3">
          <p>
            <input class="mx-2" id="ID" type="text" placeholder="ID">
          </p>
          <p>
            <input class="mx-2" id="PW" type="text" placeholder="PW">
          </p>
        </div>
        <div class="text-center">
          <input class="me-5 btn btn-dark" type="submit" value="로그인">
          <a href="#">가입하기</a>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
.back {
  background-image: url('../assets/background.png');
  background-size: cover;
  height: 100vh;
}

h1{
  text-transform:uppercase;
  font-size:60px;
  font-family:'Verdana';
  padding:10px;
  text-decoration: overline underline dashed;
  color: rgb(223, 41, 41);
  text-underline-offset: 15px;
}
</style>