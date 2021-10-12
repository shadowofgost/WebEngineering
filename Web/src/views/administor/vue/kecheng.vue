<template>
<div>
<el-form v-model="kechengform" :inline="true" style="margin-top:20px;">
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
            <el-button type="primary" icon="el-icon-circle-plus-outline" @click="addkecheng()">添加</el-button>
        </el-button-group>
    </el-col>
</el-row>
</el-form>
    <el-table :data="kecheng" border style="width: 90%;margin-left:20px" size="mini" @selection-change="handleSelectionChange">
        <el-table-column type="selection">
        </el-table-column>
        <el-table-column type="index" label="序号" width="60" align="center">
        </el-table-column>
        <el-table-column prop="id" label="课程id" width="120" align="center">
        </el-table-column>
        <el-table-column prop="name" label="课程编号" width="140" align="center">
        </el-table-column>
        <el-table-column prop="timebegin" label="开始时间" width="140" align="center">
        </el-table-column>
        <el-table-column prop="timeend" label="结束时间" width="140" align="center">
        </el-table-column>
        <el-table-column prop="id_location__name" label="地点id" width="140" align="center">
        </el-table-column>
        <el-table-column width="400px" fixed="right" label="操作" align="center">
            <template slot-scope="scope">
                <el-button type="success" icon="el-icon-more" size="mini" circle @click="viewkecheng(scope.row)"></el-button>
                <el-button type="primary" icon="el-icon-edit" size="mini" circle @click="updatekecheng(scope.row)"></el-button>
                <el-button type="danger" icon="el-icon-delete" size="mini" circle @click="deletekecheng(scope.row)"></el-button>
                <el-button type="info" icon="el-icon-view" size="mini" circle @click="handleclick(scope.row)"></el-button>
            </template>
        </el-table-column>
    </el-table>
    <el-row style="margin-top: 10px;">
        <el-col :span="8" style="text-align: left;margin-left:20px">
            <el-button type="primary" icon="el-icon-delete" size="mini" @click="deletekechengs()">批量删除</el-button>
        </el-col>
        <el-pagination         
	        @size-change="handleSizeChange"
	        @current-change="handleCurrentChange"
	        :current-page="currentpage"
            :page-size="pagesize"
	        layout="prev, pager, next, jumper"
	        :total="total">       
        </el-pagination>
    </el-row>
      <el-dialog :title="dialogTitle" :visible.sync="dialogVisible" width="50%"  @close="closeDialogForm('kechengform')">
        <el-form :model="kechengform" :rules="rules" ref="kechengform" :inline=true style="margin-left:20px;" label-width="110px" labei-position="right" size="mini">
            <el-form-item label="课程id" prop="id">
                <el-input v-model="kechengform.id" :disabled="isEdit || isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="课程编号" prop="name">
                <el-input v-model="kechengform.name" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="开始时间" prop="timebegin">
                <el-input v-model="kechengform.timebegin" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="结束时间" prop="timeend">
                <el-input v-model="kechengform.timeend" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="地点id" prop="id_location__name">
                <el-input v-model="kechengform.id_location__name" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="演讲者id" prop="id_speaker__name">
                <el-input v-model="kechengform.id_speaker__name" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="考勤类型" prop="attr">
                <el-select v-model="kechengform.attr" :disabled="isView">
                    <el-option labei="实验类型" value="实验类型"></el-option>
                    <el-option labei="普通上课类型" value="普通上课类型"></el-option>
                    <el-option labei="讲座考勤类型" value="讲座考勤类型"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="是否收费" prop="charge">
                <el-select v-model="kechengform.charge" :disabled="isView">
                    <el-option labei="免费" value="免费"></el-option>
                    <el-option labei="收费" value="收费"></el-option>
                    <el-option labei="开放" value="开放"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="派位" prop="pwaccess">
                <el-select v-model="kechengform.pwaccess" :disabled="isView">
                    <el-option labei="不派位" value="不派位"></el-option>
                    <el-option labei="刷卡派位" value="刷卡派位"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="派位连续性" prop="pwcontinuous">
                <el-select v-model="kechengform.pwcontinuous" :disabled="isView">
                    <el-option labei="连续派位" value="连续派位"></el-option>
                    <el-option labei="随机派位" value="随机派位"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="派位顺序" prop="pwdirection">
                <el-select v-model="kechengform.pwdirection" :disabled="isView">
                    <el-option labei="顺序派位" value="顺序派位"></el-option>
                    <el-option labei="逆序派位" value="逆序派位"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="是否开门" prop="dooropen">
                <el-select v-model="kechengform.dooropen" :disabled="isView">
                    <el-option labei="开门" value="开门"></el-option>
                    <el-option labei="不开门" value="不开门"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="考勤开始最早时间" prop="timebegincheckbegin">
                <el-input v-model="kechengform.timebegincheckbegin" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="考勤开始最迟时间" prop="timebegincheckend">
                <el-input v-model="kechengform.timebegincheckend" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="考勤结束最早时间" prop="timeendcheckbegin">
                <el-input v-model="kechengform.timeendcheckbegin" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="考勤结束最迟时间" prop="timeendcheckend">
                <el-input v-model="kechengform.timeendcheckend" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="参加这门课的所属学生数" prop="rangeusers">
                <el-input v-model="kechengform.rangeusers" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="座位的范围表" prop="rangeequs">
                <el-input v-model="kechengform.rangeequs" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="对应表" prop="listplaces">
                <el-input v-model="kechengform.listplaces" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="学生和座位对应表" prop="mapuser2equ">
                <el-input v-model="kechengform.mapuser2equ" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="本课程主讲人介绍" prop="aboutspeaker">
                <el-input v-model="kechengform.aboutspeaker" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="课程介绍" prop="rem">
                <el-input v-model="kechengform.rem" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <!-- <el-form-item label="记录更新时间" prop="timeupdate">
                <el-input v-model="kechengform.timeupdate" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item> -->
            <el-form-item label="修改id名称" prop="idmanager__name">
                <el-input v-model="kechengform.idmanager__name" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button type="primary" size="mini" v-show="!isView" @click="submitkechengform('kechengform')">确定</el-button>
            <el-button type="info" size="mini" @click="closeDialogForm('kechengform')">取消</el-button>
        </span>
      </el-dialog>
