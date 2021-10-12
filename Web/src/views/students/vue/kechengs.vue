<template>
<div>
<el-form :inline="true" style="margin-top:20px;">
<el-row style="margin-left:20px;">
    <el-col :span="12">
        <el-form-item label="请输入筛选条件：">
            <el-input v-model="input_string" placeholder="输入筛选条件" style="width: 420px;">
            </el-input>
        </el-form-item>
    </el-col>
    <el-col :span="8" style="text-align: right;padding-right:10px;">
        <el-button-group>
            <el-button type="primary" icon="el-icon-search" @click="querykecheng()">筛选</el-button>
            <el-button type="primary" icon="el-icon-tickets" @click="getkecheng()">全部</el-button>
        </el-button-group>
    </el-col>
</el-row>
</el-form>
    <el-table :data="kecheng" border style="width: 70%;margin-left:20px" size="mini">
        <el-table-column prop="id" label="课程id" width="120">
        </el-table-column>
        <el-table-column prop="name" label="课程编号" width="140">
        </el-table-column>
        <el-table-column prop="timebegin" label="开始时间" width="140">
        </el-table-column>
        <el-table-column prop="timeend" label="结束时间" width="140">
        </el-table-column>
        <el-table-column prop="id_location__name" label="地点id" width="140">
        </el-table-column>
        <el-table-column width="140px" fixed="right" label="操作">
            <template slot-scope="scope">
                <el-button type="success" icon="el-icon-more" size="mini" circle @click="handleclick(scope.row)"></el-button>
            </template>
        </el-table-column>
    </el-table>
    <el-row style="margin-left: 300px;">
        <el-pagination         
	        @size-change="handleSizeChange"
	        @current-change="handleCurrentChange"
	        :current-page="currentpage"
            :page-size="pagesize"
	        layout="prev, pager, next, jumper"
	        :total="total">       
        </el-pagination>
    </el-row>
</div>
</template>
<script>
import axios from 'axios'
export default {
    data(){
        return {
        baseURL:"http://localhost:9000/polls/",
        kecheng:[],//所有的设备信息align="center"
        pagekecheng:[],//分页后当前页的设备信息
        input_string:'', //输入的筛选条件
        //分页的相关参数
        a:'课程考勤记录',
        total:0, //数据的总行数
        currentpage:1, //当前的所在页
        pagesize:10,//每行显示多少页
        limits:10,
    }
    },
    mounted(){
        //自动加载数据
        this.getkecheng();
    },
     methods:{
        timeup(){
            this.kechengform.timeupdate =(new Date().getTime() - new Date
            ('2000-1-1 00:00:00').getTime())/1000;
        },

        handleclick(row){
         this.$router.push({path:'/kaoqing?index='+row.id})
        },

        getkecheng:function(){
            //记录this的地址CourseInformation/
            let that = this
            //使用Axios实现Ajax请求
            axios
            .get(that.baseURL + "CourseInformation/",{params:{page:that.currentpage,limits:that.limits}})
            .then(function(res){
                //请求成功后执行的函
                if(res.data.code == 0){
                    that.$router.push('/index');
                }else{
                    if(res.data.error_code == 0){//res.data.code ===1
                    //把数据给课程
                    that.kecheng = res.data.data;
                    //获取返回记录的总行数
                    that.total = res.data.total_number*that.limits;
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
            .catch(function(res){
                //请求失败后执行的函数
                console.log(res);
                that.$message.error('获取后端数据出现异常');
            })
            },
        //     viewkaoqing(row){
        //     let that = this;
        //     axios
        //     .get(that.baseURL + "StudentAttendance/",{params:{course_plan_id:row.id}})
        //     .then(function(res){
        //         //请求成功后执行的函
        //             if(res.data.error_code == 0){
        //             //把数据给课程
        //             that.kaoqingform = res.data.data;
        //             that.$message({
        //                 message:'数据加载成功！',
        //                 type:'success'
        //             });
        //             }else {
        //                 //数据加载失败提示
        //                 that.$message.error(res.data.message);
        //             }
        //     })
        //     .catch(function(res){
        //         //请求失败后执行的函数
        //         console.log(res);
        //         that.$message.error('获取后端数据出现异常');
        //     })
        // },
        //获取当前页设备数据
        getpagekecheng(){
            //清空pageskecheng中的数据
            this.pagekecheng = [];
            //获得当前页的数据
            for(let i=(this.currentpage -1)*this.pagesize; i< this.total;i++){
                //遍历数据添加到pageshebei中
                this.pagekecheng.push(this.kecheng[i]);
                //判断是否达到一页的要求
                if (this.pagekecheng.length === this.pagesize) break;
            }
        },
        //实现当前页的设备信息筛选
        querykecheng(){
            //使用Ajax请求--POST-->传递input_string
            let that = this;
            //开始Ajax请求
            axios                                                                                                                 
            .post(
                that.baseURL + "CourseInformation/",
                {
                    input_string: that.input_string
                }
            )
            .then(function(res){
                if(res.data.error_code == 0){
                    //that.getkecheng();
                    //把数据给课程
                    that.kecheng = res.data.data;
                    //获取返回记录的总行数
                    that.total = res.data.total_number*that.limits;
                    //数据加载成功提示
                    that.$message({
                        message:'筛选数据加载成功！',
                        type:'success'
                    });
                }else {
                    //数据加载失败提示
                    that.$message.error(res.data.message);
                }
            })
            .catch(function(err){
                console.log(err);
                that.$message.error("获取后端数据出现异常!");
            })
        },

        //分页时修改每页的行数
        handleSizeChange(size){
            //修改当前每页数据行数
            this.pagesize = size;
            //数据重新分页
            this.getkecheng();
        },

        //调整当前的页码
        handleCurrentChange(pageNumber){
            //修改当前的页码
            this.currentpage = pageNumber;
            //数据重新分页
            this.getkecheng();
        },

    },
}
</script>
<style>
html,body,.el-container{
    margin: 0px;
    padding:0px;
    height: 100%;
}

.el-dialog .avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;

}
.el-dialog .avatar-uploader .el-upload:hover {
  border-color: #409EFF;
}
.el-dialog  .avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.el-dialog .avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>
