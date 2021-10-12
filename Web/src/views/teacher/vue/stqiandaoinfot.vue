<template>
  <!-- <el-table
    :data="tableData"
    style="width: 100%">
    <el-table-column
      prop="id"
      label="ID"
      width="180">
    </el-table-column>
    <el-table-column
      prop="id_user__name"
      label="考勤者姓名"
      width="180">
    </el-table-column>
    <el-table-column
      prop="attendtimes"
      label="考勤者出勤的次数"
      width="180">
    </el-table-column>
    <el-table-column
      prop="attendtotal"
      label="应该出勤的次数"
      width="180">
    </el-table-column>
    <el-table-column
      prop="attendrates"
      label="出勤率"
      width="180">
    </el-table-column>
  </el-table> align="center" -->

<el-table :data="tableData"  style="width: 90%;margin-left:20px" size="mini">
        <el-table-column prop="id" label="ID" width="180" >
        </el-table-column>
        <el-table-column prop="id_user__name" label="考勤者姓名" width="180" >
        </el-table-column>
        <el-table-column prop="attendtimes" label="考勤者出勤的次数" width="180">
        </el-table-column>
        <el-table-column prop="attendtotal" label="应该出勤的次数" width="180">
        </el-table-column>
        <el-table-column prop="attendrates" label="出勤率" width="180">
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
    this.gets2();
    },
    methods:{
      gets2(){
        this.id = this.$route.params.id;
        if(!this.$route.params.id){
          this.$router.push({path:'kecheng/'})
        }
        let that = this;
        //that.$message.error("加载数据失败");
        axios
        .get(
            that.baseURL + 'AttendanceInformation/',{params:{course_plan_id:this.id}})
        .then(function(res){
                if(res.data.code == 0){
                  that.$router.push('/index');
                }else{
                  if(res.data.error_code == 0){//true
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
          console.log(err);
          that.$message.error("加载数据失败");
            })
      },
    }
  }
</script>