</div>
</template>
<script>
import axios from 'axios'
export default {
    data(){
        // 校验设备id是否存在
        const rulesID = (rule,value,callback) =>{
            if(this.isEdit){
                callback();
            }
            //使用axios进行校验
            axios
            .post(
                this.baseURL + 'IDEvaluation/',
                {
                    id:value,kind:7
                }
            )
            .then((res)=>{
                //请求成功
                if (true){
                    if(res.data.exists){
                        callback(new Error("课程id已存在！"));
                    }else{
                        callback();
                    }
                }else{
                    callback(new Error("检验课程id后端出现异常！"))
                }
            })
            .catch((err)=>{
                //请求失败打印
                console.log(err);
            });

        }

        return {
        baseURL:"http://localhost:9000/polls/",
        kecheng:[],//所有的设备信息
        pagekecheng:[],//分页后当前页的设备信息
        input_string:'', //输入的筛选条件
        //分页的相关参数
        total:0, //数据的总行数
        currentpage:1, //当前的所在页
        pagesize:10,//每行显示多少页
        limits:10,
        dialogVisible:false,
        kechengform:{
            id:'',
            name:'',
            timebegin:'',
            timeend:'',
            id_location__name:'',
            id_speaker__name:'',
            attr:'',
            charge:'',
            pwaccess:'',
            pwcontinuous:'',
            pwdirection:'',
            dooropen:'',
            timebegincheckbegin:'',
            timebegincheckend:'',
            timeendcheckbegin:'',
            timeendcheckend:'',
            listdepts:'',
            rangeusers:'',
            rangeequs:'',
            listplaces:'',
            mapuser2equ:'',
            aboutspeaker:'',
            rem:'',
            timeupdate:'',
            idmanager__name:'',
        },
        rules:{
            id:[
                    {required:true,message:'课程id不能为空',trigger:'blur'},
                    {validator:rulesID,trigger:'blur'},
            ],
            name:[
                    {required:true,message:'课程编号不能为空',trigger:'blur'},

            ],
            timebegin:[
                    {required:true,message:'开始时间不能为空',trigger:'blur'},

            ],
            timeend:[
                    {required:true,message:'结束时间不能为空',trigger:'blur'},

            ],
            id_location__name:[
                    {required:true,message:'地点id不能为空',trigger:'blur'},

            ],
            id_speaker__name:[
                    {required:true,message:'演讲者的id不能为空',trigger:'blur'},

            ],
            attr:[
                    {required:true,message:'考勤类型不能为空',trigger:'blur'},

            ],
            charge:[
                    {required:true,message:'是否收费不能为空',trigger:'blur'},

            ],
            pwaccess:[
                    {required:true,message:'派位不能为空',trigger:'blur'},

            ],
            pwcontinuous:[
                    {required:true,message:'派位连续性不能为空',trigger:'blur'},

            ],
            pwdirection:[
                    {required:true,message:'派位顺序不能为空',trigger:'blur'},

            ],
            dooropen:[
                    {required:true,message:'是否开门不能为空',trigger:'blur'},

            ],
            timebegincheckbegin:[
                    {required:true,message:'考勤开始最早时间不能为空',trigger:'blur'},

            ],
            timebegincheckend:[
                    {required:true,message:'考勤开始最迟时间不能为空',trigger:'blur'},

            ],
            timeendcheckbegin:[
                    {required:true,message:'考勤结束最早时间不能为空',trigger:'blur'},

            ],
            timeendcheckend:[
                    {required:true,message:'考勤结束最迟时间不能为空',trigger:'blur'},

            ],
            rangeusers:[
                    {required:true,message:'参加这门课的所属学生数不能为空',trigger:'blur'},

            ],
            rangeequs:[
                    {required:true,message:'座位的范围表不能为空',trigger:'blur'},

            ],
            listplaces:[
                    {required:true,message:'对应表不能为空',trigger:'blur'},

            ],
            mapuser2equ:[
                    {required:true,message:'学生和座位对应表不能为空',trigger:'blur'},

            ],
            aboutspeaker:[
                    {required:true,message:'本课程主讲人介绍不能为空',trigger:'blur'},

            ],
            rem:[
                    {required:true,message:'课程介绍不能为空',trigger:'blur'},

            ],
            timeupdate:[
                    {required:true,message:'记录更新时间不能为空',trigger:'blur'},

            ],
            idmanager__name:[
                    {required:true,message:'修改id名称不能为空',trigger:'blur'},

            ],
        },

        dialogTitle: "", //弹出框的标题

        isView: false, //标识是否是查看
        isEdit: false, //标识是否是修改

        selectkechengs: [],//选择复选时把选择记录存在这里

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
        datatrans1(){
                    if(this.kechengform.attr == 0){
                        this.kechengform.attr="实验类型";
                    }else if(this.kechengform.attr == 1){
                        this.kechengform.attr="普通上课类型";
                    }else{
                        this.kechengform.attr="讲座考勤类型";
                    }

                    if(this.kechengform.charge == 0){
                        this.kechengform.charge="免费";
                    }else if(this.kechengform.charge == 1){
                        this.kechengform.charge="收费";
                    }else{
                        this.kechengform.charge="开放";
                    }

                    if(this.kechengform.pwaccess == 0){
                        this.kechengform.pwaccess="不派位";
                    }else{
                        this.kechengform.pwaccess="刷卡派位";
                    }

                    if(this.kechengform.pwcontinuous == 0){
                        this.kechengform.pwcontinuous="连续派位";
                    }else{
                        this.kechengform.pwcontinuous="随机派位";
                    }

                    if(this.kechengform.dooropen == 0){
                        this.kechengform.dooropen="开门";
                    }else{
                        this.kechengform.dooropen="不开门";
                    }
        },
        datatrans2(){
                    if(this.kechengform.attr == "实验类型"){
                        this.kechengform.attr=0;
                    }else if(this.kechengform.attr == "普通上课类型"){
                        this.kechengform.attr=1;
                    }else{
                        this.kechengform.attr=2;
                    }

                    if(this.kechengform.charge == "免费"){
                        this.kechengform.charge=0;
                    }else if(this.kechengform.charge == "收费"){
                        this.kechengform.charge=1;
                    }else{
                        this.kechengform.charge=3;
                    }

                    if(this.kechengform.pwaccess == "不派位"){
                        this.kechengform.pwaccess=0;
                    }else{
                        this.kechengform.pwaccess=1;
                    }

                    if(this.kechengform.pwcontinuous == "连续派位"){
                        this.kechengform.pwcontinuous=0;
                    }else{
                        this.kechengform.pwcontinuous=1;
                    }

                    if(this.kechengform.dooropen == "开门"){
                        this.kechengform.dooropen=0;
                    }else{
                        this.kechengform.dooropen=1;
                    }
        },
        //详情生成该课程签到记录表
        handleclick(row){
         this.$router.push({path:'/qiandao?index='+row.id})
        },
        //获取所有设备信息
        getkecheng:function(){
            //记录this的地址
            let that = this
            //使用Axios实现Ajax请求
            axios
            .get(that.baseURL + "CourseInformation/",{params:{page:that.currentpage,limits:that.limits}})
            .then(function(res){
                //请求成功后执行的函数
                //console.log(res);
                if(res.data.code == 0){
                    that.$router.push('/index');
                }else{
                    if(res.data.error_code == 0){//res.data.code ===1
                    //把数据给课程
                    that.kecheng = res.data.data;
                    //获取返回记录的总行数
                    that.total = res.data.total_number*that.limits;
                    //获取当前页的数据
                    //that.getpagekecheng();
                    //数据加载成功提示
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
                that.$message.error('获取后端数据出现异常');
            })
        },
        //获取当前页设备数据
        getpagekecheng(){
            //清空pageskecheng中的数据
            this.pagekecheng = [];
            //获得当前页的数据
            for(let i=(this.currentpage -1)*this.pagesize; i< this.total;i++){
                //遍历数据添加到pageshebei中
                this.pagekecheng.push(this.kecheng[i]);
                //判断是否达到一页的要求
                //if (this.pagekecheng.length === this.pagesize) break;
            }
        },
        //实现当前页的设备信息筛选
        querykecheng(){
            //使用Ajax请求--POST-->传递input_string
            let that = this;
            //开始Ajax请求
            axios                                                                                                                 //Axios请求
            .post(
                that.baseURL + "CourseInformation/",
                {
                    input_string: that.input_string
                }
            )
            .then(function(res){
                if(res.data.error_code == 0){
                    //把数据给shebei
                    //that.kecheng = res.data.data;
                    //获取返回记录的总行数
                    //that.total = res.data.data.length;
                    //获取当前页的数据
                    //that.getpagekecheng();
                    //that.getpagekecheng();
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
                    that.$message.error(res.data.msg);
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


        //选择复选框触发操作
        handleSelectionChange(data){
            this.selectkechengs = data;
        },
        //添加课程时打开表单
        addkecheng(){
            //修改标题
            this.dialogTitle = "添加课程明细";
            //弹出表单
            this.dialogVisible = true;
        },
        //关闭弹出框的表单
        closeDialogForm(formName){
            //清空数据
            this.kechengform.id ="";
            this.kechengform.name ="";
            this.kechengform.timebegin ="";
            this.kechengform.timeend ="";
            this.kechengform.id_location__name ="";
            this.kechengform.id_speaker__name ="";
            this.kechengform.charge ="";
            this.kechengform.pwaccess ="";
            this.kechengform.pwcontinuous ="";
            this.kechengform.pwdirection ="";
            this.kechengform.dooropen ="";
            this.kechengform.timebegincheckbegin ="";
            this.kechengform.timebegincheckend ="";
            this.kechengform.timeendcheckbegin ="";
            this.kechengform.timeendcheckend ="";
            this.kechengform.rangeusers ="";
            this.kechengform.rangeequs ="";
            this.kechengform.listplaces ="";
            this.kechengform.mapuser2equ ="";
            this.kechengform.aboutspeaker ="";
            this.kechengform.rem ="";
            this.kechengform.timeupdate ="";
            this.kechengform.idmanager__name ="";

            //重置表单的校验
            this.$nextTick(()=>{
                this.$refs[formName].resetFields();
            });
            //关闭
            this.dialogVisible = false;
            this.isView = false;
            this.isEdit = false;
        },

        //查看课程的明细
        viewkecheng(row){
            //修改标题
            this.dialogTitle = "查看课程明细";
            //修改isView变量
            this.isView = true;
            //弹出表单
            this.dialogVisible = true;
            //进行深拷贝
            this.kechengform = JSON.parse(JSON.stringify(row))
            this.datatrans1();
        },
        //修改设备的信息
        updatekecheng(row) {
            //修改标题
            this.dialogTitle = "修改课程明细";
            //修改isEdit变量
            this.isEdit = true;
            //弹出表单
            this.dialogVisible = true;
            this.kechengform = JSON.parse(JSON.stringify(row))
            this.datatrans1();
        },
        //提交设备的表单（添加、修改）
        submitkechengform(formName) {
            this.$refs[formName].validate((valid) =>{
                if (valid) {
                    //校验成功后执行添加或者修改
                    if (this.isEdit){
                        this.kechengform.id = Number(this.kechengform.id);
                        this.kechengform.id_location__name = Number(this.kechengform.id_location__name);
                        this.kechengform.id_speaker__name = Number(this.kechengform.id_speaker__name);
                        //this.timeup();
                        this.datatrans2();
                        this.submitupdatakecheng();
                    }else{
                        //添加
                        this.kechengform.id = Number(this.kechengform.id);
                        this.kechengform.id_location__name = Number(this.kechengform.id_location__name);
                        this.kechengform.id_speaker__name = Number(this.kechengform.id_speaker__name);
                        //this.timeup();
                        this.datatrans2();
                        this.submitaddkecheng()
                    }
                alert('submit!');
              } else {
                    console.log('error submit!!');
                    return false;
                }
            });
        },
        //添加到数据库的函数
        submitaddkecheng(){
            let that = this;
            //执行Axios请求
            axios
            .put(that.baseURL + 'CourseInformation/', that.kechengform)
            .then(res=>{
                //执行成功
                if(res.data.error_code == 0){//res.data.code == 1
                    // //获取所有课程信息
                    // that.kecheng = res.data.data;
                    // //获取记录条数
                    // that.total = res.data.data.length;
                    // //获取分页信息
                    // that.getpagekecheng();
                    that.getkecheng();
                    //提示
                    that.$message({
                        message:'数据加载成功！',
                        type:'success'
                    });
                    //关闭窗体
                    that.closeDialogForm('kechengform');
                }else{
                    //失败提示
                    that.$message.error(res.data.message);
                }
            })
            .catch(err=>{
                //执行失败
                console.log(err);
                that.$message.error("获取后端结果出现异常");
            });
        },
        //修改更新到数据库
        submitupdatakecheng(){
            let that = this;
            //执行Axios请求
            axios
            .patch(that.baseURL + 'CourseInformation/', that.kechengform)
            .then(res=>{
                //执行成功
                if(res.data.error_code == 0){//res.data.code == 1
                    // //获取所有课程信息
                    // that.kecheng = res.data.data;
                    // //获取记录条数
                    // that.total = res.data.data.length;
                    // //获取分页信息
                    // that.getpagekecheng();
                    that.getkecheng();
                    //提示
                    that.$message({
                        message:'数据修改成功！',
                        type:'success'
                    });
                    //关闭窗体
                    that.closeDialogForm('kechengform');
                }else{
                    //失败提示
                    that.$message.error(res.data.message);
                }
            })
            .catch(err=>{
                //执行失败
                that.$message.error("获取后端结果出现异常！");
            });
        },
        //删除一条课程信息
        deletekecheng(row) {
            //等待确认
            this.$confirm('是否确认删除课程信息【课程id：' + row.id + '\t课程名称：' + row.name + '】信息？',
                '提示', {
                confirmButtonText: '确定删除',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                //确认删除响应事件
                let that = this
                //调用后端接口
                axios
                .delete(that.baseURL + 'CourseInformation/',{data:{ids:[{"data_id":row.id}]}})
                .then(res => {
                        if (res.data.error_code == 0) {
                            // //获取所有课程信息
                            // that.kecheng = res.data.data;
                            // //获取记录数
                            // that.total = res.data.data.length;
                            // //分页
                            // that.getpagekecheng();
                            that.getkecheng();
                            //提示
                            that.$message({
                                message: '数据删除成功！',
                                type: 'success'
                            });
                        } else {
                            that.$message.error('数据删除失败！');
                        }
                    })

            }).catch(() => {
                this.$message({
                    type: 'info',
                    message: '已取消删除'
                });
            });
        },
        //批量删除课程信息
        deletekechengs() {
            //等待确认
            this.$confirm("是否确认批量删除" + this.selectkechengs.length + "个课程信息吗？",
                '提示', {
                confirmButtonText: '确定删除',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                let ids = [];
                for(var i=0;i<this.selectusers.length;i++){
                    ids.push({"data_id":this.selectusers[i].id});
                }
                //确认删除响应事件
                let that = this
                //调用后端接口
                axios
                    .delete(this.baseURL + 'CourseInformation/',{data:{
                    ids:ids}
                    })
                    .then(res => {
                        if (res.data.error_code == 0) {
                            // //获取所有课程信息
                            // that.kecheng = res.data.data;
                            // //获取记录数
                            // that.total = res.data.data.length;
                            // //分页
                            // that.getpagekecheng();
                            that.getkecheng();
                            //提示
                            that.$message({
                                message: '数据批量删除成功！',
                                type: 'success'
                            });
                        } else {
                            that.$message.error('数据批量删除失败！');
                        }
                    })

            }).catch(() => {
                this.$message({
                    type: 'info',
                    message: '已取消删除'
                });
            });
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
