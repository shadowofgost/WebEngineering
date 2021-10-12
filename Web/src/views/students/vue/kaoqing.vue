<template>
<el-table :data="tableData"  style="width: 90%;margin-left:20px" size="mini">
        <el-table-column prop="param2__id_curricula__name" label="签到课程名称" width="180" >
        </el-table-column>
        <el-table-column prop="param2__timebegin" label="开始时间" width="180" >
        </el-table-column>
        <el-table-column prop="param2__timeend" label="结束时间" width="180">
        </el-table-column>
        <el-table-column prop="attendrates" label="签到" width="180">
        </el-table-column>
</el-table>
</template>

<style>
  .el-table .warning-row {
    background: rgb(212, 58, 31);
  }

  .el-table .success-row {
    background: #5aee0b;
  }
</style>

<script>
import axios from 'axios';
  export default {
    data() {
      return {
      baseURL:"http://localhost:9000/polls/",
      id:'',
      tableData:[],
      }
    },
    mounted(){
    //自动加载数据
    this.gets();
    },
    methods:{
      gets(){
        this.id = this.$route.query.index;
         if(!this.$route.query.index){
           this.$router.push({path:'kechengs/'})
         }
        console.log(this.id);
        let that = this;
        axios
        .get(
          that.baseURL + 'StudentAttendance/',{params:{user_id:80893,course_plan_id:this.id,page:10,limits:10}})
        .then(function(res){
          if(res.data.code == 0){
              that.$router.push('/index');
          }else{
              if(res.data.error_code == 0){
                    that.tableData = res.data.data;
                    that.$message({
                        message:'数据加载成功！',
                        type:'success'
                    });
                }else {
                    //数据加载失败提示
                    that.$message.error(res.data.message);
                }
          }
          })
        .catch(function(err){
        that.$message.error("加载后端数据失败！");
        })
      },
    }
  }
</script>
