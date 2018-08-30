#### 一、问题描述
flask-migrate插件是对Alembic的简单封装，当程序使用SQLite数据库作为backend的时候，使用 flask migrate命令生成自动迁移脚本，使用flask upgrade命令进行数据库更新，会出现以下问题：

1、op.alter_column、op.alter_table会报错，因为SQlite不支持替换alter column等操作。

2、对于column的一些constraint,比如：unique、foreignkey，这些操作自动脚本生成的时候无法自动探测，必须手动添加。

3、报错：ValueError: Constraint must have a name

类似下面
```
Traceback (most recent call last):
  File "/home/openlab/flasky/venv/bin/flask", line 11, in <module>
    sys.exit(main())
  File "/home/openlab/flasky/venv/lib/python3.6/site-packages/flask/cli.py", line 894, in main
    cli.main(args=args, prog_name=name)
  File "/home/openlab/flasky/venv/lib/python3.6/site-packages/flask/cli.py", line 557, in main
    return super(FlaskGroup, self).main(*args, **kwargs)
  File "/home/openlab/flasky/venv/lib/python3.6/site-packages/click/core.py", line 697, in main
    rv = self.invoke(ctx)
  File "/home/openlab/flasky/venv/lib/python3.6/site-packages/click/core.py", line 1066, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/home/openlab/flasky/venv/lib/python3.6/site-packages/click/core.py", line 1066, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/home/openlab/flasky/venv/lib/python3.6/site-packages/click/core.py", line 895, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/home/openlab/flasky/venv/lib/python3.6/site-packages/click/core.py", line 535, in invoke
    return callback(*args, **kwargs)
  File "/home/openlab/flasky/venv/lib/python3.6/site-packages/click/decorators.py", line 17, in new_func
    return f(get_current_context(), *args, **kwargs)
  File "/home/openlab/flasky/venv/lib/python3.6/site-packages/flask/cli.py", line 412, in decorator
    return __ctx.invoke(f, *args, **kwargs)
  File "/home/openlab/flasky/venv/lib/python3.6/site-packages/click/core.py", line 535, in invoke
    return callback(*args, **kwargs)
  File "/home/openlab/flasky/venv/lib/python3.6/site-packages/flask_migrate/cli.py", line 134, in upgrade
    _upgrade(directory, revision, sql, tag, x_arg)
  File "/home/openlab/flasky/venv/lib/python3.6/site-packages/flask_migrate/__init__.py", line 95, in wrapped
    f(*args, **kwargs)
  File "/home/openlab/flasky/venv/lib/python3.6/site-packages/flask_migrate/__init__.py", line 280, in upgrade
    command.upgrade(config, revision, sql=sql, tag=tag)
  File "/home/openlab/flasky/venv/lib/python3.6/site-packages/alembic/command.py", line 254, in upgrade
    script.run_env()
  File "/home/openlab/flasky/venv/lib/python3.6/site-packages/alembic/script/base.py", line 427, in run_env
    util.load_python_file(self.dir, 'env.py')
  File "/home/openlab/flasky/venv/lib/python3.6/site-packages/alembic/util/pyfiles.py", line 81, in load_python_file
    module = load_module_py(module_id, path)
  File "/home/openlab/flasky/venv/lib/python3.6/site-packages/alembic/util/compat.py", line 82, in load_module_py
    spec.loader.exec_module(module)
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "migrations/env.py", line 88, in <module>
    run_migrations_online()
  File "migrations/env.py", line 81, in run_migrations_online
    context.run_migrations()
  File "<string>", line 8, in run_migrations
  File "/home/openlab/flasky/venv/lib/python3.6/site-packages/alembic/runtime/environment.py", line 836, in run_migrations
    self.get_context().run_migrations(**kw)
  File "/home/openlab/flasky/venv/lib/python3.6/site-packages/alembic/runtime/migration.py", line 330, in run_migrations
    step.migration_fn(**kw)
  File "/home/openlab/flasky/flasky/migrations/versions/bb9a3eb8a5fb_second_migrate.py", line 30, in upgrade
    batch_op.create_unique_constraint(None, ['name'])
  File "/usr/lib/python3.6/contextlib.py", line 88, in __exit__
    next(self.gen)
  File "/home/openlab/flasky/venv/lib/python3.6/site-packages/alembic/operations/base.py", line 300, in batch_alter_table
    impl.flush()
  File "/home/openlab/flasky/venv/lib/python3.6/site-packages/alembic/operations/batch.py", line 76, in flush
    fn(*arg, **kw)
  File "/home/openlab/flasky/venv/lib/python3.6/site-packages/alembic/operations/batch.py", line 343, in add_constraint
    raise ValueError("Constraint must have a name")
ValueError: Constraint must have a name
```
#### 二、解决方案

##### 步骤1：新增插件flask-migrate以及flask_sqlalchemy的初始化实参

```
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate

###初始化插件
#定义命名惯例，不需要改
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
#初始化db,将命名惯例naming_convention传给SQL_Alchemy,解决“ValueError: Constraint must have a name"的问题
db = SQLAlchemy(app=app,metadata=MetaData(naming_convention=naming_convention))
#使用batch操作替换普通操作，因为普通操作不支持表名，列名的改变！
migrate = Migrate(app,db,render_as_batch=True)
```
> 当然，前提是安装了flask-migrate；工厂函数初始化的方式亦然；

##### 步骤2：生成自动化迁移脚本
```
>> flask db init
>> flask db migrate -m 'first migrate'
```
##### 步骤3：检查生成的脚本（./migrations/versions/XXXX.py)

```
def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name2', sa.String(length=64), nullable=True))
        batch_op.create_unique_constraint(batch_op.f('uq_roles_name'), ['name'])
        batch_op.create_unique_constraint(batch_op.f('uq_roles_name1'), ['name1'])
        batch_op.create_unique_constraint(batch_op.f('uq_roles_name2'), ['name2'])
        batch_op.drop_constraint('uq_roles_id', type_='unique')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_users_name555'), ['name555'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_users_name555'), type_='unique')

    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.create_unique_constraint('uq_roles_id', ['name1'])
        batch_op.drop_constraint(batch_op.f('uq_roles_name2'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_roles_name1'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_roles_name'), type_='unique')
        batch_op.drop_column('name2')
```

> 1. 自动生成的脚本可能有错，要人工检查。


> 2. 'uq_roles_id'就是按照naming_convention生成的constraint的name,之前该位置的值为None,这是报错 Constraint must have a name的关键。

##### 步骤4：执行更新操作

```
>> flask db upgrade
```

#### 三、参考链接

https://stackoverflow.com/questions/45527323/flask-sqlalchemy-upgrade-failing-after-updating-models-need-an-explanation-on-h

http://alembic.zzzcomputing.com/en/latest/ops.html#alembic.operations.Operations.create_foreign_key.params.name

http://alembic.zzzcomputing.com/en/latest/batch.html
