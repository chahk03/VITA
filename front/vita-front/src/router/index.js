import Vue from 'vue'
import VueRouter from 'vue-router'
import WearableView from '../views/WearableView.vue'
import MypageView from '../views/MypageView.vue'
import MainView from '../views/MainView.vue'
import FriendView from '../views/friend/FriendView.vue'
import SymptomView from '../views/SymptomView.vue'
import DiseaseView from '../views/DiseaseView.vue'
import FriendListView from '../views/friend/FriendListView.vue'
import FileUploadView from '../views/mypage/FileUploadView.vue'
import WearableFriendView from '../views/wearable/WearableFriendView.vue'
import IndexPage from '@/components/common/Index'
import OauthRedirect from '@/components/user/oauth/Redirect'
import ExtraInfoFormView from '../views/ExtraInfoFormView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: IndexPage,
    children: [
      {
        path: '/',
        name: 'main',
        component: MainView
      },
      {
        path: '/mypage',
        name: 'mypage',
        component: MypageView
      },
      {
        path: '/fileupload',
        name: 'fileupload',
        component: FileUploadView
      },
      {
        path: "/wearable",
        name: "wearable",
        component: WearableView,
      },
      {
      path: '/wearablefriend',
      name: 'wearablefriend',
      component: WearableFriendView
      },
      {
        path: "/friend",
        name: "friend",
        component: FriendView,
      },
      {
        path: "/friendlist",
        name: "friendlist",
        component: FriendListView,
        },
      {
        path: "/symptom",
        name: "symptom",
        component: SymptomView,
      },
      {
        path: "/disease",
        name: "disease",
        component: DiseaseView,
      },
      {
        path: '/oauth/redirect',
        name: 'OauthRedrect',
        component: OauthRedirect
      },
      {
        path: '/extraInfoForm',
        name: 'ExtraInfoForm',
        component: ExtraInfoFormView
      }
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
