<template>
  <!-- <el-table
    :data="tableData"
    style="width: 100%">
    <el-table-column
      prop="param2__id_curricula__name"
      label="签到课程名称"
      width="180">
    </el-table-column>
    <el-table-column
      prop="attendnumbers"
      label="学生出勤次数"
      width="180">
    </el-table-column>
    <el-table-column
      prop="totalnumbers"
      label="考勤总次数"
      width="180">
    </el-table-column>
    <el-table-column
      prop="attendrates"
      label="签到率">
    </el-table-column>
  </el-table> -->
<el-table :data="tableData" border style="width: 90%;margin-left:20px" size="mini">
        <el-table-column prop="param2__id_curricula__name" label="签到课程名称" width="180" >
        </el-table-column>
        <el-table-column prop="attendnumbers" label="学生出勤次数" width="180" >
        </el-table-column>
        <el-table-column prop="totalnumbers" label="考勤总次数" width="180">
        </el-table-column>
        <el-table-column prop="attendrates" label="签到率" width="180">
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
    // methods: {
    //   tableRowClassName({row, rowIndex}) {
    //     if (rowIndex === 1) {
    //       return 'warning-row';
    //     } else if (rowIndex === 3) {
    //       return 'success-row';
    //     }
    //     return '';
    //   }
    // },:row-class-name="tableRowClassName"
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
        this.id = this.$route.params.id;
        if(!this.$route.params.id){
          this.$router.push({path:'kecheng/'})
        }
        let that = this;
        axios
        .get(
          that.baseURL + 'AttendanceInformationClass/',{params:{course_plan_id:this.id}})
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
        console.log(err);
        })
      },
    }
  }
</script>
