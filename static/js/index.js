var shebei = `
<div id="app2">
<el-form v-model="vm.shebeiform" :inline="true" style="margin-top:20px;">
<el-row>
    <el-col :span="12">
        <el-form-item label="请输入筛选条件：">
            <el-input v-model="vm.inputStr" placeholder="输入筛选条件" style="width: 420px;">
            </el-input>
        </el-form-item>
    </el-col>
    <el-col :span="8" style="text-align: right;padding-right:10px;">
        <el-button-group>
            <el-button type="primary" icon="el-icon-search" @click="vm.queryshebei()">筛选</el-button>
            <el-button type="primary" icon="el-icon-circle-plus-outline" @click="vm.addshebei()">添加</el-button>
        </el-button-group>
    </el-col>
</el-row>
</el-form>
    <el-table :data="vm.pageshebei" border style="width: 100%" size="mini" @selection-change="vm.handleSelectionChange()">
        <el-table-column type="selection">
        </el-table-column>
        <el-table-column type="index" label="序号" width="60" align="center">
        </el-table-column>
        <el-table-column prop="ipc_id" label="设备id" width="120" align="center">
        </el-table-column>
        <el-table-column prop="location" label="地点" width="140" align="center">
        </el-table-column>
        <el-table-column label="操作" align="center">
            <template slot-scope="scope">
                <el-button type="success" icon="el-icon-more" size="mini" circle @click="vm.viewshebei(scope.row)"></el-button>
                <el-button type="primary" icon="el-icon-edit" size="mini" circle @click="vm.updateshebei(scope.row)"></el-button>
                <el-button type="danger" icon="el-icon-delete" size="mini" circle @click="vm.deleteshebei(scope.row)"></el-button>
            </template>
        </el-table-column>
    </el-table>
    <el-row style="margin-top: 10px;">
        <el-col :span="8" style="text-align: left">
            <el-button type="primary" icon="el-icon-delete" size="mini" @click="vm.deleteshebeis()">批量删除</el-button>
        </el-col>
        <el-col :span="16" style="text-align: right">
            <el-pagination
                @size-change="vm.handleSizeChange"
                @current-change="vm.handleCurrentChange"
                :current-page="vm.currentpage"
                :page-sizes="[5, 10, 50, 100]"
                :page-size="vm.pagesize"
                layout="total, sizes, prev, pager, next, jumper"
                :total="vm.total">
            </el-pagination>
        </el-col>
    </el-row>
    <el-dialog :title="vm.dialogTitle" :visible.sync="vm.dialogVisible" width="50%"  @close="vm.closeDialogForm()">
        <el-form :model="vm.shebeiform" :rules="vm.rules" ref="vm.shebeiform" :inline=true style="margin-left:20px;" label-width="110px" labei-position="right" size="mini">
            <el-form-item label="设备id" prop="ipc_id">
                <el-input v-model="vm.shebeiform.ipc_id" :disabled="vm.isEdit || vm.isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="地点" prop="location">
                <el-input v-model="vm.shebeiform.location" :disabled="vm.isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="登录用户名称" prop="user_name">
                <el-input v-model="vm.shebeiform.user_name" :disabled="vm.isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="登录用户部门" prop="department">
                <el-input v-model="vm.shebeiform.department" :disabled="vm.isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="上次登录时间">
                <el-input v-model="vm.shebeiform.last_login_time" :disabled="vm.isView" suffix-icon="el-icon-edit"></el-input>
            </el-form-item>
            <el-form-item label="设备状态" prop="active_status">
                <el-select v-model="vm.shebeiform.active_status" :disabled="vm.isView" placeholder="请选择设备状态">
                    <el-option labei="在线" value="在线"></el-option>
                    <el-option labei="离线" value="离线"></el-option>
                </el-select>
            </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button type="primary" size="mini" v-show="!vm.isView" @click="vm.submitshebeiform()">确定</el-button>
            <el-button type="info" size="mini" @click="vm.closeDialogForm()">取消</el-button>
        </span>
    </el-dialog>
</div>
             `




