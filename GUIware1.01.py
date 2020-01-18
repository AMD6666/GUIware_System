import os
import wx
a='Laoliu'
'''
GUIware 2020 Professional

编辑：刘嘉昆

调试：刘嘉昆

版权所有：刘嘉昆
'''
def white():
    class WSOD(wx.Frame):
        def __init__(self,parent,id):
            wx.Frame.__init__(self,parent=None,title='White Screen Of Death',size=(1366,768))
            panel=wx.Panel(self)
            tip=wx.StaticText(panel,label='Close the Python.\n\nFOR_SOME_RESSION_IMPORTANT_TASK_STOP 因某些原因，重要进程被终止\n\nYour computer ran into a problem and it needs to restart. You can restart.\nIt might be code error or elsewhat.\n0x00007C          GUIWARE_FAILED\n\nnotre computer a rencontré un problème et il a besoin de redémarrer. Vous pouvez redémarrer GUIWARE_FAILED.\n\nパソコンが不具合を起こしました。再起動が必要です。再開。残念だけどコード違いや違いじゃないか。\n\n你的电脑出了问题，需要重新启动。你可以重启。\n可能是代码错误或其他什么。\n0x00007C GUIWARE_FAILED',pos=(20,20))
            sad=wx.StaticText(panel,label=':(',pos=(250,450))
            Font=wx.Font(18,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
            SFont=wx.Font(100,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
            tip.SetFont(Font)
            sad.SetFont(SFont)
    if __name__=='__main__':
        app=wx.App()
        WSOD=WSOD(parent=None,id=-1)
        WSOD.Show()
        app.MainLoop()

try:
    import time
    class Taskmgr(wx.Frame):
        def __init__(self,parent,id):
            wx.Frame.__init__(self,parent=None,title='GUI任务管理器',pos=(-1,-1),size=(600,300))
            panel=wx.Panel(self)
            TIPTIP=wx.StaticText(panel,label='请选择要终止的进程',pos=(10,10))
            self.bt_csrss=wx.Button(panel,label='csrss.exe',pos=(0,60))
            self.bt_csrss.Bind(wx.EVT_BUTTON,self.csrss)
            self.bt_GUIinit=wx.Button(panel,label='GUIinit.exe',pos=(0,110))
            self.bt_GUIinit.Bind(wx.EVT_BUTTON,self.GUIinit)
            self.bt_Taskmgr=wx.Button(panel,label='Taskmgr.exe',pos=(0,160))
            self.bt_Taskmgr.Bind(wx.EVT_BUTTON,self.Taskmgr)
        def csrss(self,event):
            time.sleep(5)
            self.Close(True)
            white()
        def GUIinit(self,event):
            time.sleep(5)
            self.Close(True)
            white()
        def Taskmgr(self,event):
            self.Close(True)
    
    class File(wx.Frame):
        def __init__(self,parent,id):
            wx.Frame.__init__(self,parent=None,title='D:/文件存储区/',pos=(-1,-1),size=(600,400))
            panel=wx.Panel(self)
            RIP=wx.StaticText(panel,label='该文件夹为空',pos=(0,0))
        
    class Update(wx.Frame):
        def __init__(self,parent,id):
            wx.Frame.__init__(self,parent=None,title='更新内容.txt',pos=(-1,-1),size=(600,400))
            panel=wx.Panel(self)
            TXT=wx.StaticText(panel,label='更新了加载界面，还有计算机CD，存储文件功能删除，敬请期待系统升级！\n新增命令行“框架助手”及任务管理器。',pos=(0,0))

    class D(wx.Frame):
        def __init__(self,parent,id):
            wx.Frame.__init__(self,parent=None,title='D:/',pos=(-1,-1),size=(600,400))
            panel=wx.Panel(self)
            self.bt_f=wx.Button(panel,label='文件存储区',pos=(0,0))
            self.bt_f.Bind(wx.EVT_BUTTON,self.file)
        def file(self,event):
            if __name__=='__main__':
                app=wx.App()
                FFF=File(parent=None,id=-1)
                FFF.Show()
                app.MainLoop()
    
    class C(wx.Frame):
        '''
        提示：

        禁止修改C盘

        禁止修改任何代码
        '''
        def __init__(self,parent,id):
            wx.Frame.__init__(self,parent=None,title='C:/',pos=(-1,-1),size=(600,400))
            panel=wx.Panel(self)
            C_tip=wx.StaticText(panel,label='C盘是系统盘，GUIware禁用了C盘修改功能。',pos=(0,0))
            c1=wx.StaticText(panel,label='GUIhelper.exe                1KB\nGUIinit.exe                2KB\nnotepad.exe                2KB\nexplorer.exe                1KB\ncsrss.exe                   1.5KB\nsystem.dll                  0.5KB\nsystem.exe                  2KB\nsoftware.dll                1KB',pos=(0,25))
    
    class Explorer(wx.Frame):
        '''
        计算机界面

        有C盘和D盘

        C盘不可修改
        '''
        def __init__(self,parent,id):
            wx.Frame.__init__(self,parent=None,title='计算机',pos=(-1,-1),size=(640,480))
            panel=wx.Panel(self)
            self.bt_c=wx.Button(panel,label='本地磁盘(C:/)',pos=(0,0))
            self.bt_c.Bind(wx.EVT_BUTTON,self.OnC)
            self.bt_d=wx.Button(panel,label='本地磁盘(D:/)',pos=(100,0))
            self.bt_d.Bind(wx.EVT_BUTTON,self.OnD)
        def OnC(self,event):
            time.sleep(1)
            if __name__=='__main__':
                app=wx.App()
                CCC=C(parent=None,id=-1)
                CCC.Show()
                app.MainLoop()
        def OnD(self,event):
            time.sleep(1)
            if __name__=='__main__':
                app=wx.App()
                DDD=D(parent=None,id=-1)
                DDD.Show()
                app.MainLoop()
            
    class MyFrame(wx.Frame):
        '''
        登录界面

        保证不直接进入桌面
        '''
        def __init__(self,parent,id):
            wx.Frame.__init__(self,parent=None,title='GUIWare 1.01 Professional',size=(1366,768))
            panel=wx.Panel(self)
            title=wx.StaticText(panel,label='登录到GUIware',pos=(683,384))
            logo=wx.StaticText(panel,label='GUIware 1.01 Professional',pos=(200,200))
            Font=wx.Font(40,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
            logo.SetFont(Font)
            near=wx.StaticText(panel,label='用户名：Administrator',pos=(683,430))
            self.password=wx.TextCtrl(panel,pos=(683,450),style=wx.TE_PASSWORD)
            self.bt_login=wx.Button(panel,label='登录',pos=(636,485))
            self.bt_login.Bind(wx.EVT_BUTTON,self.Login)
            self.bt_exit=wx.Button(panel,label='关机',pos=(766,485))
            self.bt_exit.Bind(wx.EVT_BUTTON,self.OnclickExit)
        def Login(self,event):
            pw=self.password.GetValue()
            if pw==a:
                time.sleep(2)
                if __name__=='__main__':
                    app=wx.App()
                    desk=Desktop(parent=None,id=-1)
                    desk.Show()
                    self.Close(True)
                    app.MainLoop()
            else:
                wx.MessageBox('密码错误')
            
        def OnclickExit(self,event):
            time.sleep(1.5)
            self.password.SetValue('')
            quit()
            
    class Desktop(wx.Frame):
        '''
        Explorer.exe的代码扩展

        请勿修改

        桌面代码
        '''
        def __init__(self,parent,id):
            wx.Frame.__init__(self,parent=None,title='GUIware Desktop',size=(1366,768))
            panel=wx.Panel(self)
            logo=wx.StaticText(panel,label='GUIware 1.01 Professional',pos=(100,100))
            self.bt_exit=wx.Button(panel,label='关机',pos=(0,0))
            self.bt_exit.Bind(wx.EVT_BUTTON,self.Clickexit)
            self.bt_logoff=wx.Button(panel,label='注销',pos=(0,50))
            self.bt_logoff.Bind(wx.EVT_BUTTON,self.Logoff)
            self.bt_explorer=wx.Button(panel,label='计算机',pos=(0,100))
            self.bt_explorer.Bind(wx.EVT_BUTTON,self.Onexplorer)
            self.bt_update=wx.Button(panel,label='更新内容.txt',pos=(0,150))
            self.bt_update.Bind(wx.EVT_BUTTON,self.UpdateTxt)
            self.bt_sub=wx.Button(panel,label='框架助手',pos=(0,200))
            self.bt_sub.Bind(wx.EVT_BUTTON,self.GUIer)
            self.bt_mgr=wx.Button(panel,label='任务管理器',pos=(0,250))
            self.bt_mgr.Bind(wx.EVT_BUTTON,self.mgr)
        def Clickexit(self,event):
            time.sleep(3)
            quit()
        def Onexplorer(self,event):
            time.sleep(1)
            if __name__=='__main__':
                app=wx.App()
                explorer=Explorer(parent=None,id=-1)
                explorer.Show()
                app.MainLoop()
        def UpdateTxt(self,event):
            time.sleep(0.5)
            if __name__=='__main__':
                app=wx.App()
                up=Update(parent=None,id=-1)
                up.Show()
                app.MainLoop()
        def Logoff(self,event):
            if __name__=='__main__':
                app=wx.App()
                time.sleep(1)
                self.Close(True)
                ADD=MyFrame(parent=None,id=-1)
                ADD.Show()
                app.MainLoop()
        def GUIer(self,event):
            wx.MessageBox('请转至GUIware命令行以启动框架助手,类似于"Python"的就是命令行。')
            os.system('cls')
            print('ThirdBlood GUIware 2020 Professional <TB>\n版权所有TB GUIware 2020 框架助手。')
            while True:
                cmd=input(r'C:\>')
                if cmd=='exit':
                    wx.MessageBox('请换回桌面')
                    break
                elif cmd=='help':
                    print('exit===============退出命令行')
                    print('help===============请求命令帮助')
                    print('version============查看GUIware版本')
                    print('dir================查看GUIware所有文件')
                    print('kill===============输入后换行有参数，输入要杀掉的进程。输入miss解除。')
                    print('logoff=============注销')
                    print('shutdown===========关机')
                elif cmd=='version':
                    print('GUIware版本2020 Professional专业版 正式版本1.01')
                elif cmd=='dir':
                    print('C:')
                    print(r'C:\GUIhelper.exe')
                    print(r'C:\GUIinit.exe')
                    print(r'C:\notepad.exe')
                    print(r'C:\explorer.exe')
                    print(r'C:\csrss.exe')
                    print(r'C:\system.exe')
                    print(r'C:\system.dll')
                    print('D:')
                    print(r'D:\文件存储区')
                elif cmd=='kill':
                    print('csrss.exe')
                    print('GUIinit.exe')
                    kill=input('kill>')
                    if kill=='csrss.exe' or kill=='GUIinit.exe':
                        time.sleep(5)
                        self.Close(True)
                        white()
                    elif kill=='miss':
                        pass
                elif cmd=='logoff':
                    if __name__=='__main__':
                        app=wx.App()
                        ADD=MyFrame(parent=None,id=-1)
                        time.sleep(1)
                        self.Close(True)
                        ADD.Show()
                        app.MainLoop()
                elif cmd=='shutdown':
                    time.sleep(4)
                    quit()
                elif cmd=='':
                    pass
                else:
                    print('错误的命令')
        def mgr(self,event):
            if __name__=='__main__':
                app=wx.App()
                mgr=Taskmgr(parent=None,id=-1)
                mgr.Show()
                app.MainLoop()
                
    if __name__=='__main__':
        #初始化GUIware
        #然后马上启动
        print('程序初始化……')
        for i in range(2):
            time.sleep(0.2)
            os.system('cls')
            time.sleep(0.2)
        time.sleep(0.8)
        z=0
        for i in range(4):
            z+=1
            y=z*25
            print('正在启动GUIware',y,'%',z*'|')
            time.sleep(1)
            os.system('cls')
        print('请稍候……')
        time.sleep(1)
        app=wx.App()
        Frame=MyFrame(parent=None,id=-1)
        Frame.Show()
        app.MainLoop()
except:
    #白屏死机代码，禁止删除，否则将导致编译器崩溃，使GUIware崩溃
    time.sleep(5)
    white()
