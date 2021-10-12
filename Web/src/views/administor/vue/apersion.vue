<template>
   <div>
        <el-form :model="userform" :rules="rules" ref="userform"  auto-complete="on" label-position="left" >
       <ul>
           <li>
              <el-upload
              style="margin-left:270px;"
              action="http://localhost:9000/polls/Picture/"
              :auto-upload="true"
              :data="uploadData"
              :http-request="imageChange"
		          :beforeUpload="beforeAvatarUpload"
		          accept=".jpg"
              >
              <el-button type="primary" class="buttons2">上传图片</el-button>
              </el-upload>
                <el-dialog :visible.sync="dialogVisible">
                    <img width="100%" :src="dialogImageUrl" alt="">
                </el-dialog>
               <table >
                   <tr>
                        <td>id:</td>
                        <td><el-form-item prop="id" >
                            <el-input prefix-icon='iconfont icon-edit' v-model="userform.id" :disabled="true"    auto-complete="on"></el-input>
                        </el-form-item></td>
                    </tr>
                   <tr>
                        <td>卡号:</td>
                        <td><el-form-item prop="nocard" >
                            <el-input prefix-icon='iconfont icon-edit' v-model="userform.nocard" :disabled="true"    auto-complete="on"></el-input>
                        </el-form-item></td>
                   </tr>
                   <tr>
                        <td>身份id:</td>
                        <td><el-form-item prop="nouser" >
                            <el-input prefix-icon='iconfont icon-edit' v-model="userform.nouser" :disabled="true"    auto-complete="on"></el-input>
                        </el-form-item></td>
                   </tr>
                   <tr>
                        <td>姓名:</td>
                        <td><el-form-item prop="name" >
                            <el-input prefix-icon='iconfont icon-edit' v-model="userform.name" :disabled="true"    auto-complete="on"></el-input>
                        </el-form-item></td>
                   </tr>
                   <tr>
                        <td>部门:</td>
                        <td><el-form-item prop="deptid__name" >
                            <el-input prefix-icon='iconfont icon-edit' v-model="userform.deptid__name" :disabled="true"    auto-complete="on"></el-input>
                        </el-form-item></td>
                   </tr>
                   <tr>
                        <td>性别:</td>
                        <td><el-form-item prop="sex" >
                            <el-input prefix-icon='iconfont icon-edit' v-model="userform.sex" :disabled="true"    auto-complete="on"></el-input>
                        </el-form-item></td>
                   </tr>
                   <tr>
                        <td>权限:</td>
                        <td><el-form-item prop="attr" >
                            <el-input prefix-icon='iconfont icon-edit' v-model="userform.attr" :disabled="true"    auto-complete="on"></el-input>
                        </el-form-item></td>
                   </tr>
                   <tr>
                        <td>信息更新时间:</td>
                        <td><el-form-item prop="timeupdate" >
                            <el-input prefix-icon='iconfont icon-edit' v-model="userform.timeupdate" :disabled="true"    auto-complete="on"></el-input>
                        </el-form-item></td>
                   </tr>
                   <tr>
                        <td>管理员地点:</td>
                        <td><el-form-item prop="localid" >
                            <el-input prefix-icon='iconfont icon-edit' v-model="userform.localid" :disabled="true"    auto-complete="on"></el-input>
                        </el-form-item></td>
                   </tr>
                   <tr>
                        <td>timeupdate:</td>
                        <td><el-form-item prop="userex_related_to_user_information__timeupdate" >
                            <el-input prefix-icon='iconfont icon-edit' v-model="userform.userex_related_to_user_information__timeupdate" :disabled="true"    auto-complete="on"></el-input>
                        </el-form-item></td>
                   </tr>
                   <tr>
                        <td>管理员姓名:</td>
                        <td><el-form-item prop="userex_related_to_user_information__idmanager__name" >
                            <el-input prefix-icon='iconfont icon-edit' v-model="userform.userex_related_to_user_information__idmanager__name" :disabled="true"    auto-complete="on"></el-input>
                        </el-form-item></td>
                   </tr>
                   <tr>
                        <td>描述:</td>
                        <td><el-form-item prop="userex_related_to_user_information__rem" >
                            <el-input prefix-icon='iconfont icon-edit' v-model="userform.userex_related_to_user_information__rem" :disabled="true"    auto-complete="on"></el-input>
                        </el-form-item></td>
                   </tr>
                   <tr>
                        <td>密码：</td>
                        <td><el-form-item prop="psw" >
                            <el-input prefix-icon='iconfont icon-edit' v-model="userform.psw" show-password auto-complete="on"></el-input>
                        </el-form-item></td>
                   </tr>
               </table>

                <el-form-item>
                    <el-button :loading="loading" type="primary" style="margin-left:200px;" size="medium" @click ="idltpwd()">保 存</el-button>
                </el-form-item>
            </li>
       </ul>
         </el-form>
   </div>
