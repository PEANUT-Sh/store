const { app, Menu, BrowserWindow } = require('electron');

//------------------------------------
// メニュー
//------------------------------------
// メニューを準備する
const template = Menu.buildFromTemplate([
    {
      label: "Pi-Store",
      submenu: [
        { role:'reload', label:'再読込' }
      ]
    },
]);

// メニューを適用する
Menu.setApplicationMenu(template);

//------------------------------------
// ウィンドウ
//------------------------------------
// 初期化が終了したらウィンドウを新規に作成する
app.whenReady().then(()=>{
  const win = new BrowserWindow({
    width: 1024,
    height: 800,
    webPreferences: {
      nodeIntegration: true,
    }
  })
  win.loadFile('index.html')
})



  // メインウィンドウが閉じられたときの処理
  mainWindow.on("closed", () => {
    mainWindow = null;
  });

//  初期化が完了した時の処理
app.whenReady().then(() => {
  createWindow();

  // アプリケーションがアクティブになった時の処理(Macだと、Dockがクリックされた時）
  app.on("activate", () => {
    // メインウィンドウが消えている場合は再度メインウィンドウを作成する
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

// 全てのウィンドウが閉じたときの処理
app.on("window-all-closed", () => {
  // macOSのとき以外はアプリケーションを終了させます
  if (process.platform !== "darwin") {
    app.quit();
  }
});
