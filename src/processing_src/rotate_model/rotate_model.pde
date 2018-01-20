import saito.objloader.*;
OBJModel model;
float rotX=0, rotY=0;

// 初期設定
void setup(){
  // 画面サイズ
  size(400, 300, P3D);
  // フレームレート
  frameRate(30);
  // OBJファイルの読み込み
  model = new OBJModel(this, "bunny.obj", "absolute", TRIANGLES);
  model.enableDebug();
  // 座標保存
  model.scale(13);
  model.translateToCenter();  // 中央に配置
  stroke(255);
  noStroke();
}

void draw(){
  // 座標保存
  background(0,0,0);
  // 座標保存
  pushMatrix();
  // オブジェクトの移動
  translate(width/2, height/2, 0);
  // オブジェクトの回転(引数はラジアン)
  rotateX(rotX);
  rotateY(rotY);
  // モデルの描画
  model.draw();
  // 座標保存
  popMatrix();
  // 回転角の増加 30degree (1/6π rad)
  rotX = rotX + PI*(1/6);
  rotY = rotY + PI*(1/6);
  // 回転角が360[deg](=6.28[rad])以上なら0に戻す
  if(rotX >= 6.28) rotX = 0;
  if(rotY >= 6.28) rotY = 0;
}
