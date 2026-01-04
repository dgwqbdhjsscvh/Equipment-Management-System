# 运行说明

## 项目结构

```
jnu_lab_system/
├── lab_management/          # 主应用模块
│   ├── templates/          # HTML模板
│   │   ├── user/          # 普通用户页面
│   │   ├── admin/         # 管理员页面
│   │   ├── manager/       # 负责人页面
│   │   ├── base.html      # 基础模板
│   │   └── login.html     # 登录页面
│   ├── migrations/        # 数据库迁移文件
│   ├── views.py          # 视图函数
│   ├── urls.py           # URL路由配置
│   ├── models.py         # 数据模型
│   ├── admin.py          # Django管理后台
│   └── apps.py           # 应用配置
├── jnu_lab_system/        # 项目配置
│   ├── settings.py       # Django设置
│   ├── urls.py           # 项目URL配置
│   ├── wsgi.py           # WSGI配置
│   └── asgi.py           # ASGI配置
├── db.sqlite3            # SQLite数据库文件
├── manage.py             # Django管理脚本
└── requst.md             # 需求文档
```

## 安装和运行

### 环境要求
- Python 3.8 或更高版本

### 安装步骤

1. **克隆或下载项目到本地**
   ```bash
   # 进入文件夹
   cd v0
   ```
2. **创建虚拟环境（推荐）**
   ```bash
   python -m venv venv
   
   # Windows激活虚拟环境
   venv\Scripts\activate
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

4. **数据库初始化**
   ```bash
   python manage.py migrate
   ```

5. **创建超级用户（可选，用于Django管理后台）**
   ```bash
   python manage.py createsuperuser
   ```

### 运行系统

1. **启动开发服务器**
   ```bash
   python manage.py runserver
   ```

2. **访问系统**
   打开浏览器访问：http://127.0.0.1:8000
