<template>
  <v-app>
    <v-app-bar app color="primary" dark class="my-auto">
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <span class="text-xl-h4 d-none d-sm-block"
        ><v-icon>mdi-head-check-outline</v-icon>信息爬虫 &nbsp; &nbsp;</span
      >
      <v-text-field
        label="標簽搜索"
        hide-details="auto"
        v-model="source"
      ></v-text-field>

      <v-btn icon @click="depl()"><v-icon>mdi-magnify</v-icon></v-btn>
      <v-spacer></v-spacer>
      <!--通知菜单-->
      <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn v-bind="attrs" v-on="on" icon @click="clearNotice()">
            <v-badge color="white" :value="noticeJudge" dot
              ><v-icon>mdi-bell-outline</v-icon></v-badge
            ></v-btn
          >
        </template>
        <v-card max-height="auto" max-width="auto">
          <v-list dense>
            <v-list-item
              v-for="(notice, noticeIndex) in chipData"
              :key="noticeIndex"
              color="primary"
              link
            >
              <v-list-item-action
                @click="chipClick(notice)"
                class="font-weight-light"
                >您订阅的"{{ notice }}"标签已更新!</v-list-item-action
              >
            </v-list-item>
          </v-list>
        </v-card>
      </v-menu>
      <!--设置菜单-->
      <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn v-bind="attrs" v-on="on" icon>
            <v-icon>mdi-cog</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item>
            <v-list-item-action-text>暗色模式</v-list-item-action-text>
            <v-list-item-action
              ><v-switch color="indigo" v-model="$vuetify.theme.dark"></v-switch
            ></v-list-item-action>
          </v-list-item>
          <v-list-item link @click="TomoriNao = !TomoriNao">
            <v-list-item-action-text class="font-weight-light"
              >关于</v-list-item-action-text
            >
          </v-list-item>
        </v-list>
      </v-menu>

      <v-btn
        icon
        class="d-none d-sm-block"
        @click="Jump('https://cutting-edge.site')"
        ><v-icon>mdi-compass</v-icon></v-btn
      >
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app temporary>
      <v-list>
        <v-list-item class="d-none d-sm-block">
          <v-list-item-content>
            <v-list-item-title class="text-h4"
              >你可以试试以下标签</v-list-item-title
            >
            <v-list-item-subtitle
              >如需更多标签可以联系管理员</v-list-item-subtitle
            ></v-list-item-content
          >
        </v-list-item>
        <v-list-item class="d-sm-none">
          <v-list-item-content>
            <v-list-item-title
              ><v-icon>mdi-head-check-outline</v-icon>信息爬蟲！Mobile!
            </v-list-item-title>
            <v-list-item-subtitle>你可以選擇下方的標簽</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-divider />
      <v-container>
        <v-chip-group column>
          <v-chip
            v-for="(tag, tagIndex) in chipData"
            :key="tagIndex"
            color="primary"
            @click="
              chipClick(tag);
              drawer = !drawer;
            "
          >
            {{ tag }}
          </v-chip>
        </v-chip-group>
      </v-container>
    </v-navigation-drawer>

    <v-main>
      <v-overlay :value="overlaySearch" />
      <v-overlay :value="TomoriNao">
        <v-card class="mx-auto" max-width="350">
          <v-img
            class="white--text align-end"
            height="200px"
            src="./assets/ContributeHead.png"
            gradient="to top right,  rgba(0,0,0,.7),rgba(255,255,255,.33)"
          >
            <v-card-title>Contributers</v-card-title>
          </v-img>

          <v-card-subtitle class="pb-0">
            这群人做出了这个信息爬虫。
          </v-card-subtitle>

          <v-list>
            <v-list-item
              two-line
              v-for="(man, manIndex) in ourData"
              :key="manIndex"
            >
              <v-list-item-avatar>
                <v-img :src="man.src" />
              </v-list-item-avatar>

              <v-list-item-content>
                <v-list-item-title>{{ man.name }}</v-list-item-title>
                <v-list-item-subtitle>{{ man.tag }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-list>

          <v-card-actions>
            <v-btn color="orange" text @click="TomoriNao = !TomoriNao">
              关闭
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-overlay>

      <div>
        <!--状态栏-->
        <v-snackbar v-model="tips" top timeout="-1"
          >請等待......<v-progress-circular indeterminate size="20">
          </v-progress-circular
        ></v-snackbar>
        <v-snackbar v-model="netWorkError" top color="red"
          >服务器挂掉了......</v-snackbar
        >
        <v-snackbar v-model="netWorkSuccess" top color="primary"
          >查询成功！</v-snackbar
        >

        <!--主体部分-->
        <v-container>
          <!--欢迎卡片-->
          <v-card height="auto" id="welcome">
            <v-card-title>歡迎使用信息爬蟲！</v-card-title>
            <v-card-subtitle
              >搜索你想要的標簽或點擊菜單圖標看看大家都在搜什麽</v-card-subtitle
            >
            <v-divider />
            <v-card-text>
              <p>無論是考研，復試，一切你想知道的升學機會都在這裏！</p>
              <p>本站基於爬蟲技術，替你收集各個高校的升學信息！</p>
              <p>再也不因爲信息差而煩惱！</p>
            </v-card-text>
          </v-card>
          <!--失败卡片-->
          <v-card class="d-none" id="emptyResult">
            <v-card-title>好像什么...也没有？</v-card-title>
            <v-card-text
              >要不要试着搜点别的？没能得到你想要的真的是很抱歉.....</v-card-text
            >
          </v-card>
          <!--结果卡片组-->
          <v-row v-for="(cardData, cardIndex) in jsonData" :key="cardIndex">
            <v-col cols="12">
              <v-card max-height="500" elevation="3">
                <v-card-title class="text-xl-h4 text-truncate">
                  {{ cardData.TITLE }}
                </v-card-title>
                <v-divider />
                <v-card-text class="d-inline-block text-truncate">
                  {{ cardData.CONTEXT }}
                </v-card-text>
                <v-card-actions>
                  <v-btn
                    text
                    color="teal accent-4"
                    @click="
                      overlay = !overlay;
                      DataPresent = cardData.CONTEXT;
                    "
                  >
                    详情
                  </v-btn>
                  <v-btn text color="teal accent-4" :href="cardData.HREF">
                    原链接
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-col>
          </v-row>
        </v-container>

        <!--详情overlay遮罩-->
        <v-overlay :value="overlay" z-index="999">
          <v-card max-width="300" max-height="600" class="">
            <v-card-text class="text-truncate text-np-wrap" max-height="auto">{{
              DataPresent
            }}</v-card-text>
            <v-card-actions>
              <v-btn text @click="overlay = !overlay"> 关闭 </v-btn>
            </v-card-actions>
          </v-card>
        </v-overlay>
      </div>
    </v-main>
  </v-app>
</template>

<script src="https://cdn.staticfile.org/jquery/1.10.2/jquery.min.js"></script>
<script>
</script>


<script>
import $ from "jquery";
export default {
  name: "App",

  data: () => ({
    noticeJudge: true,
    TomoriNao: false,
    jsonData: null,
    source: "",
    overlay: false,
    DataPresent: "",
    drawer: false,
    chipData: [
      "复试",
      "硕士",
      "初试",
      "培养方案",
      "成绩",
      "夏令营",
      "博士",
      "奖学金",
      "招生",
      "调剂",
    ],
    ourData: [
      {
        name: "Moyi@友利奈绪天下第一",
        tag: "后端工程师",
        src: require("./assets/Nao.jpg"),
      },
      {
        name: "Symbolic@少女前线天下第一",
        tag: "前端工程师",
        src: require("./assets/wo.jpg"),
      },
      {
        name: "樱树下星光点点",
        tag: "产品经理",
        src: require("./assets/XU.png"),
      },
      { name: "Harysi", tag: "产品经理", src: require("./assets/zhu.jpg") },
    ],
    tips: false,
    overlaySearch: false,
    netWorkError: false,
    netWorkSuccess: false,
    expandSettings: false,

    //
  }),
  methods: {
    //var arr = [];
    depl() {
      this.get_data();
    },
    chipClick(name) {
      this.source = name;
      this.get_data();
    },

    get_data() {
      this.tips = true;
      this.overlaySearch = true;
      var self = this;
      var postArr = [];
      var postData = { tar: "" };

      postData.tar = self.source;
      postArr.push(postData);
      postArr = JSON.stringify(postArr);
      /* $.post(
        "http://127.0.0.1:5000/test",
        postArr,
        function (data, status) {
          console.log(data);
          self.tips = false;
          self.overlaySearch = false;
          $("#welcome").remove();
          self.jsonData = data;
          console.log(self.jsonData);
          if (data.length == 0) {
            $("#emptyResult").removeClass("d-none");
          } else {
            $("#emptyResult").addClass("d-none");
          }
        },
        "json"
      ); */
      $.ajax({
        url: "https://cutting-edge.site/SSearcher/upload",
        data: postArr,
        type: "POST",
        success: function (data, status) {
          console.log(data);
          self.tips = false;
          self.netWorkSuccess = true;
          self.overlaySearch = false;
          $("#welcome").remove();
          self.jsonData = data;
          console.log(self.jsonData);
          if (data.length == 0) {
            $("#emptyResult").removeClass("d-none");
          } else {
            $("#emptyResult").addClass("d-none");
          }
        },
        error: function () {
          self.overlaySearch = false;
          self.tips = false;
          self.netWorkError = true;
        },
      });
    },
    jump(link) {
      window.location.href = link;
    },
    clearNotice() {
      this.noticeJudge = false;
    },
  },
  watch: {
    netWorkError(val) {
      val &&
        setTimeout(() => {
          this.netWorkError = false;
        }, 2000);
    },
    netWorkSuccess(val) {
      val &&
        setTimeout(() => {
          this.netWorkSuccess = false;
        }, 2000);
    },
  },
};
</script>
