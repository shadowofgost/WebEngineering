<!--
 * @Author: Albert Wang
 * @LastEditors: Albert Wang
 * @Date: 2021-10-12 09:02:42
 * @LastEditTime: 2021-10-12 11:30:55
 * @Description:basic 
 * @FilePath: \\WebEngineering\\templates\\Vue\\src\\App.vue
 * @Copyright Notice:  2021 Albert Wang 王子睿.All Rights Reserved.
-->
<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "App"
};
</script>

<style>
#app {
  padding: 0;
  margin: 0;
  overflow: hidden;
}
</style>