</template>
<script>
//action="https://jsonplaceholder.typicode.com/posts/"
import axios from 'axios';
export default {
    data(){
        return{
        dialogImageUrl: '',
        dialogVisible: false,
        loading:false,
        baseURL:"http://localhost:9000/polls/",
        uploadData:{
          pic:{},
          user_id:'',
        },
        userform:{
            id:'',
            nocard:'',
            nouser:'',
            name:'',
            psw:'',
            deptid__name:'',
            sex:'',
            attr:'',
            timeupdate:'',
            localid:'',
            userex_related_to_user_information__timeupdate:'',
            userex_related_to_user_information__idmanager__name:'',
            userex_related_to_user_information__rem:'',
        },
        rules:{
            psw:[{ required: true, message: '密码不允许为空', trigger: 'blur' }]
        },
    }
    },
    mounted(){
        //自动加载数据
        this.getuser();
    },
    methods: {


        timeup(){
            this.userform.timeupdate = new Date().getTime() - new Date
            ('2000-1-1 00:00:00').getTime();
            this.userform.userex_related_to_user_information__timeupdate = new Date().getTime() - new Date
            ('2000-1-1 00:00:00').getTime();
        },
        handleRemove(file, fileList) {
            console.log(file, fileList);
        },
        handlePictureCardPreview(file) {
            this.dialogImageUrl = file.url;
            this.dialogVisible = true;
      },
        getuser(){
            let that = this;
            axios
            .get(that.baseURL + 'PersonInformation/')
            .then(function(res){
                //请求成功后执行的函数
                console.log(res);
                if(res.data.code == 0){
                    that.$router.push('/index');
                }else{
                if(true){ //res.data.code == 1
                //把数据给userform
                that.userform = res.data.data[0];
                if(that.userform.attr == 0){
                        that.userform.attr = '超级管理员';
                    }else if(that.userform.attr == 1){
                        that.userform.attr = '教务处管理员';
                    }else if(that.userform.attr == 2){
                        that.userform.attr = '辅导员';
                    }else if(that.userform.attr == 3){
                        that.userform.attr = '教师';
                    }else{
                        that.userform.attr = '学生';
                    }
                    if(that.userform.sex == 0){
                        that.userform.sex = '女性';
                    }else{
                        that.userform.sex = '男性';
                    }
                that.$message({
                    message:'数据加载成功！',
                    type:'success'
                });
                }else {
                    //数据加载失败提示
                    that.$message.error('获取数据出现异常');
                }
                }
            })
            .catch(function(err){
                //请求失败后执行的函数
                console.log(err);
                that.$message.error('获取数据出现异常');
            })
        },
        beforeAvatarUpload(file) {
	    //图片格式
		console.log(file.type)
		const isJPG = file.type === 'image/jpeg' || file.type === 'image/jpg' || file.type === 'image/png'|| file.type === 'image/PNG'|| file.type === 'image/JPG';

		if (!isJPG) {
			this.$message.error('上传图片只能为jpg或png格式');
		}
			return isJPG ;
		},
		 // 提交图片
    imageChange(param,type,file){
      let formData = new FormData()
      formData.append('pic', param.file);
      formData.append('user_id', this.userform.id);
      this.$http.post('http://localhost:9000/polls/Picture/', formData).then(res => {
		  this.$message.success('上传成功')
      }).catch(err=>{
        this.$message.error('上传失败')
      });
    },

        //修改密码
        idltpwd(){
            let that = this;
            this.timeup();
            axios
            .patch(that.baseURL + 'PersonInformation/',
                 {
                    "psw":that.userform.psw,
                    "sex":that.userform.sex,
                    "name":that.userform.name
                 }
                 )
            .then(res=>{
                //执行成功
                if(true){//res.data.code == 1
                    that.getuser();
                }else{
                    //数据加载失败提示
                    that.$message.error(res.data.msg);
                }
            })
            .catch(function(err){
                //请求失败后执行的函数
                console.log("保存失败！");
            })
        },
    }
}




</script>
<style scoped>
table{
    width:500px;
}
tr td{
    font-family: "微软雅黑";
}
tr td:nth-child(1){
    width:85px;
    padding: 10px 30px 10px 70px;
}
.el-form-item,.el-form-item .el-date-picker{
    width: 260px;
}
.el-form-item .el-button{
    width: 160px;
    padding: 10px ;
    margin-left: 70px;
    margin-top: 15px;
}
/* .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  } */
  /* .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  } */
</style>
