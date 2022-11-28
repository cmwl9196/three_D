from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
    def __init__(self):
        super(MyApp, self).__init__()

        # 加载场景模型（场景树）
        self.scene = self.loader.loadModel("models/environment")
        # 将render设为场景模型的父节点
        self.scene.reparentTo(self.render)

        # 改变场景大小，并设置镜头初始位置
        self.scene.setScale(0.25, 0.25,0.25)
        self.scene.setPos(-8, 42, 0)

app = MyApp()
app.run()