var yonghu = `
<div id="app2">

<el-form :inline="true" style="margin-top:20px;">
<el-row>
    <el-col :span="12">
        <el-form-item label="请输入筛选条件：">
            <el-input placeholder="输入筛选条件" style="width: 420px;">
            </el-input>
        </el-form-item>
    </el-col>
    <el-col :span="8" style="text-align: right;padding-right:10px;">
        <el-button-group>
            <el-button type="primary" icon="el-icon-search">筛选</el-button>
            <el-button type="primary" icon="el-icon-circle-plus-outline">添加</el-button>
        </el-button-group>
    </el-col>
</el-row>
</el-form>
    <el-table :data="vm.yonghu" border style="width: 100%" size="mini">
        <el-table-column type="selection">
        </el-table-column>
        <el-table-column type="index" label="序号" width="60" align="center">
        </el-table-column>
        <el-table-column prop="name" label="姓名" width="80" align="center">
        </el-table-column>
        <el-table-column prop="sno" label="学号/教工号" width="120" align="center">
        </el-table-column>
        <el-table-column prop="department" label="部门" width="120" align="center">
        </el-table-column>
        <el-table-column label="操作" align="center">
            <el-button type="success" icon="el-icon-more" size="mini" circle></el-button>
            <el-button type="primary" icon="el-icon-edit" size="mini" circle></el-button>
            <el-button type="danger" icon="el-icon-delete" size="mini" circle></el-button>
        </el-table-column>
    </el-table>
    <el-row style="margin-top: 10px;">
        <el-col :span="8" style="text-align: left">
            <el-button type="primary" icon="el-icon-delete" size="mini">批量删除</el-button>
        </el-col>
        <el-col :span="16" style="text-align: right">
            <el-pagination
                :current-page="vm.currentpage"
                :page-sizes="[5, 10, 50, 100]"
                :page-size="vm.pagesize"
                layout="total, sizes, prev, pager, next, jumper"
                :total="vm.total">
            </el-pagination>
        </el-col>
    </el-row>
</div>
             `;

var kebiao = `
<div id="app2">

<el-form :inline="true" style="margin-top:20px;">
<el-row>
    <el-col :span="12">
        <el-form-item label="请输入筛选条件：">
            <el-input placeholder="输入筛选条件" style="width: 420px;">
            </el-input>
        </el-form-item>
    </el-col>
    <el-col :span="8" style="text-align: right;padding-right:10px;">
        <el-button-group>
            <el-button type="primary" icon="el-icon-search">筛选</el-button>
            <el-button type="primary" icon="el-icon-circle-plus-outline">添加</el-button>
        </el-button-group>
    </el-col>
</el-row>
</el-form>
    <el-table :data="vm.kebiao" border style="width: 100%" size="mini">
        <el-table-column type="selection">
        </el-table-column>
        <el-table-column type="index" label="序号" width="60" align="center">
        </el-table-column>
        <el-table-column prop="name" label="课程名称" width="140" align="center">
        </el-table-column>
        <el-table-column prop="time" label="时间" width="120" align="center">
        </el-table-column>
        <el-table-column prop="place" label="地点" width="120" align="center">
        </el-table-column>
        <el-table-column prop="teacher" label="教师" width="120" align="center">
        </el-table-column>
        <el-table-column prop="people" label="课程人数" width="120" align="center">
        </el-table-column>
        <el-table-column label="操作" align="center">
            <el-button type="success" icon="el-icon-more" size="mini" circle></el-button>
            <el-button type="primary" icon="el-icon-edit" size="mini" circle></el-button>
            <el-button type="danger" icon="el-icon-delete" size="mini" circle></el-button>
        </el-table-column>
    </el-table>
    <el-row style="margin-top: 10px;">
        <el-col :span="8" style="text-align: left">
            <el-button type="primary" icon="el-icon-delete" size="mini">批量删除</el-button>
        </el-col>
        <el-col :span="16" style="text-align: right">
            <el-pagination
                :current-page="vm.currentpage"
                :page-sizes="[5, 10, 50, 100]"
                :page-size="vm.pagesize"
                layout="total, sizes, prev, pager, next, jumper"
                :total="vm.total">
            </el-pagination>
        </el-col>
    </el-row>
</div>
             `;

