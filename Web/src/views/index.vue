<template>
    <div class="body" style="min-length:400px;">
        <div class="center">
                <h2>考勤信息管理系统</h2>
                <h3>登录</h3>
            <!-- <loginSelect class="select"/> -->
            <loginMain/>
        </div>
    </div>
</template>
<script>
import loginSelect from './login/loginSelect'
import loginMain from './login/loginMain'

export default{
    deta(){
        return{
            p:0,
        }
    },
    components:{
        loginSelect,
        loginMain
    },
    mounted(){
        
        this.p=0.1
        setInterval(()=>{
            this.$nextTick(()=>{
                if(this.p<=1){
                    this.p=10*this.p
                }

        })},500)
    }
///assets/logo/
}
</script>
<style scoped>
.body{
  top:0;
  background-image: url('../assets/logo/bg.jpg'); 
  background-color: rgba(34, 180, 42, 0.788);
  background-size:cover;
  width: 100%;
  height: 100%;
  position:fixed;
  /* position:absolute; */
  background-repeat: no-repeat;
  margin: 0;
  padding: 0;
}
.center{
    -webkit-border-radius: 5px;
    border-radius: 5px;
    -moz-border-radius: 5px;
    background-clip: padding-box;
    margin: 180px auto;
    width: 350px;
    padding: 40px 40px 18px 40px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
}
.select{
    margin-bottom: 15px;
}
h2 {
      margin: -100px auto 40px auto;
      text-align: center;
      color: #bac0c5;
    }
h3{
      margin: 0px auto 40px auto;
      text-align: center;
      color: #505458;
    }
    .remember {
      margin: 0px 0px 35px 0px;
    }
</style>