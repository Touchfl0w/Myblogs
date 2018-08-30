

1、git log 查询commit(快照)记录

2、git reflog 查询commit命令操作记录；可以查询历史commit id

3、git checkout -- file 使用本地版本库中的文件替换工作区文件，即丢弃工作区的修改

4、git reset HEAD file 将文件从缓存区退回工作区

5、git rm file 删除版本库中的文件；配合git commit才能生效

6、关联远程仓库
```
#远程库的本地别名origin
git remote add origin git@server-name:path/repo-name.git
#第一次推送本地库内容时：-u关联本地master分支与远程master分支
git push -u origin master
#这里的master指代本地master分支，远程master分支已关联，可简化
git push  origin master
```
7、分支

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-8-10/57480087.jpg)

8、commit版本回退

git reset --hard 【commitID】


9、合并分支

+ 普通模式

git merge 【subbranch】
合并自分支到当前分支

+ no fast forward模式，可以查看到合并记录，推荐！

git merge --no-ff -m "merge with no-ff" 【subbranch】

> 如遇冲突，将冲突文件修改一致，然后提交，即完成合并

> 所谓合并分支，是按较长的分支来合并，比如master比subbranch长，合并分支后subbranch和master一样长。

> 只要两个分支中不同时修改同一个文件，而各自分支又有不同的修改对象，合并就不会有问题

10、查看分支合并线图

git log --graph --pretty=oneline --abbrev-commit

11、删除分支

git branch -d 【subbranch】


12、分支合理使用思路

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-8-16/47437315.jpg)

13、git stash 

保存工作区改动，使用后，工作区清空；可以去新建分支，修改bug

14、git stash list 

展示所有保存的stash信息

15、git stash apply <stashID>恢复工作现场

16、git stash pop :恢复现场，并删除stash记录

17、Feature分支

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-8-16/38628556.jpg)


18、

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-8-16/18189760.jpg)

19、创建删除远程分支

git push origin 【local branch】：【remote branch】

不存在的远程分支会在github被创建；该命令可以在本地任意分支上被执行
> 前提是先创建本地分支

git push origin :【remote branch】

删除远程已存在的分支！该命令可以在本地任意分支上被执行


20、创建本地分支与远程分支的对应关系

git branch --set-upstream origin/【remote branch】 【local branch】  

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-8-19/38849734.jpg)

> 截图中的创建关联命令有误

21、给commit打标签

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-8-19/9999402.jpg)

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-8-19/66300822.jpg)

22、gitignore

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-8-19/42890402.jpg)

> 放在git工作区即可，gitignore文件使用github自动生成即可。https://github.com/github/gitignore/blob/master/Python.gitignore

23、操作简化：重命名

```
git config --global alias.ck checkout
git config --global alias.st status
git config --global alias.cm commit
git config --global alias.br branch
git config --global alias.unstage 'reset HEAD'
git config --global alias.last 'log -1'
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```
***
##### 总结

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-8-19/34953763.jpg)

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-8-19/52528906.jpg)
##### 参考

https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000