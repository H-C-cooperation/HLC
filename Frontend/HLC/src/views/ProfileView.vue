 <!-- 1. 인풋박스 누르면 글씨 없어지게
  2. 인풋박스 위아래 중간으로
  3. 배경색 덜적용됨  -->

  <template>
    <div class="container bg-black">
      <div class="outline">
        <header>
          <h1>프로필 수정</h1>
          <hr />
        </header>
        <nav>
          <div class="d-flex align-items-center">
            <img src="./assets/profile.png" alt="내프로필이미지" class="m-3" />
            <div class="inputbox">
              <div>
                <p><input type="text" placeholder="유저 이름" class="inputbox" /></p>
                <p><input type="text" placeholder="유저 이메일" class="inputbox" /></p>
              </div>
            </div>
          </div>
        </nav>
        <main class="d-flex">
          <article class="articlestyle">
            <h3>Your Followers</h3>
            <hr />
            <!-- follower 이미지 -->
            <img src="" alt="follower 이미지" />
  
            <!-- followings 이미지 -->
            <h3>Followings</h3>
            <hr />
            <img src="" alt="followings 이미지" />
  
            <h3>Your Favorite Genres</h3>
            <hr />
            <p>
              Genre1 ...
              <!-- 좋아하는 장르 다 적기 -->
            </p>
  
            <button>EDIT</button>
          </article>
        </main>
        <nav>
          <hr />
          <button>SAVE</button>
          <button class="cancelbtn">CANCEL</button>
        </nav>
      </div>
    </div>
  </template>
  
  <script setup></script>
  
  <style scoped>
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  
    color: white;
    height: 100vh;
  }
  
  .outline {
    width: 80%;
  }
  
  .articlestyle {
    margin-left: 120px;
    width: 100%;
  }
  
  .inputbox {
    width: 100%;
  }
  
  .cancelbtn {
    border: solid white 1px;
    color: white;
  }

  template {
    background-color: black;
    width: 100%;
  }
  
  img {
    width: 80px;
    height: 80px;
  }
  
  button {
    width: 100px;
  }
  </style>