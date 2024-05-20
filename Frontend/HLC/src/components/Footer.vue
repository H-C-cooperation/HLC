<template>
  <!-- Footer -->
  <footer id="footer">
    <section>
      <div class="text-center text-md-start mt-5 bg-dark p-5">
        <div class="d-flex flex-row mb-3">
          <div md="3" lg="4" xl="3" class="mx-auto mb-4">
            <h6 class="text-uppercase fw-bold mb-4">HLC</h6>
            <p>맞춤형 영화를 제공하는 영화 추천 서비스입니다.</p>
          </div>
          <div md="2" lg="2" xl="2" class="mx-auto mb-4">
            <h6 class="text-uppercase fw-bold mb-4">SITE MAP</h6>
            <p>
              <RouterLink
                class="text-reset"
                :to="{ name: 'home' }"
              >Home</RouterLink>
            </p>
            <p>
              <RouterLink
                class="text-reset"
                :to="{ name: 'movie' }"
              >Movies</RouterLink>
            </p>
            <p>
              <RouterLink
                class="text-reset"
                :to="{ name: 'favorite' }"
              >Favorite</RouterLink>
            </p>
            <p>
              <RouterLink
                class="text-reset"
                :to="{ name: 'recommend' }"
              >Recommendations</RouterLink>
            </p>
          </div>
          <div md="3" lg="2" xl="2" class="mx-auto mb-4">
            <h6 class="text-uppercase fw-bold mb-4">Used Skills</h6>
            <p>Python</p>
            <p>Django</p>
            <p>HTML/CSS/JavaScript</p>
            <p>Vue</p>
          </div>

          <div md="4" lg="3" xl="3" class="mx-auto mb-md-0 mb-4">
            <h6 class="text-uppercase fw-bold mb-4">members</h6>
            <p>Choi Jiwon</p>
            <p>Hwnag Jun</p>
            <p>Lee Jian</p>
          </div>
        </div>
      </div>
    </section>
    <div class="text-center p-4" style="background-color: #1f1f1f">
      © 2022 Copyright:
      <a class="text-reset fw-bold">HLC</a>
    </div>
  </footer>
</template>

<script>
import { RouterLink } from 'vue-router';
export default {
  name: "FooterBar",
};
</script>

<style>
#footer {
  color: rgb(176, 174, 174);
}
</style>