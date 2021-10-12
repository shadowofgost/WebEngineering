<template>

<div>
<el-form v-model="shebeiform" :inline="true" style="margin-top:20px;">
<el-row style="margin-left:20px;">
    <el-col :span="12">
        <el-form-item label="请输入筛选条件：">
            <el-input v-model="input_string" placeholder="输入筛选条件" style="width: 420px;">
            </el-input>
        </el-form-item>
    </el-col>
    <el-col :span="8" style="text-align: right;padding-right:10px;">
        <el-button-group>
            <el-button type="primary" icon="el-icon-search" @click="queryshebei()">筛选</el-button>
            <el-button type="primary" icon="el-icon-tickets" @click="getshebei()">全部</el-button>
            <el-button type="primary" icon="el-icon-circle-plus-outline" @click="addshebei()">添加</el-button>
        </el-button-group>
    </el-col>
</el-row>

</el-form>
    <el-table :data="shebei" border style="width: 90%;margin-left:20px" size="mini" @selection-change="handleSelectionChange">
        <el-table-column type="selection">
        </el-table-column>
        <el-table-column type="index" label="序号" width="60" align="center">
        </el-table-column>
        <el-table-column prop="id" label="设备id" width="120" align="center">
        </el-table-column>
        <el-table-column prop="id_location__name" label="设备所在地点" width="140" align="center">
        </el-table-column>
        <el-table-column prop="id_ip" label="设备的ip地址" width="140" align="center">
        </el-table-column>
        <!-- <el-table-column prop="timeupdate" label="更新时间" width="140" align="center">
        </el-table-column>  -->
        <el-table-column prop="portlisten" label="数据端口" width="140" align="center">
        </el-table-column>
        <el-table-column prop="type_field" label="刷卡器类型" width="140" align="center">
        </el-table-column>
         <el-table-column  width="400px" fixed="right" label="操作" align="center" >
            <template slot-scope="scope">
                <el-button type="success" icon="el-icon-more" size="mini" circle @click="viewshebei(scope.row)"></el-button>
                <el-button type="primary" icon="el-icon-edit" size="mini" circle @click="updateshebei(scope.row)"></el-button>
                <el-button type="danger" icon="el-icon-delete" size="mini" circle @click="deleteshebei(scope.row)"></el-button>
            </template>
        </el-table-column>
    </el-table>
    <el-row style="margin-top: 10px;">
        <el-col :span="8" style="text-align: left;margin-left:20px">
            <el-button type="primary" icon="el-icon-delete" size="mini" @click="deleteshebeis()">批量删除</el-button>
        </el-col>
        <!-- <el-col :span="16" style="text-align: right">
            <el-pagination
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                :current-page="currentpage"
                :page-sizes="[5, 10, 50, 100]"
                :page-size="pagesize"
                layout="total, sizes, prev, pager, next, jumper"
                :total="total">
            </el-pagination>
        </el-col> -->
            <el-pagination         
	        @size-change="handleSizeChange"
	        @current-change="handleCurrentChange"
	        :current-page.sync="currentpage"
            :page-size="pagesize"
	        layout="total,prev, pager, next, jumper"
	        :total="total">       
            </el-pagination>
    </el-row>
    <!-- <el-scrollbar style="height:300px;"> -->
    <el-dialog :title="dialogTitle" :visible.sync="dialogVisible" width="50%"  @close="closeDialogForm('shebeiform')">
        <el-form :model="shebeiform" :rules="rules" ref="shebeiform" :inline=true style="margin-left:20px;" label-width="110px" labei-position="right" size="mini">
            <el-form-item label="设备id" prop="id">
                <el-input v-model="shebeiform.id" :disabled="isEdit || isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="设备名称" prop="name">
                <el-input v-model="shebeiform.name" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="设备所在地点的名称" prop="id_location__name">
                <el-input v-model="shebeiform.id_location__name" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="设备所在位置内部的编号" prop="id_location_sn">
                <el-input v-model="shebeiform.id_location_sn" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="设备的ip地址" prop="id_ip">
                <el-input v-model="shebeiform.id_ip" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="设备的mac地址" prop="mac">
                <el-input v-model="shebeiform.mac" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="设备状态" prop="state">
                <el-select v-model="shebeiform.state" :disabled="isView" placeholder="请选择设备状态">
                    <el-option labei="正常空闲" value="正常空闲"></el-option>
                    <el-option labei="故障" value="故障"></el-option>
                    <el-option labei="其他" value="其他"></el-option>
                    <el-option labei="正常使用中" value="正常使用中"></el-option>
                    <el-option labei="开放" value="开放"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="登录状态" prop="login">
                <el-select v-model="shebeiform.login" :disabled="isView" placeholder="请选择设备状态">
                    <el-option labei="未登录" value="未登录"></el-option>
                    <el-option labei="已经登录" value="已经登录"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="网络状态" prop="link">
                <el-select v-model="shebeiform.link" :disabled="isView" placeholder="请选择设备状态">
                    <el-option labei="脱机" value="脱机"></el-option>
                    <el-option labei="在线" value="在线"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="设备种类" prop="class_field">
                <el-select v-model="shebeiform.class_field" :disabled="isView" placeholder="无">
                    <el-option labei="PC 设备" value="PC 设备"></el-option>
                    <el-option labei="刷卡 设备" value="刷卡 设备"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="设备的像素x位置信息" prop="dx">
                <el-input v-model="shebeiform.dx" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="设备的像素y位置信息" prop="dy">
                <el-input v-model="shebeiform.dy" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="使用者的姓名" prop="id_user__name">
                <el-input v-model="shebeiform.id_user__name" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="设备所关联的课程安排表" prop="id_plan">
                <el-input v-model="shebeiform.id_plan" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="itimebegin">
                <el-date-picker type="date" placeholder="选择日期" v-model="shebeiform.itimebegin" value-format="yyyy-MM-dd" :disabled="isView" suffix-icon="el-icon-edit">
                </el-date-picker>
            </el-form-item>
            <el-form-item label="itimelogin">
                <el-date-picker type="date" placeholder="选择日期" v-model="shebeiform.itimelogin" value-format="yyyy-MM-dd" :disabled="isView" suffix-icon="el-icon-edit">
                </el-date-picker>
            </el-form-item>
            <el-form-item label="whitelist" prop="whitelist">
                <el-input v-model="shebeiform.whitelist" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="设备说明" prop="rem">
                <el-input v-model="shebeiform.rem" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <!-- <el-form-item label="更新时间" prop="timeupdate">
                <el-input  v-model="shebeiform.timeupdate" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item> -->
            <el-form-item label="最后修改信息的管理员" prop="idmanager__name">
                <el-input v-model="shebeiform.idmanager__name" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="数据端口" prop="portlisten">
                <el-input v-model="shebeiform.portlisten" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="刷卡器类型" prop="type_field">
                <el-input v-model="shebeiform.type_field" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="开门延迟时间" prop="timedelay">
                <el-input v-model="shebeiform.timedelay" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="取消键键码" prop="keycancel">
                <el-input v-model="shebeiform.keycancel" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="确定键键码" prop="keyOk">
                <el-input v-model="shebeiform.keyOk" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="删除键键码" prop="keydel">
                <el-input v-model="shebeiform.keydel" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="功能键键码" prop="keyf1">
                <el-input v-model="shebeiform.keyf1" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="门禁刷卡总是开门" prop="onall">
                <el-input v-model="shebeiform.onall" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="管理设备范围" prop="rangeequs">
                <el-input v-model="shebeiform.rangeequs" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="管理地点范围" prop="listplaces">
                <el-input v-model="shebeiform.listplaces" :disabled="isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button type="primary" size="mini" v-show="!isView" @click="submitshebeiform('shebeiform')">确定</el-button>
            <el-button type="info" size="mini" @click="closeDialogForm('shebeiform')">取消</el-button>
        </span>
    </el-dialog>
    <!-- </el-scrollbar> -->
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
                this.baseURL + "EquipmentInformation/",
                {
                    id:value,kind:2
                }
            )
            .then((res)=>{
                //请求成功
                if (true){
                    if(res.data.exists){
                        callback(new Error("设备id已存在！"));
                    }else{
                        callback();
                    }
                }else{
                    callback(new Error("检验设备id后端出现异常！"))
                }
            })
            .catch((err)=>{
                //请求失败打印
                console.log(err);
            });

        }
        return {
        total:0,
        currentpage:1,  //默认第一页
        pagesize:10, //默认展示10条数据
        limits:10,
        baseURL:"http://localhost:9000/polls/",
        shebei:[],//所有的设备信息
        pageshebei:[],//分页后当前页的设备信息
        input_string:'', //输入的筛选条件
        //分页的相关参数
        //total:0, //数据的总行数
        //currentpage:1, //当前的所在页
        //pagesize:10,//每行显示多少页
        dialogVisible:false,
        shebeiform:{
            id:'',
            name:'',
            id_location__name:'',
            id_location_sn:'',
            id_ip:'',
            mac:'',
            state:'',
            login:'',
            link:'',
            class_field:'',
            dx:'',
            dy:'',
            id_user__name:'',
            id_plan:'',
            itimebegin:'',
            itimelogin:'',
            whitelist:'',
            rem:'',
            timeupdate:'',
            idmanager__name:'',
            portlisten:'',
            type_field:'',
            timedelay:'',
            keycancel:'',
            keyOk:'',
            keydel:'',
            keyf1:'',
            onall:'',
            rangeequs:'',
            listplaces:'',
        },
        rules:{
            id:[
                    {required:true,message:'设备id不能为空',trigger:'blur'},
                    {validator:rulesID,trigger:'blur'},
            ],
            name:[
                    {required:true,message:'设备名称不能为空',trigger:'blur'},

            ],
            id_location__name:[
                    {required:true,message:'设备所在地点名称不能为空',trigger:'blur'},

            ],
            id_location_sn:[
                    {required:true,message:'设备所在位置的内部编号不能为空',trigger:'blur'},

            ],
            id_ip:[
                    {required:true,message:'设备的ip地址不能为空',trigger:'blur'},

            ],
            mac:[
                    {required:true,message:'设备的mac地址不能为空',trigger:'blur'},

            ],
            state:[
                    {required:true,message:'设备状态不能为空',trigger:'blur'},

            ],
            login:[
                    {required:true,message:'登录状态不能为空',trigger:'blur'},

            ],
            link:[
                    {required:true,message:'设备网络连接状态不能为空',trigger:'blur'},

            ],
            class_field:[
                    {required:true,message:'设备种类不能为空',trigger:'blur'},

            ],
            dx:[
                    {required:true,message:'设备的像素x位置信息不能为空',trigger:'blur'},

            ],
            dy:[
                    {required:true,message:'设备的像素y位置信息不能为空',trigger:'blur'},

            ],
            id_user__name:[
                    {required:true,message:'使用者姓名不能为空',trigger:'blur'},

            ],
            id_plan:[
                    {required:true,message:'设备所关联的课程安排表id不能为空',trigger:'blur'},

            ],
            whitelist:[
                    {required:true,message:'whitelist不能为空',trigger:'blur'},

            ],
            rem:[
                    {required:true,message:'设备说明不能为空',trigger:'blur'},

            ],
            timeupdate:[
                    {required:true,message:'更新时间不能为空',trigger:'blur'},

            ],
            idmanager__name:[
                    {required:true,message:'最后修改信息的管理员的姓名不能为空',trigger:'blur'},

            ],
            portlisten:[
                    {required:true,message:'数据端口不能为空',trigger:'blur'},

            ],
            type_field:[
                    {required:true,message:'刷卡器类型不能为空',trigger:'blur'},

            ],
            timedelay:[
                    {required:true,message:'开门延迟时间不能为空',trigger:'blur'},

            ],
            keycancel:[
                    {required:true,message:'取消键键码不能为空',trigger:'blur'},
            ],
            keyOk:[
                    {required:true,message:'确定键键码不能为空',trigger:'blur'},
            ],
            keydel:[
                    {required:true,message:'删除键键码不能为空',trigger:'blur'},

            ],
            keyf1:[
                    {required:true,message:'功能键键码不能为空',trigger:'blur'},

            ],
            onall:[
                    {required:true,message:'门禁刷卡总是开门不能为空',trigger:'blur'},

            ],
            rangeequs:[
                    {required:true,message:'管理设备范围不能为空',trigger:'blur'},

            ],
            listplaces:[
                    {required:true,message:'管理地点范围不能为空',trigger:'blur'},

            ],
        },

        dialogTitle: "", //弹出框的标题type="date" value-format="yyyy-MM-dd"

        isView: false, //标识是否是查看
        isEdit: false, //标识是否是修改

        selectshebeis: [],//选择复选时把选择记录存在这里
        is_status:false,
        }
    },
    mounted(){
        //自动加载数据
        this.getshebei();
        //this.created();
    },
    methods:{
        //数据转换
        timeup(){
            this.userform.timeupdate =(new Date().getTime() - new Date
            ('2000-1-1 00:00:00').getTime())/1000;
        },

        datatrans1(){
            if(this.shebeiform.state == 0){
                this.shebeiform.state="正常空闲";
            }else if(this.shebeiform.state == 1){
                this.shebeiform.state="故障";
            }else if(this.shebeiform.state == 2){
                this.shebeiform.state="其它";
            }else if(this.shebeiform.state == 3){
                this.shebeiform.state="正常使用中";
            }else{
                this.shebeiform.state="开放";
            }
            if(this.shebeiform.login == 0){
                this.shebeiform.login="未登录";
            }else{
                this.shebeiform.login="已经登录";
            }

            if(this.shebeiform.link == 0){
                this.shebeiform.link="脱机";
            }else{
                this.shebeiform.link="在线";
            }

            if(this.shebeiform.class_field == 0){
                this.shebeiform.class_field="PC设备";
            }else{
                this.shebeiform.class_field="刷卡设备";
            }
        },

        datatrans2(){
            if(this.shebeiform.state == "正常空闲"){
                this.shebeiform.state=0;
            }else if(this.shebeiform.state == "故障"){
                this.shebeiform.state=1;
            }else if(this.shebeiform.state == "其它"){
                this.shebeiform.state=2;
            }else if(this.shebeiform.state == "正常使用中"){
                this.shebeiform.state=3;
            }else{
                this.shebeiform.state=4;
            }

            if(this.shebeiform.login == "未登录"){
                this.shebeiform.login=0;
            }else{
                this.shebeiform.login=1;
            }

            if(this.shebeiform.link == "脱机"){
                this.shebeiform.link=0;
            }else{
                this.shebeiform.link=1;
            }

            if(this.shebeiform.class_field == "PC设备"){
                this.shebeiform.class_field=0;
            }else{
                this.shebeiform.class_field=1;
            }
        },
        //获取所有设备信息
        getshebei:function(){
            //记录this的地址
            let that = this
            //使用Axios实现Ajax请求
            axios
            .get(that.baseURL + "EquipmentInformation/",{params:{page:that.currentpage,limits:that.limits}}) //,{page:that.currentpage,limits:that.limits}
            .then(function(res){
                if(res.data.code == 0){
                    that.$router.push('/index');
                }else{
                if(res.data.error_code == 0){ //res.data.error_code == 0
                    //把数据给shebei
                        that.shebei = res.data.data;
                    //获取返回记录的总行数
                        that.total = res.data.total_number*that.limits;
                        //console.log(that.total);
                    //获取当前页的数据
                    //that.getpageshebei();
                    //数据加载成功提示
                    that.$message({
                        message:'数据加载成功！',
                        type:'success'
                    });
                }else{
                    //数据加载失败提示
                    that.$message.error(res.data.message);
                    }
                }
            })
            .catch(function(err){
                //请求失败后执行的函数
                that.$message.error("请求后端数据失败");
            })
        },

        //实现当前页的设备信息筛选
        queryshebei(){
            //使用Ajax请求--POST-->传递input_string
            let that = this;
            //开始Ajax请求
            axios
            .post(
                that.baseURL + "EquipmentInformation/",
                {
                    input_string: that.input_string
                }
            )
            .then(function(res){
                if(res.data.error_code == 0){
                    
                    //把数据给shebei
                        that.shebei = res.data.data;
                    //获取返回记录的总行数
                        that.total = res.data.total_number*that.limits;
                    //that.getshebei();
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
                //console.log(err);
                that.$message.error("筛选信息失败！");
            })
        },

        // //获取当前页设备数据
        // getpageshebei(){
        //     //清空pageshebei中的数据
        //     this.pageshebei = [];
        //     //获得当前页的数据
        //     for(let i=(this.currentpage -1)*this.pagesize; i< this.total;i++){
        //         //遍历数据添加到pageshebei中
        //         this.pageshebei.push(this.shebei[i]);
        //         //判断是否达到一页的要求
        //         //if (this.pageshebei.length === this.pagesize) break;
        //     }
        // },

        //分页时修改每页的行数
        handleSizeChange(size){
             //修改当前每页数据行数
             this.pagesize = size;
            //this.currentpage = 1;
             //数据重新分页
             this.getshebei();
         },
        //调整当前的页码
        handleCurrentChange(pageNumber){
            //修改当前的页码
            this.currentpage = pageNumber;
            //数据重新分页
            this.getshebei();
        },


        //选择复选框触发操作
        handleSelectionChange(data){
            this.selectshebeis = data;
        },
        //添加设备时打开表单
        addshebei(){
            //修改标题
            this.dialogTitle = "添加设备明细";
            //弹出表单
            this.dialogVisible = true;
        },
        //关闭弹出框的表单
        closeDialogForm(formName){
            //清空数据
            this.shebeiform.id='';
            this.shebeiform.name='';
            this.shebeiform.id_location__name='';
            this.shebeiform.id_location_sn='';
            this.shebeiform.id_ip='';
            this.shebeiform.mac='';
            this.shebeiform.state='';
            this.shebeiform.login='';
            this.shebeiform.link='';
            this.shebeiform.class_field='';
            this.shebeiform.dx='';
            this.shebeiform.dy='';
            this.shebeiform.id_user__name='';
            this.shebeiform.id_plan='';
            this.shebeiform.itimebegin='';
            this.shebeiform.whitelist='';
            this.shebeiform.rem='';
            this.shebeiform.timeupdate='';
            this.shebeiform.idmanager__name='';
            this.shebeiform.portlisten='';
            this.shebeiform.type_field='';
            this.shebeiform.timedelay='';
            this.shebeiform.keycancel='';
            this.shebeiform.keyOk='';
            this.shebeiform.keydel='';
            this.shebeiform.keyf1='';
            this.shebeiform.onall='';
            this.shebeiform.rangeequs='';
            this.shebeiform.listplaces='';
            console.log(this.shebeiform);
            //重置表单的校验
            this.$nextTick(()=>{
                this.$refs[formName].resetFields();
            });
            //关闭
            this.dialogVisible = false;
            this.isView = false;
            this.isEdit = false;
        },
        
        

        //查看设备的明细
        viewshebei(row){
            //修改标题
            this.dialogTitle = "查看设备明细";
            //修改isView变量
            this.isView = true;
            //弹出表单
            this.dialogVisible = true;
            //进行深拷贝
            this.shebeiform = JSON.parse(JSON.stringify(row));
            this.datatrans1();

        },
        //修改设备的信息
        updateshebei(row) {
            //修改标题
            this.dialogTitle = "修改设备明细";
            //修改isEdit变量
            this.isEdit = true;
            //弹出表单
            this.dialogVisible = true;
            //进行深拷贝
            this.shebeiform = JSON.parse(JSON.stringify(row));
            this.datatrans1();
        },
        //提交设备的表单（添加、修改）
        submitshebeiform(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    //校验成功后执行添加或者修改
                    if (this.isEdit){
                        this.shebeiform.id = Number(this.shebeiform.id);
                        this.shebeiform.id_location__name = Number(this.shebeiform.id_location__name);
                        this.shebeiform.id_user__name = Number(this.shebeiform.id_user__name);
                        //this.timeup();
                        this.datatrans2();
                        this.submitupdatashebei();
                    }else{
                        //添加
                        this.shebeiform.id = Number(this.shebeiform.id);
                        this.shebeiform.id_location__name = Number(this.shebeiform.id_location__name);
                        this.shebeiform.id_user__name = Number(this.shebeiform.id_user__name);
                        //this.timeup();
                        this.datatrans2();
                        this.submitaddshebei()
                    }
                alert('submit!');
              } else {
                    console.log('error submit!!');
                    return false;
                }
            });
        },

        //添加到数据库的函数
        submitaddshebei(){
            let that = this;
            //执行Axios请求
            axios
            .put(that.baseURL + 'EquipmentInformation/', that.shebeiform)
            .then(res=>{
                //执行成功
                if(res.data.error_code == 0){//res.data.code == 1
                    // //获取所有设备信息
                    // that.shebei = res.data.data;
                    // //获取记录条数
                    // that.total = res.data.data.length;
                    // //获取分页信息
                    // that.getpageshebei();
                    that.getshebei();
                    //提示
                    that.$message({
                        message:'数据加载成功！',
                        type:'success'
                    });
                    //关闭窗体
                    that.closeDialogForm('shebeiform');
                }else{
                    //失败提示
                    that.$message.error(res.data.message);
                }
            })
            .catch(res=>{
                //执行失败
                console.log(res);
                that.$message.error("后端数据异常！");
            });
        },
        //修改更新到数据库
        submitupdatashebei(){
            let that = this;
            //执行Axios请求
            axios
            .patch(that.baseURL + 'EquipmentInformation/', that.shebeiform)
            .then(res=>{
                //执行成功
                if(res.data.error_code == 0){//res.data.code == 1
                    // //获取所有设备信息
                    // that.shebei = res.data.data;
                    // //获取记录条数
                    // that.total = res.data.data.length;
                    // //获取分页信息
                    // that.getpageshebei();
                    that.getshebei();
                    //提示
                    that.$message({
                        message:'数据修改成功！',
                        type:'success'
                    });
                    //关闭窗体
                    that.closeDialogForm('shebeiform');
                }else{
                    //失败提示
                    that.$message.error(res.data.message);
                }
            })
            .catch(err=>{
                //执行失败
                console.log(err);
                that.$message.error("获取后端数据异常");
            });
        },
        //删除一条设备记录
        deleteshebei(row) {
            //等待确认
            this.$confirm('是否确认删除设备【设备id：' + row.id + '\t地点：' + row.id_location__name + '】信息？',
                '提示', {
                confirmButtonText: '确定删除',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                //确认删除响应事件
                let that = this
                //调用后端接口
                axios
                .delete(that.baseURL + 'EquipmentInformation/',{data:{ids:[{"data_id":row.id}]}})
                .then(res => {
                        if (res.data.error_code == 0){
                            // that.shebei = res.data.data;
                            // //获取记录数
                            // that.total = res.data.data.length;
                            // //分页
                            // that.getpageshebei();
                            that.getshebei();
                            //把数据给shebei
                            //that.shebei = res.data.data;
                            //获取返回记录的总行数
                            //that.total = res.data.total_number*that.limits;
                            //提示
                            that.$message({
                                message: '数据删除成功！',
                                type: 'success'
                            });
                        } else {
                            that.$message.error(res.data.message);
                        }
                    })

            }).catch(() => {
                this.$message({
                    type: 'info',
                    message: '已取消删除'
                });
            });
        },
        //批量删除设备记录
        deleteshebeis() {
            //等待确
          this.$confirm("是否确认批量删除" + this.selectshebeis.length + "个设备信息吗？",
                '提示', {
                confirmButtonText: '确定删除',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                let ids = [];
                for(var i=0;i<this.selectshebeis.length;i++){
                    ids.push({"data_id":this.selectshebeis[i].id});
                }
                //确认删除响应事件
                let that = this
                //调用后端接口
                axios
                .delete(that.baseURL + 'EquipmentInformation/',{data:{
                ids:ids}
                })
                .then(res => {
                        if (res.data.error_code == 0) {
                            that.getshebei();
                            //提示
                            that.$message({
                                message: '数据删除成功！',
                                type: 'success'
                            });
                        } else {
                            that.$message.error(res.data.message);
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