var xinxi = `
<div id="app2">

<el-form :inline="true" style="margin-top:20px;">
<el-row>
    <el-col :span="12">
        <el-form-item label="请输入筛选条件：">
            <el-input placeholder="输入筛选条件" style="width: 420px;">
            </el-input>
        </el-form-item>
    </el-col>
    <el-col :span="8" style="text-align: right;padding-right:10px;">
        <el-button-group>
            <el-button type="primary" icon="el-icon-search">筛选</el-button>
            <el-button type="primary" icon="el-icon-circle-plus-outline">添加</el-button>
        </el-button-group>
    </el-col>
</el-row>
</el-form>
    <el-table :data="vm.student" border style="width: 100%" size="mini">
        <el-table-column type="selection">
        </el-table-column>
        <el-table-column type="index" label="序号" width="60" align="center">
        </el-table-column>
        <el-table-column prop="name" label="姓名" width="80" align="center">
        </el-table-column>
        <el-table-column prop="sno" label="学号" width="120" align="center">
        </el-table-column>
        <el-table-column prop="profession" label="专业" width="120" align="center">
        </el-table-column>
        <el-table-column label="操作" align="center">
            <el-button type="success" icon="el-icon-check" size="mini" circle></el-button>
            <el-button type="primary" icon="el-icon-edit" size="mini" circle></el-button>
            <el-button type="danger" icon="el-icon-delete" size="mini" circle></el-button>
        </el-table-column>
    </el-table>
    <el-row style="margin-top: 10px;">
        <el-col :span="8" style="text-align: left">
            <el-button type="primary" icon="el-icon-delete" size="mini">批量删除</el-button>
        </el-col>
        <el-col :span="16" style="text-align: right">
            <el-pagination
                :current-page="vm.currentpage"
                :page-sizes="[5, 10, 50, 100]"
                :page-size="vm.pagesize"
                layout="total, sizes, prev, pager, next, jumper"
                :total="vm.total">
            </el-pagination>
        </el-col>
    </el-row>
</div>
            `;

var vm = new Vue({
    el: '#app2',
    router:new VueRouter({
      routes:[
        //{path:'/',redirect:'/shebei'}, // 这个表示会默认渲染shebei
        {path:'/shebei',component:{template: shebei}},
        {path:'/yonghu',component:{template: yonghu}},
        {path:'/kebiao',component:{template: kebiao}},
        {path:'/xinxi',component:{template: xinxi}}
      ]
    }),
    data(){
        // 校验设备id是否存在
        const rulesID = (rule,value,callback) =>{
            //使用axios进行校验
            axios
            .post(
                this.baseURL + 'ipc_id/check/',
                {
                    ipc_id:value,
                }
            )
            .then((res)=>{
                //请求成功
                if (res.data.code === 1){
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
        baseURL:"http://10.20.7.53:85/polls/",
        shebei:[],//所有的设备信息
        pageshebei:[],//分页后当前页的设备信息
        inputStr:'', //输入的筛选条件
        //分页的相关参数
        total:0, //数据的总行数
        currentpage:1, //当前的所在页
        pagesize:10,//每行显示多少页
        dialogVisible:false,
        shebeiform:{
            ipc_id:'',
            location:'',
            user_name:'',
            department:'',
            last_login_time:'',
            active_status:'',
        },
        rules:{
            ipc_id:[
                    {required:true,message:'设备id不能为空',trigger:'blur'},
                    {validator:rulesID,triggler:'blur'},
            ],
            location:[
                    {required:true,message:'地点不能为空',trigger:'blur'},

            ],
            user_name:[
                    {required:true,message:'用户姓名不能为空',trigger:'blur'},
            ],
            department:[
                    {required:true,message:'用户部门不能为空',trigger:'blur'},
            ],
            active_status:[
                    {required:true,message:'设备状态不能为空',trigger:'blur'},
            ]
        },

        dialogTitle: "", //弹出框的标题

        isView: false, //标识是否是查看
        isEdit: false, //标识是否是修改

        selectshebeis: [],//选择复选时把选择记录存在这里

        }
    },
    mounted(){
        //自动加载数据
        this.getshebei();
    },
     methods:{
        //获取所有设备信息
        getshebei:function(){
            //记录this的地址
            let that = this
            //使用Axios实现Ajax请求
            axios
            .get(that.baseURL + "shebei/")
            .then(function(res){
                //请求成功后执行的函数
                console.log(res);
                if(res.data.code ===1 ){
                    //把数据给shebei
                    that.shebei = res.data.data;
                    //获取返回记录的总行数
                    that.total = res.data.data.length;
                    //获取当前页的数据
                    that.getpageshebei();
                    //数据加载成功提示
                    that.$message({
                        message:'数据加载成功！',
                        type:'success'
                    });
                }else {
                    //数据加载失败提示
                    that.$message.error('获取数据出现异常');
                }
            })
            .catch(function(err){
                //请求失败后执行的函数
                console.log(err);
            })
        },

        //获取当前页设备数据
        getpageshebei(){
            //清空pageshebei中的数据
            this.pageshebei = [];
            //获得当前页的数据
            for(let i=(this.currentpage -1)*this.pagesize; i< this.total;i++){
                //遍历数据添加到pageshebei中
                this.pageshebei.push(this.shebei[i]);
                //判断是否达到一页的要求
                if (this.pageshebei.length === this.pagesize) break;
            }
        },
        //实现当前页的设备信息查询
        queryshebei(){
            //使用Ajax请求--POST-->传递InputStr
            let that = this;
            //开始Ajax请求
            axios                                                                                                                 //Axios请求
            .post(
                that.baseURL + "shebei/shaixuan/",
                {
                    inputStr: that.inputStr
                }
            )
            .then(function(res){
                if(res.data.code === 1){
                    //把数据给shebei
                    that.shebei = res.data.data;
                    //获取返回记录的总行数
                    that.total = res.data.data.length;
                    //获取当前页的数据
                    that.getpageshebei();
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
            this.getpageshebei();
        },
        //调整当前的页码
        handleCurrentChange(pageNumber){
            //修改当前的页码
            this.currentpage = pageNumber;
            //数据重新分页
            this.getpageshebei();
        },
        //选择复选框触发操作
        handleSelectionChange(){
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
            //重置表单的校验
            this.$refs[formName].resetFields();
            //清空数据
            this.shebeiform.ipc_id ="";
            this.shebeiform.location ="";
            this.shebeiform.user_name ="";
            this.shebeiform.department ="";
            this.shebeiform.last_login_time ="";
            this.shebeiform.active_status ="";
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
            this.shebeiform = JSON.parse(JSON.stringify(row))

        },
        //修改设备的信息
        updateshebei(row) {
            //修改标题
            this.dialogTitle = "修改设备明细";
            //修改isEdit变量
            this.isEdit = true;
            //弹出表单
            this.dialogVisible = true;
        },
        //提交设备的表单（添加、修改）
        submitshebeiform(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                  alert('submit!');
                } else {
                  console.log('error submit!!');
                  return false;
                }
              });
        },
        //删除一条设备记录
        deleteshebei(row) {
            //等待确认
            this.$confirm('是否确认删除设备信息【设备id：' + row.name + '\t地点：' + row.place + '】信息？',
                '提示', {
                confirmButtonText: '确定删除',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                //确认删除响应事件
                let that = this
                //调用后端接口
                axios.post() //##################后端URL########################                                                     //Axios
                    .then(res => {
                        if (res.data.code === 1) { //与前段相同，code为假定参数，由后端决定
                            //获取所有设备信息
                            that.shebei = res.data.data; //与前段相同，后一个data为假定参数，由后端决定
                            //获取记录数
                            that.total = res.data.data.length; //与前段相同，后一个data为假定参数，由后端决定
                            //分页
                            that.getpageshebei();
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
        //批量删除设备记录
        deleteshebeis() {
            //等待确认
            this.$confirm("是否确认批量删除" + this.selectshebeis.length + "个设备信息吗？",
                '提示', {
                confirmButtonText: '确定删除',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                //确认删除响应事件
                let that = this
                //调用后端接口
                axios.post() ////##################后端URL########################
                    .then(res => {
                        if (res.data.code === 1) {
                            //获取所有设备信息
                            that.shebeis = res.data.data;  //与前段相同，后一个data为假定参数，由后端决定
                            //获取记录数
                            that.total = res.data.data.length; //与前段相同，后一个data为假定参数，由后端决定
                            //分页
                            that.getpageshebei();
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
})
